num = int(input('Enter Your Loop: '))
total = []
for i in range(num):
    data = int(input('Enter Your Data: '))
    total += [data]
print(total)
total.sort()
print(max(total))
print(min(total))