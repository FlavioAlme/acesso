funcionario=input("gerente,analista,estagiario")
dia_da_semana=input("qual dia da semana?")
if(funcionario=='gerente'):
    print("acesso permitido")
elif(dia_da_semana=="sabado" or dia_da_semana=="domingo"):
    print("acesso negado")
else:
    print("acesso permitido")