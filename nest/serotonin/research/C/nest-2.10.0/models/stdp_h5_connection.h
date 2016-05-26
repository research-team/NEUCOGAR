/* Based on stdp_dopa_connection */

#ifndef STDP_H5_CONNECTION_H
#define STDP_H5_CONNECTION_H

/* BeginDocumentation

   Name: stdp_serotonin_synapse - Synapse type for serotonin-modulated spike-timing dependent
   plasticity.
*/

#include "connection.h"
#include "volume_transmitter.h"
#include "spikecounter.h"
#include "numerics.h"

namespace nest
{

/**
 * Class containing the common properties for all synapses of type serotonin connection.
 */
class STDPH5CommonProperties : public CommonSynapseProperties
{
public:
  /**
   * Default constructor.
   * Sets all property values to defaults.
   */
  STDPH5CommonProperties();

  /**
   * Get all properties and put them into a dictionary.
   */
  void get_status( DictionaryDatum& d ) const;

  /**
   * Set properties from the values given in dictionary.
   */
  void set_status( const DictionaryDatum& d, ConnectorModel& cm );

  Node* get_node();

  long_t get_vt_gid() const;

  volume_transmitter* vt_;
  double_t A_plus_;
  double_t A_minus_;
  double_t tau_plus_;
  double_t tau_c_;
  double_t tau_n_;
  double_t b_;
  double_t Wmin_;
  double_t Wmax_;
};

inline long_t
STDPH5CommonProperties::get_vt_gid() const
{
  if ( vt_ != 0 )
    return vt_->get_gid();
  else
    return -1;
}

/**
 * Class representing an STDPH5Connection with homogeneous parameters,
 * i.e. parameters are the same for all synapses.
 */
template < typename targetidentifierT >
class STDPH5Connection : public Connection< targetidentifierT >
{

public:
  typedef STDPH5CommonProperties CommonPropertiesType;
  typedef Connection< targetidentifierT > ConnectionBase;

  /**
   * Default Constructor.
   * Sets default values for all parameters. Needed by GenericConnectorModel.
   */
  STDPH5Connection();

  /**
   * Copy constructor from a property object.
   * Needs to be defined properly in order for GenericConnector to work.
   */
  STDPH5Connection( const STDPH5Connection& );

  // Explicitly declare all methods inherited from the dependent base ConnectionBase.
  // This avoids explicit name prefixes in all places these functions are used.
  // Since ConnectionBase depends on the template parameter, they are not automatically
  // found in the base class.
  using ConnectionBase::get_delay;
  using ConnectionBase::get_delay_steps;
  using ConnectionBase::get_rport;
  using ConnectionBase::get_target;

  /**
   * Get all properties of this connection and put them into a dictionary.
   */
  void get_status( DictionaryDatum& d ) const;

  /**
   * Set properties of this connection from the values given in dictionary.
   */
  void set_status( const DictionaryDatum& d, ConnectorModel& cm );

  /**
   * Send an event to the receiver of this connection.
   * \param e The event to send
   */
  void send( Event& e, thread t, double_t, const STDPH5CommonProperties& cp );

  void trigger_update_weight( thread t,
    const vector< spikecounter >& h5_spikes,
    double_t t_trig,
    const STDPH5CommonProperties& cp );

  class ConnTestDummyNode : public ConnTestDummyNodeBase
  {
  public:
    // Ensure proper overriding of overloaded virtual functions.
    // Return values from functions are ignored.
    using ConnTestDummyNodeBase::handles_test_event;
    port
    handles_test_event( SpikeEvent&, rport )
    {
      return invalid_port_;
    }
  };

  /*
   * This function calls check_connection on the sender and checks if the receiver
   * accepts the event type and receptor type requested by the sender.
   *
   * \param s The source node
   * \param r The target node
   * \param receptor_type The ID of the requested receptor type
   * \param t_lastspike last spike produced by presynaptic neuron (in ms)
   */
  void
  check_connection( Node& s,
    Node& t,
    rport receptor_type,
    double_t t_lastspike,
    const CommonPropertiesType& cp )
  {
    if ( cp.vt_ == 0 )
      throw BadProperty( "No volume transmitter has been assigned to the serotonin synapse." );

    ConnTestDummyNode dummy_target;
    ConnectionBase::check_connection_( dummy_target, s, t, receptor_type );

    t.register_stdp_connection( t_lastspike - get_delay() );
  }

  void
  set_weight( double_t w )
  {
    weight_ = w;
  }

private:
  // update serotonin trace from last to current serotonin spike and increment index
  void update_serotonin_( const vector< spikecounter >& h5_spikes,
    const STDPH5CommonProperties& cp );

  void
  update_weight_( double_t c0, double_t n0, double_t minus_dt, const STDPH5CommonProperties& cp );

  void process_h5_spikes_( const vector< spikecounter >& h5_spikes,
    double_t t0,
    double_t t1,
    const STDPH5CommonProperties& cp );
  void facilitate_( double_t kplus, const STDPH5CommonProperties& cp );
  void depress_( double_t kminus, const STDPH5CommonProperties& cp );

  // data members of each connection
  double_t weight_;
  double_t Kplus_;
  double_t c_;
  double_t n_;

  // h5_spikes_idx_ refers to the serotonin spike that has just been processes
  // after trigger_update_weight a pseudo serotonin spike at t_trig is stored at index 0 and
  // h5_spike_idx_ = 0
  index h5_spikes_idx_;

  // time of last update, which is either time of last presyn. spike or time-driven update
  double_t t_last_update_;
};

//
// Implementation of class STDPH5Connection.
//

template < typename targetidentifierT >
STDPH5Connection< targetidentifierT >::STDPH5Connection()
  : ConnectionBase()
  , weight_( 1.0 )
  , Kplus_( 0.0 )
  , c_( 0.0 )
  , n_( 0.0 )
  , h5_spikes_idx_( 0 )
  , t_last_update_( 0.0 )
{
}

template < typename targetidentifierT >
STDPH5Connection< targetidentifierT >::STDPH5Connection( const STDPH5Connection& rhs )
  : ConnectionBase( rhs )
  , weight_( rhs.weight_ )
  , Kplus_( rhs.Kplus_ )
  , c_( rhs.c_ )
  , n_( rhs.n_ )
  , h5_spikes_idx_( rhs.h5_spikes_idx_ )
  , t_last_update_( rhs.t_last_update_ )
{
}

template < typename targetidentifierT >
void
STDPH5Connection< targetidentifierT >::get_status( DictionaryDatum& d ) const
{

  // base class properties, different for individual synapse
  ConnectionBase::get_status( d );
  def< double_t >( d, names::weight, weight_ );

  // own properties, different for individual synapse
  def< double_t >( d, "c", c_ );
  def< double_t >( d, "n", n_ );
}

template < typename targetidentifierT >
void
STDPH5Connection< targetidentifierT >::set_status( const DictionaryDatum& d, ConnectorModel& cm )
{
  // base class properties
  ConnectionBase::set_status( d, cm );
  updateValue< double_t >( d, names::weight, weight_ );

  updateValue< double_t >( d, "c", c_ );
  updateValue< double_t >( d, "n", n_ );
}

template < typename targetidentifierT >
inline void
STDPH5Connection< targetidentifierT >::update_serotonin_(
  const vector< spikecounter >& h5_spikes,
  const STDPH5CommonProperties& cp )
{
  double_t minus_dt = h5_spikes[h5_spikes_idx_].spike_time_ - h5_spikes[h5_spikes_idx_ + 1].spike_time_;
  // increase spikes counter
  ++h5_spikes_idx_;
  // exp decay
  n_ = n_ * std::exp( minus_dt / cp.tau_n_ );
  // Check current level of h5 (n) in relation to its baseline (b_).
  // There are 3 possible ways:
  // 1) n > b_ : self-coincidense is good, spike will increase the "n"
  // 2) _b/2 < n < b_ :	uncertainty in making decision, spike will decrease the "n"
  // 3) n < b_/2 :	pure self-coincidense, spike will slightly increase the "n" to prevent permanent ground level of "n"
  if (n_ > cp.b_) /// if h5 level is greater than baseline
  { 
    // self-confidence
    n_ = n_ + h5_spikes[h5_spikes_idx_].multiplicity_ / cp.tau_n_;
  } else {
	  if (n >= cp.b_/2) {
        // uncertainty
        n_ = n_ - h5_spikes[h5_spikes_idx_].multiplicity_ / cp.tau_n_;
	  } else {
		// increase the confidence to prevent zero self-confidence
		n_ = n_ + cp.b_ * (1 / tau_c_ + 1 / tau_n_);
	  }
  }
}

template < typename targetidentifierT >
inline void
STDPH5Connection< targetidentifierT >::update_weight_( double_t c0,
  double_t n0,
  double_t minus_dt,
  const STDPH5CommonProperties& cp )
{
  const double_t tau_ave_ = 1/(1 / cp.tau_c_ + 1 / cp.tau_n_);

  weight_ = weight_ - c0 * (n0 * tau_ave_ * numerics::expm1(minus_dt/tau_ave_));

  if (weight_ < cp.Wmin_) weight_ = cp.Wmin_;
  if (weight_ > cp.Wmax_) weight_ = cp.Wmax_;
}

template < typename targetidentifierT >
inline void
STDPH5Connection< targetidentifierT >::process_h5_spikes_(
  const vector< spikecounter >& h5_spikes,
  double_t t0,
  double_t t1,
  const STDPH5CommonProperties& cp )
{
  // h5 trace at t0
  double_t n0 = n_ * std::exp( ( h5_spikes[h5_spikes_idx_].spike_time_ - t0 ) / cp.tau_n_ );

  double_t minus_dt = 0;

  // process h5 spikes in (t0, t1], send weights from t0 to t1
  if ( (h5_spikes.size() > h5_spikes_idx_+1) && (h5_spikes[h5_spikes_idx_ + 1].spike_time_<=t1) )
  {
    // there is at least 1 h5 spike in (t0, t1]
    // propagate weight up to first h5 spike and update serotonin trace
    // weight and eligibility c are at time t0 but serotonin trace n is at time of last h5 spike

    update_weight_(c_, n0, t0 - h5_spikes[h5_spikes_idx_+1].spike_time_, cp);
    update_serotonin_(h5_spikes, cp);

    // process remaining h5 spikes in (t0, t1]
    double_t cd;
    while ( (h5_spikes.size() > h5_spikes_idx_+1) && (h5_spikes[h5_spikes_idx_+1].spike_time_<= t1) )
    {
      // propagate weight up to next h5 spike and update serotonin trace
      // weight and serotonin trace n are at time of last h5 spike td but eligibility c is at time
      // t0
      // compute "cd" is eligibility trace at time of td

      minus_dt = h5_spikes[h5_spikes_idx_].spike_time_ - h5_spikes[h5_spikes_idx_+1].spike_time_;
      cd = c_ * std::exp( (t0 - h5_spikes[h5_spikes_idx_].spike_time_)/cp.tau_c_);
      
	  update_weight_(cd, n_, minus_dt, cp);
      update_serotonin_( h5_spikes, cp );
    }

    // propagate weight up to t1
    // weight and serotonin trace n are at time of last h5 spike td but eligibility c is at time t0
    cd = c_ * std::exp( (t0 - h5_spikes[h5_spikes_idx_].spike_time_)/cp.tau_c_);
    update_weight_(cd, n_, h5_spikes[h5_spikes_idx_].spike_time_ - t1, cp);
  }
  else
  {
    // no serotonin spikes in (t0, t1]
    // weight and eligibility c are at time t0 but serotonin trace n is at time of last h5 spike
	//update_serotonin_( h5_spikes, cp );
    update_weight_( c_, n0, t0 - t1, cp );
  }

  // update eligibility trace
  c_ = c_ * std::exp( ( t0 - t1 ) / cp.tau_c_ );
}

template < typename targetidentifierT >
inline void
STDPH5Connection< targetidentifierT >::facilitate_( double_t kplus,
  const STDPH5CommonProperties& cp )
{
  c_ += cp.A_plus_ * kplus;
}

template < typename targetidentifierT >
inline void
STDPH5Connection< targetidentifierT >::depress_( double_t kminus,
  const STDPH5CommonProperties& cp )
{
  c_ -= cp.A_minus_ * kminus;
}

/**
 * Send an event to the receiver of this connection.
 * \param e The event to send
 * \param p The port under which this connection is stored in the Connector.
 * \param t_lastspike Time point of last spike emitted
 */
template < typename targetidentifierT >
inline void
STDPH5Connection< targetidentifierT >::send( Event& e,
  thread t,
  double_t,
  const STDPH5CommonProperties& cp )
{
  // t_lastspike_ = 0 initially

  Node* target = get_target( t );

  // purely dendritic delay
  double_t dendritic_delay = get_delay();

  double_t t_spike = e.get_stamp().get_ms();

  // get history of serotonin spikes
  const vector< spikecounter >& h5_spikes = cp.vt_->deliver_spikes();

  // get spike history in relevant range (t_last_update, t_spike] from post-synaptic neuron
  std::deque< histentry >::iterator start;
  std::deque< histentry >::iterator finish;
  target->get_history(
    t_last_update_ - dendritic_delay, t_spike - dendritic_delay, &start, &finish );

  // facilitation due to post-synaptic spikes since last update
  double_t t0 = t_last_update_;
  double_t minus_dt;
  while ( start != finish )
  {
    process_h5_spikes_( h5_spikes, t0, start->t_ + dendritic_delay, cp );
    t0 = start->t_ + dendritic_delay;
    minus_dt = t_last_update_ - t0;
    if ( start->t_ < t_spike ) // only depression if pre- and postsyn. spike occur at the same time
      facilitate_( Kplus_ * std::exp( minus_dt / cp.tau_plus_ ), cp );
    ++start;
  }

  // depression due to new pre-synaptic spike
  process_h5_spikes_( h5_spikes, t0, t_spike, cp );
  depress_( target->get_K_value( t_spike - dendritic_delay ), cp );

  e.set_receiver( *target );
  e.set_weight( weight_ );
  e.set_delay( get_delay_steps() );
  e.set_rport( get_rport() );
  e();

  Kplus_ = Kplus_ * std::exp( ( t_last_update_ - t_spike ) / cp.tau_plus_ ) + 1.0;
  t_last_update_ = t_spike;
}

template < typename targetidentifierT >
inline void
STDPH5Connection< targetidentifierT >::trigger_update_weight( thread t,
  const vector< spikecounter >& h5_spikes,
  const double_t t_trig,
  const STDPH5CommonProperties& cp )
{
  // propagate all state variables to time t_trig
  // this does not include the depression trace K_minus, which is updated in the postsyn. neuron

  double_t dendritic_delay = get_delay();

  // get spike history in relevant range (t_last_update, t_trig] from postsyn. neuron
  std::deque< histentry >::iterator start;
  std::deque< histentry >::iterator finish;
  get_target(t)->get_history(t_last_update_ - dendritic_delay, t_trig - dendritic_delay, &start, &finish);

  // facilitation due to postsynaptic spikes since last update
  double_t t0 = t_last_update_;
  double_t minus_dt;
  while ( start != finish )
  {
    process_h5_spikes_( h5_spikes, t0, start->t_ + dendritic_delay, cp );
    t0 = start->t_ + dendritic_delay;
    minus_dt = t_last_update_ - t0;
    facilitate_( Kplus_ * std::exp( minus_dt / cp.tau_plus_ ), cp );
    ++start;
  }

  // send weight, c, serotonin trace, and facilitation trace K_plus to time t_trig
  process_h5_spikes_( h5_spikes, t0, t_trig, cp );
  n_ = n_ * std::exp( ( h5_spikes[h5_spikes_idx_].spike_time_ - t_trig ) / cp.tau_n_ );
  Kplus_ = Kplus_ * std::exp( ( t_last_update_ - t_trig ) / cp.tau_plus_ );

  t_last_update_ = t_trig;
  h5_spikes_idx_ = 0;
}

} // of namespace nest

#endif // of #ifndef STDP_H5_CONNECTION_H
