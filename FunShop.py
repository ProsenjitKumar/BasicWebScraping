# input abcdef nibe
# first a ke nie * print korbe avabe sobgulo ke kore store korbe a variable a
#

# It is a console program "FunShop"
print("-------- Welcome In Our Fun Shopping ---------------")
print("Note: Just for kidding.")

class Shop:

    def super_computer(self):

        print("Details")
        buy = input("press 1 for buy this product\n"
                    "")

    def aircraft(self):
        print("Details")

    def pen(self):
        print("Details")

    def python_book(self):
        print("Details")

    def titanic_ship(self):
        print("Details")

    def asia(self):
        print("Details")

    def europe(self):
        print("Details")

    def africa(self):
        print("Details")

    def south_america(self):
        print("Details")

    def oceania(self):
        print("Details")

    def north_america(self):
        print("Details")

    def antarctica(self):
        print("Details")

    def registration(self):
        self.fullname = input("Enter your fullname: ")
        self.email = input("Enter your Email: ")
        self.__password_1 = input("Enter Your Password: ")
        self.__password_2 = input("Enter confirm Password: ")
        if self.__password_1 == self.__password_2:
            print("Your account has been created. Thanks.")
            return self.signin()
        else:
            print("Your password dosent match, Try again.")
            return self.registration()

    def signin(self):
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        if email == self.email:
            if password == self.__password_1:
                print("You are singed in")
                return self.category()
            else:
                print("password doesn't matching\nTry again")
                return self.signin()
        else:
            print("Email doesn't matching\nTry again")
            return self.signin()

    def category(self):
        choose = input("Your choice\n"
                       "1. Super Computer\n"
                       "2. Aircraft\n"
                       "3. Pen\n"
                       "4. Python Book\n"
                       "5. Titanic Ship\n"
                       "6. Asia\n"
                       "7. Europe\n"
                       "8. Africa\n"
                       "9. South America\n"
                       "10. Oceania\n"
                       "11. North America\n"
                       "12. Antarctica\n"
                       "\npress a number: ")
        if choose == 1:
            self.super_computer()
        elif choose ==2:
            return self.aircraft()
        elif choose ==3:
            return self.pen()
        elif choose ==4:
            return self.python_book()
        elif choose ==5:
            return self.titanic_ship()
        elif choose ==6:
            return self.asia()
        elif choose ==7:
            return self.europe()
        elif choose ==8:
            return self.africa()
        elif choose ==9:
            return self.south_america()
        elif choose ==10:
            return self.oceania()
        elif choose ==11:
            return self.north_america()
        elif choose ==12:
            return self.antarctica()

shop_obj = Shop()
shop_obj.registration()