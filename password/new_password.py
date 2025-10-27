import random
import string

def generate_password(length=12):
    """Belirtilen uzunlukta rastgele bir şifre oluşturur."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    try:
        length = int(length)
        if length > 0:
            for i in range(length):
                password += random.choice(characters)
            return password
        else:
            return "Uzunluk sıfırdan büyük olmalıdır"
    except:
        return "Sayısal bir değer girin"

# Kullanım örneği
password_length = "asd"  # İstediğiniz herhangi bir şifre uzunluğunu seçebilirsiniz
#print("Yeni şifreniz:", generate_password(password_length))
for i in range(20):
    x = generate_password(password_length)
    if " " in x:
        print(" Boşluk varmış")
    else:
        print("Boşluk yokmuş")
