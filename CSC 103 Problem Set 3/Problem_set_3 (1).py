#Hope Crisafi
#Problem Set 3
#4/18/2021

#NJW 21/22

#Part A

x = float(input('enter a float:'))

if x > 100:
    y = 20
    z = 40


#Part B

a = int(input('enter an integer:'))

if a < 10:
    b = 0

else:
    b = 99


#Part C

score = int(input('Enter your score here, any value 1-100:'))

A_score = 90
B_score = 80
C_score = 70
D_score = 60

if score >= A_score:
    print('Your grade is A')
else:
    if score >= B_score:
        print('Your grade is B')
    else:
        if score >= C_score:
            print('Your grade is C')
        else:
            if score >= D_score:
                print('Your grade is D')
            else:
                print('Your grade is F')


#Part D

amount1 = int(input('enter amount here:'))
amount2 = int(input('enter a second amount here:'))

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(amount1,'is the greater value')
    elif amount1 < amount2:
        print(amount2,'is the greater value')

#NJW If the problem doesn't say what to do in
#NJW an else situation, don't invent it!

else:
    print('invalid')


#Part E

speed = int(input('enter your speed:'))

if 24 <= speed <= 56:
    print('speed is normal')

else:
    print('speed is abnormal')


#Task 1

length1 = int(input('enter length  of rectangle 1 here:'))
width1 = int(input('enter width of rectangle 1 here: '))
length2 = int(input('enter length of rectangle 2 here: '))
width2 = int(input('enter width of rectangle 2 here: '))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print('rectangle 1 is the larger rectangle')
elif area2 > area1:
    print('rectangle 2 is the larger rectangle')
#NJW else
elif area1 == area2:
    print('both rectangles are equal in area')


#Task 2

age = int(input('enter age here:'))

if 0 < age <= 1:
    print('they are an infant')
#NJW we don't need the first part of this
#NJW (1 <) if it's an if/elif/else 
elif 1 < age < 13:
    print('they are a child')
elif 13 <= age <= 20:
    print('they are a teenager')
elif age > 20:
    print('they are an adult')
else:
    print('please enter a valid number')


#Task 3

color1 = input('enter a primary color here:')
color2 = input('enter another primary color here:')

if color1 == 'red' and color2 == 'blue':
    print('makes Purple')
elif color1 == 'blue' and color2 == 'red':
    print('makes Purple')
elif color1 == 'red' and color2 == 'yellow':
    print('makes Orange')
elif color1 == 'yellow' and color2 == 'red':
    print('makes Orange')
elif color1 == 'blue' and color2 == 'yellow':
    print('makes Green')
elif color1 == 'yellow' and color2 == 'blue':
    print('makes Green')
else:
    print('invalid input')



#Task 4

#knuts
#sickles - 29 knuts
#galleons - 17 sickles

#NJW But 494 knuts prints 0 sickles, and it shouldn't! (-1)

knuts = int(input('enter number of Knuts here:'))
sickles = knuts // 29
galleons = sickles // 17
knutsRemaining = knuts % 29
sicklesRemaining = sickles % 17

if 0 <= knuts < 29:
    print('you have',knuts,'Knut(s).')

elif 29 <= knuts < 493:
    #there are 493 knuts in one galleon
    print('you have',sickles,'Sickle(s), and',knutsRemaining,'Knut(s).')

elif knuts >=493:
    print('you have',galleons,'Galleon(s),',sicklesRemaining,'Sickle(s), and',knutsRemaining,'Knut(s).')

else:
    print('invalid input')

