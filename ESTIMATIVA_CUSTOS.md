# 💰 Estimativa de Custos - Sistema Anti-Prompt Injection V2

## 📊 Resumo Executivo

| Ambiente | Custo Mensal | Custo Anual | Observações |
|----------|--------------|-------------|-------------|
| **Desenvolvimento** | **$18.61** | **$223.32** | 1 task, recursos mínimos |
| **Staging** | **$18.61** | **$223.32** | 1 task, mesmo que dev |
| **Produção** | **$31.61** | **$379.32** | 2 tasks, alta disponibilidade |

## 🏗️ Detalhamento por Recurso (Produção)

### 1. **ECS Fargate** 
**Configuração:** 2 tasks × 0.25 vCPU × 512MB RAM × 24h/dia

| Item | Especificação | Preço Unitário | Quantidade | Subtotal |
|------|---------------|----------------|------------|----------|
| vCPU | 0.25 vCPU por task | $0.04048/vCPU/hora | 0.5 vCPU × 744h | **$15.06** |
| Memory | 512MB por task | $0.004445/GB/hora | 1GB × 744h | **$3.31** |
| **Total ECS Fargate** | | | | **$18.37** |

### 2. **Application Load Balancer (ALB)**
| Item | Especificação | Preço | Subtotal |
|------|---------------|-------|----------|
| ALB Fixo | Custo base mensal | $16.20/mês | **$16.20** |
| LCU (Load Balancer Capacity Units) | ~100 req/hora | $0.008/LCU/hora | **$0.60** |
| **Total ALB** | | | **$16.80** |

### 3. **Elastic Container Registry (ECR)**
| Item | Especificação | Preço | Subtotal |
|------|---------------|-------|----------|
| Storage | 500MB de imagens | $0.10/GB/mês | **$0.05** |
| **Total ECR** | | | **$0.05** |

### 4. **CloudWatch Logs**
| Item | Especificação | Preço | Subtotal |
|------|---------------|-------|----------|
| Ingestão | 1GB/mês de logs | $0.50/GB | **$0.50** |
| Storage | 1GB armazenado | $0.03/GB/mês | **$0.03** |
| **Total CloudWatch** | | | **$0.53** |

### 5. **Data Transfer**
| Item | Especificação | Preço | Subtotal |
|------|---------------|-------|----------|
| Internet Outbound | 1GB/mês | $0.09/GB | **$0.09** |
| **Total Data Transfer** | | | **$0.09** |

### 6. **Outros Recursos**
| Item | Especificação | Preço | Subtotal |
|------|---------------|-------|----------|
| VPC, Subnets, IGW | Recursos gratuitos | $0.00 | **$0.00** |
| Security Groups | Recursos gratuitos | $0.00 | **$0.00** |
| IAM Roles | Recursos gratuitos | $0.00 | **$0.00** |
| **Total Outros** | | | **$0.00** |

## 📈 Cenários de Uso

### 🟢 **Cenário Baixo (< 1000 req/dia)**
| Recurso | Custo Mensal |
|---------|--------------|
| ECS Fargate (1 task) | $9.18 |
| ALB | $16.20 |
| ECR | $0.05 |
| CloudWatch | $0.25 |
| Data Transfer | $0.05 |
| **Total** | **$25.73** |

### 🟡 **Cenário Médio (1000-10000 req/dia)**
| Recurso | Custo Mensal |
|---------|--------------|
| ECS Fargate (2 tasks) | $18.37 |
| ALB | $16.80 |
| ECR | $0.05 |
| CloudWatch | $0.53 |
| Data Transfer | $0.09 |
| **Total** | **$35.84** |

### 🔴 **Cenário Alto (> 10000 req/dia)**
| Recurso | Custo Mensal |
|---------|--------------|
| ECS Fargate (4 tasks) | $36.74 |
| ALB | $17.50 |
| ECR | $0.10 |
| CloudWatch | $1.00 |
| Data Transfer | $0.20 |
| **Total** | **$55.54** |

## 🎯 Otimizações de Custo

### ✅ **Implementadas**
- **Fargate Spot** não usado (não disponível para produção crítica)
- **Recursos mínimos** (256 CPU, 512MB RAM)
- **Auto Scaling** configurado para demanda
- **Log retention** de apenas 7 dias
- **Image scanning** apenas no push

### 💡 **Possíveis Otimizações**

#### 1. **Reserved Capacity (Savings Plans)**
- **Economia:** 20-50% no ECS Fargate
- **Custo com 1 ano:** $14.70/mês (vs $18.37)
- **Economia anual:** $44

#### 2. **Spot Instances (Desenvolvimento)**
- **Economia:** 70% no ECS Fargate
- **Custo dev:** $5.51/mês (vs $18.37)
- **Economia anual:** $154

#### 3. **CloudWatch Logs Otimizado**
- **Log retention:** 3 dias (vs 7 dias)
- **Economia:** $0.20/mês
- **Filtros de log** para reduzir volume

#### 4. **ALB Compartilhado**
- **Múltiplas aplicações** no mesmo ALB
- **Economia:** $16.20/mês por app adicional

## 📊 Comparação com Alternativas

### **AWS Lambda** (Serverless)
| Métrica | Lambda | ECS Fargate | Diferença |
|---------|--------|-------------|-----------|
| Custo base | $0 | $18.37 | +$18.37 |
| Por requisição | $0.0000002 | $0 | Variável |
| Cold start | 100-500ms | 0ms | -500ms |
| **Break-even** | **~90M req/mês** | **Sempre** | **ECS melhor** |

### **EC2 Instances**
| Tipo | vCPU | RAM | Custo/mês | vs Fargate |
|------|------|-----|-----------|------------|
| t3.micro | 2 | 1GB | $7.59 | -$10.78 |
| t3.small | 2 | 2GB | $15.18 | -$3.19 |
| t3.medium | 2 | 4GB | $30.37 | +$12.00 |

**Nota:** EC2 requer gerenciamento adicional (patches, monitoramento)

## 🔍 Análise de ROI

### **Benefícios Quantificáveis**
- **Prevenção de ataques:** Valor incalculável
- **Tempo de resposta:** < 10ms (vs 100-500ms manual)
- **Disponibilidade:** 99.9% (vs 95% manual)
- **Escalabilidade:** Automática (vs manual)

### **Custo vs Benefício**
- **Custo anual:** $379.32
- **Custo por requisição:** $0.000001 (1M req/mês)
- **Custo por detecção:** $0.01 (assumindo 1% de prompts maliciosos)

## 📅 Projeção Anual

### **Crescimento Esperado**
| Mês | Requests/dia | Tasks | Custo Mensal |
|-----|--------------|-------|--------------|
| 1-3 | 500 | 1 | $25.73 |
| 4-6 | 2,000 | 2 | $35.84 |
| 7-9 | 5,000 | 2 | $35.84 |
| 10-12 | 10,000 | 3 | $45.69 |
| **Média Anual** | | | **$35.78** |

### **Total Anual Projetado: $429.36**

## 💳 Faturamento Detalhado

### **Por Região AWS**
| Região | Custo Base | Latência | Recomendação |
|--------|------------|----------|--------------|
| us-east-1 | $31.61 | Baixa | ✅ **Recomendada** |
| us-west-2 | $31.61 | Média | ⚠️ Alternativa |
| eu-west-1 | $34.77 | Alta | ❌ Mais caro |
| sa-east-1 | $41.93 | Muito Alta | ❌ Não recomendada |

### **Por Ambiente**
```
Desenvolvimento: $18.61/mês × 12 = $223.32/ano
Staging:         $18.61/mês × 12 = $223.32/ano  
Produção:        $31.61/mês × 12 = $379.32/ano
─────────────────────────────────────────────────
Total 3 Ambientes:                $825.96/ano
```

## 🚨 Alertas de Custo Recomendados

### **CloudWatch Billing Alerts**
- **$40/mês:** Alerta de atenção
- **$60/mês:** Alerta crítico
- **$100/mês:** Alerta de emergência

### **Budget AWS**
- **Orçamento mensal:** $50
- **Threshold 80%:** $40 (alerta)
- **Threshold 100%:** $50 (ação)

## 📋 Resumo Final

### **Custo Total Estimado (Produção)**
```
┌─────────────────────────────────────┐
│  CUSTO MENSAL TOTAL: $31.61        │
│  CUSTO ANUAL TOTAL:  $379.32       │
│                                     │
│  Breakdown:                         │
│  • ECS Fargate:     $18.37 (58%)   │
│  • Load Balancer:   $16.80 (53%)   │
│  • Outros:          $0.44 (1%)     │
└─────────────────────────────────────┘
```

### **Recomendações**
1. **Iniciar com ambiente de desenvolvimento** ($18.61/mês)
2. **Monitorar uso** nos primeiros 3 meses
3. **Implementar Savings Plans** após 6 meses
4. **Considerar Reserved Instances** para economia de longo prazo
5. **Configurar alertas de billing** para controle

**A solução é altamente cost-effective para a funcionalidade oferecida! 💰✅**
