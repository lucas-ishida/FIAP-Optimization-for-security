access = input("Ola qual e o sue nivel de acesso?")
access_pad = access.lower()
if access_pad != "adm" and access_pad != "usr" and access_pad != "guest":
    print ("Ola Desconhecido.")
elif access_pad == "guest":
    print ("Ola Visitante.")
else:    
    genre = input("Qual e o seu genero (Masculino ou feminino)")
    genre_pad = genre.lower()  
    if genre_pad != "masculino" and genre_pad != "feminino":
        print ("Digite seu genero corretamente (Masculino ou Feminino)")
    else:
        if access_pad == "adm" and genre_pad == "masculino":
            print ("Ola administrador")
        elif access_pad == "adm" and genre_pad == "feminino":
            print ("Ola Administradora")
        elif access_pad == "usr" and genre_pad == "masculino":
            print ("Ola Usuario")
        elif access_pad == "usr" and genre_pad == "feminino":
            print ("Ola Usuaria")
        else:
            print ("Ola Desconhecido")
