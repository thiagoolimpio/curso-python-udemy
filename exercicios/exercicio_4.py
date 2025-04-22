#peça ao usuario o nome dele
#peça ao usuario para digitar a idade dele 
#se o nome e idade forem digitados, exiba:
#seu nome é {nome}
#seu nome invertido é {nome_invertido}
#seu nome contém espaços {ou nao} espaços
#seu nome tem {n} letras 
#a primeira letra do seu nome é {letra}
#a ultima letra do seu nome é {letra}
#se nada for digitado exiba : nada foi digitado, voce deixou campos incompletos

nome = input('digite seu nome: ')
idade = input("Digite sua idade: ")
if nome and idade :   
    print(f"Seu nome é {nome} ")
    print("Seu nome invertido é: ", (nome[::-1]) )
if nome and idade:
    print("Seu nome tem:", (len(nome)), "letras")
if nome and idade:
    print("a primeira letra do seu nome é:", (nome[0]))
    print("A ultima letra do seu nome é:", (nome[5]))
else:
    print("Campo vazio, nao podemos prosseguir!")
    



