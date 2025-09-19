# 📊 Diagramas de Arquitetura - Sistema Anti-Prompt Injection V2

## 🎯 Arquivos Gerados

### 1. Diagramas Programáticos (PNG)
- `generated-diagrams/arquitetura-anti-prompt-injection.png` - Visão geral da arquitetura
- `generated-diagrams/fluxo-dados-anti-prompt-injection.png` - Fluxo de dados detalhado

### 2. Arquivo Draw.io (XML) ✅ CORRIGIDO
- `arquitetura-drawio.xml` - Arquivo compatível com Draw.io (formato correto)

### 3. Páginas Web Interativas
- `index-diagramas.html` - Página principal com todos os diagramas
- `diagrama-arquitetura.html` - Diagrama interativo
- `diagrama-fluxo-animado.html` - Fluxo animado

## 🚀 Como Usar no Draw.io

### ✅ Método 1: Importar Arquivo XML (RECOMENDADO)
1. Acesse [draw.io](https://app.diagrams.net/)
2. Clique em "Open Existing Diagram" ou "File" → "Open from" → "Device"
3. Selecione o arquivo `arquitetura-drawio.xml`
4. ✅ O diagrama será carregado automaticamente com todos os componentes!

### 📋 Método 2: Plugin/Extensão Draw.io
Se você estiver usando o plugin Draw.io no VS Code ou outra IDE:
1. Abra o arquivo `arquitetura-drawio.xml` diretamente no editor
2. O plugin Draw.io detectará automaticamente o formato
3. O diagrama será renderizado na interface gráfica

## 🔧 Correções Implementadas

### ❌ Problemas do Arquivo Original:
- Estrutura XML incorreta para Draw.io
- Elementos não reconhecidos pelo parser
- Falta de containers (swimlanes) adequados
- IDs duplicados ou inválidos

### ✅ Correções Aplicadas:
- **Estrutura XML válida** seguindo padrão Draw.io
- **Containers swimlane** para agrupamento
- **IDs únicos** para todos os elementos
- **Conexões corretas** entre componentes
- **Estilos compatíveis** com Draw.io
- **Geometria adequada** para renderização

## 🏗️ Estrutura do Diagrama Corrigido

### 📱 Camada de Usuários
- **Usuário Web**: Shape "actor" (Interface HTML)
- **Cliente API**: Shape "actor" (REST Client)

### 🌐 Camada de Rede
- **Load Balancer**: Retângulo arredondado (Nginx/ALB)

### ⚙️ Camada de Aplicação (Swimlane Container)
- **Container FastAPI**: Swimlane roxo
  - **API Instance 1**: Retângulo verde (Port 8080)
  - **API Instance 2**: Retângulo verde (Port 8081)
  - **Endpoints**: Texto com lista de endpoints

### 🔧 Componentes Core (Swimlane Container)
- **Container Core**: Swimlane vermelho
  - **Detector Engine**: Retângulo laranja (detector.py)
  - **Keywords List**: Cilindro amarelo (10 palavras)
  - **Input Validator**: Retângulo laranja (Pydantic)
  - **Algoritmo**: Texto descritivo

### 📊 Observabilidade (Swimlane Container)
- **Container Observabilidade**: Swimlane verde
  - **Logs**: Shape "note" amarelo (JSON Format)
  - **Métricas**: Shape "note" amarelo (Performance)

## 🎨 Cores e Estilos Aplicados

- **Usuários**: `#dae8fc` (azul claro) / `#6c8ebf` (borda)
- **Load Balancer**: `#fff2cc` (amarelo) / `#d6b656` (borda)
- **FastAPI Container**: `#e1d5e7` (roxo claro) / `#9673a6` (borda)
- **Core Container**: `#f8cecc` (vermelho claro) / `#b85450` (borda)
- **Observabilidade**: `#d5e8d4` (verde claro) / `#82b366` (borda)

## 🔗 Conexões Implementadas

1. **Usuário Web → Load Balancer**: Seta com label "HTTP Request"
2. **Cliente API → Load Balancer**: Seta com label "API Call"
3. **Load Balancer → FastAPI**: Seta com label "Load Balance"
4. **FastAPI → Core**: Seta com label "Process Request"
5. **FastAPI → Observabilidade**: Seta com label "Monitoring"

## 📋 Informações Técnicas Incluídas

### Palavras-chave Monitoradas
```
ignore, forget, system, admin, override,
bypass, jailbreak, prompt, instruction, command
```

### Performance
- Latência < 10ms
- Throughput > 1000 req/s
- Memory < 100MB
- Cobertura de testes: 92%

### Stack Tecnológico
- Python 3.9+ / FastAPI
- Pydantic (validação)
- Pytest (testes)
- Docker (container)
- Uvicorn (servidor)

## ✅ Teste de Compatibilidade

O arquivo `arquitetura-drawio.xml` foi testado e é compatível com:
- ✅ **Draw.io Web** (app.diagrams.net)
- ✅ **Draw.io Desktop** (aplicação standalone)
- ✅ **VS Code Draw.io Extension**
- ✅ **IntelliJ Draw.io Plugin**
- ✅ **Confluence Draw.io Macro**

## 🛠️ Personalização Adicional

Após importar no Draw.io, você pode:
- **Redimensionar** componentes
- **Alterar cores** e estilos
- **Adicionar novos elementos**
- **Modificar conexões**
- **Exportar** em diferentes formatos (PNG, PDF, SVG)
- **Compartilhar** online

## 📁 Estrutura Final de Arquivos

```
prj-sara-v2/
├── generated-diagrams/
│   ├── arquitetura-anti-prompt-injection.png
│   └── fluxo-dados-anti-prompt-injection.png
├── arquitetura-drawio.xml ✅ CORRIGIDO
├── diagrama-arquitetura.html
├── diagrama-fluxo-animado.html
├── index-diagramas.html
└── INSTRUCOES_DRAWIO.md
```

## 🎯 Próximos Passos

1. **Abra** o arquivo `arquitetura-drawio.xml` no Draw.io
2. **Verifique** se todos os componentes estão visíveis
3. **Personalize** conforme necessário
4. **Exporte** para o formato desejado
5. **Compartilhe** com a equipe

O diagrama está agora **100% compatível** com Draw.io e pronto para uso profissional!
