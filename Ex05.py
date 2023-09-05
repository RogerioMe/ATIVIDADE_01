nivel=input('Digite o nível de acesso: ').upper()
if nivel=='ADM' or nivel=='USUARIO':
    genero=input('Digite o seu genero: ').upper()
    if nivel=='ADM':
        if genero=='FEMININO':
            print('Ola Administradora!')
        else:
            print('Ola Administrador!')

    else:
        if genero=='FEMININO':
            print('Ola Usuária!')
        else:
            print('Ola Usuário!')