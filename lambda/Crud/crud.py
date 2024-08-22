def main():
    lista_funcionarios = []
    resp = 1

    while (resp != 0):
        print("1- Inserir Funcionário")
        print("2- Alterar Funcionário")
        print("3- Excluir Funcionário")
        print("4- Exibir Funcionário")
        opc = int(input("Digite a opção desejada(1-4): "))
        match opc:
            case 1:
                inserir_funcionario((lista_funcionarios))
            case 2:
                nome_func = input("Digite o funcionário a ser alterado: ")
                indice = buscar_nome_funcionario(lista_funcionarios, nome_func)
                if(indice != -1):
                    alterar_funcionario(lista_funcionarios, indice)
                else:
                    print("Funcionário encontrado")
            case 3:
                nome_func = input("Digite o funcionário a ser excluido: ")
                indice = excluir_funcionario(lista_funcionarios, nome_func)
                if (indice != -1):
                    alterar_funcionario(lista_funcionarios, indice)
                else:
                    print("Funcionário não encontrado")
            case 4:
                exibir_funcionarios(lista_funcionarios)
        resp = input("Deseja continuar (1-SIM/0-NÃO): ")


def inserir_funcionario(lista_funcionarios):
    try:
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        salario = input("Digite o salario: ")
    except ValueError:
        print("Digite número para idade e salarios")
    else:
        funcionario = {"Nome": nome, "Idade": idade, "Salario":salario}
        lista_funcionarios.append(funcionario)
    finally:
        print("Operação Finalizada")

def buscar_nome_funcionario(lista_funcionarios, nome_func):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if(lista_funcionarios[i] ['Nome'] == nome_func):
            indice = i
    return(indice)

def alterar_funcionario(lista_funcionarios, indice):
    try:
        print(f"Nome :{lista_funcionarios[indice]['Nome']}")
        nome = input("Digite o novo nome: ")
        print(f"Idade :{lista_funcionarios[indice]['Idade']}")
        idade = input("Digite a nova idade: ")
        print(f"Salario :{lista_funcionarios[indice]['Salario']}")
        salario = input("Digite o novo salario: ")
    except ValueError:
        print("Digite número para idade e salarios")
    else:
        lista_funcionarios[indice]['Nome'] = nome
        lista_funcionarios[indice]['Idade'] = idade
        lista_funcionarios[indice]['Salario'] = salario
        print("Dados aterados com sucesso")
    finally:
        print("Operação Finalizada")


def excluir_funcionario(lista_funcionarios, indice):
    lista_funcionarios.pop(indice)
    print("Funcionário com sucesso")

def exibir_funcionarios(lista_funcionarios):
    for i in range(len(lista_funcionarios)):
        for chave,valor in lista_funcionarios[i].items():
            print(f"{chave}: {valor}")
        print("----------------------------------------------")

if __name__ == "__main__":
    main()