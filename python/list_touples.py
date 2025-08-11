
marks = [10,20,"hoi"]
print(marks)
print(marks[0])
print(marks[-1]) #hoi
print(marks[-2]) #20

# print(marks[-4]) index out range

print(marks[0:2])
print(marks[0:3])
print(marks[2:3])

for score in marks:
    #print(score +  " ") typeError int and string concat
    print(score)
    print(" ")

marks.append(100)

marks.insert(0,3)
print(marks)

#---------------tuples
marks = (97,100,101)
print(marks[0])

# marks[0] = 40
# tuplea are immutable

marks= (97,100,97,104,97)
print(marks.count(97)) 

#---------sets
marks = {97,100,101,97,104,97}
print(marks) #97 is only printed once\

#----------dictionary

marks = {"babal":10,
         "rahul":20
         }
print(marks)
print(marks["babal"])
marks["ria"] = 101
print(marks)

marks["babal"] = 0