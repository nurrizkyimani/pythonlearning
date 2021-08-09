import json 

pyjson = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"] }

resjson = json.dumps(pyjson, indent=4, sort_keys=True)

with open('person.json', 'w') as file:
  json.dumps(pyjson, file, indent=4)


# decode = json.loads(resjson)