# CHATBOT - BOITATA  🐍
  <img width="333" height="381" alt="Boitatá" src="https://github.com/user-attachments/assets/ad3fc9dc-eea3-408a-8f19-9568c462bc7e">

Foi desenvolvido um chatbot voltado para assuntos relacionados à Física, Ciência de Dados e Tecnologia. O sistema utiliza uma base de conhecimento armazenada em um arquivo JSON, contendo perguntas, palavras-chave e respostas pré-definidas.

O bot é capaz de interagir com os usuários por meio dessas respostas cadastradas, identificando intenções e retornando informações compatíveis com o contexto da conversa. Além disso, sua base de conhecimento pode ser facilmente expandida, bastando adicionar novos conteúdos ao arquivo JSON, sem necessidade de alterar o código-fonte da aplicação. 


## Estrutura
```text
Bot-Boitata/
├── Source/
│   ├── Core/
│   │   ├── main.py              # Execução via terminal
│   │   └── app.py               # Execução via interface web
│   │
│   ├── Json/
│   │   └── intents.json         # Base de intenções e respostas
│   │
│   ├── static/
│   │   ├── style/
│   │   │   └── style.css        # Estilização da aplicação
│   │   │
│   │   ├── img/
│   │   │   └── boitata.png      # Avatar do chatbot
│   │   │
│   │   └── js/
│   │       └── app.js           # Lógica e interações do chat
│   │
│   └── Templates/
│       └── index.html           # Página principal da aplicação
│
└── README.md                    # Documentação do projeto
```
