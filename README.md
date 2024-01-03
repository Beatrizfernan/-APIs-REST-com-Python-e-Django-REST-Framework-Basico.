# Curso **API**

Esta é uma API simples desenvolvida em Django para gerenciar cursos e avaliações.

## **Conteúdo**

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Estrutura do Projeto](https://chat.openai.com/c/53db5aab-641c-4898-b59f-55946c6a6dd8#estrutura-do-projeto)
3. [Requisitos](https://chat.openai.com/c/53db5aab-641c-4898-b59f-55946c6a6dd8#requisitos)
4. [Configuração do Ambiente](https://chat.openai.com/c/53db5aab-641c-4898-b59f-55946c6a6dd8#configura%C3%A7%C3%A3o-do-ambiente)
5. [Endpoints](https://chat.openai.com/c/53db5aab-641c-4898-b59f-55946c6a6dd8#endpoints)
6. [Administração](https://chat.openai.com/c/53db5aab-641c-4898-b59f-55946c6a6dd8#administra%C3%A7%C3%A3o)

---

## **Sobre o Projeto**

A Escola API é uma aplicação Django que fornece endpoints para gerenciar cursos e avaliações. Ela inclui funcionalidades básicas, como listar todos os cursos, criar um novo curso, listar todas as avaliações e criar uma nova avaliação para um curso específico.

---

## **Estrutura do Projeto**

A estrutura do projeto está organizada da seguinte forma:

- CURSO**/**
    - **cursos/**
        - **models.py**: Define os modelos de dados para Curso e Avaliação.
        - **views.py**: Contém as classes de visualização para manipular requisições HTTP.
        - **admin.py**: Configurações do painel de administração do Django.
        - **serializers.py**: Serializadores para converter dados entre objetos Python e JSON.
    - **escola/**
        - **settings.py**: Configurações do projeto Django, como banco de dados, aplicativos instalados e middleware.
    

---

## **Requisitos**

Certifique-se de ter o Python e o Django instalados em seu ambiente. Você pode instalar as dependências usando o arquivo **`requirements.txt`**. Execute o seguinte comando:

```bash

pip install -r requirements.txt

```

---

## **Configuração do Ambiente**

### **Banco de Dados**

O projeto utiliza um banco de dados SQLite por padrão. Você pode modificar as configurações de banco de dados no arquivo **`escola/settings.py`**. Para aplicar as migrações e criar o banco de dados, execute:

```bash

python manage.py migrate

```

### **Executando o Servidor**

Inicie o servidor de desenvolvimento Django com o seguinte comando:

```bash

python manage.py runserver

```

A API estará acessível em **`http://127.0.0.1:8000/`**.

---

## **Endpoints**

### **Cursos**

- **Listar Todos os Cursos**
    - Método: GET
    - Endpoint: **`/api/v1/cursos/`**
- **Criar um Novo Curso**
    - Método: POST
    - Endpoint: **`/api/v1/cursos/`**

### **Avaliações**

- **Listar Todas as Avaliações**
    - Método: GET
    - Endpoint: **`/api/v1/avaliacoes/`**
- **Criar uma Nova Avaliação**
    - Método: POST
    - Endpoint: **`/api/v1/avaliacoes/`**

---

## **Administração**

O painel de administração do Django está disponível em **`http://127.0.0.1:8000/admin/`**. Você pode fazer login usando as credenciais de superusuário.

---
