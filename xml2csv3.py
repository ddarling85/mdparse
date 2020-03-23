from xml.dom import minidom

xmldoc = minidom.parse('testxmlfile.xml')
hw_lst = xmldoc.getElementsByTagName('hw')
defu_lst = xmldoc.getElementsByTagName('def')

with open('your.csv', 'a') as out_file:
    for i in range(len(hw_lst)):
        out_file.write('{0}, {1}\n'.format(hw_lst[i].firstChild.data, defu_lst[i].firstChild.data)) 

