# Web Scraper de Reviews de Produtos

Este projeto é um scraper de reviews de produtos usando Python, Selenium, Flask (para o backend) e React (para o frontend). Ele permite coletar e exibir reviews de produtos de sites como Amazon.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o scraping.
- **Selenium**: Biblioteca para automação de navegadores.
- **Flask**: Framework web para criar o backend.
- **React**: Biblioteca JavaScript para construir a interface do usuário.
- **Node.js**: Para gerenciar pacotes e executar o aplicativo React.

## Estrutura do Projeto

web-scraper-reviews/ 
├── backend/ │ 
             ├── scraper.py 
             # Script de scraping │ 
             ├── requirements.txt 
             # Dependências do Python │
             └── app.py # API do Flask 
├── frontend/ │ 
               ├── package.json # Gerenciador de pacotes do React │ 
                ├── src/ │ 
                         │ 
                         ├── App.js # Componente principal do React │
                         │ └── ... # Outros arquivos e componentes do React └── README.md # Este arquivo


bash
Copiar código

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Ansoferreiro/web-scraper-reviews.git
   cd web-scraper-reviews
Configurar o Backend:

Navegue até a pasta backend:
bash
Copiar código
cd backend
Instale as dependências:
bash
Copiar código
pip install -r requirements.txt
Configurar o Frontend:

Navegue até a pasta frontend:
bash
Copiar código
cd ../frontend
Instale as dependências:
bash
Copiar código
npm install
Executando o Projeto
Inicie o servidor Backend:

No diretório backend, execute:
bash
Copiar código
python app.py
Inicie o servidor Frontend:

No diretório frontend, execute:
bash
Copiar código
npm start
Acesse a aplicação:

Abra seu navegador e vá para http://localhost:3000 para visualizar a aplicação.
Contribuição
Contribuições são bem-vindas! Para contribuir:

Faça um fork deste repositório.
Crie uma nova branch (git checkout -b feature-XYZ).
Faça suas alterações e adicione os arquivos (git add .).
Faça um commit das suas alterações (git commit -m 'Add some feature').
Envie para o repositório remoto (git push origin feature-XYZ).
Abra um Pull Request.                         
