#!/usr/bin/env python

# download.py - givenconfigurations, download a JSONL file from Constellate

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# March 15, 2023 - first investigations; while at Code4Lib 2023 (Princeton, NJ)


# configure
DIRECTORY = '/Users/eric/Desktop'
FILENAME  = 'dataset.gz'
DATASET   = '9828620c-9e7f-3e5a-3d02-5f8a204c9753'
TYPE      = 'jsonl'

# require
from   pathlib import Path
import constellate

# initialize; denote where to save the download
directory = Path( DIRECTORY )
filename  = directory/FILENAME

# do the work and done
constellate.download( DATASET, TYPE, fname=filename )

