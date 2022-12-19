#!/usr/bin/python3
try:
    raise Exception('spam','mike','coke')
except Exception as inst:
    print("good")
    print(type(inst))
    print(inst.args)
    x,y,z = inst.args
    print("x:",x,"y:",y,"z:",z)

