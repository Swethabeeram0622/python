# finding palindrome in list of words...
def find_palindromes(words):
    palindromes = []
    for word in words:
        if word == word[::-1]:  # Check if word is same forwards and backwards
            palindromes.append(word)
    return palindromes
words_list = ["level", "python", "radar", "hello"]
result = find_palindromes(words_list)
print(result)
