import string

def check_password(password):
    """
    >>> check_password('A1213pokl')
    False
    >>> check_password('bAse730onE')
    True
    >>> check_password('asasasasasasasaas')
    False
    >>> check_password('QWERTYqwerty')
    False
    >>> check_password('123456123456')
    False
    >>> check_password('QwErTy911poqqqq')
    True
    """
    if len(password) < 10:
        return False
    has_digit = any(c in string.digits for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    return has_digit and has_lower and has_upper

def main():
    tests = [
        'A1213pokl',
        'bAse730onE',
        'asasasasasasasaas',
        'QWERTYqwerty',
        '123456123456',
        'QwErTy911poqqqq'
    ]
    for t in tests:
        print(t, "->", check_password(t))

if __name__ == '__main__':
    main()
