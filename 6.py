user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in user_input if char in vowels)
print("Number of vowels:", vowel_count)
