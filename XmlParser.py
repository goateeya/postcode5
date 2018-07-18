import xml.etree.ElementTree as ET
import sqlite3
insert_list = []
tree = ET.parse('Xml_10706.xml')
root = tree.getroot()
conn = sqlite3.connect('zip5.db')
cursor = conn.cursor()
for item in root:
    zip5 = item.find('Zip5').text
    city = item.find('City').text
    area = item.find('Area').text
    road = item.find('Road').text
    scope = item.find('Scope').text
    insert_list.append((zip5, city, area, road, scope))
cursor.executemany('insert into zip (zip5, city, area, road, scope) values (?, ?, ?, ?, ?)', insert_list)
cursor.close()
conn.commit()
conn.close()