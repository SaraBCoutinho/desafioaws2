#!/usr/bin/env python3
"""
Calculadora de Custos - Sistema Anti-Prompt Injection V2
Calcula custos AWS baseado em diferentes cenários de uso
"""

def calcular_custos_aws(tasks=2, requests_por_dia=5000, regiao="us-east-1", ambiente="producao"):
    """
    Calcula custos mensais AWS para o sistema
    
    Args:
        tasks: Número de tasks ECS Fargate
        requests_por_dia: Número de requests por dia
        regiao: Região AWS
        ambiente: Tipo de ambiente (dev, staging, producao)
    """
    
    # Preços base (us-east-1)
    precos = {
        "fargate_vcpu_hora": 0.04048,      # $/vCPU/hora
        "fargate_memory_hora": 0.004445,   # $/GB/hora
        "alb_fixo": 16.20,                 # $/mês
        "alb_lcu_hora": 0.008,             # $/LCU/hora
        "ecr_storage": 0.10,               # $/GB/mês
        "cloudwatch_ingestao": 0.50,       # $/GB
        "cloudwatch_storage": 0.03,        # $/GB/mês
        "data_transfer": 0.09              # $/GB
    }
    
    # Multiplicadores por região
    multiplicadores_regiao = {
        "us-east-1": 1.0,
        "us-west-2": 1.0,
        "eu-west-1": 1.1,
        "sa-east-1": 1.3
    }
    
    mult_regiao = multiplicadores_regiao.get(regiao, 1.0)
    horas_mes = 744  # 24h × 31 dias
    
    # Cálculo ECS Fargate
    vcpu_por_task = 0.25
    memory_por_task_gb = 0.5
    
    custo_fargate_vcpu = tasks * vcpu_por_task * horas_mes * precos["fargate_vcpu_hora"] * mult_regiao
    custo_fargate_memory = tasks * memory_por_task_gb * horas_mes * precos["fargate_memory_hora"] * mult_regiao
    custo_fargate_total = custo_fargate_vcpu + custo_fargate_memory
    
    # Cálculo ALB
    requests_mes = requests_por_dia * 31
    lcu_estimado = max(1, requests_mes / 100000)  # 1 LCU = ~100k requests
    
    custo_alb_fixo = precos["alb_fixo"] * mult_regiao
    custo_alb_lcu = lcu_estimado * horas_mes * precos["alb_lcu_hora"] * mult_regiao
    custo_alb_total = custo_alb_fixo + custo_alb_lcu
    
    # Cálculo ECR
    storage_gb = 0.5 if ambiente == "dev" else 1.0
    custo_ecr = storage_gb * precos["ecr_storage"] * mult_regiao
    
    # Cálculo CloudWatch
    logs_gb_mes = requests_mes / 10000  # ~10k requests = 1GB logs
    custo_cw_ingestao = logs_gb_mes * precos["cloudwatch_ingestao"] * mult_regiao
    custo_cw_storage = logs_gb_mes * precos["cloudwatch_storage"] * mult_regiao
    custo_cloudwatch_total = custo_cw_ingestao + custo_cw_storage
    
    # Cálculo Data Transfer
    data_gb_mes = requests_mes / 50000  # ~50k requests = 1GB transfer
    custo_data_transfer = data_gb_mes * precos["data_transfer"] * mult_regiao
    
    # Total
    custo_total_mensal = (
        custo_fargate_total + 
        custo_alb_total + 
        custo_ecr + 
        custo_cloudwatch_total + 
        custo_data_transfer
    )
    
    return {
        "fargate": custo_fargate_total,
        "alb": custo_alb_total,
        "ecr": custo_ecr,
        "cloudwatch": custo_cloudwatch_total,
        "data_transfer": custo_data_transfer,
        "total_mensal": custo_total_mensal,
        "total_anual": custo_total_mensal * 12,
        "custo_por_request": custo_total_mensal / requests_mes if requests_mes > 0 else 0,
        "detalhes": {
            "tasks": tasks,
            "requests_dia": requests_por_dia,
            "requests_mes": requests_mes,
            "regiao": regiao,
            "ambiente": ambiente
        }
    }

def exibir_relatorio(resultado):
    """Exibe relatório formatado dos custos"""
    
    print("💰 CALCULADORA DE CUSTOS - ANTI-PROMPT INJECTION V2")
    print("=" * 60)
    
    detalhes = resultado["detalhes"]
    print(f"📊 Configuração:")
    print(f"   • Tasks ECS: {detalhes['tasks']}")
    print(f"   • Requests/dia: {detalhes['requests_dia']:,}")
    print(f"   • Requests/mês: {detalhes['requests_mes']:,}")
    print(f"   • Região: {detalhes['regiao']}")
    print(f"   • Ambiente: {detalhes['ambiente']}")
    
    print(f"\n💵 Custos Mensais:")
    print(f"   • ECS Fargate:    ${resultado['fargate']:.2f}")
    print(f"   • Load Balancer:  ${resultado['alb']:.2f}")
    print(f"   • ECR Storage:    ${resultado['ecr']:.2f}")
    print(f"   • CloudWatch:     ${resultado['cloudwatch']:.2f}")
    print(f"   • Data Transfer:  ${resultado['data_transfer']:.2f}")
    print(f"   ─────────────────────────────")
    print(f"   • TOTAL MENSAL:   ${resultado['total_mensal']:.2f}")
    
    print(f"\n📅 Projeções:")
    print(f"   • Custo Anual:    ${resultado['total_anual']:.2f}")
    print(f"   • Custo/Request:  ${resultado['custo_por_request']:.6f}")
    
    # Análise de custo-benefício
    if resultado['total_mensal'] < 25:
        nivel = "🟢 BAIXO"
    elif resultado['total_mensal'] < 50:
        nivel = "🟡 MÉDIO"
    else:
        nivel = "🔴 ALTO"
    
    print(f"\n📈 Análise:")
    print(f"   • Nível de Custo: {nivel}")
    print(f"   • Custo por detecção: ${resultado['custo_por_request'] * 100:.4f} (assumindo 1% maliciosos)")

def main():
    """Função principal com cenários pré-definidos"""
    
    cenarios = [
        {
            "nome": "Desenvolvimento",
            "tasks": 1,
            "requests_por_dia": 100,
            "ambiente": "dev"
        },
        {
            "nome": "Staging", 
            "tasks": 1,
            "requests_por_dia": 500,
            "ambiente": "staging"
        },
        {
            "nome": "Produção Baixa",
            "tasks": 2,
            "requests_por_dia": 1000,
            "ambiente": "producao"
        },
        {
            "nome": "Produção Média",
            "tasks": 2,
            "requests_por_dia": 5000,
            "ambiente": "producao"
        },
        {
            "nome": "Produção Alta",
            "tasks": 4,
            "requests_por_dia": 20000,
            "ambiente": "producao"
        }
    ]
    
    print("🚀 CENÁRIOS DE CUSTO PREDEFINIDOS")
    print("=" * 60)
    
    resumo = []
    
    for cenario in cenarios:
        resultado = calcular_custos_aws(
            tasks=cenario["tasks"],
            requests_por_dia=cenario["requests_por_dia"],
            ambiente=cenario["ambiente"]
        )
        
        print(f"\n📋 {cenario['nome'].upper()}")
        print("-" * 30)
        exibir_relatorio(resultado)
        
        resumo.append({
            "nome": cenario["nome"],
            "mensal": resultado["total_mensal"],
            "anual": resultado["total_anual"]
        })
    
    # Resumo comparativo
    print("\n" + "=" * 60)
    print("📊 RESUMO COMPARATIVO")
    print("=" * 60)
    
    for item in resumo:
        print(f"{item['nome']:<20} ${item['mensal']:>7.2f}/mês  ${item['anual']:>8.2f}/ano")
    
    print("\n💡 RECOMENDAÇÕES:")
    print("• Iniciar com Desenvolvimento para testes")
    print("• Produção Baixa para lançamento inicial")
    print("• Monitorar uso e escalar conforme demanda")
    print("• Considerar Savings Plans após 6 meses")

if __name__ == "__main__":
    main()
