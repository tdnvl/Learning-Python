
# coding: utf-8

# # List Nuances
#
# Let's go over some nuances about lists

# ## Indexing into a list
#
# The general syntax it the following. Assuming `l` is your list:
#
# `m = l[begin:end:step]`
#
# `begin` tells you where you start accessing in the list.  `end` tells you where you stop but **does not include** that value (exclusive) and `step` is the increment of what you need to access starting from `begin`.

# In[2]:


l = [1, 2, 3, 4, 5, 1, 2, 3]
#    0  1  2  3  4  5  6  7
m = l[2:6:2] # Start from index 2, ends at index 6 (but does not include) and we access the elements in steps of 2
# m = [3,5]
print(m)

# If we do not include the step, we assume that the increment is 1
m2 = l[2:6]
# m2 = [3,4,5,1]
print(m2)


# `begin` and `end` can be negative, but you must ensure that the increment is also negative. Negative indices mean that we are approaching the list in reverse order

# In[ ]:


# l = [1, 2, 3,  4, 5,  1, 2, 3]
#    -8  -7  -6 -5  -4 -3 -2 -1
m3 = l[-1:-6:-2]
#m3 = [3, 1, 4]
print(m3)


# You can omit the `begin` and `end`.  It assumes that they are `0` and the end of the list respectively
#

# In[8]:


# l = [1, 2, 3,  4, 5,  1, 2, 3]
#      0  1  2   3  4   5  6  7
m4 = l[:5] # specifying the begin is omitted which means that it is automatically starts at 0
print(m4)
m5  = l[5:] # begin is 5, but specifying the end is omitted, so automatically go to the end of list
print(m5)
m6 = l[::2] # begin is 0, end is the end of the list, increment is 2 - skips every other element
print(m6)
m7 = l[::-1] # A trick to go in reverse order
print(m7)


# # Inserting elements in a list
#
# We can insert elements in a list at any position we want.  There are two methods to allow us to insert.  One method is called `append`.  Adds an element to the end of the list.  You can use the `insert` method to insert values in the list and shift everything to the right.  New element goes where you specified where to insert.

# In[11]:


A = [1, 'string', [0, 1, 2]]
print(A)

# We can add another element to this list at the end
A.append('hello')
print(A)

# We can also insert in any arbitrary position
A.insert(2, 'world')
print(A)


# # Counting elements in a list
#
# We can also count how many times we encounter an element in a `list`.  We can use the `count` method for that.

# In[14]:


# A = [1, 'string', 'world', [0, 1, 2], 'hello']
c = A.count(1)
print(c)
d = A.count('world')
print(d)


# # Extending in a list
#
# To extend a `list` means that you are gluing two lists together

# In[16]:


D = [1, 2, 3, 4]
E = [5, 6, 7]

# If we appended E to D, we would get a 5 element list, with the [5, 6, 7] attached at the end
D.append(E)
print(D)

# In order to make D an EXTENDED version of this list (i.e. 7 elements), you use the extend method
D = [1, 2, 3, 4]
D.extend(E)
print(D)


# # Popping and Removing Items
#
# The `pop` method allows you to remove elements in a list at the end (which is the default) or at any position you desire

# In[19]:


V = [5, 4, 3, 2, 1]
print(V)
# V.pop will:
# 1. It removes the last element from this list
# 2. It returns that element to you in a variable
d = V.pop()
print(V)
print(d)
# You can just do
# V.pop() which will just remove the last element and you don't save that element variable

# You can also remove at any arbitrary position.  Just specify the index of where you want to remove in the pop method
# V = [5, 4, 3, 2]
e = V.pop(1)
print(V)
print(e)


# We can use `remove` remove the first occurrence of an element that exists in the list.  We don't operate on the indices or locations of the list

# In[24]:


F = [1, 2, 1, 1, 3, 2, 3, 'hello', 'hello']

F.remove(1)
print(F)
F.remove(1)
print(F)
F.remove(3)
print(F)
F.remove('hello')
print(F)
F.remove('world')


# # Sorting
#
# Last but not least - We can `sort` a list

# In[25]:


A = [1, 5, 4, 3, 3, 2, 10, 20, -1 # Create a list
A.sort() # The sort method sorts a list - it does in place
print(A)


# If you want to return a newly sorted list while maintaining the original one, use the `sorted` method.  This is a function built-in to Python:

# In[26]:


A = [1, 5, 4, 3, 3, 2, 10, 20, -1]
B = sorted(A)
print(A)
print(B)


# # Tuples
#
# They are like lists, but once you create them you cannot change their contents.   You use tuples to ensure that the information is not changed.  To create them, just use parantheses instead of `[]`

# In[30]:


B = (1, 2, 'hello', 'thomas')
print(B)
print(B[0])
print(B[1:])  # Gives you another tuple of just the last three elements
B[2] = -1


# # Looping over lists
#
# We can certainly loop over each element in list and we can do something with each element

# In[31]:


B = ['hello', 'how', 1, 2, 3, 'are', 'you']

# l will contain one element from the list B and this starts from
# the beginning, to the end
for l in B:
    print(l)


# # Using `enumerate`
#
# We can also determine the position of where each element in the list occurred.  Use the `enumerate` object in a loop

# In[32]:


for (i, l) in enumerate(B): # i contains the position and l contains the corresponding element from the list
    print (i, l)


# # Using `zip`
#
# Given a pair of lists that are the same size, we can iterate and access individual elements in the same position of the lists
#

# In[34]:


A = [0, 8, 5, 4, 3]
B = ['a', 'c', 'thomas', 'hello', 'ray']

for (i, j, k ,l) in zip(A, B): # zip returns a tuple that is of the same size for as many lists that you put in
    print (i, j)         # Each element i is an element from the list A and j is an element from the list B
                               # The elements correspond to the same positions starting from left to right
