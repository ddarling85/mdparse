import xml.etree.ElementTree as ET
import csv
import logging

#tree = ET.parse("resident.xml")
tree = ET.parse("metatest.xml")
root = tree.getroot()
#root = ET.fromstring(tree)
logging.basicConfig(filename='metatest.log',level=logging.DEBUG)

# open a file for writing

Resident_data = open('testxmlfile.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []

count = 0

for member in root.findall():
#for member in root:

   testEmnt = member.find('{urn:oasis:names:tc:SAML:2.0:metadata}EntityDescriptor')
#   print(member.find('{urn:oasis:names:tc:SAML:2.0:metadata}SPSSODescriptor'))
#   print(root.tag, root.attrib)
#   print(root, root.tag, root.attrib)
#   print(root)
#   print(member.tag, member.attrib)
   print(member.find('entityID'))
   print(member, member.tag, member.attrib)
#   print(testEmnt.attrib('entityID').text)

Resident_data.close()

