import pickle
friends1 = {"Dan": [20, "London", 13123213], "Maria":[25,"Madrid",534543543]}
friends2 = {"Jack": [33, "New Jersey", 131233413], "Peter":[40,"Boston",344543543]}
friends = (friends1,friends2)

with open ('friends.dat','wb') as f:
    pickle.dump(friends,f)

with open('friends.dat','rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)