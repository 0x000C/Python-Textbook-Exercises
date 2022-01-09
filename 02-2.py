# Write code that asks the user to enter their birthday in the form
# mm/dd/yyyy, and then prints a string of the form 'You were born in the
# year yyyy.'

complete_birthday = input('Enter birthday (format: mm/dd/yyyy): ')

birth_year = complete_birthday[len(complete_birthday) - 4:]

print(f'You were born in the year {birth_year}.')
