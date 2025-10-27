import string
from password.new_password import generate_password

def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters

def test_password_length():
    length = 100
    password = generate_password(length)
    assert len(password) == length


def test_password_twice():
    length = 13
    password1 = generate_password(length)
    password2 = generate_password(length)
    assert password1 != password2



def test_password_too_big():
    length = 200000
    password = generate_password(length)
    assert len(password) == length


def test_password_negative_length():
    length = -20
    password = generate_password(length)
    assert password == "Uzunluk sıfırdan büyük olmalıdır"


def test_password_string_length():
    length = "asd"
    password = generate_password(length)
    assert password == "Sayısal bir değer girin"

def test_password_include_space():
    length=100000
    password = generate_password(length)
    if " " in password:
        sonuc = "bulundu"
    else:
        sonuc = "bulunmadı" 
    assert sonuc == "bulunmadı"

