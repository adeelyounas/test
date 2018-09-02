import sys

from collections import OrderedDict

# define ordered dict to iterate in a sequence
ROMAN_NUMBER_MAPPING = OrderedDict(
	[
	    ("M", 1000),
	    ("CM", 900),
	    ("D", 500),
	    ("CD", 400),
	    ("C", 100),
	    ("XC", 90),
	    ("L", 50),
	    ("XL", 40),
	    ("X", 10),
	    ("IX", 9),
	    ("V", 5),
	    ("IV", 4),
	    ("I", 1)
	]
)

def func(number):
    roman_numerals = []
    for numeral, value in ROMAN_NUMBER_MAPPING.items():
        count = number // value # get the remainder 
        number -= count * value # subtract remainder from the given number
        roman_numerals.append(numeral * count) # add numeral to list if remainder is not 0

    return ''.join(roman_numerals) # join all the numerals


# TESTS
def test():
	assert func(1) == "I"
	assert func(1994) == "MCMXCIV"
	print("Looks Good.")


if __name__ == "__main__":
	arg = sys.argv[1]
	if arg and arg == 'test':
		test()
	else:
		try:
			print(func(int(arg)))
		except ValueError:
			print('Please enter valid number!')
