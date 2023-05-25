#!/usr/bin/env python

# constellate2reader.py - given configurations, output plain text and a metadata file for the Reader

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# March 14, 2023 - first investigations; while at Code4Lib 2023 (Princeton, NJ)


# configure
JSON      = 'truth-beauty-honor-justice.jsonl'
DIRECTORY = 'truth-beauty-honor-justice'
COLUMNS   = [ 'author', 'title', 'date', 'file' ]
EXTENSION = '.txt'
PADDING   = 6

# require
from   pathlib import Path
import json
import pandas as pd

# make sane
directory = Path( DIRECTORY )
directory.mkdir( exist_ok=True )

# read all records
with open( JSON ) as handle : records = list( handle )

# process each record; create a file of each full text item, as well as capture metadata
metadata = []
for index, record in enumerate( records ) :

	# re-initialize
	record = json.loads( record )
		
	# parse; author
	try               : author = record[ 'creator' ][ 0 ]
	except KeyError   : author = ''
	except IndexError : author = ''
	
	# parse some more
	title    = record[ 'title' ]
	date     = record[ 'publicationYear' ]
	fulltext = record[ 'fullText' ]
	
	# create file name and save ful text
	fulltext = ' '.join( fulltext )
	filename = str( index ).zfill( PADDING ) + EXTENSION
	with open( directory/filename, 'w' ) as handle : handle.write( fulltext )
			
	# update
	metadata.append( [ author, title, date, filename ] )
	
# create a data frame from the metadata, output, and done
metadata = pd.DataFrame( metadata, columns=COLUMNS )
print( metadata.to_csv( index=False ) )
exit()
