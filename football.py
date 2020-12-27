from random import sample
names = ["Hossein", "Maziyar", "Akbar", "Nima", "Mehdi", "Farhad", "Mohammad", "Khashayar", "Milad", "Mostafa", "Amin", 
        "Saeid", "Poya", "Poriya", "Reza", "ALi", "Behzad", "Soheil", "Behrooz", "Shahrooz", "Saman", "Mohsen"
]

class Human:

    name = names

class fotballer(Human):

    def team_A ():
        Names_of_Players = sample(Human.name, k=11)
        for i in range(0, 11):
            print('A', Names_of_Players[i])
            names.remove(Names_of_Players[i])

    def team_B ():
        Names_of_Players = sample(Human.name, k=11)
        for i in range(0, 11):
            print('B', Names_of_Players[i])
    
a = fotballer.team_A()
b = fotballer.team_B()

#sample(value and k)