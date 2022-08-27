banco_de_dados = {}

def set_usuarios():
    primeiro_nome = input('Primeiro nome: ')
    sobrenome = input('Sobrenome: ')
    email = input(
        'E-mail: ') + '@gmail.com'  # colocar @gmail.com no final de emails, é uma regra de negócios que foi definida
    senha = input('Senha: ')
    confirmar_senha = input('Confirmar senha: ')

    # vamos começar a implementar as regras de negócios ao banco de dados

    if len(primeiro_nome) < 3:
        return {'msg': f'Muito curto: {primeiro_nome}'}

    banco_de_dados['primeiro nome'] = primeiro_nome  # criando dados dinâmicamente
    banco_de_dados['sobrenome'] = sobrenome
    banco_de_dados['email'] = email
    banco_de_dados['senha'] = senha
    banco_de_dados['confirmar senha'] = confirmar_senha


print(set_usuarios())  # estou chamando a função que eu criei
print(banco_de_dados)