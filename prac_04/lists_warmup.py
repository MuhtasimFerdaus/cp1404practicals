""""
cp1404/cp5632
warmup for using list
"""
#list of numbers
numbers=[3,1,4,1,5,9,2]
#expected outcomes:
#numbers[0]= 3
#numbers[-1]= 2
#numbers[3]= 1
#numbers[:-1]= 3,1,4,1,5,9
#numbers[3:4]= 1
#5 in numbers= True
#7 in numbers= False
#"3" in numbers= False
#numbers + [6, 5 , 3]= [3,1,4,1,5,9,6,5,3]
print("The numbers:")
print(numbers)

numbers[0]= "ten"

numbers[-1]= 1
print("Numbers after changing first and last elements:")
print(numbers)

print(f"Elements from numbers except first two: {numbers[2:]}")

print(f"If 9 is an element of numbers: {9 in numbers}")