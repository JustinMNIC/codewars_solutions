"""How many elephants can the spider web hold?

Imagine a spider web that is defined by two variables:

strength, measured as the weight in kilograms that the web holds. Strength + 1 elephant will break the web
length, measured as the number of elephants that fit one after the other on the web :)
Paraphrasing the song "One elephant went out to play", how many elephants will the web hold if we put them one after the other, without breaking?

You must take into account two things:

elephants like to create super high pyramids, so, on each level of the structure fits one elephant less than in the previous one.
elephants sitting on the first row weight 1000 kg, the ones sitting on the second row weight 2000 kg, and so on. When rows are full of elephants, next elephants go up one level, and weight 1000 kg more than the previous ones.
Visualy represented:

Width: 3 Strength: 10000

3000Kg: E6
2000Kg: E4 E5
1000Kg: E1 E2 E3
The elephants weight 10000Kg. Since the web can hold 10000Kg (strength), the solution is 6 elephants.

Have fun!

Notes:

check all the possible values for the input parameters, even absurd ones :D"""


def break_the_web(strength, width):
    if strength < 1000 or width < 1:
        return 0
    else:
        max_number_of_elephants = 0
        for elepahnt_in_row in range(1, width+1):
            max_number_of_elephants += elepahnt_in_row
        
        elephants_total_weight = 0
        elephants_wight = 1000
        elephants = 0
        cash_widht = width
        cash_index = 1
        while elephants_total_weight <= strength:
            if max_number_of_elephants == 0:
                return elephants
            if cash_widht == 0:
                cash_widht = width - cash_index 
                cash_index += 1
                elephants_wight += 1000
            elephants += 1
            elephants_total_weight += elephants_wight
            cash_widht -= 1
            max_number_of_elephants -= 1
        return elephants - 1