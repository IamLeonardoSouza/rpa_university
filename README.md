# Projeto de Geração e Envio de Boletos Universitários

## Descrição

Este projeto é uma aplicação em Python projetada para automatizar o processo de geração e envio de boletos de pagamento para alunos de uma universidade. O sistema acessa o portal do aluno da universidade na web com as devidas credenciais, realiza a autenticação necessária, gera o boleto de pagamento com vencimento próximo e, em seguida, envia o boleto gerado para o responsável pagante via Telegram, utilizando o Chat ID e o Token do bot.

### Funcionalidades

- **Acesso ao Portal do Aluno:** O sistema se conecta ao portal do aluno da universidade, realizando login com credenciais fornecidas e acessando a seção específica para a geração de boletos.
- **Geração de Boleto:** Após a autenticação, o sistema localiza o boleto com vencimento próximo e realiza o download ou a geração do mesmo em formato PDF.
- **Envio via Telegram:** Utilizando a API do Telegram, o sistema envia o boleto gerado para o Chat ID do responsável pagante, através do bot configurado com o Token fornecido.

### Tecnologias Utilizadas

- **Python:** Linguagem de programação principal utilizada para desenvolver a aplicação.
- **Selenium:** Biblioteca utilizada para automação de navegação web e interação com o portal da universidade.
- **PDF:** Formato de arquivo utilizado para o boleto gerado.
- **Telegram API:** Utilizada para enviar o boleto gerado para o responsável pagante via Telegram.

### Pré-Requisitos

Antes de executar o projeto, certifique-se de ter o seguinte:

- Python 3.12.4 instalado
- Bibliotecas Python necessárias instaladas. Utilize o comando `pip install -r requirements.txt` para instalar todas as dependências.
- Credenciais válidas para o portal do aluno da universidade.
- Chat ID e Token do bot do Telegram configurados para o envio de mensagens.
