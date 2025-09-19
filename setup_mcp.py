#!/usr/bin/env python3
"""
Script de configuração do MCP Server para Anti-Prompt Injection
"""

import json
import os
import sys
from pathlib import Path

def setup_mcp_server():
    """Configura o servidor MCP"""
    
    print("🔧 Configurando MCP Server Anti-Prompt Injection")
    print("=" * 50)
    
    # Diretório atual do projeto
    project_dir = Path(__file__).parent.absolute()
    
    # Configuração do MCP
    mcp_config = {
        "mcpServers": {
            "anti-prompt-injection": {
                "command": sys.executable,
                "args": [str(project_dir / "mcp_server.py")],
                "env": {
                    "PYTHONPATH": str(project_dir)
                }
            }
        }
    }
    
    # Salvar configuração
    config_file = project_dir / "mcp_config.json"
    with open(config_file, 'w') as f:
        json.dump(mcp_config, f, indent=2)
    
    print(f"✅ Configuração salva em: {config_file}")
    
    # Tornar executável
    mcp_server_file = project_dir / "mcp_server.py"
    os.chmod(mcp_server_file, 0o755)
    
    print(f"✅ Servidor MCP configurado: {mcp_server_file}")
    
    # Instruções de uso
    print("\n📋 Instruções de Uso:")
    print("1. Para testar o servidor:")
    print(f"   python {project_dir / 'mcp_client.py'}")
    
    print("\n2. Para usar com Q CLI:")
    print("   Adicione a configuração do mcp_config.json ao seu cliente MCP")
    
    print("\n3. Ferramentas disponíveis:")
    print("   • check_prompt_injection - Detecta prompt injection")
    print("   • get_monitored_keywords - Lista palavras-chave")
    print("   • analyze_text_safety - Análise detalhada de segurança")
    
    print("\n4. Recursos disponíveis:")
    print("   • anti-prompt-injection://system/info - Info do sistema")
    print("   • anti-prompt-injection://keywords/list - Lista de keywords")
    
    print("\n" + "=" * 50)
    print("✅ MCP Server configurado com sucesso!")
    
    return config_file

if __name__ == "__main__":
    setup_mcp_server()
