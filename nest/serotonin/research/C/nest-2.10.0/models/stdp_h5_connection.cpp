/* Based on stdp_dopa_connection */

#include "network.h"
#include "dictdatum.h"
#include "connector_model.h"
#include "common_synapse_properties.h"
#include "stdp_h5_connection.h"
#include "event.h"
#include "nestmodule.h"

namespace nest
{
//
// Implementation of class STDPH5CommonProperties.
//

STDPH5CommonProperties::STDPH5CommonProperties()
  : CommonSynapseProperties()
  , vt_( 0 )
  , A_plus_( 1.5 )
  , A_minus_( 1.8 )
  , tau_plus_( 10.0 )
  , tau_c_( 2000.0 )
  , tau_n_( 1000.0 )
  , b_( 0.4 )
  , Wmin_( 0.0 )
  , Wmax_( 200.0 )
{
}

void
STDPH5CommonProperties::get_status( DictionaryDatum& d ) const
{
  CommonSynapseProperties::get_status( d );

  if ( vt_ != 0 )
    def< long_t >( d, "vt", vt_->get_gid() );
  else
    def< long_t >( d, "vt", -1 );

  def< double_t >( d, "A_plus", A_plus_ );
  def< double_t >( d, "A_minus", A_minus_ );
  def< double_t >( d, "tau_plus", tau_plus_ );
  def< double_t >( d, "tau_c", tau_c_ );
  def< double_t >( d, "tau_n", tau_n_ );
  def< double_t >( d, "b", b_ );
  def< double_t >( d, "Wmin", Wmin_ );
  def< double_t >( d, "Wmax", Wmax_ );
}

void
STDPH5CommonProperties::set_status( const DictionaryDatum& d, ConnectorModel& cm )
{
  CommonSynapseProperties::set_status( d, cm );

  long_t vtgid;
  if ( updateValue< long_t >( d, "vt", vtgid ) )
  {
    vt_ = dynamic_cast< volume_transmitter* >( NestModule::get_network().get_node( vtgid ) );

    if ( vt_ == 0 )
      throw BadProperty( "Serotonine source must be volume transmitter" );
  }

  updateValue< double_t >( d, "A_plus", A_plus_ );
  updateValue< double_t >( d, "A_minus", A_minus_ );
  updateValue< double_t >( d, "tau_plus", tau_plus_ );
  updateValue< double_t >( d, "tau_c", tau_c_ );
  updateValue< double_t >( d, "tau_n", tau_n_ );
  updateValue< double_t >( d, "b", b_ );
  updateValue< double_t >( d, "Wmin", Wmin_ );
  updateValue< double_t >( d, "Wmax", Wmax_ );
}

Node*
STDPH5CommonProperties::get_node()
{
  if ( vt_ == 0 )
    throw BadProperty( "No volume transmitter has been assigned to the serotonin synapse." );
  else
    return vt_;
}

} // of namespace nest
