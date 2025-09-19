#!/usr/bin/env python3
"""
MCP Server para Sistema Anti-Prompt Injection V2
Expõe funcionalidades do sistema via Model Context Protocol
"""

import asyncio
import json
from typing import Any, Dict, List, Optional, Sequence
from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.types import (
    Resource, 
    Tool, 
    TextContent, 
    ImageContent, 
    EmbeddedResource
)
import mcp.server.stdio

# Importar módulos do sistema
from src.detector import detect_injection
from src.keywords import KEYWORDS

# Criar instância do servidor MCP
server = Server("anti-prompt-injection")

@server.list_tools()
async def handle_list_tools() -> List[Tool]:
    """Lista as ferramentas disponíveis no MCP server"""
    return [
        Tool(
            name="check_prompt_injection",
            description="Analisa um prompt para detectar tentativas de prompt injection",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "O prompt a ser analisado para detecção de injection"
                    }
                },
                "required": ["prompt"]
            }
        ),
        Tool(
            name="get_monitored_keywords",
            description="Retorna a lista das 10 palavras-chave monitoradas pelo sistema",
            inputSchema={
                "type": "object",
                "properties": {},
                "additionalProperties": False
            }
        ),
        Tool(
            name="analyze_text_safety",
            description="Análise detalhada de segurança de texto com métricas",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Texto a ser analisado"
                    },
                    "include_metrics": {
                        "type": "boolean",
                        "description": "Incluir métricas detalhadas na resposta",
                        "default": False
                    }
                },
                "required": ["text"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
    """Manipula chamadas de ferramentas"""
    
    if name == "check_prompt_injection":
        prompt = arguments.get("prompt", "")
        
        if not prompt:
            return [TextContent(
                type="text",
                text="Erro: Prompt não pode estar vazio"
            )]
        
        # Executar detecção
        result = detect_injection(prompt)
        
        # Formatar resposta
        response = {
            "detected": result["detected"],
            "word_found": result["word_found"],
            "processing_time_ms": result["processing_time_ms"],
            "timestamp": result["timestamp"],
            "prompt_length": len(prompt),
            "status": "INJECTION_DETECTED" if result["detected"] else "SAFE"
        }
        
        return [TextContent(
            type="text",
            text=json.dumps(response, indent=2)
        )]
    
    elif name == "get_monitored_keywords":
        response = {
            "keywords": KEYWORDS,
            "total_count": len(KEYWORDS),
            "description": "Lista das palavras-chave monitoradas para detecção de prompt injection"
        }
        
        return [TextContent(
            type="text",
            text=json.dumps(response, indent=2)
        )]
    
    elif name == "analyze_text_safety":
        text = arguments.get("text", "")
        include_metrics = arguments.get("include_metrics", False)
        
        if not text:
            return [TextContent(
                type="text",
                text="Erro: Texto não pode estar vazio"
            )]
        
        # Executar análise
        result = detect_injection(text)
        
        # Análise básica
        response = {
            "text_length": len(text),
            "detected": result["detected"],
            "word_found": result["word_found"],
            "processing_time_ms": result["processing_time_ms"],
            "safety_score": 0 if result["detected"] else 100,
            "risk_level": "HIGH" if result["detected"] else "LOW"
        }
        
        # Métricas detalhadas se solicitado
        if include_metrics:
            words = text.lower().split()
            detected_keywords = [kw for kw in KEYWORDS if kw in text.lower()]
            
            response["metrics"] = {
                "word_count": len(words),
                "character_count": len(text),
                "detected_keywords": detected_keywords,
                "detection_ratio": len(detected_keywords) / len(KEYWORDS) * 100,
                "algorithm_complexity": f"O(n*m) where n={len(text)}, m={len(KEYWORDS)}"
            }
        
        return [TextContent(
            type="text",
            text=json.dumps(response, indent=2)
        )]
    
    else:
        return [TextContent(
            type="text",
            text=f"Erro: Ferramenta '{name}' não encontrada"
        )]

@server.list_resources()
async def handle_list_resources() -> List[Resource]:
    """Lista recursos disponíveis"""
    return [
        Resource(
            uri="anti-prompt-injection://system/info",
            name="System Information",
            description="Informações sobre o sistema Anti-Prompt Injection",
            mimeType="application/json"
        ),
        Resource(
            uri="anti-prompt-injection://keywords/list",
            name="Keywords List",
            description="Lista completa das palavras-chave monitoradas",
            mimeType="application/json"
        )
    ]

@server.read_resource()
async def handle_read_resource(uri: str) -> str:
    """Lê recursos do sistema"""
    
    if uri == "anti-prompt-injection://system/info":
        info = {
            "name": "Sistema Anti-Prompt Injection V2",
            "version": "2.0.0",
            "description": "Sistema de detecção de prompt injection baseado em palavras-chave",
            "algorithm": "Busca sequencial O(n*m)",
            "performance": {
                "latency": "< 10ms",
                "throughput": "> 1000 req/s",
                "memory": "< 100MB"
            },
            "keywords_count": len(KEYWORDS),
            "case_sensitive": False,
            "supported_languages": ["Portuguese", "English"]
        }
        return json.dumps(info, indent=2)
    
    elif uri == "anti-prompt-injection://keywords/list":
        keywords_info = {
            "keywords": KEYWORDS,
            "total": len(KEYWORDS),
            "categories": {
                "control": ["ignore", "forget", "override", "bypass"],
                "system": ["system", "admin", "command"],
                "security": ["jailbreak"],
                "instruction": ["prompt", "instruction"]
            },
            "detection_method": "substring_match",
            "case_sensitive": False
        }
        return json.dumps(keywords_info, indent=2)
    
    else:
        raise ValueError(f"Recurso não encontrado: {uri}")

async def main():
    """Função principal do servidor MCP"""
    # Executar servidor via stdio
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="anti-prompt-injection",
                server_version="2.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                )
            )
        )

if __name__ == "__main__":
    asyncio.run(main())
