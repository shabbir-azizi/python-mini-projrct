# def caesar(text, shift, encrypt=True):

#     if not isinstance(shift, int) or isinstance(shift, bool):
#         return 'Shift must be an integer value.'

#     if shift < 1 or shift > 25:
#         return 'Shift must be an integer between 1 and 25.'

#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     if not encrypt:
#         shift = - shift
    
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
#     return text.translate(translation_table)

# def encrypt(text, shift):
#     return caesar(text, shift)
    
# def decrypt(text, shift):
#     return caesar(text, shift, encrypt=False)

# encrypted_text = caesar('freeCodeCamp', 3)
# print(encrypted_text)

# a,*b = (1,2,3,4)
# print(b)






# f = lambda x: x + 2
# g = lambda x: f(x) *2
# print(g(3))

# fruit = ['apple ','banana', 'chery']
# fruit.pop(1)
# print(fruit)
text = 'False'
if text == True:
    print('True')
else :
    print('False')