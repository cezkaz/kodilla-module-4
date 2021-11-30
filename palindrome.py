def isPalindrome(x):
    x = x.lower().replace(" ","")
    return x == x[::-1]

word = input("Wpisz dowolny wyraz: ")
reverse = isPalindrome(word)
if reverse:
    print(word, "jest palindromem")
else:
    print(word,"nie jest palindromem")

# ============================