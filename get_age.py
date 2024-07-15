import requests

class AgeNotValidError(Exception):
    def _init_(self, message="Invalid age, must be between 1 and 120"):
        self.message = message
        super()._init_(self.message)

def get_user_age():
    age = int(input("Enter your age: "))
    if age > 120 or age < 0:
        # return -1
        raise AgeNotValidError("")
    return age


# try:
#     age = get_user_age()
# except AgeNotValidError:
#     print("Invalid age, must be between 1 and 120")
# except BaseException as e:
#     if type(e) is ValueError:
#         print("unable to convert age to int")
#     else:
#         print(e.args)


def get_user_gender():
    g = input('Enter gender: ')
    response = requests.get("https://en.wikipedia.org/wiki/" + g)
    if str.upper(g) == 'M':
        return 'Male'
    elif str.upper(g) == 'F':
        return 'Mmale'
    elif str.upper(g) == 'APACHE':
        return 'Apache'


def get_user_age2():
    # try:
        age = int(input('enter age: '))
        if age > 120 or age < 0:
            # print('Sorry, weirdo detected!')
            raise ValueError('Invalid age, must be between 1 and 120', age)
        return age
    # except ValueError as e:
    #     print(e, e.args)

# try:
#     age = get_user_age()
# except ValueError as e:
#     print(e)
