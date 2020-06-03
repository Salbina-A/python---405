#1st task

import json

j_str = {'Jonas': 1, 'Mikkel': 7, 'Hannah': 3, 'Ines': 4, 'Adam': 13, 'Noah': 2}
print(json.dumps(j_str, indent=4))

#2nd task
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sampleJson_conv = json.loads(sampleJson)
print(sampleJson_conv["company"]["employee"]["payble"]["salary"])

#3rd task
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

obj_to_json = json.dumps(vehicle.__dict__, indent=5)
print(obj_to_json)


#4th task
import json

json_data  = """{
     "name": "Toyota Rav4",
     "engine": "2.5L",
     "price": 32000
}"""

json_to_object = json.loads(json_data)
print(json_to_object)

#5th task
import xml.etree.ElementTree as ET

etree = ET.parse("movies.xml")
root = etree.getroot()
for i in root.iter():
    print(i.tag, i.attrib)


#6th task
import xml.etree.ElementTree as ET

etree = ET.parse("movies.xml")
root = etree.getroot()

tag_list = []
for i in root.iter():
	tag_list.append(i.tag)
print(tag_list)

#7th task
import xml.etree.ElementTree as ET

etree = ET.parse("movies.xml")
root = etree.getroot()

for i in root.findall("./genre/decade/movie/[year='1992']"):
	print(i.attrib) 

#8th task
import xml.etree.ElementTree as ET

etree = ET.parse("movies.xml")
root = etree.getroot()

for i in root.findall("./genre/decade/movie/format[@multiple='Yes'].."):
	print(i.attrib) 

#9th task
import xml.etree.ElementTree as ET

etree = ET.parse("movies.xml")
root = etree.getroot()


for i in root.iter("movie"):
	if i.attrib["title"] == "Back 2 the Future":
		i.attrib["title"] = "Back to the Future"
		print(i.attrib["title"])


#10th task

#11th task
