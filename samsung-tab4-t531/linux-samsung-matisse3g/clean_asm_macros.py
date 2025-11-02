#!/usr/bin/env python3
"""
Script para limpar macros arm(), thumb(), W() e BSYM() de arquivos assembly ARM
Uso: python3 clean_asm_macros.py <arquivo.S>
"""

import re
import sys

def clean_asm_macros(content):
    """Remove macros arm(), thumb(), W() e BSYM() do conteúdo assembly"""
    
    # Remover arm(...) mantendo conteúdo - múltiplas passagens para nested
    iterations = 0
    while iterations < 10:  # Limite de segurança
        new_content = re.sub(r'\barm\s*\(\s*([^)]+)\s*\)', r'\1', content)
        if new_content == content:
            break
        content = new_content
        iterations += 1
    
    # Remover thumb(...) completamente - múltiplas passagens
    iterations = 0
    while iterations < 10:
        new_content = re.sub(r'\bthumb\s*\([^)]*\)', '', content)
        if new_content == content:
            break
        content = new_content
        iterations += 1
    
    # Remover W(...) mantendo conteúdo
    iterations = 0
    while iterations < 10:
        new_content = re.sub(r'\b[Ww]\s*\(\s*([^)]+)\s*\)', r'\1', content)
        if new_content == content:
            break
        content = new_content
        iterations += 1
    
    # Remover BSYM(...) mantendo conteúdo
    iterations = 0
    while iterations < 10:
        new_content = re.sub(r'\bBSYM\s*\(\s*([^)]+)\s*\)', r'\1', content)
        if new_content == content:
            break
        content = new_content
        iterations += 1
    
    # Remover linhas vazias extras (mantém max 1 linha vazia)
    content = re.sub(r'\n\n\n+', '\n\n', content)
    
    # Remover espaços em branco trailing
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    return content

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <arquivo.S>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as f:
            original = f.read()
        
        cleaned = clean_asm_macros(original)
        
        with open(filename, 'w') as f:
            f.write(cleaned)
        
        # Estatísticas
        orig_lines = original.count('\n')
        clean_lines = cleaned.count('\n')
        
        print(f"✓ {filename}")
        print(f"  Linhas: {orig_lines} → {clean_lines}")
        
        # Contar macros removidas
        arm_count = len(re.findall(r'\barm\s*\(', original))
        thumb_count = len(re.findall(r'\bthumb\s*\(', original))
        w_count = len(re.findall(r'\b[Ww]\s*\(', original))
        bsym_count = len(re.findall(r'\bBSYM\s*\(', original))
        
        if arm_count + thumb_count + w_count + bsym_count > 0:
            print(f"  Macros removidas: arm({arm_count}) thumb({thumb_count}) W({w_count}) BSYM({bsym_count})")
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao processar '{filename}': {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
