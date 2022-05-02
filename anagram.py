def check_angram(str1, str2):
    list1=''.join(sorted(str1))
    list2=''.join(sorted(str2))
    if list1==list2:
        return True


if(check_angram('abcdef','fedcba')):
    print("True")

