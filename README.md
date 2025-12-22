# 🐾 PetShop Project

Um sistema web completo para petshops desenvolvido em Django com funcionalidades para gerenciamento de produtos, galeria de fotos e área institucional.

## 📋 Funcionalidades

### 🏠 Área Institucional (Main)
- **Home Page**: Página inicial com apresentação do petshop
- **Sobre Nós**: Informações sobre a empresa
- **Contato**: Formulário de contato com sistema de mensagens
- **Newsletter**: Sistema de inscrição para newsletter

### 📦 Catálogo (Catalog)
- **Gestão de Categorias**: Organização de produtos por categorias
- **Produtos e Serviços**: Cadastro completo com:
  - Nome, descrição e imagem
  - Preço regular e promocional
  - Controle de estoque
  - Sistema de ativação/desativação
- **Sistema de Slugs**: URLs amigáveis para SEO

### 📸 Galeria (Gallery)
- **Galeria de Fotos**: Exposição de pets atendidos
- **Sistema de Upload**: Upload de imagens com títulos e legendas
- **Organização Cronológica**: Ordenação por data de upload

### 🔧 Funcionalidades Técnicas
- **API REST**: Interface para integração com outros sistemas
- **Admin Django**: Painel administrativo completo
- **Sistema de Templates**: Interface responsiva
- **Gestão de Mídia**: Upload e servimento de imagens
- **Banco de Dados**: PostgreSQL para produção

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 6.0
- **Database**: PostgreSQL (Docker) / SQLite (desenvolvimento)
- **API**: Django REST Framework
- **Frontend**: HTML/CSS/JavaScript com templates Django
- **Imagens**: Pillow para processamento
- **Container**: Docker e Docker Compose
- **Admin Interface**: PgAdmin para gerenciamento do banco

## 📁 Estrutura do Projeto

```
petshop_project/
├── core/                    # Configurações principais
├── main/                    # App institucional (home, contato, sobre)
├── catalog/                 # App de produtos e categorias
├── gallery/                 # App de galeria de fotos
├── templates/               # Templates globais
├── staticfiles/             # Arquivos estáticos coletados
├── data/                    # Dados do PostgreSQL e PgAdmin
├── docker-compose.yml       # Configuração dos containers
├── Dockerfile              # Imagem da aplicação
├── requirements.txt        # Dependências Python
└── manage.py               # CLI do Django
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.13+
- Docker e Docker Compose (para execução completa)
- Git

### 1. Clone o Repositório
```bash
git clone <url-do-repositorio>
cd petshop_project
```

### 2. Executando com Docker (Recomendado)

#### Configure as Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:

```env
# Django
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True

# PostgreSQL
POSTGRES_DB=petshop
POSTGRES_USER=petshop_user
POSTGRES_PASSWORD=senha123

# PgAdmin
PGADMIN_DEFAULT_EMAIL=admin@petshop.com
PGADMIN_DEFAULT_PASSWORD=admin123
```

#### Execute os Containers
```bash
# Suba todos os serviços
docker-compose up --build

# Para executar em background
docker-compose up -d --build
```

#### Acesse a Aplicação
- **Aplicação Web**: http://localhost:8000
- **Admin Django**: http://localhost:8000/admin
- **PgAdmin**: http://localhost:8080

### 3. Executando Localmente (Desenvolvimento)

#### Configure o Ambiente Virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

#### Instale as Dependências
```bash
pip install -r requirements.txt
```

#### Configure o Banco de Dados
```bash
python manage.py migrate
python manage.py createsuperuser
```

#### Execute o Servidor
```bash
python manage.py runserver
```

## 📊 Modelos de Dados

### Catalog App
- **Category**: Categorias de produtos
  - Nome, slug, descrição
- **Product**: Produtos e serviços
  - Categoria, nome, descrição, preço, preço promocional, estoque, imagem, status

### Main App
- **ContactMessage**: Mensagens de contato
  - Nome, email, telefone, mensagem, data, status de leitura
- **NewsletterSubscriber**: Inscritos na newsletter
  - Email, data de inscrição

### Gallery App
- **Photo**: Fotos da galeria
  - Título, legenda, imagem, data de upload

## 🔐 Admin Django

Para acessar o painel administrativo:

1. Crie um superusuário:
```bash
python manage.py createsuperuser
```

2. Acesse: http://localhost:8000/admin

## 🌐 API REST

O projeto inclui uma API REST para integração:

- **Base URL**: http://localhost:8000/api/
- **Endpoints** (em desenvolvimento):
  - `/produtos/` - Listagem de produtos
  - `/galeria/` - Galeria de fotos

## 📝 Comandos Úteis

```bash
# Migrar banco de dados
python manage.py migrate

# Criar migrations
python manage.py makemigrations

# Coletar arquivos estáticos
python manage.py collectstatic

# Shell Django
python manage.py shell

# Ver logs do Docker
docker-compose logs -f

# Parar containers
docker-compose down

# Limpar volumes (CUIDADO: apaga dados)
docker-compose down -v
```

## 🐛 Troubleshooting

### Problemas Comuns

1. **Erro de conexão com banco**: Verifique se o PostgreSQL está rodando
2. **Imagens não carregam**: Execute `python manage.py collectstatic`
3. **Permissões no Docker**: Verifique permissões da pasta `data/`

### Logs
```bash
# Logs da aplicação
docker-compose logs web

# Logs do banco
docker-compose logs db

# Logs do PgAdmin
docker-compose logs pgadmin
```

## 📚 Próximas Implementações

- [ ] Sistema de API do projeto
- [ ] Sistema de autenticação de usuários
- [ ] Carrinho de compras
- [ ] Sistema de pedidos
- [ ] Integração com Frete
- [ ] Notificações por email
- [ ] Dashboard de vendas
- [ ] Sistema de avaliações

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Desenvolvedor

**Leonardo Garrido** - Projeto desenvolvido como parte dos estudos na Infinity School

---

**🐾 PetShop Project** - Cuidando dos seus pets com tecnologia e carinho!