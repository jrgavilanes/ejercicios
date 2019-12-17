import bcrypt


stored_password = '$2b$12$xblMW.aLVr/gMeKphGo76OTIPERbKrBR5K.d34Ngx6m4D1a9XUrxS'

texto_plano = "encripta este texto en español"
semilla = bcrypt.gensalt()

texto_hasheado = bcrypt.hashpw(texto_plano.encode(), semilla)

print(texto_plano, texto_hasheado.decode())


if bcrypt.checkpw(texto_plano.encode(),stored_password.encode()):
    print("me cuadra")
else:
    print("no me cuadra")


if bcrypt.checkpw(texto_plano.encode(),texto_hasheado):
    print("me cuadra")
else:
    print("no me cuadra")
