print("Seja bem-vindo a biblioteca do Nícolas Antônio")
print("\n")

lista_livro = []
livros = {}
id_global = 0

def cadastrar_livro(id):
  print("-" * 10 + "Menu Cadastrar Livro" + "-" * 10)
  nome_livro = input("Qual o nome do livro que deseja cadastrar? ").title()
  autor_livro = input("Digite o nome do autor desse livro: ").title()
  editora_livro = input("Entre com o nome da editora do livro: ").title()

      
  for livro in lista_livro:
    if livro["Autor"] == autor_livro:
      print(f"São Cadastrados mais de 2 livros com o Autor: {autor_livro}")
  livros = {"id": id, "Nome": nome_livro, "Autor": autor_livro, "Editora": editora_livro}
  lista_livro.append(livros.copy())

def consultar_livro():
  while True:
    print("\n")
    print("-" * 10 + "Menu Consultar Livro" + "-" * 10)
    print("Escolha a opção desejada:")
    print("1 - Consultar Todos")
    print("2 - Consultar por ID")
    print("3 - Consultar por Autor")
    print("4 - Retornar ao Menu")

    opcao = int(input(">> "))

    if(opcao == 1):
      for livro in lista_livro:
        print(f"Id: {livro['id']}")
        print(f"Nome: {livro['Nome']}")
        print(f"Autor: {livro['Autor']}")
        print(f"Editora: {livro['Editora']}")
        print("\n")

    elif(opcao == 2):
      pesquisa_ID = int(input("Digite o Id do livro: "))
      livro = next((l for l in lista_livro if l["id"] == pesquisa_ID), None)
      if livro:
        print(f"Id: {livro['id']}")
        print(f"Nome: {livro['Nome']}")
        print(f"Autor: {livro['Autor']}")
        print(f"Editora: {livro['Editora']}")
        print("\n")

    elif(opcao == 3):
      pesquisa_Escritor = input("Digite o autor do(s) livro(s): ").title()
      livro_Encontrado = [l for l in lista_livro if l["Autor"] == pesquisa_Escritor]
      for livro in livro_Encontrado:
        print(f"Id: {livro['id']}")
        print(f"Nome: {livro['Nome']}")
        print(f"Autor: {livro['Autor']}")
        print(f"Editora: {livro['Editora']}")
        print("\n")

    elif(opcao == 4):
      break

    else:
      print("Opção inválida! \n")
      continue

def remover_livro():
  print("-" * 10 + "Menu Remover Livro" + "-" * 10)
  deletar_por_ID = int(input ("Digite o Id do livro a ser removido:"))
  for livro in lista_livro:
    if livro["id"] == deletar_por_ID:
      lista_livro.remove(livro)
      return


while True:
  print("-" * 10 + "Menu Principal" + "-" * 10)
  try:
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar Programa")

    opcao_inicial = int(input(">> "))
    if opcao_inicial == 1:
      cadastrar_livro(id_global)
      id_global += 1
      print("\n")

    elif opcao_inicial == 2:
      consultar_livro()
      print("\n")

    elif opcao_inicial == 3:
      remover_livro()
      print("\n")
    elif opcao_inicial == 4:
      break
    else:
      continue
  except ValueError:
      print("Valor não numérico.")
      print("Por favor, entre com o indice das opções.\n")
      continue
