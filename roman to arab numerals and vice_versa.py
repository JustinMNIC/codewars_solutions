class RomanNumerals:
    @staticmethod
    def to_roman(arab_number):
        dictionary = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        roman_numeral = ""
        for value, numeral in sorted(dictionary.items(), reverse=True):
            while arab_number >= value:
                roman_numeral += numeral
                arab_number -= value
        return roman_numeral

    @staticmethod
    def from_roman(roman_num):
        dictionary = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        arabic_numeral = 0
        prev_value = 0

        for numeral in reversed(roman_num):
            value = dictionary.get(numeral, 0)
            if value < prev_value:
                arabic_numeral -= value
            else:
                arabic_numeral += value
            prev_value = value

        return arabic_numeral


print(RomanNumerals.to_roman(44))
print(RomanNumerals.from_roman("IV"))


