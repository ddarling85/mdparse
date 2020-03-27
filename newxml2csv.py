import xml.etree.ElementTree as ET
import csv
import logging

#tree = ET.parse("resident.xml")
tree = ET.parse("metatest.xml")
root = tree.getroot()
#root = ET.fromstring(tree)
logging.basicConfig(filename='metatest.log',level=logging.DEBUG)

# open a file for writing

Resident_data = open('metatest.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []

count = 0

#for member in root.iter():
#for member in root.findall('{urn:oasis:names:tc:SAML:2.0:metadata}EntityDescriptor'):
for member in root.findall('{urn:oasis:names:tc:SAML:2.0:metadata}ContactPerson'):
#for member in root:

#   testEmnt = member.find("ContactPerson")
   testEmnt = member.find('{urn:oasis:names:tc:SAML:2.0:metadata}Company')
#   testEmnt1 = member.findall('{urn:oasis:names:tc:SAML:2.0:metadata}EntityDescriptor')
#   testEmnt2 = member.attrib.find('entityID')
   testEmnt2 = member.get('contactType')
#   print(member.find('{urn:oasis:names:tc:SAML:2.0:metadata}SPSSODescriptor'))
#   print(root, root.tag, root.attrib)
#   print(root.tag, root.attrib)
#   print(root.attrib)
#   print(member.tag, member.attrib)
#   print(member.find('entityID'))
   print(member, member.tag, member.attrib)
#   print(member.tag, member.attrib)
#   print(member.attrib)
#   print(member.tag)
#   print(member)
#   print(member[0][0].text)
#   print(member('entityID').text)
#   print(testEmnt('entityID').text)
   print(testEmnt.tag)
#   print(testEmnt1)
   print(testEmnt2)

Resident_data.close()

