def is_palindrome(scentence):
    scentence = scentence.replace(" ", "").lower()
    if len(scentence) == 0 or len(scentence) == 1:
        return True
    if scentence[0] == scentence[len(scentence) - 1]:
        return is_palindrome(scentence[1:len(scentence) - 1])
    return False

if __name__ == '__main__':
    test = [None] * 3
    test[0] = "Natur i rutan"
    test[1] = "Sirap i Paris"
    test[2] = "Inte ett palindrom"
    for i in range(len(test)):
        print(is_palindrome(test[i]))

    
