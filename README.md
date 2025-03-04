# Projeto_ITextual
ITextual é um programa de anotações simples e eficiente, permitindo a organização por categorias e classes. Criado inicialmente totalmente em python para ser usado sem interface gráfica , o projeto visa expansões futuras para web, Android e sincronização entre dispositivos.

# Recursos básicos
- Criação de notas personalizadas.
- Sistema de classificação na [Metodologia (ESH)](metodologia.md)
- Armazenamento baseado em arquivos de texto por categoria ( personalizável)
- Suporte a Markdown ( em construção!)

# Estrutura do Projeto

```
ProjetoITextual/
│
├── itextual/
│   ├── __init__.py
│   ├── main.py        # Arquivo principal
│   ├── models.py      # Definição de classes
│   ├── storage.py     # Manipulação de arquivos
│
├── notas/             # Diretório para armazenar notas
│   ├── efemeras/
│   ├── solidas/
│   └── historicas/
│
└── categorias.json     # Armazena as categorias
```

# Instalação

1. Clone o repositório:
```
git clone https://github.com/Lordenny/Projeto_Itextual
cd Projeto_Itextual
```
2. Certifique-se de que o Python 3 está instalado.
3. Execute o programa:
```
python -m itextual.main
```

# Como usar
1. Escolha uma das opções do menu:
- Criar uma nova nota.
- Listar notas existentes.
- Gerenciar categorias.
- Sair do programa.

2. As notas serão salvas em arquivos .md dentro das respectivas categorias

# Futuras Implementações

1. **Implementar Expiração para Notas Efêmeras**
- Criar um sistema para deletar automaticamente notas após X dias.
- Poder configurar manualmente o tempo de expiração.

2. **Indexação e Busca**
- Criar um mecanismo de busca por palavra-chave, data ou categoria.
- Implementar uma CLI para facilitar o acesso às notas via terminal.

3. **Histórico de Alterações para Notas Sólidas**
- Armazenar versões anteriores de uma nota (tipo git para textos).

4. **Exportação e Backup**
- Opção de exportar notas para .md, .txt ou .json.
- Criar backups automáticos das notas históricas.

5. **Integração com Notificações**
- Notificações para lembrar de notas efêmeras antes de expirarem.

6. **Modo de Sincronização Local**
- Criar uma funcionalidade para sincronizar notas entre PCs via Wi-Fi ou servidor local.

7. **Interface Gráfica**
- Um pequeno app em PyQt ou Tkinter para gerenciar as notas visualmente.

8. **Criptografia e bloqueio**
- Sistema de criptografia para notas históricas e bloqueio de edição

# Licença
Este projeto está licenciado sob a MIT License.