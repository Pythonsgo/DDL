# Author: Selma Gomez Orr <selmagomezorr@gmail.com> Copyright (C) May 8, 2016

##########################################################################
## Imports
##########################################################################

import csv
import re
from BeautifulSoup import BeautifulSoup
import urllib2

##########################################################################
## Module Constants
##########################################################################

DATAPATH = 'languageWikiList.csv'
OUTPATH = 'languageFileInfo.csv'

field_names = ["Language", "Code", "Wiki", "Download_url", "Backup_date", "Size"]

##########################################################################
## Modules
##########################################################################

# This function reads a CSV file and loads content into a dictionary.
def read_file_location(path, fieldnames):
	with open(path, 'rU') as data:
		reader = csv.DictReader(data, fieldnames = fieldnames)
		for row in reader:
			yield row		
									
			
# This function takes a url for an html page and returns a beautiful soup object
def get_soup(url):
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)
	return soup	
	

##########################################################################
## Program takes list of wikipedia languages and obtains the url for the
## location of the back-up files for each language, the back-up date, and 
## their size and creates a CSV of this information.
##########################################################################

if __name__ == "__main__":	
    with open(OUTPATH, 'wb') as f:
	    dict_writer = csv.DictWriter(f, field_names)
            for row in read_file_location(DATAPATH, field_names):
                wiki_url = "http://dumps.wikimedia.org/%s/latest/" % row["Wiki"]
                soup = get_soup(wiki_url)
                #Use regex to find the url's of interest for each language wiki and write back-up file information.
                for link in soup.findAll("a"):
                    if re.match(row["Wiki"] + '-latest-pages-articles\d?\d?\.xml-?.*\.(bz2)$', link['href']) != None:
                        file_info = link.next.next.split()
                        row['Download_url'] = wiki_url + str(link['href'])
                        row['Backup_date'] = str(file_info[0])
                        row['Size'] = str(file_info[2]) 
                        dict_writer.writerow(row)