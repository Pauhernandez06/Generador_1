import random

contraseña = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitudcontraseña = int(input("Introduce la longitud de tu contraseña: "))

password = ""
for i in range(longitudcontraseña):
    password += random.choice(contraseña)

print(password)
