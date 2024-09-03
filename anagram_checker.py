def anagram_checker(s1, s2):
    return sorted(s1)==sorted(s2)

print(anagram_checker("listen","silent"))