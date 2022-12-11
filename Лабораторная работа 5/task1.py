# TODO решить с помощью list comprehension и распечатать его
import pprint
list_ = [{'bin': bin(number), 'dec': number, 'hex': hex(number), 'oct': oct(number)} for number in range(16)]
pprint.pprint(list_)

