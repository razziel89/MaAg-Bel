# makefile for libFireDeamon

default: clean
	$(MAKE) doc

# ===== C++ documetnation =====
.PHONY : doc
doc:
	@which doxygen
	@echo "Creating documentation using doxygen..."
	doxygen Doxyfile

# ===== distribution rules =====

.PHONY : dist
dist: clean_dist
	@echo "Creating source distribution"
	@python setup.py sdist

.PHONY : publish
publish: dist
	@echo "Publishing to PyPI"
	@python -m twine upload dist/*

# ===== clean rules =====

.PHONY : clean
clean : clean_doc clean_dist

.PHONY : clean_doc
clean_doc : 
	rm -rf docs

.PHONY : clean_dist
clean_dist: 
	rm -rf build dist
