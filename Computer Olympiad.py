n = int(input())

lst =[]
for i in range(n):
    lst.append(input())

for i in range(n):
    temp = lst[i].split(".")
    temp[1] = temp[1].title()
    lst[i] = " ".join(temp)

lst.sort()
for i in range(n):
    print(lst[i])
