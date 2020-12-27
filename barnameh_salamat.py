def __input__():
    num_of_students = int(input())
    age = input().split(' ')
    height = input().split(' ')
    weight = input().split(' ')

    age = list(map(lambda n : int(n), age))
    height = list(map(lambda n : int(n), height))
    weight = list(map(lambda n : int(n), weight))

    return num_of_students, age, height, weight

class A:
    
    info = __input__()
    num_of_students = info[0]
    age = info[1]
    height = info[2]
    weight = info[-1]


        
    age_average = sum(age) / num_of_students
    height_average = sum(height) / num_of_students
    weight_average = sum(weight) / num_of_students

    output = [age_average, height_average, weight_average]
    
    def get_output(self):
        print(A.age_average)
        print(A.height_average)
        print(A.weight_average)

    
class B:

    info = __input__()
    num_of_students = info[0]
    age = info[1]
    height = info[2]
    weight = info[-1]

        
    age_average = sum(age) / num_of_students
    height_average = sum(height) / num_of_students
    weight_average = sum(weight) / num_of_students

    output = [age_average, height_average, weight_average]
    
    def get_output(self):
        print(B.age_average)
        print(B.height_average)
        print(B.weight_average)



class_a = A()
class_b = B()
if (class_a.output[1] > class_b.output[1]):
    class_a.get_output()
    class_b.get_output()
    print('A')
elif (class_a.output[1] < class_b.output[1]):
    class_a.get_output()
    class_b.get_output()
    print('B')
elif (class_a.output[-1] > class_b.output[-1]):
    class_a.get_output()
    class_b.get_output()
    print('A')
elif (class_a.output[-1] < class_b.output[-1]):
    class_a.get_output()
    class_b.get_output()
    print('B')
else:
    class_a.get_output()
    class_b.get_output()
    print('Same')
