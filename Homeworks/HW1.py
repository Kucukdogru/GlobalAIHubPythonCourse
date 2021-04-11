#!/usr/bin/env python
# coding: utf-8

# ### Create a List and swap the second half of the list with the first half of the list and print this list on the screen.

# In[76]:


liste = list(range(10))


type(liste)


# In[78]:


print(liste)


half1 = [int(i) for i in liste[:len(liste)//2]]
half2 = [int(i) for i in liste[len(liste)//2:]]


print(half1)



print(half2)


type(half2)



print(type(half1))




liste = [half2, half1]
print(liste)



### Ask the user to input a single digit integer to a variable 'n'. Then, print out all of the even numbers from 0 to n (including n)
number = int(input("Please enter a single digit positive number: "))
while number<1 or number>10:
    number = int(input("Please enter a single digit positive number: "))
    if number>1 and number<10:
        myList = list(range(number+1))
        for x in myList[0:number+1:2]:
            print(x)
    else:
        print("Error")
