# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) May 9, 2016

##########################################################################
## Imports
##########################################################################

import csv

##########################################################################
## Module Constants
##########################################################################

DATAPATH = 'languageWikiList.csv'
OUTPATH = 'languageFileURL.csv'

field_names = ["Language", "Code", "Wiki", "Download_url"]

##########################################################################
## Modules
##########################################################################

# This function reads a CSV file and loads content into a dictionary.
def read_file_location(path, fieldnames):
	with open(path, 'rU') as data:
		reader = csv.DictReader(data, fieldnames = fieldnames)
		for row in reader:
			yield row		
									
##########################################################################
## Program takes list of wikipedia languages and obtains the url for the
## location of the back-up files for each language.
##########################################################################

if __name__ == "__main__":	
    with open(OUTPATH, 'wb') as f:
	    dict_writer = csv.DictWriter(f, field_names)
            for row in read_file_location(DATAPATH, field_names):
                row['Download_url'] = "http://dumps.wikimedia.org/%s/latest/%s-latest-pages-articles.xml.bz2" \
                 % (row["Wiki"], row["Wiki"])
                dict_writer.writerow(row)