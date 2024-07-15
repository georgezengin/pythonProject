from use_age import get_user_data

print()
ud = get_user_data()
if ud['gender'] == 'Female':
    print('hello sis!!')
if ud['gender'] == 'Male':
    print('hello bro!!')
