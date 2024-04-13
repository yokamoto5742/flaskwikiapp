from passlib.hash import sha256_crypt
from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password):
    # パスワードをハッシュ化
    hashed_password = sha256_crypt.hash(password)

    # ハッシュ値を120文字以内に切り詰める
    truncated_password = hashed_password[:120]

    return truncated_password


def set_password(password):
    setted_password = generate_password_hash(password)
    return setted_password


# パスワードをハッシュ化
password = "your_password"
hashed_password = hash_password(password)
setted_password = set_password(password)

print("Hashed Password:", hashed_password)
print("Setted Password:", setted_password)
