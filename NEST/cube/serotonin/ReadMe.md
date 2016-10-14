## Serotonin in NEST

#### Implementation details
**In short**

Based on NEST-2.10.0 source code

1) Added two new files based on stdp_dopa_connection:
"nest-2.10.0/models/stdp_h5_connection.cpp"
"nest-2.10.0/models/stdp_h5_connection.h"
As a result, the following two classes were added "STDPH5CommonProperties", "STDPH5Connection" to handle serotonin dynamics.

2) NEST's source file "nest-2.10.0/models/modelsmodule.cpp" was modified to register "STDPH5Connection" synapse alias in a Python as "stdp_serotonine_synapse":
```bash
#include "stdp_h5_connection.h"
...
register_connection_model<STDPH5Connection<TargetIdentifierPtrRport>>(net_, "stdp_serotonine_synapse");
```
3) NEST's source file "nest-2.10.0/nestkernel/conn_builder.cpp" was modified to handle possible errors due to initialization of STDPH5Connection:
```bash
if (syn_name == "stdp_serotonin_synapse") {
...
}
```

4) NEST's "Makefile.am" and "Makefile.in" were modified to add our new serotonin-related sources to compilation pipeline:

"nest-2.10.0/models/Makefile.am":

```bash
stdp_h5_connection.h stdp_h5_connection.cpp\
```

"nest-2.10.0/models/Makefile.in":

```bash
...
libmodelsmodule_la-stdp_h5_connection.lo \
...
stdp_h5_connection.h stdp_h5_connection.cpp\
...
@AMDEP_TRUE@@am__include@ @am__quote@./$(DEPDIR)/libmodelsmodule_la-stdp_h5_connection.Plo@am__quote@
...
@am__fastdepCXX_TRUE@	$(AM_V_CXX)$(LIBTOOL) $(AM_V_lt) --tag=CXX $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CXX) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(libmodelsmodule_la_CXXFLAGS) $(CXXFLAGS) -MT libmodelsmodule_la-stdp_h5_connection.lo -MD -MP -MF $(DEPDIR)/libmodelsmodule_la-stdp_h5_connection.Tpo -c -o libmodelsmodule_la-stdp_h5_connection.lo `test -f 'stdp_h5_connection.cpp' || echo '$(srcdir)/'`stdp_h5_connection.cpp
@am__fastdepCXX_TRUE@	$(AM_V_at)$(am__mv) $(DEPDIR)/libmodelsmodule_la-stdp_h5_connection.Tpo $(DEPDIR)/libmodelsmodule_la-stdp_h5_connection.Plo
@AMDEP_TRUE@@am__fastdepCXX_FALSE@	$(AM_V_CXX)source='stdp_h5_connection.cpp' object='libmodelsmodule_la-stdp_h5_connection.lo' libtool=yes @AMDEPBACKSLASH@
@AMDEP_TRUE@@am__fastdepCXX_FALSE@	DEPDIR=$(DEPDIR) $(CXXDEPMODE) $(depcomp) @AMDEPBACKSLASH@
@am__fastdepCXX_FALSE@	$(AM_V_CXX@am__nodep@)$(LIBTOOL) $(AM_V_lt) --tag=CXX $(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=compile $(CXX) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) $(libmodelsmodule_la_CXXFLAGS) $(CXXFLAGS) -c -o libmodelsmodule_la-stdp_h5_connection.lo `test -f 'stdp_h5_connection.cpp' || echo '$(srcdir)/'`stdp_h5_connection.cpp
```
**In detail**

To be continued...


