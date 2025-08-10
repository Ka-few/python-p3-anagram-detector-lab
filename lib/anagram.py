class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        # Sort the letters of the initialized word
        sorted_word = ''.join(sorted(self.word))
        # Return list of words that are anagrams (same sorted letters, case-insensitive)
        return [w for w in words if ''.join(sorted(w.lower())) == sorted_word and w.lower() != self.word]
# your code goes here!
# word = input("Enter a word: ")
# word_list = input("Enter a list of words to check for anagrams (comma-separated): ").split(',')
# word_list = [w.strip() for w in word_list]
# anagram = Anagram(word)
# result = anagram.match(word_list)
# print(f"Anagrams of '{word}': {result}")