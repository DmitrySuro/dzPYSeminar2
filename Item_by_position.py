user_number = int(input('Insert your number: '))

position_one = int(input('Insert first position'))
position_two = int(input('Insert second position'))

user_list = list(range(-user_number, user_number))
print(user_list)

if position_one != 0 and position_two != 0:
    print(user_list[position_one - 1] * user_list[position_two -1])
elif position_one == 0 and position_two > 0:
    print(user_list[position_one] * user_list[position_two - 1])
elif position_two == 0 and position_one > 0:
    print(print(user_list[position_one - 1] * user_list[position_two]))
