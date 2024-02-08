def center_text(text, width):
    padding = max(0, (width - len(text)) // 2)
    centered_text = ' ' * padding + text + ' ' * padding
    return centered_text


def prYellow(skk): print("\033[93m {}\033[00m".format(skk))


def prCyan(skk): print("\033[96m {}\033[00m".format(skk))


def prBlue(skk): print("\033[30;41m {}\033[00m".format(skk))


# Gonçalo Marinho [this had a list before but now add its list with a txt]
# Make 2  empty lists
livros = []
emprestimo = []


# ChatGPT, Bruno Moreira and Ihor Berezovskyy
# Read txt file
def read_file():
    """
    Reads data from a text file named "Livros.txt" and populates the 'livros' list.
    """
    # Attempt to open the file "Livros.txt" using (try) for error handling
    try:
        # Open the file "Livros.txt" in read mode with UTF-8 encoding
        with open('Livros.txt', 'r', encoding='utf-8') as file_l:
            # Make loop that loops each line in the file
            for line_l in file_l:
                # Each line is evaluated to be recognized as dictionaries.
                book_dict = eval(line_l.strip())
                # Then are added to the list 'livros'.
                livros.append(book_dict)

        # Open the file "Emprestimos.txt" in read mode with UTF-8 encoding
        with open('Emprestimos.txt', 'r', encoding='utf-8') as file_b:
            # Make loop that loops each line in the file
            for line_b in file_b:
                # Each line is evaluated to be recognized as dictionaries.
                borrow_dict = eval(line_b.strip())
                # Then are added to the list 'livros'.
                emprestimo.append(borrow_dict)
    # If the file is not found, catch the 'FileNotFoundError' exception and print a message.
    except FileNotFoundError:
        print("File 'Livros.txt' or 'Emprestimos.txt' not found.")


# Save txt file
def save_to_file():
    """
    Save data from the 'livros' list to a text file named 'Livros.txt'.
    """
    # Open the file "Livros.txt" in write mode with UTF-8 encoding
    with open('Livros.txt', 'w', encoding='utf-8') as file_l:
        # Make loop that loops each line in the file "Livros.txt"
        for book_dict in livros:
            # Save and add dictionaries from the list "livros" to the file, followed by a newline
            file_l.write(str(book_dict) + '\n')


# Ihor Berezovskyy
# Search book
def search():
    """
    Searches for a book by title, author, or ISBN and print its information.
    """

    # Read output from user and added to the variable "search_term"
    search_term = input("Escreva o titulo, autor ou ISBN do livro pretendido: ")

    # Make a boolean and set it to "False"
    found = False

    # make a loop that loops same amount as the dictionaries in the list "livros"
    for data in livros:
        # Do (if statement) validate by if the variable "search_term" matches
        # the dictionaries items between 'titulo', 'autor' or 'isbn' from list "livros"
        if (search_term.lower() == data['titulo'].lower()
                or search_term.lower() == data['autor'].lower()
                or search_term.lower() == data['isbn'].lower()):
            # then prints the all the items from each dictionary in the list in organized manner
            print(f"\nTítulo: {data['titulo']} "
                  f"\nAutor: {data['autor']} "
                  f"\nISBN: {data['isbn']}"
                  f"\nAno de publicação: {data['ano_publicacao']}"
                  f"\nEditora: {data['editora']}"
                  f"\nCategoria: {data['categoria']}"
                  f"\nGénero: {data['genero']}")
            # and set boolean "found" to be "True"
            found = True

    # Read the output of user [it does nothing but as "enter" input]
    input("\nPressione Enter para continuar: ")

    # Do (if statement) validate by if the boolean "found" is set to "False"
    if not found:
        print(f"the {search_term} was Not Found")


# Rui Conceição
# List all books
def list_book():
    """
    Lists all the books available in the library, and their data.
    """

    # Make a variable and set it to o
    i = 0
    # Make loop that loops until the variable "i" is less than the length of the list 'livros'
    while i < len(livros):
        # Print text and read the variable ("i" + 1) and also read all the dictionaries items from the list "livros"
        print(f"{i + 1} -  Titulo: {livros[i]['titulo']}, Autor: {livros[i]['autor']}, ISBN: {livros[i]['isbn']}, "
              f" Ano Publicação: {livros[i]['ano_publicacao']}, Editora: {livros[i]['editora']}, "
              f" Categoria: {livros[i]['categoria']}, Genero: {livros[i]['genero']}")
        # Add +1 incrementally to the variable "i"
        i += 1

    # Read the output of user [it does nothing but as "enter" input]
    input("Pressione Enter para continuar: ")


# Add book
def add_book():
    """
    Asks the user for inputs regarding the books data, and adds it as a dictionary entry on the main book list.
    """
    # Read the output of user as striped and in uppercase
    resp_add = input("Assegure-se que tem todos os dados necessarios que possam identificar o livro,"
                     " normalmente encontrados nas primeiras paginas do mesmo, e introduza [Y] para continuar."
                     " Introduza [N] para voltar ao menu anterior. \n---->").strip().upper()

    # plus_book = {} (not really need it working without declaring it) Remove this line after reading the code

    isbn_verif = 0
    while resp_add == "Y":
        # asks necessary data to insert the book
        titu = input("Introduza o título do livro: ")
        autor = input("Introduza o autor do livro: ")
        isbn = input("Introduza o ISBN do livro: ").replace("-", "").strip()
        # does checks to make sure the ISBN introduced is in one of the 2 correct lengths,
        # or if it has any non-numeric elements
        while isbn_verif == 0:
            if not isbn.isnumeric():  # Changed from "if isbn.isnumeric() == False" to the "if not isbn.isnumeric()"
                print("O ISBN introduzido não esta correto, algum dos carateres nao e numerico. Tente novamente.")
                isbn = input("Introduza o ISBN do livro: ").replace("-", "").strip()
                # checks if ISBN is introduced on the 2 possible length formats
            elif int(len(isbn)) != 10 and int(len(isbn)) != 13:
                print("O ISBN introduzido não contêm o número correto de carateres. Tente novamente.")
                isbn = input("Introduza o ISBN do livro: ").replace("-", "").strip()
            else:
                isbn_verif = 1
        # asks necessary data to insert the book for the rest
        ano_pub = input("Introduza o ano de publicação do livro: ")
        # asks necessary data to insert the book for the rest once more
        editora = input("Introduza a editora do livro: ")
        cat = input("Introduza a categoria do livro: ")
        gen = input("Introduza o género do livro: ")

        # Ihor Berezovskyy
        # Add values of the quantity of items in the list "livros" with adding +1 then -1
        # Checks how many ID are there in sense and adds a new ID
        id_num = (len(livros) + 1) - 1

        # defines book in order to be added to
        plus_book = {'id': id_num,
                     'titulo': titu,
                     'autor': autor,
                     'isbn': isbn,
                     'ano_publicacao': ano_pub,
                     'editora': editora,
                     'categoria': cat,
                     'genero': gen}

        # the defined data from before is added to the list
        livros.append(plus_book)
        # Save the data to file
        save_to_file()

        # confirms that it has been the book has been added
        print("O livro foi adicionado com sucesso.")

        # checks if you want to add more books, or exit to the menu before
        resp_util = ""
        while resp_util == "":
            resp_util = input(
                "Pretende adicionar um novo livro [Y], ou pretende retornar ao menu anterior [N]? \n").strip().upper()
            if resp_util == "Y":
                add_book()
                break
            if resp_util == "N":
                menu()
                break
            else:
                print("Resposta inválida. Selecione uma das opções possivéis.")


# Remove book
def rem_book():
    """
    Removes book from the dictionary, prints all the books available with all the info showing, so user can choose
    """
    # Make a variable and set it to 0
    rem_veri = 0
    # Print text
    print("Escolha o livro que pretende remover: ")
    # Make loop that loops until the variable "rem_veri" is bigger than the length of the list 'livros'
    while rem_veri < len(livros):
        # Print text and read the variable ("rem_veri" + 1)
        # and also read all the dictionaries items from the list "livros"
        print(rem_veri + 1, "-", livros[rem_veri]['titulo'], ":", livros[rem_veri]['autor'], livros[rem_veri]['isbn'],
              ",", livros[rem_veri]['ano_publicacao'], livros[rem_veri]['editora'], livros[rem_veri]['categoria'],
              livros[rem_veri]['genero'])
        # Add +1 incrementally to the variable "rem_veri"
        rem_veri += 1

    # Read the output of user [it does nothing but as "enter" input]
    resp_num = int(input("Introduza aqui o número do livro--> "))

    # Remove a specific dictionary
    # [!Removed the "pop_book =" it works without it reason pycharm says so!] Remove this line after reading the code
    livros.pop(resp_num - 1)
    # Save Data to file
    save_to_file()

    # Make a variable and set it "blank"
    resp_util = ""
    # Make loop that loops until the variable "resp_util" is not empty
    while resp_util == "":
        # Read output from user
        resp_util = input("Pretende continuar a remover [Y], ou voltar ao menu [N]? \n")
        # Do (if statement) validate by if the variable is set to "Y" then use function "rem_book" and break at end
        if resp_util == "Y":
            rem_book()
            break
        # Do (if statement) validate by if the variable is set to "N" then use function "menu" and break at end
        if resp_util == "N":
            menu()
            break
        # (else) print text
        else:
            print("Resposta inválida. Selecione uma das opções possivéis.")


# Ihor Berezovskyy
# Borrow book


def borrow():
    """
    Lists to a print text and recognizes which ones are available for borrow
    """

    counter = 0
    # Print text
    print("Escolha o livro que pretende emprestar: ")
    # Make loop that loops until the variable "rem_veri" is bigger than the length of the list 'livros'
    for i in range(len(livros)):
        if livros[i]['disponibilidade'] == 'yes':
            counter += 1
            # Print text and read the variable ("rem_veri" + 1)
            # and also read all the dictionaries items from the list "livros"
            print(counter, "-", livros[i]['titulo'], ":", livros[i]['autor'], livros[i]['isbn'],
                  ",", livros[i]['ano_publicacao'], livros[i]['editora'], livros[i]['categoria'],
                  livros[i]['genero'])


    # Read the output of user [it does nothing but as "enter" input]
    resp_num = int(input("Introduza aqui o número do livro--> ")) - 1

    # defines book to be added to
    plus_borrow = {'retornar': 'Temp change this text to work with "Date"', 'livros_id': resp_num}

    # Replaces the selected book's "disponibilidade" to be no
    livros[resp_num]['disponibilidade'] = 'no'
    # save the files
    save_to_file_book()
    save_to_file_borrow()

    # the defined data from before is added to the list
    emprestimo.append(plus_borrow)

    # Make a variable and set it "blank"
    resp_util = ""
    # Make loop that loops until the variable "resp_util" is not empty
    while resp_util == "":
        # Read output from user
        resp_util = input("Pretende continuar a emprestar mais livros [Y], ou voltar ao menu [N]? \n")
        # Do (if statement) validate by if the variable is set to "Y" then use function "rem_book" and break at end
        if resp_util == "Y":
            rem_book()
            break
        # Do (if statement) validate by if the variable is set to "N" then use function "menu" and break at end
        if resp_util == "N":
            menu()
            break
        # (else) print text
        else:
            print("Resposta inválida. Selecione uma das opções possivéis.")

# Gonçalo Marinho
# Main menu
def menu():
    # Make a variable and set it to 0
    opcao = 0

    prBlue(center_text('GESTÃO DE LIVROS', 40))
    # Make Loop that loops until the variable "opcao" is set to 6
    while opcao != 6:
        # Print text with newline on start and end
        prYellow('\nPor favor escolha uma opção.\n')
        # Print 6 texts
        prCyan("[ 1 ] Adicionar Livro")
        prCyan("[ 2 ] Remover")
        prCyan("[ 3 ] Listar")
        prCyan("[ 4 ] Procurar")
        prCyan("[ 5 ] Emprestar")
        prCyan("[ 6 ] SAIR")
        # Read the output of user
        opcao = input("---> ")

        # Do (if statement) validate by if the variable "opcao" is set 1
        # then for all (if statement) and (else if) print text except the functions each has their own
        if opcao == "1":
            print("Opção 1 selecionada: Adicionar Livro")
            # Add book
            add_book()
        # Do (else if) validate by if the variable "opcao" is set 2
        elif opcao == "2":
            print("Opção 2 selecionada: Remover")
            # Remove book
            rem_book()
        # Do (else if) validate by if the variable "opcao" is set 3
        elif opcao == "3":
            # List all books
            list_book()
        # Do (else if) validate by if the variable "opcao" is set 4
        elif opcao == "4":
            print("Opção 4 selecionada: Procurar")
            # Search book
            search()
        # Do (else if) validate by if the variable "opcao" is set 5
        elif opcao == "5":
            print("Opção 5 selecionada: Emprestar")
            borrow()
        # Do (else if) validate by if the variable "opcao" is set 6
        elif opcao == "6":
            print("A sair do programa...")
            # Then break the loop
            break
        else:
            # Print text
            print("Opção inválida. Tente de novo.")


# Use to function "read_file"
read_file()
# Use to function "menu"
menu()
# Use to function "save_to_file"
save_to_file()