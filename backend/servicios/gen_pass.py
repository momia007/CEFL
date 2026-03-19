# servicios/gen_pass.py

from werkzeug.security import generate_password_hash

password = input("Ingresá la contraseña: ")
hash = generate_password_hash(password)
print("Hash generado:", hash)
