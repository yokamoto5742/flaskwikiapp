from passlib.hash import sha256_crypt


def hash_password(password):
    # パスワードをハッシュ化
    hashed_password = sha256_crypt.hash(password)

    # ハッシュ値を120文字以内に切り詰める
    truncated_password = hashed_password[:120]

    return truncated_password


# パスワードをハッシュ化
password = "your_password"
hashed_password = hash_password(password)

print("Hashed Password:", hashed_password)
