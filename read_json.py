import json
file = open('recipes.json','r')
data = json.loads(file.read())

splitted_data=[]
for i in data:
    for y in i['ingredients']:
        if "eggs" in y or "egg" in y :
            print('The recipie with id ', i['id'] , 'has eggs')

# for datas in load_data:
#     print(datas)


# with open("reci.json","r") as json_file:
#     data = json.load(json_file)
#     print(data['id'])
    
    
