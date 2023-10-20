S = 'shrubbery'
L = list(S)
print(L)

B = bytearray(b'da')
B.extend(b'net')
x = B.decode()
print(x)
s = "Spam"
x = s.find('pa')
print(x)
y = s.replace("pa", "xsa")
print(y)

string = '%s, eggs, and %s' % ('spam', 'SPAM!')
string2 = '{0}, eggs, and {1}'.format('spam', 'SPAM!')
string3 = '{}, eggs, and {}'.format('spam', 'SPAM!')
# print(string)
# print(string2)
# string = string.__add__(" nothing here!")
# print(string)
# n_str = """132123
# 12312313
# 412414
# 142124"""
# print(n_str.replace("\n", "_"))
# string =
z = u'x'.encode() + b'y'
print(z.decode())
L = [123,]
# list comprehenshion
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
col = [row[1] for row in M]
print(col)