#!/usr/bin/env python
# coding: utf-8

# ### Course Grade Application
#  - Create 5 students. Ask these students from the user
#  - Each of these students should have a midterm grade, project grade, and final grade.
#  - Each student will have a course passing grade.
#  - passingGrade = midterm * (0.3)  + project * (0.3) + final * (0.4) passing grade should be determined like this.
#  - Create a dictionary that keeps these students' information.
#  - Calculate the students' grades and transfer them to the list with the help of indexing.
#  - Finally, set the student with the highest grade to be in the first index and the student with the lowest grade to be in the last index of the list.

# In[ ]:


students = {}


# In[27]:


type(students)


# In[9]:


student1_name1 = input("Please name: ")
student1_surname1 = input("Please surname: ")
student1_midterm1 = input("Please midterm: ")
student1_project1 = input("Please project: ")
student1_final1 = input("Please final: ")


# In[10]:


students1= {"name":student1_name1, 
            "surname":student1_surname1, 
            "midterm":student1_midterm1, 
            "project":student1_project1, 
            "final":student1_final1}


# In[11]:


students1


# In[12]:


student2_name2 = input("Please name: ")
student2_surname2 = input("Please surname: ")
student2_midterm2 = input("Please midterm: ")
student2_project2 = input("Please project: ")
student2_final2 = input("Please final: ")


# In[14]:


students2= {"name":student2_name2, 
            "surname":student2_surname2, 
            "midterm":student2_midterm2, 
            "project":student2_project2, 
            "final":student2_final2}


# In[15]:


students2


# In[16]:


student3_name3 = input("Please name: ")
student3_surname3 = input("Please surname: ")
student3_midterm3 = input("Please midterm: ")
student3_project3 = input("Please project: ")
student3_final3 = input("Please final: ")


# In[17]:


students3= {"name":student3_name3, 
            "surname":student3_surname3, 
            "midterm":student3_midterm3, 
            "project":student3_project3, 
            "final":student3_final3}


# In[18]:


students3


# In[19]:


student4_name4 = input("Please name: ")
student4_surname4 = input("Please surname: ")
student4_midterm4 = input("Please midterm: ")
student4_project4 = input("Please project: ")
student4_final4 = input("Please final: ")


# In[20]:


students4= {"name":student4_name4, 
            "surname":student4_surname4, 
            "midterm":student4_midterm4, 
            "project":student4_project4, 
            "final":student4_final4}


# In[21]:


students4


# In[22]:


student5_name5 = input("Please name: ")
student5_surname5 = input("Please surname: ")
student5_midterm5 = input("Please midterm: ")
student5_project5 = input("Please project: ")
student5_final5 = input("Please final: ")


# In[23]:


students5= {"name":student5_name5, 
            "surname":student5_surname5, 
            "midterm":student5_midterm5, 
            "project":student5_project5, 
            "final":student5_final5}


# In[24]:


students5


# In[36]:


students["name"] = {student1_name1, student2_name2, student3_name3, student4_name4, student5_name5}
students["surname"] = {student1_surname1, student2_surname2, student3_surname3, student4_surname4, student5_surname5}
students["midterm"] = {student1_midterm1, student2_midterm2, student3_midterm3, student4_midterm4, student5_midterm5}
students["project"] = {student1_project1, student2_project2, student3_project3, student4_project4, student5_project5}
students["final"] = {student1_final1, student2_final2, student3_final3, student4_final4, student5_final5}


# In[37]:


students


# In[ ]:





# In[138]:


students["passingGrade"] = {int(student1_midterm1) * (0.3) + int(student1_project1) * (0.3) + int(student1_final1) * (0.4),
                            int(student2_midterm2) * (0.3) + int(student2_project2) * (0.3) + int(student2_final2) * (0.4),
                            int(student3_midterm3) * (0.3) + int(student3_project3) * (0.3) + int(student3_final3) * (0.4),
                            int(student4_midterm4) * (0.3) + int(student4_project4) * (0.3) + int(student4_final4) * (0.4),
                            int(student5_midterm5) * (0.3) + int(student5_project5) * (0.3) + int(student5_final5) * (0.4)
                           }


# In[139]:


students


# In[140]:


students["passingGrade"]


# In[141]:


notes = list(students["passingGrade"])
    


# In[142]:


notes_copy = notes.copy()


# In[143]:


notes_copy


# In[149]:


max_puan = 0
for i in range(len(notes)):
    if notes[i]>max_puan:
        max_puan = notes[i]

print(max_puan)


# In[150]:


min_puan = notes[1]
for i in range(len(notes)):
    if notes[i]<min_puan:
        min_puan = notes[i]

print(min_puan)


# In[153]:


for i in range(len(notes)):
    if notes[i]==max_puan:
        notes.pop(i)


# In[155]:


for i in range(len(notes)-1):
    if notes[i]==min_puan:
        notes.pop(i)


# In[158]:


notes = [max_puan, notes, min_puan]
notes
