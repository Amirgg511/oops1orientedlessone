class clown():
    nickname = ""
    age = 12

    def __init__(self):                                  
        print("make a new class clown") 

    def change_details(self):
        self.nickname = input("please enter your nickname")
        self.age = int(input("please enter your age"))
    def show_details(self):
        print("details of class clown are:")
        print(self.nickname)
        print(self.age)

obj1 = clown()
obj1.change_details()
obj1.show_details()

    