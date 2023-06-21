word1 = "abcd"
word2 = "pq"
sol = []
flag = 0
count1 = 0
count2 = 0
while not((len(sol)==len(word1+word2))):
        print(sol)
        if flag==0:
            if (count1 == len(word1)):
                 flag = 1
                 pass
            else:   
                sol.append(word1[count1])
                flag = 1
                count1 +=1
        elif flag==1:
            if(count2 == len(word2)):
                 flag = 0
                 pass
            else:
                sol.append(word2[count2])
                flag = 0
                count2 +=1
    
    

a = ' '.join(sol)
print(a)
