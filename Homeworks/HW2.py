#!/usr/bin/env python
# coding: utf-8

# ### User login application
#  - Get username and password values from the user.
#  - Check the values in an if statement and tell the user if they were succesful.

# In[19]:


kullanici_adi = "merve"
sifre = "12345"
print("********Welcome to login application!!!********")


# In[33]:


username = input("Enter username : ")
password = input("Enter password : ")


# In[35]:


if(kullanici_adi == username and sifre == password):
    print("Congratulations, your information is correct.")
    print("Hello {}".format(username).upper())
elif(kullanici_adi != username and sifre == password):
    print("Invalid username")
elif(kullanici_adi == username and sifre != password):
    print("Invalid password")
elif(kullanici_adi != username and sifre != password):
    print("Invalid username and password")


# ### Extra:
#  - Try building the same user login application but this time, use a dictionary.

# In[40]:


dictionary = {"username":"merve", "password":"12345"}
kullanici_adi = input("Enter username: ")
sifre = input("Enter password: ")
if(dictionary["username"]==kullanici_adi and dictionary["password"]==sifre):
    print("Congratulations, your information is correct.")
    print("Hello {}".format(dictionary["username"]).upper())
elif(dictionary["username"] != kullanici_adi and dictionary["password"] == sifre):
    print("Invalid username")
elif(dictionary["username"] == kullanici_adi and dictionary["password"] != sifre):
    print("Invalid password")
elif(dictionary["username"] != kullanici_adi and dictionary["password"] != sifre):
    print("Invalid username and password")
