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
print("=" * 25)
print("Wersja 2")

def isPalindrome(x):
    x = x.lower().replace(" ", "")
    for i in range(0, int(len(x) / 2)):
        if x[i] != x[len(x) -i-1]:
            return False
    return True

word = input("Wpisz dowolny wyraz: ")
reverse = isPalindrome(word)
if reverse:
    print(word, "jest palindromem")
else:
    print(word, "nie jest palindromem")

# ==============================
print("=" * 25)
print("Wersja 3")

def isPalindrome(x):
    x = x.lower().replace(" ", "")
    for i in range(len(x)-1):
        # if x[i] != x[len(x) -i-1]:
        if x[i] == x[len(x) - i - 1]:
            # return
            return True
    # return True
    return False
word = input("Wpisz dowolny wyraz: ")
reverse = isPalindrome(word)
if r
    everse:
    print(word, "jest palindromem")
else:
    print(word, "nie jest palindromem")




