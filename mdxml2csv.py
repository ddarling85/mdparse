import xml.etree.ElementTree as ET
import csv
import logging

tree = ET.parse("testxmlfile.xml")
root = tree.getroot()
logging.basicConfig(filename='mdxml2csv.log',level=logging.DEBUG)

# open a file for writing

Resident_data = open('testX2csv.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []

count = 0
for member in root.iter():
	EntityDescriptor = []
	address_list = []
	if count == 0:
		entityID = member.attrib('entityID')
		resident_head.append(entityID)
#		realm = member.find('realm').tag
#		resident_head.append(realm)
		URL = member.find('OrganizationURL').tag
		resident_head.append(OrganizationURL)
		LO = member.find('OrganizationName').tag
		resident_head.append(OrganizationName)
		PhoneNumber = member.find('PhoneNumber').tag
		resident_head.append(PhoneNumber)
		Technical_POC = member.find('EmailAddress').tag
		resident_head.append(EmailAddress)
		csvwriter.writerow(resident_head)
		count = count + 1

#	entityID = member.attrib('entityID').text
#	resident.append(entityID)
#	realm = member.find('realm').text
#	resident.append(realm)
	URL = member.find('OrganizationURL').text
	resident.append(OrganizationURL)
	LO = member.find('OrganizationName').text
	resident.append(OrganizationName)
	PhoneNumber = member.find('PhoneNumber').text
	resident.append(PhoneNumber)
	Technical_POC = member.find('EmailAddress').text
	resident.append(EmailAddress)
	csvwriter.writerow(resident)
Resident_data.close()

