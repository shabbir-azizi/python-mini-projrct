abs_1 = 57
abs_2 = 13
asa_1 = 6.4
asa_2 = 13.0



print('Integer Addition:', abs_1 + abs_2)
print('Float Addition:', asa_1 + asa_2) 

print('Int Subtraction:', abs_1 - abs_2) 
print('Float Subtraction:',  asa_2 - asa_1) 


print('Int Multiplication:', abs_1 * abs_2) 
print('Float Multiplication:', asa_2 * asa_1) 

print('Division:', abs_1 / abs_2) 
print('Float Division:', asa_2 / asa_1) 
running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)
per_person = round (final_bill)
print(per_person)






from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) 
print(cos_value) 



