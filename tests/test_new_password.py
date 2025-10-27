import string
from password.new_password import generate_password

def test_password_characters():
    global password
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters

"""
Aşağıda önerilenlerden birini kullanarak başka bir test yazın. Alternatif olarak, kendi testinizi de oluşturabilirsiniz!
Daha fazla test yazabilirseniz harika olur!

1. Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test edin  
2. Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test edin 
"""

def test_pw_length():
    global pw_length
    pw_length = 100
    password = generate_password(pw_length)
    assert len(password) == pw_length

def test_pw_twice():
    passwords = []
    
    for i in range(2):
        password = generate_password(12)
        passwords.append(password)

    assert passwords[0] != passwords[1]

def test_pw_length_above_zero():
    assert pw_length > 1
