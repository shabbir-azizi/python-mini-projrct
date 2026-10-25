def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int) or isinstance(shift, bool):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)

a,*b = (1,2,3,4)
print(b)






f = lambda x: x + 2
g = lambda x: f(x) *2
print(g(3))

fruit = ['apple ','banana', 'chery']
fruit.pop(1)
# print(fruit)
text = 'False'
if text == True:
    print('True')
else :
    print('False')

studenttuple =("asd", "qwe", "bnp","ajk")
print(type(studenttuple))
print(studenttuple.index("ajk"))
print(studenttuple.count("bnp"))
print(len(studenttuple))


def total (*num):
    return len (num)
print(total((4,8,15)))

programingLisr =["A","B","C","D","E"]
print(type(programingLisr))

programingLisr = set(programingLisr)
print(type(programingLisr))

fruits = ['apple','mango','3']
for f in fruits :
    print(f)
    print(fruits[1])
    print(fruits[0])
    print(fruits[-1])
    print(fruits[-2])
    print(fruits[-3])

s = {1, 2, 2, 3}
s.add(True)
s.add (4)
print(len(s))

n = 1
while n<=16:
    print(n, end="")
    n =n *2
else:
    print("done")

def f (n):
    n * 2
x = f (4)
print(x)
def f (n):
    n * 2
x = f (4)
print(x)

s = "aabbaa"
s = s.replace("aa","bb")
s = s.replace("bb","c")
print(s)
