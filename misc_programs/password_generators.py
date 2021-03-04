#function to generate random passwords
import random
def password_generator(user_category):
    password_data = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    if user_category == '1':
        #weak password
        pass_length = 4
        new_password = ''.join(random.sample(password_data, pass_length))
        return new_password
    elif user_category == '2':
        #strong password
        pass_length = 8
        new_password = ''.join(random.sample(password_data, pass_length))
        return new_password
    else:
        return False

#displaying the result
user_category = input('Enter 1 for weak password or 2 for strong password: ')
result = password_generator(user_category)
print(result)




