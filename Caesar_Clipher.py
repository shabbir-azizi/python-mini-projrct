def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

