candies = [2,3,5,1,3]
extraCandies = 3
sol = []
maxc = max(candies)

for i in candies:
   
    if (i+extraCandies >= maxc):
        sol.append('true')
    else:
        sol.append('false')

print(sol)
