
print("Simple Text Analysis Tool")

text = input("Enter your text: ")

print("\nAnalysis Results:")

words = text.split()
word_count = len(words)
print("1. Total number of words:", word_count)

space_count = 0
for char in text:
    if char == ' ':
        space_count = space_count + 1
print("2. Number of spaces:", space_count)


clean_text = ""
for char in text.lower():
    if char.isalpha() or char == ' ':
        clean_text = clean_text + char

words = clean_text.split()
word_freq = {}


for word in words:
    if word in word_freq:
        word_freq[word] = word_freq[word] + 1
    else:
        word_freq[word] = 1

print("3. Word frequencies:", word_freq)


top_words = []
for i in range(3):
    max_word = ""
    max_count = 0
    for word in word_freq:
        already_selected = False
        for selected_word, selected_count in top_words:
            if word == selected_word:
                already_selected = True
                break
        
        if not already_selected and word_freq[word] > max_count:
            max_word = word
            max_count = word_freq[word]
    
    if max_word:
        top_words.append((max_word, max_count))

print("   Top 3 most frequent words:")
for i in range(len(top_words)):
    word = top_words[i][0]
    freq = top_words[i][1]
    print("   " + str(i + 1) + ". '" + word + "' appears " + str(freq) + " times")


vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count = vowel_count + 1
print("4. Number of vowels:", vowel_count)


char_list = []
for char in text:
    char_list.append(char)

# Bubble sort in descending order
n = len(char_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if char_list[j] < char_list[j + 1]:
            # Swap elements
            temp = char_list[j]
            char_list[j] = char_list[j + 1]
            char_list[j + 1] = temp

# Convert back to string
sorted_text = ""
for char in char_list:
    sorted_text = sorted_text + char

print("5. Text in reverse ascending order:", sorted_text)

print("-" * 40)
print("Analysis complete!")

