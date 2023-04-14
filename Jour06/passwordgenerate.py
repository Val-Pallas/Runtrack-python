import os, string

def get_pass(password_len=12):
  new_password=None
  symbols='+!'
  chars=string.ascii_lowercase+\
        string.ascii_uppercase+\
        string.digits+\
        symbols

  while new_password is None or \
        new_password[0] in string.digits or \
        new_password[0] in symbols:
     new_password=''.join([chars[ord(os.urandom(1)) % len(chars)] \
                             for i in range(password_len)])
  return new_password

print(get_pass())