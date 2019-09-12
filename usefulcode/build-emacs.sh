#!/bin/bash

# discard stuff from last build
git reset --hard

# delete all of the last build stuff
git clean -xdf

# get latest update
git pull

./autogen.sh
./configure
make bootstrap -j8
make -j8
