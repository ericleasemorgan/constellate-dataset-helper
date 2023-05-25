# Constellate Dataset Helper

<em>tl;dnr - Given a Constellate data set identifier, do stuff with the data set's content.</em>

This tiny repository contains three Python scripts hacked together during my brief stint at the 2023 Code4Lib Annual Meeting (Princeton, NJ). More specifically, taking what I learned from a [pre-conference workshop on Ithika's Constellate](https://2023.code4lib.org/workshops/text-analysis-constellate-the-technology-and-the-lab), these scripts do interesting things with Constellate data sets:

  1. `./bin/helper.py` - given a few configurations, output an HTML file describing a data set as well as links to a few visualizations; the resulting HTML file is intended to be edited by hand, supplemented with commentary, and then shared more widely
  2. `./bin/download.py` - given a few configurations, download a data set (as JSONL); once downloaded, the programmer can do all sorts of things with the resulting information
  3. `./bin/constellate2reader.py` - given a few configurations, create a directory filled with .txt files and a metadata.csv file suitable for creating Distant Reader study carrels; creating additional data sets is an example of something the programmer can do with results Script #2
  
The tricks to use the scripts are a many-fold:

  1. You will need to install a Python module called [Constellate Client](https://constellate.org/docs/constellate-client)
  2. [Log into Constellate](https://constellate.org) and create a dataset. Note the data set's identifier, and it will look something like this: 9828620c-9e7f-3e5a-3d02-5f8a204c9753
  3. Edit the scripts, and most importantly, configure the value for DATASET
  4. Run the scripts.
  5. Go to Step #1; the process is not difficult, but it does require practice
  
---  
Eric Lease Morgan &lt;emorgan@nd.edu&gt;  
May 25, 2023
