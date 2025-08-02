# usertype=['admin', 'manager','qa']


# for utype in usertype:
#     print(f'user types: {utype}')

#     for i,utype in enumerate(usertype):
#         print(f'Index: {i}, - type: {utype}')

# ranks=[3,9,5,6,7]
# ranks.sort() 
# for rank in ranks:
#     print(f'ranks : {rank}')



user_data=[]
numvals=input('how many values user wanna add in aarry')
numvals=int(numvals)
for i in range(numvals):
    user_data.append(int(input('enter value')))

for i in user_data:
    print(f' values : {i}')

    
sum=0
for i in user_data:
    sum += int(i)

print(f'sum: {sum}')

for n in user_data:
     if(n%2== 0):          
        print(f"{n} is even")
     else:        
        print(f"{n} is odd")