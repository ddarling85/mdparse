from lxml import etree

with open(r'path/to/xml', 'r') as xml:
    text = xml.read()
tree = lxml.etree.fromstring(text)
row = ['', '']
for item in tree.iter('hw', 'def'):
    if item.tag == 'hw':
       row[0] = item.text
    elif item.tag == 'def':
       row[1] = item.text

line = ','.join(row)

with open(r'path/to/csv', 'a') as csv:
     csv.write(line + '\n')

