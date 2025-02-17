Name = input("What is the name of the student?")
Grade = [int(input("What is the first grade")), int(input("Second?")), int(input("Third?")), int(input("Fourth?")), int(input("Fifth"))]
Average = ((Grade[0]+Grade[1]+Grade[2]+Grade[3]+Grade[4])/len(Grade))
Letter = ("A")
if Average < 90:
    Letter = ("B")
    if Average < 80:
        Letter = ("C")
        if Average < 70:
            Letter = ("D")
            if Average < 60:
                Letter = ("F")

print("Name:", Name)
print("Average:", Average)
print("Letter grade:", Letter)
#Made By Luis Hernandez