import random
import string

def generate_password(length=12, word=None):
    """Belirtilen uzunlukta ve isteğe bağlı olarak içinde 'word' içeren bir şifre üretir."""
    valid_characters = string.ascii_letters + string.digits + string.punctuation

    if word:
        if len(word) > length:
            raise ValueError("Kelime, şifrenin uzunluğundan daha uzun olamaz.")

        remaining_length = length - len(word)

       
        random_part = ''.join(random.choice(valid_characters) for _ in range(remaining_length))

       
        insert_index = random.randint(0, remaining_length)
        password = random_part[:insert_index] + word + random_part[insert_index:]

        return password

    return ''.join(random.choice(valid_characters) for _ in range(length))
