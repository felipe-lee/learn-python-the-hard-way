age = raw_input('How old are you?')

print('So you are {age} {years} old?'.format(age=age, years='year' if age == '1' else 'years'))
