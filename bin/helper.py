#!/usr/bin/env python

# helper.py - given configurations, output HTML describing a Constellate dataset
# usage: ./bin/helper.py > ~/Desktop/helper.html; open ~/Desktop/helper.html

# Eric Lease Morgan <emorgan@nd.edu>

# March 15, 2023 - first investigations
# March 17, 2023 - actually output html


# configure
DATASET  = '9828620c-9e7f-3e5a-3d02-5f8a204c9753'
TERMS    = [ 'truth', 'beauty', 'honor', 'justice' ]
TEMPLATE = 'template.txt'
ETC      = 'etc'

# require
from constellate import charts
import constellate
from pathlib import Path

# get metadata
description = constellate.client.get_description( DATASET )
query       = description[ 'search_description' ]
hits        = description[ 'num_documents' ]

# get download data
downloads = description[ 'downloads' ]
for download in downloads :

	# we only want the full meal deal
	if download[ 'name' ] == 'jsonl' :
	
		# parse
		date = download[ 'updated' ]
		url  = download[ 'url' ]
		size = download[ 'size' ]

# get visualizations
categories = charts.categories_over_time( DATASET, url_only=True )
cloud      = charts.word_cloud( DATASET, url_only=True )
documents  = charts.documents_over_time( DATASET, url_only=True )
frequency  = charts.term_frequency( DATASET, terms=TERMS, url_only=True )
phrases    = charts.keyphrases( DATASET, url_only=True )
treemap    = charts.category_treemap( DATASET, url_only=True )

# open the template
etc      = Path( ETC )
template = etc/TEMPLATE
with open( template ) as handle : html = handle.read()

# process substiutions
html = html.replace( '##QUERY##', query )
html = html.replace( '##HITS##', str( hits ) )
html = html.replace( '##DATE##', date )
html = html.replace( '##SIZE##', str( size ) )
html = html.replace( '##URL##', url )
html = html.replace( '##CATEGORIES##', categories )
html = html.replace( '##CLOUD##', cloud )
html = html.replace( '##DOCUMENTS##', documents )
html = html.replace( '##FREQUENCY##', frequency )
html = html.replace( '##PHRASES##', phrases )
html = html.replace( '##TREEMAP##', treemap )

# output and done
print( html )
exit()
