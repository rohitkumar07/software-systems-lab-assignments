.SUFFIXES: .java

# Programs
SHELL 	= bash
JC     	= javac
LD	= ld
RM 	= rm
ECHO	= /bin/echo
CAT	= cat
PRINTF	= printf
SED	= sed
DOXYGEN = doxygen

######################################

# Project Paths
PROJECT_ROOT :=$(CURDIR)
DOCDIR = $(PROJECT_ROOT)/doc
SRCDIR = $(PROJECT_ROOT)/src
BINDIR = $(PROJECT_ROOT)/bin

######################################

NO_COLOR=\e[0m
OK_COLOR=\e[1;32m
ERR_COLOR=\e[1;31m
WARN_COLOR=\e[1;33m
MESG_COLOR=\e[1;34m
FILE_COLOR=\e[1;37m

OK_STRING="[OK]"
ERR_STRING="[ERRORS]"
WARN_STRING="[WARNINGS]"
OK_FMT="${OK_COLOR}%30s\n${NO_COLOR}"
ERR_FMT="${ERR_COLOR}%30s\n${NO_COLOR}"
WARN_FMT="${WARN_COLOR}%30s\n${NO_COLOR}"

########################################################################################

.PHONY: all compile doc clean

all: 

compile:
	@$(ECHO) "Setting up compilation..."
	@mkdir -p bin
	@ cd $(SRCDIR) && \
	$(JC) MovieAnalysisG18.java -d $(BINDIR)
	@$(ECHO) "Done"
	
########################################################################################

doc:
	@$(ECHO) -n "Generating Doxygen Documentation ...  "
	@$(RM) -rf doc/html
	@$(DOXYGEN) $(DOCDIR)/Doxyfile
	@$(ECHO) "Done"

########################################################################################

clean:
	@$(ECHO) -n "Cleaning up...  "
	@$(RM) -rf *~ $(DOCDIR)/html $(BINDIR)
	@$(ECHO) "Done"

