# 🐾 PetShop Project

Um sistema web completo para petshops desenvolvido em Django com funcionalidades para gerenciamento de produtos, galeria de fotos, área institucional e sistema completo de usuários.

## 📋 Funcionalidades

### 🏠 Área Institucional (Main)
- **Home Page**: Página inicial com apresentação do petshop
- **Sobre Nós**: Informações sobre a empresa
- **Contato**: Formulário de contato com sistema de mensagens
- **Newsletter**: Sistema de inscrição para newsletter
- **Dashboard**: Painel personalizado para usuários logados

### 👥 Sistema de Usuários (Accounts)
- **Autenticação Completa**: Sistema de login, logout e cadastro
- **Perfil Personalizado**: Usuário customizado com:
  - CPF (com validação brasileira)
  - Telefone
  - Foto de perfil
- **Integração**: Sistema integrado com todos os módulos

### 🏠 Gerenciamento de Endereços (Addresses)
- **Múltiplos Endereços**: Usuários podem cadastrar vários endereços
- **Endereço Principal**: Sistema de endereço padrão
- **Validação Brasileira**: Campos adequados ao padrão brasileiro
- **CRUD Completo**: Criar, editar, visualizar e excluir endereços

### 🐕 Gestão de Pets (Pets)
- **Cadastro de Pets**: Registro completo dos animais de estimação
- **Informações Detalhadas**:
  - Nome, espécie (cão/gato), raça
  - Data de nascimento
  - Observações de saúde e comportamento
- **Vinculação ao Proprietário**: Pets ligados aos usuários cadastrados

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
- **Sistema de Moderação**: Fotos com status de aprovação (ativo/inativo/pendente)
- **Organização Cronológica**: Ordenação por data de upload

### 🔧 Funcionalidades Técnicas
- **API REST**: Interface completa para integração com outros sistemas
- **Sistema de Autenticação**: Login/logout com usuário customizado
- **Admin Django**: Painel administrativo completo
- **Sistema de Templates**: Interface responsiva com Bootstrap 5
- **Gestão de Mídia**: Upload e servimento de imagens
- **Banco de Dados**: PostgreSQL para produção, SQLite para desenvolvimento
- **Validações Brasileiras**: CPF, CEP e outros campos com validação local

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 6.0
- **Database**: PostgreSQL (Docker) / SQLite (desenvolvimento)
- **API**: Django REST Framework
- **Frontend**: HTML/CSS/JavaScript com Bootstrap 5
- **Autenticação**: Sistema customizado de usuários Django
- **Validações**: Django Localflavor para validações brasileiras
- **Forms**: Crispy Forms com Bootstrap 5
- **Imagens**: Pillow para processamento
- **Container**: Docker e Docker Compose
- **Admin Interface**: PgAdmin para gerenciamento do banco

## 📁 Estrutura do Projeto

```
petshop_project/
├── core/                    # Configurações principais
├── main/                    # App institucional (home, contato, sobre, dashboard)
├── accounts/                # Sistema de autenticação e usuários
├── addresses/               # Gerenciamento de endereços
├── pets/                    # Cadastro e gestão de pets
├── catalog/                 # App de produtos e categorias
├── gallery/                 # App de galeria de fotos
├── templates/               # Templates globais
├── staticfiles/             # Arquivos estáticos coletados
├── media/                   # Arquivos de mídia (fotos, uploads)
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

### Accounts App
- **User**: Usuário customizado (AbstractUser)
  - CPF (com validação), telefone, foto de perfil
  - Todos os campos padrão do Django (username, email, etc.)

### Addresses App
- **Address**: Endereços dos usuários
  - CEP, logradouro, número, complemento
  - Bairro, cidade, estado
  - Flag de endereço principal

### Pets App
- **Pet**: Cadastro de animais de estimação
  - Nome, espécie (cão/gato), raça
  - Data de nascimento, observações
  - Vinculação com o proprietário (User)

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
- **SiteConfiguration**: Configurações do site
  - Banners, imagens institucionais

### Gallery App
- **Photo**: Fotos da galeria
  - Título, legenda, imagem, status de ativação, data de upload

## 🔐 Admin Django

Para acessar o painel administrativo:

1. Crie um superusuário:
```bash
python manage.py createsuperuser
```
2. Acesse: http://localhost:8000/admin
3.  Crie um token para API:
```bash
python manage.py drf_create_token {nome_superusuário}
```

## 🌐 API REST

O projeto inclui uma API REST completa para integração com outros sistemas:

- **Base URL**: http://localhost:8000/api/v1
- **Autenticação**: DRF Token Authentication
- **Permissões**: IsAuthenticatedOrReadOnly (leitura pública, escrita autenticada)

### 📚 Endpoints Disponíveis

#### 🏷️ Categorias - `/categories/`
**Somente Leitura** (ReadOnlyModelViewSet)
- `GET /api/v1/categories/` - Lista todas as categorias com produtos
- `GET /api/v1/categories/{id}/` - Detalhes de uma categoria específica

**Campos retornados:**
```json
{
  "id": 1,
  "name": "Ração Premium",
  "slug": "racao-premium",
  "products": [
    {
      "id": 1,
      "name": "Ração Golden Special",
      "description": "Ração premium para cães adultos",
      "price": "89.90",
      "image": "/media/products/racao-golden.jpg",
      "category": 1,
      "category_name": "Ração Premium",
      "is_active": true
    }
  ]
}
```

#### 📦 Produtos - `/products/`
**CRUD Completo** (ModelViewSet)
- `GET /api/v1/products/` - Lista todos os produtos ativos
- `POST /api/v1/products/` - Cria um novo produto (autenticação necessária)
- `GET /api/v1/products/{id}/` - Detalhes de um produto específico
- `PUT /api/v1/products/{id}/` - Atualiza um produto completo (autenticação necessária)
- `PATCH /api/v1/products/{id}/` - Atualiza parcialmente um produto (autenticação necessária)
- `DELETE /api/v1/products/{id}/` - Remove um produto (autenticação necessária)

**Campos retornados:**
```json
{
  "id": 1,
  "name": "Ração Golden Special",
  "description": "Ração premium para cães adultos de todas as raças",
  "price": "89.90",
  "image": "/media/products/racao-golden.jpg",
  "category": 1,
  "category_name": "Ração Premium",
  "is_active": true
}
```

#### � Usuários - `/accounts/`
**CRUD Completo** (ModelViewSet)
- `GET /api/v1/accounts/` - Lista usuários (requer autenticação)
- `POST /api/v1/accounts/` - Cria um novo usuário
- `GET /api/v1/accounts/{id}/` - Detalhes de um usuário específico
- `PUT /api/v1/accounts/{id}/` - Atualiza usuário completo (requer autenticação)
- `PATCH /api/v1/accounts/{id}/` - Atualiza parcialmente usuário (requer autenticação)
- `DELETE /api/v1/accounts/{id}/` - Remove usuário (requer autenticação)

#### �📸 Galeria - `/gallery/`
**CRUD Completo** (ModelViewSet)
- `GET /api/v1/gallery/` - Lista todas as fotos (ordenadas por data)
- `POST /api/v1/gallery/` - Adiciona uma nova foto (autenticação necessária)
- `GET /api/v1/gallery/{id}/` - Detalhes de uma foto específica
- `PUT /api/v1/gallery/{id}/` - Atualiza uma foto completa (autenticação necessária)
- `PATCH /api/v1/gallery/{id}/` - Atualiza parcialmente uma foto (autenticação necessária)
- `DELETE /api/v1/gallery/{id}/` - Remove uma foto (autenticação necessária)

**Campos retornados:**
```json
{
  "id": 1,
  "title": "Rex após o banho",
  "caption": "Nosso cliente Rex ficou lindo após o banho e tosa!",
  "image": "/media/gallery/rex-banho.jpg",
  "uploaded_at": "2024-12-23T10:30:00Z"
}
```

#### ⚙️ Configuração do Site - `/site-config/`
**Somente Leitura** (ReadOnlyModelViewSet)
- `GET /api/v1/site-config/` - Lista configurações do site
- `GET /api/v1/site-config/{id}/` - Detalhes de configuração específica

#### 📞 Mensagens de Contato - `/contact/`
**Somente Criação** (CreateModelMixin)
- `POST /api/v1/contact/` - Cria uma nova mensagem de contato

**Campos para envio:**
```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "phone": "(11) 99999-9999",
  "message": "Gostaria de mais informações sobre os serviços",
  "created_at": "2024-12-23T10:30:00Z"
}
```

### 🔐 Autenticação

#### Obter Token de Autenticação
```bash
# Via Django Command
python manage.py drf_create_token {username}

# Via API (se configurado)
POST /api-auth/login/
```

#### Usar Token nas Requisições
```bash
# Header de Autorização
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

# Exemplo com curl
curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
     http://localhost:8000/api/v1/products/
```

### 📝 Exemplos de Uso

#### Listar Produtos
```bash
curl -X GET http://localhost:8000/api/v1/products/
```

#### Criar um Produto
```bash
curl -X POST http://localhost:8000/api/v1/products/ \
  -H "Authorization: Token SEU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Brinquedo Kong",
    "description": "Brinquedo resistente para cães",
    "price": "45.90",
    "category": 2,
    "is_active": true
  }'
```

#### Filtrar Produtos por Categoria
```bash
curl -X GET "http://localhost:8000/api/v1/products/?category=1"
```

#### Enviar Mensagem de Contato
```bash
curl -X POST http://localhost:8000/api/v1/contact/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Maria Santos",
    "email": "maria@email.com", 
    "phone": "(11) 88888-8888",
    "message": "Interessada nos serviços de banho e tosa"
  }'
```

### 🌐 Rotas Web (Frontend)

#### Páginas Institucionais
- `GET /` - Home page
- `GET /sobre-nos/` - Página sobre a empresa  
- `GET /contato/` - Formulário de contato

#### Sistema de Usuários
- `GET /contas/login/` - Página de login
- `GET /contas/signup/` - Página de cadastro
- `GET /contas/dashboard/` - Painel do usuário (requer login)

#### Gestão de Pets
- `GET /pets/` - Lista de pets do usuário (requer login)
- `GET /pets/novo/` - Cadastro de novo pet
- `GET /pets/{id}/editar/` - Edição de pet

#### Gestão de Endereços
- `GET /enderecos/` - Lista de endereços do usuário (requer login)
- `GET /enderecos/novo/` - Cadastro de novo endereço
- `GET /enderecos/{id}/editar/` - Edição de endereço

#### Catálogo de Produtos
- `GET /catalogo/` - Lista de produtos por categoria

#### Galeria
- `GET /galeria/` - Galeria de fotos dos pets

#### Administração
- `GET /admin/` - Painel administrativo Django
- `GET /api-auth/` - Interface de autenticação DRF

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

- [x] Sistema de API completo do projeto
- [x] Sistema de autenticação de usuários
- [x] Cadastro e gestão de pets
- [x] Sistema de endereços múltiplos
- [x] Dashboard personalizado para usuários
- [x] Sistema de moderação de fotos na galeria
- [ ] Carrinho de compras
- [ ] Sistema de pedidos e agendamentos
- [ ] Integração com sistema de pagamento
- [ ] Sistema de agendamento de serviços
- [ ] Notificações por email
- [ ] Dashboard de vendas para administradores
- [ ] Sistema de avaliações e comentários
- [ ] Histórico de serviços por pet
- [ ] Relatórios gerenciais

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