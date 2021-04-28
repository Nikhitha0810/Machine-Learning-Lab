#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


conn = sqlite3.connect('exp2.db')
cur = conn.cursor()
print("connected to database successfully")


# In[4]:


conn.execute('''create table company(Id int primary key not null,Name text,Age int not null,Address char(50) not null,Salary real);''')
print("table created successfully")


# In[5]:


conn.execute("insert into company values(100,'paul',26,'hyderabad',100000.00)");


# In[6]:


conn.execute("insert into company values(101,'allen',28,'mumbai',300000.00)");
conn.execute("insert into company values(102,'sania',29,'chennai',300000.00)");
conn.execute("insert into company values(103,'teddy',26,'hyderabad',200000.00)");


# In[7]:


conn.commit()


# In[8]:


for r in conn.execute('select * from company'):
    print(r)


# In[9]:


conn.commit()
conn.close()


# In[ ]:




