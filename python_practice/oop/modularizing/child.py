import parent

class Person:
    def pay_bill(self):
        raise NotImplementedError
class Millionaire(Person):
    def pay_bill(self):
        print("Keep the change you filthy animal.")
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you?")

chad = GradStudent()
chad.pay_bill()

# print(locals())