## ----------------------------------------------------------- ##
## Don't touch the next line unless you know what you're doing.##
## ----------------------------------------------------------- ##
include ${SOFT_WORKDIR}/env/compilation/compilevars.mk

# Name of the module
LOCAL_NAME := platform/netdevice/tools/evtwatch

# Compile the sub-modules, except when the "upnp" must be used as a library.
# list all the modules that need to be compiled prior to using this module
LOCAL_MODULE_DEPENDS := \

# list all modules APIs that are necessary to compile this module
LOCAL_API_DEPENDS := \
                     	platform \
			platform/adaptation/media \
 			platform/adaptation/io \
                     	platform/adaptation/common \
                     	platform/base/sx \
			platform/csw \
		     	platform/chip/defs \
                   	platform/chip/hal \
			platform/edrv/aud \
			platform/mdi \
			platform/netdevice \
			target \
			target/${CT_TARGET} \
			
## ------------------------------------ ##
## 	Add your custom flags here          ##
## ------------------------------------ ##
LOCAL_EXPORT_FLAG += 
# This is a top-level module
IS_TOP_LEVEL := no

# For a toplevel module, define which tests to include in delivery
# Skip the 'tests' in the names. Beware that everything from the 
# given tests directories will be included...
TOPLEVEL_DELIVER_TESTS := 


## --------------------------- ##
## Override toplevel settings  ##
## --------------------------- ##

# Set more dependencies as binary : they will not be compiled from source.
LOCAL_BINARY_LIBS ?=

# Set dependencies as source : the library will be generated from source
# This supersedes the BINARY (local+global) setting in case of conflict
LOCAL_SRC_LIBS ?=

## ------------------------------------- ##
##	List all your sources here           ##
## ------------------------------------- ##

# Assembly / C code
S_SRC := ${notdir ${wildcard src/*.S}} # uncomment to take all .S files
C_SRC := ${notdir ${wildcard src/*.c}} # uncomment to take all .c files

# Simulation specific inputs
INPUT_FILES :=  

## ------------------------------------------------------------------------- ##
# Documentation configuration
## ------------------------------------------------------------------------- ##


## ------------------------------------- ##
##  Do Not touch below this line         ##
## ------------------------------------- ##
include ${SOFT_WORKDIR}/env/compilation/compilerules.mk


