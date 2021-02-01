import json
friends = {"Dan": [20, "London", 13123213], "Maria":[25,"Madrid",534543543]}

with open ('friends.json','w') as f:
    json.dump(friends,f,indent=4)

json_strning = json.dumps(friends,indent=4)
print(json_strning)
