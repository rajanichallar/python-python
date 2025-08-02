hex_emps=[]
i=0
while i <2:
    name = input("Enter emp name").strip()
    if name.lower() == 'skip':
        print('skippingg')
        continue
    if name.lower() == 'stop':
        print('skippingg')
        break
    while True:
        age=input("enter ahge :").strip()
        if(age.isdigit()):
            age=int(age)
            break
        else:
            print('please enter valid age')

    city=input("enter city :").strip()

    # dictionary
    emp={
        'name':name        ,
        'age':age        ,
        'city':city
    }

    hex_emps.append(emp)
    i += 1

print("Emplyeeeeeee")
for index,emp in enumerate(hex_emps,start=1):
    print(f" {index}: EmpName: {emp['name']} - Age: {emp['age']} - City: {emp['city']}")