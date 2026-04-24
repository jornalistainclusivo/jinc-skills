#!/usr/bin/env python3
"""
SDD Validator - Antigravity Kit
================================
Valida estritamente o contrato YAML (Frontmatter) em arquivos Markdown.
Desenhado para ser executado via lint-staged em pre-commit hooks.

Regras de Aceitação:
1. Deve existir um bloco YAML demarcado por '---'.
2. As chaves 'name' e 'description' são obrigatórias.
3. Os valores devem ser válidos (preferencialmente com aspas duplas, 
   o PyYAML garantirá o parsing correto).
"""

import sys
import os
import yaml

class Colors:
    HEADER = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def validate_sdd_contract(filepath: str) -> bool:
    if not os.path.exists(filepath):
        print(f"{Colors.RED}❌ Ficheiro não encontrado: {filepath}{Colors.ENDC}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verifica se o arquivo tem metadados YAML
    if not content.startswith('---'):
        print(f"{Colors.RED}❌ Falha de SDD em {filepath}: Ausência de Frontmatter YAML ('---').{Colors.ENDC}")
        return False

    # Extrai o bloco YAML
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"{Colors.RED}❌ Falha de SDD em {filepath}: Bloco YAML malformado (falta fechamento '---').{Colors.ENDC}")
        return False

    yaml_block = parts[1]

    try:
        # O safe_load já valida se existem erros de parsing estrutural
        meta = yaml.safe_load(yaml_block)
        
        if not isinstance(meta, dict):
            print(f"{Colors.RED}❌ Falha de SDD em {filepath}: Frontmatter deve ser um dicionário YAML.{Colors.ENDC}")
            return False

        # Validação Estrita das Chaves
        missing_keys = []
        if 'name' not in meta:
            missing_keys.append('name')
        if 'description' not in meta:
            missing_keys.append('description')

        if missing_keys:
            print(f"{Colors.RED}❌ Falha de SDD em {filepath}: Chaves obrigatórias ausentes: {', '.join(missing_keys)}{Colors.ENDC}")
            return False

        print(f"{Colors.GREEN}✅ Contrato SDD validado: {filepath}{Colors.ENDC}")
        return True

    except yaml.YAMLError as exc:
        print(f"{Colors.RED}❌ Falha de parsing YAML em {filepath}:{Colors.ENDC}\n{exc}")
        return False

if __name__ == "__main__":
    target_files = sys.argv[1:]
    
    if not target_files:
        print("Nenhum arquivo submetido para validação SDD.")
        sys.exit(0)

    print(f"\n{Colors.BOLD}{Colors.HEADER}=== Iniciando Validação SDD (Gatekeeper) ==={Colors.ENDC}\n")
    
    all_passed = True
    for file in target_files:
        if not validate_sdd_contract(file):
            all_passed = False

    if not all_passed:
        print(f"\n{Colors.BOLD}{Colors.RED}Acesso Negado: O commit violou as regras arquiteturais SDD.{Colors.ENDC}")
        sys.exit(1)

    sys.exit(0)
