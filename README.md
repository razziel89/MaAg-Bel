# MaAg-bel

This is MaAg-bel, a reduced fork of the Open Babel chemical toolbox desiged to work with
the tools distributed as  [Manipulate
Aggregates](https://github.com/razziel89/ManipulateAggregates). It is meant to be used
only as a Python package. Its functionality is reduced to that needed by Manipulate
Aggregates.

## Notable changes

Most notable changes with respect to the Open Babel base are:

* one library containing all the functionality instead of multiple ones
* standalone ops removed
* eigen3 added as a hard dependency
* removed cmake as dependency
* XML and ZLIB functionality removed
* inchi, smiles and cml formats removed (the latter 2 depend on inchi to some degree)
* more formats removed:
  * JOSN-based
  * XML-based
* Windows compatibility removed (use the WSL is you need to use Windows)
* MacOS compatibility removed

## Installation

Make sure that eigen version 3 is installed. Afterwards, run `pip install maagbel`. If
you are using conda, run `conda install eigen` to install it. Most likely, you want to
install this as a dependency of ManipulateAggregates.

## More information regarding Open Babel

Open Babel is a chemical toolbox designed to speak the many languages
of chemical data. It's an open, collaborative project allowing anyone
to search, convert, analyze, or store data from molecular modeling,
chemistry, solid-state materials, biochemistry, or related areas.

* Ready-to-use programs, and complete programmer's toolkit
* Read, write and convert over 90 chemical file formats
* Filter and search molecular files using SMARTS and other methods
* Generate 2D and 3D coordinates for SMILES and other formats
* Supports molecular modeling, cheminformatics, bioinformatics,
  organic chemistry, inorganic chemistry, solid-state materials,
  nuclear chemistry...

Open Babel is distributed under the GNU General Public License (GPL).
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License. Full details
can be found in the file "COPYING" which should be included in your
distribution.

For more information, check the [Open Babel website](
<http://openbabel.org/).
