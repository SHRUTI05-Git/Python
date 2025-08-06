# Simple program to compare two paragraphs - Beginner level

print("Simple Paragraph Comparison Tool")
print("=" * 40)

# Get two paragraphs from user
print("Enter first paragraph:")
paragraph1 = input()

print("Enter second paragraph:")
paragraph2 = input()

print("\nResults:")
print("-" * 20)

# Make both paragraphs lowercase for easy comparison
paragraph1 = paragraph1.lower()
paragraph2 = paragraph2.lower()

# Split paragraphs into words
words1 = paragraph1.split()
words2 = paragraph2.split()

print("Words in paragraph 1:", words1)
print("Words in paragraph 2:", words2)

# 1. Find unique words in paragraph 1
unique_words1 = []
for word in words1:
    if word not in unique_words1:
        unique_words1.append(word)

print("\n1. Unique words in paragraph 1:")
print(unique_words1)
print("Total unique words in paragraph 1:", len(unique_words1))

# Find unique words in paragraph 2
unique_words2 = []
for word in words2:
    if word not in unique_words2:
        unique_words2.append(word)

print("\nUnique words in paragraph 2:")
print(unique_words2)
print("Total unique words in paragraph 2:", len(unique_words2))

# 2. Find common words
common_words = []
for word in unique_words1:
    if word in unique_words2:
        common_words.append(word)

print("\n2. Common words in both paragraphs:")
print(common_words)
print("Total common words:", len(common_words))

# 3. Find total unique words in both paragraphs
all_words = []

# Add words from paragraph 1
for word in unique_words1:
    all_words.append(word)

# Add words from paragraph 2 (only if not already added)
for word in unique_words2:
    if word not in all_words:
        all_words.append(word)

print("\n3. All unique words from both paragraphs:")
print(all_words)
print("Total unique words in both paragraphs:", len(all_words))

print("\n" + "=" * 40)
print("Done!")