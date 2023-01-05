#string
'''
name = "siraz"
print(name[4])
print(name[0:5])
print(name[2:4])
print(name[0::2])
'''
#string function

story = "once upon a time there was a youtuber named siraz"
print(len(story)) #count alphabet
print(story.endswith("siraz")) #word is in or out
print(story.count("o")) #who many alphabet
print(story.replace("siraz","sana")) #replace name


'''
stroy = "once upon a time .\nmovie"

print(stroy)
'''


#LETTER
letter = ''' Dear <|NAME|>,
Greetings from Z coding house. 
i am happy to tell 
you are selected!

date: <|DATE|>
'''
'''
name = input("enter your name\n")
date = input("enter date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter) '''