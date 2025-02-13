1. Site de Serviços tipo portifolio
![imagem_principal](/assets/img/1.png)
![menu](/assets/img/menu.png)
![sobre](/assets/img/sobre.png)
![contato-me](/assets/img/5.png)

# Documentação do Projeto Landing Page - Django

## Descrição do Projeto
Este projeto é uma Landing Page desenvolvida utilizando Django para gerenciar e exibir serviços oferecidos. O objetivo é fornecer um sistema dinâmico onde serviços podem ser cadastrados, gerenciados e exibidos de forma intuitiva.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do backend
- **Django**: Framework web para gerenciamento do backend
- **HTML/CSS**: Estruturação e estilização da interface
- **SQLite**: Banco de dados padrão do Django

## Estrutura do Projeto
1. **Configuração do Django**
   - Instalação e configuração do framework
   - Criação do projeto `backend`
   - Criação da aplicação `servicos`

2. **Banco de Dados**
   - Modelo `Servico` definido com os campos:
     - `titulo`: Nome do serviço
     - `descricao`: Descrição detalhada
     - `preco`: Valor do serviço
     - `criado_em`: Data de criação
   - Migração do banco de dados

3. **Administração**
   - Registro do modelo `Servico` no Django Admin
   - Criação de um superusuário para gerenciar os serviços

4. **Views e Templates**
   - Criada a view `lista_servicos` para exibir os serviços
   - Criado o template `lista.html` para renderizar os dados

5. **Rotas e URLs**
   - Configuração das URLs para acessar a lista de serviços
   - Integração das rotas no projeto principal

## Implementações Futuras
- Integração com um banco de dados PostgreSQL ou MySQL
- Autenticação de usuários para permitir cadastro e login
- Implementação de um painel administrativo mais avançado
- Adição de um sistema de pagamento para serviços
- Deploy em um servidor de produção (Heroku, AWS, Vercel)

## Destaques do Projeto
✅ Estrutura bem organizada com Django
✅ Banco de dados integrado para gerenciamento dinâmico
✅ Painel administrativo pronto para gerenciamento dos serviços
✅ Frontend simples e funcional, pronto para aprimoramentos

---
### Como Rodar o Projeto
```bash
pip install django  # Instalar Django se ainda não estiver instalado
django-admin startproject backend
cd backend
python manage.py startapp servicos
python manage.py makemigrations servicos
python manage.py migrate
python manage.py createsuperuser  # Criar um superusuário
python manage.py runserver  # Rodar o servidor
```
---
Essa documentação pode ser expandida conforme o projeto evolui! 🚀

