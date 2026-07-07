# DOCUMENT API 

API REST desenvolvida em Python utilizando Flask para validação de documentos brasileiros e outros tipos de dados.

O objetivo do projeto é fornecer endpoints simples para validar informações como:

- CPF
- CNPJ *(Em desenvolvimento)*
- CNH *(Em desenvolvimento)*
- CEP *(Em desenvolvimento)*
- E-mail *(Em desenvolvimento)*
- Telefone *(Em desenvolvimento)*

---

# Tecnologias

- Python 3
- Flask
- Blueprint
- JSON
- REST API

---

# Estrutura do Projeto

```
validator-api/

├── app.py
├── routes/
│   └── route_cpf.py
│
├── services/
│   └── cpf_validation.py
│
└── README.md
```

---

# Como executar

Clone o projeto

```bash
git clone https://github.com/Matheushlopes/document-validator-api.git
```

Entre na pasta

```bash
cd validator-api
```

Crie o ambiente virtual

```bash
python -m venv venv
```

Ative

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Instale as dependências

```bash
pip install flask
```

Execute

```bash
python main.py
```

Servidor

```
http://127.0.0.1:5000
```

---

# Endpoints

## Validar CPF

```
GET /api/v1/validate/cpf/<cpf>
```

### Exemplo

```
GET /api/v1/validate/cpf/09584479938
```

### Resposta

```json
{
    "cpf": "09584479938",
    "valido": true
}
```

---

# Status Code

| Código | Descrição |
|---------|-----------|
| 200 | Requisição realizada com sucesso |
| 400 | Documento inválido |
| 404 | Endpoint não encontrado |
| 500 | Erro interno |

---

# Roadmap

- [x] Validação de CPF
- [ ] Validação de CNPJ
- [ ] Validação de CNH
- [ ] Validação de CEP
- [ ] Validação de E-mail
- [ ] Validação de Telefone
- [ ] Testes automatizados
- [ ] Docker
- [ ] CI/CD
- [ ] Deploy

---

# Exemplo utilizando Python

```python
import requests

response = requests.get(
    "http://127.0.0.1:5000/api/v1/validators/cpf/09584479938"
)

print(response.json())
```

---

# Objetivo

Este projeto foi desenvolvido para estudo de:

- Desenvolvimento de APIs REST
- Organização em camadas
- Aplicar conhecimento adiquirido
- Flask
- Blueprints
- Estruturação de projetos Python
- Boas práticas de Backend
- Validação de documentos brasileiros

---

# Licença

MIT License
