import bcrypt

def hash_pw_wrapper(pw):
    return bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())

if __name__ == '__main__':
    pw = input('Enter your pw: ')
    print(hash_pw_wrapper(pw).decode('utf-8'))