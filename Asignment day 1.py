#!/usr/bin/env python
# coding: utf-8

# In[7]:



# Define a Function to Preform Sum Of Natural Numbers.

        
def naturalnum(A):
    A=(A*(A+1))/2
    print(round(A))
    
naturalnum(25)        
            
        
        


# In[37]:


# Using String Slicing Print the Reverse Of Middle Characters of Ur Mobile Number.

N='7416251307'
N[5:3:-1]


# In[2]:


# Define a Function to Print Armstrong Number.

#n=int(input('enter any value:'))
def arm(num):
    count=0
    n=num
    while(n>0):
        rem=n%2
        count=count+rem**3
        n=n/10
    if(num==count):
        print("it is Armstrong number")
    else:
        print("it is not Armstrong number")
arm(100)    
    


# In[ ]:





# In[ ]:




