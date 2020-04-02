# makefile for libFireDeamon

default: clean
	$(MAKE) cppdoc

# C++ documetnation
.PHONY : cppdoc
cppdoc:
	@which doxygen
	@echo "Creating documentation using doxygen..."
	doxygen Doxyfile

.PHONY : clean
clean : clean_doc

.PHONY : clean_doc
clean_doc : 
	rm -rf docs
