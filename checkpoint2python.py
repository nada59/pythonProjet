#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Question 1
lastName=input()
firstName=input()
print(lastName+" "+firstName)


# In[15]:


#Question 2
n=int(input())
nn=int(str(n)+str(n))
nnn=int(str(n)+str(n)+str(n))
print(n+nn+nnn)
    


# In[16]:


#Question 3
x=int(input())
if x % 2 ==0:
    print("even")
else:
    print("odd")


# In[17]:


#Question 4
for i in range (2000,3201):
    if i % 7==0 and i% 5 !=0:
        print(i,end=" ")
    
    


# In[ ]:


#Question 5
k=int(input())
i=1
ch=" "
while i<=k :
    ch=ch+str(i)+"!"+"*"
    i=i+1
print(str(k)+"!"+"=", ch)    
    
    


# In[ ]:


#Question 6
ch=input()
result=" "
for i in range(len(ch)):
    if i % 2 ==0:
        result=result+ch[i]
print(result)


# In[ ]:


#Question 7
x=float(input("le prix de l'article "))
if (x>=500):
    print("le prix est",x/2)
elif (x<=200):
    print("le prix est",x*90/100)
else:
    print("le prix est",x*70/100)


# In[ ]:




