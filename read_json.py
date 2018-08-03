import json,re
file = open('recipes.json','r')
data = json.loads(file.read())


for i in data:
    for y in i['ingredients']:
        matching_eggs = re.search(r'\beggs\b',y)
        matching_egg = re.search(r'\begg\b',y)
        if matching_eggs or matching_egg:
            string ="The recipie with id {} has eggs".format(i['id']) 
            print(string)
            break
            
