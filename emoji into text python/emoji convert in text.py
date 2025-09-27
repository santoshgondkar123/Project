emoji_dict = {
    "love": "❤️",
    "happy": "😊",
    "smile": "😄",
    "pizza": "🍕",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "star": "⭐"
}

text = input("Enter your sentence: ")

words = text.split()

output_words = []
for word in words:
    lower_word = word.lower()
    if lower_word in emoji_dict:
        output_words.append(emoji_dict[lower_word])
    else:
        output_words.append(word)

final_text = " ".join(output_words)

print("Emoji Text:", final_text)
