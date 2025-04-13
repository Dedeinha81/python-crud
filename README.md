CRUD de Usuários com Python e SQLite
Este é um projeto básico que permite gerenciar usuários em um banco de dados. Com ele, você pode adicionar, ver, atualizar e excluir usuários usando Python e SQLite.

O que o Projeto Faz
Este programa tem quatro funções principais:

Adicionar Usuário: Cria um novo registro de usuário com nome, email e idade.
Ler Usuários: Mostra todos os usuários cadastrados.
Atualizar Usuário: Atualiza as informações de um usuário existente usando seu id.
Deletar Usuário: Remove um usuário do banco de dados usando seu id.
Como Funciona
O projeto usa SQLite para salvar os dados em um arquivo chamado usuarios.db. A estrutura do banco de dados é bem simples, com uma tabela (usuarios) que contém:

id: número único para cada usuário.
nome: nome do usuário.
email: email do usuário.
idade: idade do usuário.
Esses dados são salvos no arquivo usuarios.db, permitindo que você mantenha as informações mesmo após fechar o programa.

Como Usar o Projeto
Executar o programa: Execute o arquivo crud.py no terminal:


Ao iniciar, você verá um menu com opções:
Digite 1 para adicionar um novo usuário.
Digite 2 para listar todos os usuários.
Digite 3 para atualizar um usuário existente.
Digite 4 para deletar um usuário.
Digite 5 para sair.
Exemplo de Uso:

Para adicionar um usuário, escolha 1 e insira os dados como nome, email e idade.
Para ver todos os usuários cadastrados, escolha 2.
Para atualizar ou deletar um usuário, você precisará do id do usuário, que aparece na listagem de usuários.
Estrutura do Projeto
Arquivo crud.py: Contém todo o código do programa, incluindo a conexão com o banco de dados e as funções de adicionar, ler, atualizar e deletar usuários.
Banco de Dados usuarios.db: Onde os dados dos usuários são salvos.
Requisitos
Python 3.x (SQLite já está incluído)
