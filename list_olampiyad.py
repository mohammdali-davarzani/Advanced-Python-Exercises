# this is basic program
number_of_names = int(input())
infos  = list()

for i in range (0, number_of_names):
    info = input().split(".")
    infos.append(info)

x = 0
y = 1

for letter in range (0,len(infos)):
    infos[x][y] = infos[x][y].lower()
    infos[x][y] = infos[x][y].capitalize()
    x += 1


infos.sort(key= lambda x : (x[0], x[1]))

item = 0
for i in infos:
    print(*infos[item])
    item += 1

