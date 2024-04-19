from passlib.hash import pbkdf2_sha256



def hash(password: str):
    return pbkdf2_sha256.hash(password)

def verify(plain, hashed_p):
    return pbkdf2_sha256.verify(plain, hashed_p)