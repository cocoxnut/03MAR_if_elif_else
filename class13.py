birth = int(input('Your year of birth:'))
if 2022 - birth >= 18:
    print('ADULT')
elif 2022 - birth <= 4:
    print('KIDDO')
else:
    print('UNDER AGE')
