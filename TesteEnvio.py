escolha = input("Escolha: Juan ou Gustavo\n")

match escolha:
    case "Juan":
        print("Juan:\n")
        print("Olha a olha onda olha a onda pan pan")

    case "Gustavo":
        print("Gustavo:\n")
        print("VI BRASIL:")

    case _:
        print("Opa chefia, se pa que tu errou o nome, letra maiscula importa.")