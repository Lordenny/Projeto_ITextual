import os
import json
import shutil

BASE_DIR = "notas"
CATEGORIAS_FILE = "categorias.json"

def salvar_nota(nota):
    categoria_dir = os.path.join(BASE_DIR, nota.categoria)
    if not os.path.exists(categoria_dir):
        os.makedirs(categoria_dir)
    nota_filename = f"{nota.titulo}.md"
    with open(os.path.join(categoria_dir, nota_filename), 'w') as file:
        file.write(nota.texto)


def listar_notas(categoria):
    dir_path = os.path.join(BASE_DIR, categoria)
    if not os.path.join(dir_path):
        print(f"Nenhuma nota encontrada {categoria}.")
        return []
    return os.listdir(dir_path)


def carregar_categorias():

    try:
        with open("categorias.json", "r") as f:
          return json.load(f)
    except json.JSONDecodeError:
        return []


def salvar_categorias(categorias):
    with open(CATEGORIAS_FILE, "w", encoding = "utf-8") as f:
        json.dump(categorias, f, indent = 4)   

def adicionar_categoria(categoria):
    categorias = carregar_categorias()
    if categoria not in categorias:
        categorias.append(categoria)
        salvar_categorias(categorias)
        os.makedirs(os.path.join(BASE_DIR, categoria), exist_ok = True)
        print(f"Categoria '{categoria}' adicionada com sucesso!")
    else:
        print(f"Categoria '{categoria}' já existe.")

def visualizar_nota():
    categorias = listar_categorias()
    print("Categorias disponíveis:")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i}. {cat}")
    categoria_index = int(input("Escolha a categoria pelo número: ")) - 1
    if categoria_index < 0 or categoria_index >= len(categorias):
        print("Categoria inválida.")
        return
    categoria = categorias[categoria_index]
    notas = listar_notas(categoria)
    if notas:
        for i, nota in enumerate(notas, start=1):
            print(f"{i}. {nota}")
        nota_index = int(input("Escolha a nota pelo número: ")) - 1
        if nota_index < 0 or nota_index >= len(notas):
            print("Nota inválida.")
            return
        nota_selecionada = notas[nota_index]
        with open(os.path.join(BASE_DIR, categoria, nota_selecionada), 'r') as file:
            conteudo = file.read()
        print(f"\n{conteudo}")
    else:
        print("Nenhuma nota encontrada.")

def listar_categorias():
    return carregar_categorias()

def deletar_nota():
    categorias = listar_categorias()
    print("Categorias disponíveis:")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i}. {cat}")
    categoria_index = int(input("Escolha a categoria pelo número: ")) - 1
    if categoria_index < 0 or categoria_index >= len(categorias):
        print("Categoria inválida.")
        return
    categoria = categorias[categoria_index]
    notas = listar_notas(categoria)
    if notas:
        for i, nota in enumerate(notas, start=1):
            print(f"{i}. {nota}")
        nota_index = int(input("Escolha a nota pelo número: ")) - 1
        if nota_index < 0 or nota_index >= len(notas):
            print("Nota inválida.")
            return
        nota_selecionada = notas[nota_index]
        os.remove(os.path.join(BASE_DIR, categoria, nota_selecionada))
        print(f"Nota '{nota_selecionada}' deletada com sucesso.")
    else:
        print("Nenhuma nota encontrada.")

def deletar_categoria():
    categorias = listar_categorias()
    print("Categorias disponíveis:")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i}. {cat}")
    categoria_index = int(input("Escolha a categoria pelo número: ")) - 1
    if categoria_index < 0 or categoria_index >= len(categorias):
        print("Categoria inválida.")
        return
    categoria = categorias[categoria_index]
    notas = listar_notas(categoria)
    if notas:
        for nota in notas:
            os.remove(os.path.join(BASE_DIR, categoria, nota))
        os.rmdir(os.path.join(BASE_DIR, categoria))
        categorias.remove(categoria)
        salvar_categorias(categorias)
        print(f"Categoria '{categoria}' deletada com sucesso.")
    else:
        print("Nenhuma nota encontrada.")