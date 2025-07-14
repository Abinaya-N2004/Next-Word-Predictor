import re
import random
from collections import defaultdict

def preprocess_text(text):
    """
    Cleans and tokenizes the input text.
    Converts to lowercase, removes punctuation, splits into words.
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return words

def build_ngram_model(words, n=2):
    """
    Builds an n-gram model using a dictionary.
    Keys are n-1 word tuples, values are lists of possible next words.
    """
    model = defaultdict(list)
    for i in range(len(words) - n):
        key = tuple(words[i:i + n - 1])
        next_word = words[i + n - 1]
        model[key].append(next_word)
    return model

def predict_next_word(model, seed_text, n=2):
    """
    Predicts the next word based on the last (n-1) words of the input.
    Returns a random next word from the model, or a fallback message.
    """
    seed = tuple(seed_text.lower().split()[-(n - 1):])
    if seed in model:
        return random.choice(model[seed])
    else:
        return "No prediction available."

def main():
    try:
        with open("sample.txt", "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("Error: sample.txt not found.")
        return

    words = preprocess_text(text)

    n = 2  # Use 2 for bigram, 3 for trigram
    model = build_ngram_model(words, n)

    print("✅ Next Word Predictor Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input(f"Enter {n - 1} word(s): ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        prediction = predict_next_word(model, user_input, n)
        print("🔮 Prediction:", prediction)

if __name__ == "__main__":
    main()
