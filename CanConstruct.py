def Can_construct(TargetWord, wordbank, memo = {}):
    if TargetWord in memo:
        return memo[TargetWord]
    if TargetWord == "":
        return True
    for word in wordbank:
        if TargetWord.find(word) == 0:
            suffix = TargetWord[len(word):]
            if Can_construct(suffix, wordbank, memo):
                memo[TargetWord] = True
                return True
    memo[TargetWord] = False
    return False

if __name__ == "__main__":
    print(Can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(Can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))

    print(Can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
    ["ee", 
    "eee", 
    "eeee", 
    "eeeee", 
    "eeeeee", 
    "eeeeeee", 
    "eeeeeeee"]))



