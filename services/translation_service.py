import string

# Constants
VOWELS = "aeiouAEIOU"
PUNCTUATION = string.punctuation

def has_punctuation(word: str) -> str:
    """Check if a word ends with punctuation and return the punctuation character."""
    if word[-1] in PUNCTUATION:
        return word[-1]
    return ''

def remove_punctuation(word: str) -> str:
    """Remove punctuation from the end of a word."""
    return word[:-1] if word[-1] in PUNCTUATION else word

def is_uppercase(word: str) -> bool:
    """Check if the word starts with an uppercase letter."""
    return word[0].isupper()

def translate_vowel_start(word: str) -> str:
    """Translate words that start with a vowel by appending 'ay'."""
    return word + 'ay'

def translate_consonant_start(word: str) -> str:
    """Translate words that start with a consonant by moving consonants to the end."""
    consonant_prefix = ''
    for i, char in enumerate(word):
        if char.lower() not in VOWELS:
            consonant_prefix += char
        else:
            word = word[i:]
            break
    return word + consonant_prefix.lower() + 'ay'

def capitalize_word(word: str, is_uppercase: bool) -> str:
    """Capitalize the word if it originally started with an uppercase letter."""
    if is_uppercase:
        return word.capitalize()
    return word

def consonant_translation(text: str) -> str:
    """Translate a text into Pig Latin by handling vowels, consonants, and punctuation."""
    translated_words = []

    for word in text.split():
        # Handle punctuation
        punctuation = has_punctuation(word)
        word_without_punctuation = remove_punctuation(word)

        # Check if the word starts with an uppercase letter
        is_word_uppercase = is_uppercase(word_without_punctuation)

        # Translate based on whether the word starts with a vowel or consonant
        if word_without_punctuation[0].lower() in VOWELS:
            translated_word = translate_vowel_start(word_without_punctuation)
        else:
            translated_word = translate_consonant_start(word_without_punctuation)

        # Capitalize the word if needed and add punctuation back
        translated_word = capitalize_word(translated_word, is_word_uppercase) + punctuation

        # Append the translated word to the list
        translated_words.append(translated_word)

    return ' '.join(translated_words)
