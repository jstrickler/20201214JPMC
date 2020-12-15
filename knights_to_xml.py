import lxml.etree as ET

root = ET.Element('knights')

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        k = ET.SubElement(root, 'knight', title=title)
        name_element = ET.SubElement(k, 'name')
        name_element.text = name
        ET.SubElement(k, 'color').text = color
        ET.SubElement(k, 'quest').text = quest
        ET.SubElement(k, 'comment').text = comment


print(ET.tostring(root, xml_declaration=True, pretty_print=True).decode())

doc = ET.ElementTree(root)  # make a "Tree" object
doc.write('knights.xml', xml_declaration=True, pretty_print=True)
