# itextual/main.py
from itextual.models import Nota
from itextual.storage import (
    listar_categorias,
    adicionar_categoria,
    deletar_categoria,
    visualizar_nota,
    deletar_nota,
    listar_notas,
    salvar_nota,
    carregar_categorias,
    salvar_categorias
)

def main():
    print("Bem-vindo ao ITextual!")
    while True:
        print("\n1. Criar nota")
        print("2. Gerenciar categorias")
        print("3. Visualizar nota")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título da nota: ")
            texto = input("Digite o texto da nota: ")
            print("Categorias disponíveis:")
            categorias = listar_categorias()
            for i, cat in enumerate(categorias, start=1):
                print(f"{i}. {cat}")
            categoria_index = int(input("Escolha a categoria pelo número: ")) - 1
            if categoria_index < 0 or categoria_index >= len(categorias):
                print("Categoria inválida.")
                continue
            categoria = categorias[categoria_index]
            classe = input("Classe (efemeras/solidas/historicas): ").lower()
            nota = Nota(titulo, texto, categoria, classe)
            salvar_nota(nota)


        elif opcao == "2":
            print("\n1. Adicionar categoria")
            print("2. Listar categorias")
            print("3. Deletar categorias")
            sub_opcao = input("Escolha uma opção: ")

            if sub_opcao == "1":
                nova_categoria = input("Digite o nome da nova categoria: ").strip().lower()
                adicionar_categoria(nova_categoria)
            elif sub_opcao == "2":
                categorias = listar_categorias()
                print("Categorias disponíveis:")
                for cat in categorias:
                    print(f"- {cat}")
            elif sub_opcao == "3":
                deletar_categoria()

        elif opcao == "3":
            visualizar_nota()

        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

