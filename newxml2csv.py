import xml.etree.ElementTree as ET
import csv
import logging

tree = ET.parse("metatest.xml")
root = tree.getroot()
logging.basicConfig(filename='example.log',level=logging.DEBUG)

# open a file for writing

Resident_data = open('testxmlfile.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []

count = 0

for member in root.iter('{urn:oasis:names:tc:SAML:2.0:metadata}EntityDescriptor'): 
   print member.attrib

Resident_data.close()

