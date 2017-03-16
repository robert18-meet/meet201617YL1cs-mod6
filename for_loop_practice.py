import turtle

#Question 1
for i in range (1,5):
    print(i*'*')
#Question 2
my_drawing=[(0,0),(0,100),(100,100),(100,0),(0,0)]
for j in range (0,5):
    turtle.goto(my_drawing[j])
#Question 3
x=3
x=x+3
x-=3
print(x-3)
print(x)    
