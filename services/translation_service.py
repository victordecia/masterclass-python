import string

def consonant_translation(text: str) -> str:
    vowels = "aeiouAEIOU"
    translated_words = []

    for word in text.split():
        punctuation = ''
        if word[-1] in string.punctuation:
            punctuation = word[-1]
            word = word[:-1]

        is_uppercase = word[0].isupper()

        if word[0].lower() in vowels:
            translated_word = word + 'ay'
        else:
            consonant_prefix = ''
            for i, char in enumerate(word):
                if char.lower() not in vowels:
                    consonant_prefix += char
                else:
                    word = word[i:]
                    break

            translated_word = word + consonant_prefix.lower() + 'ay'

        if is_uppercase:
            translated_word = translated_word.capitalize()

        translated_word += punctuation
        translated_words.append(translated_word)

    return ' '.join(translated_words)
