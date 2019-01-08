#!/usr/bin/env python
# coding: utf-8

# In[ ]:


l = list(range(2000,3200+1))
#print(l)
for number in l :
    #print(number)
    isDivided = (number%7)
    fiveDivided = number%5
    if isDivided == 0 and fiveDivided != 0:
        print(number)


# In[ ]:


# Write  a program which will find all such numbers which are divisible by 7
# but not multiple of 5 between 2000 to 3200 both included
l = list(range(2000,3200+1))
new_list = [number * 1 for number in l if ((number%7 == 0) and (number%5 != 0))]
print(new_list)


# In[ ]:


#Reverse first name and last name provided by user space between first name and lastname
first_Name = input("Please provide first name ")
lats_Name = input("Please provide last name ")
first_last_name = [first_Name,'  ',lats_Name]
#first_last_name = first_last_name.reverse()
first_last_name.reverse()
username = ''
for name in first_last_name:
   # print(name)
    l = []
    l.extend(name)
    l.reverse()
    #print("=====",l)
    for n in l:
        username = username + n
print(username)


# In[ ]:


# Python Program to find Volume and Surface Area of Sphere using Functions
 
import math
 
def Area_of_Triangle(radius):
    sa =  4 * math.pi * radius * radius
    Volume = (4 / 3) * math.pi * radius * radius * radius
    print("\n The Surface area of a Sphere = %.2f" %sa)
    print("\n The Volume of a Sphere = %.2f" %Volume)
 
Area_of_Triangle(12)


# In[ ]:


# Accepts comma seperated sequence and generate list
comma_separated = input("Please provide comma separated list - ")
comma_separated_list = []
for word in comma_separated:
    #print(word)
  
    comma_separated_list.extend(word)
    if word == ',':
        comma_separated_list.remove(word)
print(comma_separated_list)


# In[3]:


#Nested for loop
for i in range(0,5):
    j=i+1
    s=""
    for k in range(0,j):
        s=s+"*"
    print(s)
h=4
for i in s:
    s=s[0:h]
    h=h-1
    print(s)


# In[ ]:


#Reverse word after accepting from user
word = input("Please provide first name ")
word_list = [word]
#first_last_name = first_last_name.reverse()
word_list.reverse()
#print(word_list)
reversWord = ""
for rword in word_list:
    l = []
    l.extend(rword)
    l.reverse()
    
for n in l:
        reversWord = reversWord + n
print(reversWord)

