from datetime import date
age = input().split('/')
age = list(map(lambda item : int(item), age))

today = date.today()


class your_age:

    day = today.day
    month = today.month
    year = today.year

    if (age[0] > year) or (age[1] > 12) or (age[-1] > 31):
        print("WRONG")
    
    else:
        if (day < age[-1]):
            month -= 1
            day += 10 
            day = [day - age[-1]]
        else:
            day = [day - age[-1]]
        


        if (month < age[1]):
            year -= 1
            month += 10
            month = [month - age[1]]
        else :
            month = [month - age[1]]
        
        

        year -= age[0]
        
        print(year)



your_age()