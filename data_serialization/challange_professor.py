import pickle
import json

def serialize(object,file,protocol):
    if protocol == pickle:
        with open (file,'wb') as f:
            pickle.dump(object,f)
    elif protocol == json:
        with open(file, 'w') as f:
            json.dump(object, f, indent=4)
    else:
        print ('voce inseriu o protocolo errado')

def deserialize(file,protocol):
    if protocol == pickle:
        with open(file, 'rb') as f:
            obj = pickle.load(f)
            print(obj)
    elif protocol == json:
        with open(file, 'rt') as f:
            obj = json.load(f)
            print(obj)
    else:
        print ('voce inseriu o protocolo errado')

friends1 = {"Dan": [20, "London", 13123213], "Maria":[25,"Madrid",534543543]}
friends2 = {"Jack": [33, "New Jersey", 131233413], "Peter":[40,"Boston",344543543]}
friends = (friends1,friends2)


friends_j = {"Dan": [20, "London", 13123213], "Maria":[25,"Madrid",534543543]}
serialize(friends,'friends_challange.dat',pickle)
serialize(friends_j,'friends_j_challange.json',json)
deserialize('friends_challange.dat',pickle)
deserialize('friends_j_challange.json',json)

