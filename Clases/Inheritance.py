class Human:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Human):

    def __init__(self, first_name, last_name, score):
        super().__init__(first_name=first_name, last_name=last_name, score=score)


class Worker(Human):

    def __init__(self, first_name, last_name, wage, working_hours):
        super().__init__(first_name=first_name, last_name=last_name)
        self.wage = int(wage)
        self.working_hours = int(working_hours)

    def income(self):
        return self.wage * self.working_hours

    def print_info(self):
        print(f'First name: {self.first_name}, Last Name {self.last_name}, Calculated income:{self.income()}')


number_of_workers = int(input("Please enter a number of workers: "))

workers = []

for i in range(number_of_workers):
    user_input = input()
    split_string = user_input.split()
    print(split_string)
    first_name = split_string[0]
    last_name = split_string[1]
    wage_per_hour = split_string[2]
    working_hour = split_string[3]

    workers.append(Worker(first_name, last_name, wage_per_hour, working_hour))

print(workers[0].print_info())
