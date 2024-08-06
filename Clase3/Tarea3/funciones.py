def anagram(string1, string2):
    str1 = ''.join(string1.lower().split())
    str2 = ''.join(string2.lower().split())

    return sorted(str1) == sorted(str2)