myDict = {
    "fast": "in a quick manner",
    "harry": "a coder",
    "hello": "kya haal hai"
}
print(myDict['hello'])  
print(myDict.values()) #print keys of the dic
print(myDict.keys()) #print keys of the dic
print(myDict.items()) 

updateDict = {
    "hi": "hola"    #update dict
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("hello2")) #not error getting
print(myDict["hello2"]) #error throw