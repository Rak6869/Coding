#Bob has a playlist of N songs, each song has a singer associated with it (denoted by an integer)
#Favourite singer of Bob is the one whose songs are the most on the playlist
#Count the number of Favourite Singers of Bob

ttl = int(input())
rank = input()
a = rank.split(' ')
from collections import Counter
c = Counter(a)
print(c)
maxv = int(max(c.values()))

count = 0
for k,v in c.items():
    print(k,v,count,maxv)
    if v>=maxv:
        
        maxv = v
        print(maxv)
        count =count + 1
print(count)
