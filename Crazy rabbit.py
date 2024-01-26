"""
Crazy rabbit is in a coffee field with boundries in an initial given cell (pos = 0 in example). Each field cell might have coffee beans.


  |             |
  |R____________|
   2 2 4 1 5 2 7 # Crazy rabbit at the start"
Crazy rabbit eats all coffee beans that available in the cell. And his jump power increases. Total jump power is equal to the number of total beans eaten

  |             |
  |R____________|
   0 2 4 1 5 2 7 # Crazy rabbit eat coffee beans and his jump power is now 2
Crazy rabbit jumps (initially to the right) if he has a jump power.

     _
  | / \         |
  |R___↓________|
   0 2 4 1 5 2 7 #Crazy rabbit jumps to next position
Crazy rabbit bounces back from a boundries if he jumps too strong


           ___
  |       /   \ |
  |      /     \|
  |     /     / |
  |____R_____↓__|
   0 2 0 1 5 2 7  # next jump will have power of 6, because he ate 4 more coffee beans)
Crazy rabbit position in a field cell is always in the middle. That means that if Crazy rabbit stays right next to the border and have power of jump = 1 then he will be bounced back to the same positon.

After hitting a boundry Crazy rabbit jumps in an opposite direction.

You will be given:

a field as a list (linear array) of numbers
Can Crazy rabbit eat all the beans? return boolean"""

def crazyRabbit(field, position):
    dict_field = {}
    index = 1

    for coffee_or_life_same_thing in field:
        dict_field[index] = coffee_or_life_same_thing
        index += 1

    direction = "r"
    index = position + 1

    for _ in range(300):
        if _ == 0:
            power = dict_field[index]
        else:
            power += dict_field[index]
        dict_field[index] = 0
        cash_power = power
        while cash_power != 0:
            if direction == "r":
                if index == len(field):
                    direction = "l"
                else:
                    index += 1
            elif direction == "l":
                if index == 1:
                    direction = "r"
                else:
                    index -= 1

            cash_power -= 1

    return sum(dict_field.values()) == 0


print(crazyRabbit([1, 0, 1], 0)) # True

print(crazyRabbit([3, 0, 0, 3], 0)) # True

print(crazyRabbit([1, 3, 7], 0)) # True
    
print(crazyRabbit([2, 2, 4, 1, 5, 2, 7], 0)) #False
    
print(crazyRabbit([2, 0, 2, 0, 0, 0, 1], 0)) # True   
    
print(crazyRabbit([2, 0, 3, 0, 0, 1, 0], 0)) # True

print(crazyRabbit([7, 5, 4, 5, 2, 10, 4, 7], 2)) # True
