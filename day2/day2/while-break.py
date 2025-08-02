hex_emps=[]
i=0
while i < 5:
    name = input("Enter emp name").strip()
    if name.lower() == 'skip':
        print('skippingg')
        continue
    if name.lower() == 'stop':
        print('skippingg')
        break
    hex_emps.append(name)
    i += 1

print("Emplyeeeeeee")
for emp in hex_emps:
    print(f'EmpName: {emp}')