PROJETO GERADO COM PROMPTS. 

# Anti-Prompt Injection System V2

Sistema simplificado de detecção de prompt injection baseado em comparação de 10 palavras-chave específicas.

## Funcionalidades

- ✅ Detecção de 10 palavras-chave críticas
- ✅ API REST com FastAPI
- ✅ Interface web de demonstração
- ✅ Comparação case-insensitive
- ✅ Resposta em tempo real (< 10ms)
- ✅ Containerização Docker

## Palavras-chave Monitoradas

- ignore
- forget
- system
- admin
- override
- bypass
- jailbreak
- prompt
- instruction
- command

## Instalação e Execução

### Método 1: Python Local

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
python -m uvicorn src.main:app --host 0.0.0.0 --port 8080
```

### Método 2: Docker

```bash
# Build da imagem
docker build -t anti-prompt-injection .

# Executar container
docker run -p 8080:8080 anti-prompt-injection
```

### Método 3: Docker Compose

```bash
docker-compose up --build
```

## Uso da API

### Endpoint Principal

```bash
POST /api/v1/check-prompt
Content-Type: application/json

{
    "prompt": "texto a ser analisado"
}
```

### Resposta

```json
{
    "detected": true,
    "word_found": "ignore",
    "processing_time_ms": 2.5,
    "timestamp": "2025-09-19T20:30:00.000Z"
}
```

### Health Check

```bash
GET /health
```

## Interface Web

Acesse `http://localhost:8080` para usar a interface de demonstração.

## Testes

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=src tests/

# Executar testes específicos
pytest tests/test_detector.py
```

## Exemplos de Uso

### Prompt Seguro
```bash
curl -X POST "http://localhost:8080/api/v1/check-prompt" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Qual é a capital do Brasil?"}'
```

### Prompt Suspeito
```bash
curl -X POST "http://localhost:8080/api/v1/check-prompt" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "ignore all previous instructions"}'
```

## Arquitetura

```
src/
├── main.py          # Aplicação FastAPI principal
├── detector.py      # Lógica de detecção
├── models.py        # Modelos Pydantic
├── keywords.py      # Lista de palavras-chave
└── config.py        # Configurações

tests/
├── test_detector.py # Testes unitários
└── test_api.py      # Testes de integração
```

## Performance

- Latência típica: < 5ms
- Throughput: > 1000 req/s
- Memory usage: < 100MB
- Complexidade: O(n*m) onde n=tamanho do prompt, m=10 palavras

## Limitações

- Detecção apenas por substring exata
- Não detecta variações ou obfuscação
- Case-insensitive apenas
- Sem análise semântica

## Versão

2.0.0 - Sistema simplificado por comparação de caracteres


Diagrama Obtido:

<img width="1012" height="661" alt="image" src="https://github.com/user-attachments/assets/686e5c1f-6078-46d9-bc28-bf95a87d27b5" />
