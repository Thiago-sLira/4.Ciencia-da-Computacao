try:
    with open("exercicio.txt", "r") as file:
        file_content = file.read()
        file_content_list = file_content.split()
        grades = []
        names = []
        reproved = []
        for content in file_content_list:
            if content.isdigit():
                grades.append(content)
            else:
                names.append(content)
        for grade in grades:
            if int(grade) < 6:
                reproved.append(names[grades.index(grade)])

    # with open("recuStudents.txt", mode="w") as recu_students_file:
    #     print(reproved)
    # recu_students_file.writelines()

except FileNotFoundError:
    # será executado caso haja a exceção 'FileNotFoundError'
    print("Arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    for student in reproved:
        print(student)
    print("Arquivo manipulado e fechado com sucesso")
finally:
    # será sempre executado, independentemente de erro
    print("Fim da tentativa de ler o arquivo")
