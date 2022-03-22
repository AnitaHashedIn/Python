# 5. Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.
lst1=["Netflix", "Hulu", "Sling", "Hbo"]

lst2=[198, 166, 237, 125]
d={}
for i,j in zip(lst1,lst2):
    d[i] = j
print(d)