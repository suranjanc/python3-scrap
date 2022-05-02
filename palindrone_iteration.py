def check_palindrone(nos):
    reversed_string=''.join(reversed(str(nos)))
    if str(nos)==reversed_string:
        return True


if(check_palindrone("abcba")):
    print("True")
