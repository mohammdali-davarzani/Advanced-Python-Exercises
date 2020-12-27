
def divisor (n):
    my_list = list()
    for number in range (1, n+1):
        if n % number == 0:
            my_list.append(number)
    return my_list
    

lst = list()
for i in range (0,10):
    number = int(input())
    div = divisor(number)

    prime = 0
    for n in div:
        for i in range(2, n):
            if (n % i) == 0:
                break  
        else:
            prime += 1
    prime = prime - 1
    lst.append(number)
    lst.append(prime)

d = {lst[ele]: lst[ele+1] for ele in range (0, len(lst), 2)}
sort_d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
l = [[k,v] for k, v in sort_d.items()]
l = l[-1]
output = {l[ele]: l[ele +1] for ele in range (0, len(l), 2)}
n = list(output.keys())
p = list(output.values())
print(str(n[0]), str(p[0]))
print(d)