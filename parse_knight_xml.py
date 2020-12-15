import lxml.etree as ET

doc = ET.parse('knights.xml')

for knight in doc.findall('.//knight'):
    quest = knight.find('quest')
    print(knight.get('title'), knight.findtext('name'), quest.text)

