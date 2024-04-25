from node_search_tree import Node


# Función para insertar una palabra en el árbol
def insertar(root, word, filename):
    if root is None:
        return Node(word, filename)
    elif word < root.data:
        root.left = insertar(root.left, word, filename)
    elif word > root.data:
        root.right = insertar(root.right, word, filename)
    else:
        root.count += 1
        root.files.add(filename)
    return root


# Función para buscar una palabra en el árbol y devolver su frecuencia y en qué archivos aparece
def buscar(root, word):
    if root is None:
        return 0, set()
    elif word < root.data:
        return buscar(root.left, word)
    elif word > root.data:
        return buscar(root.right, word)
    else:
        return root.count, root.files


# Función para procesar el archivo y construir el árbol correspondiente
def process_file(filename):
    root = None
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.strip().lower()
                if word.isalpha():
                    if root is None:
                        root = Node(word, filename)
                    else:
                        root = insertar(root, word, filename)  # Insertar palabras como hijos
    return root


def inorder_traversal(root, filename):
    if root:
        inorder_traversal(root.left, filename)
        print(root.data, root.count, filename)
        inorder_traversal(root.right, filename)


# Función principal
def main():
    files = ["archivo_1.txt", "archivo_2.txt", "archivo_3.txt", "archivo_4.txt", "archivo_5.txt",
             "archivo_6.txt", "archivo_7.txt", "archivo_8.txt", "archivo_9.txt", "archivo_10.txt"]

    roots = {}  # Diccionario para los árboles de cada archivo
    for file in files:
        roots[file] = process_file(file)

    while True:
        print("\nMenu:")
        print("1. Mostrar palabras en un archivo")
        print("2. Buscar una palabra en todos los archivos")
        print("3. Salir")

        option = input("Ingrese su elección: ")

        if option == "1":
            print("Seleccione un archivo:")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            file_index = int(input("Ingrese el número del archivo: ")) - 1
            if 0 <= file_index < len(files):
                filename = files[file_index]
                print(f"\nPalabras en {filename} (Inorder):")
                inorder_traversal(roots[filename], filename)
            else:
                print("Número de archivo inválido.")
        elif option == "2":
            word = input("Ingrese la palabra a buscar: ").strip().lower()
            print(f"Buscando la palabra '{word}' en todos los archivos:")
            total_count = 0
            for filename, root in roots.items():
                count, files = buscar(root, word)
                total_count += count
                print(f"'{word}' aparece {count} veces en '{filename}'")
            print(f"\nLa palabra '{word}' aparece {total_count} veces en todos los archivos.")
        elif option == "3":
            print("Fin del programa")
            break
        else:
            print("Seleccione una opción válida")


# Llamada a la función principal del programa
main()
