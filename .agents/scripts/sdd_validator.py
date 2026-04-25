#!/usr/bin/env python3
import sys, os

class Colors:
    HEADER, GREEN, RED, ENDC, BOLD = '\033[95m', '\033[92m', '\033[91m', '\033[0m', '\033[1m'

EXEMPT_FILES = ['readme.md', 'architecture.md', 'changelog.md']

def validate_sdd_contract(filepath: str) -> bool:
    if not os.path.exists(filepath): return False
    
    filename = os.path.basename(filepath).lower()
    # Proteção para Rules e Isentos
    if filename in EXEMPT_FILES or '/.agents/rules/' in filepath.replace('\\', '/').lower():
        print(f"{Colors.HEADER}⏭️ Isento: {filename}{Colors.ENDC}")
        return True

    try:
        # Lê o arquivo de forma bruta (ignora YAML, foca em texto)
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read().lower()

        # Verifica apenas se as strings existem no topo do arquivo
        # Buscamos apenas nos primeiros 1000 caracteres para garantir performance
        header_sample = content[:1000]
        has_name = 'name:' in header_sample
        has_desc = 'description:' in header_sample

        if has_name and has_desc:
            print(f"{Colors.GREEN}✅ Validado: {filename}{Colors.ENDC}")
            return True
        else:
            print(f"{Colors.RED}❌ Falha em {filename}: Chaves não encontradas no texto.{Colors.ENDC}")
            return False

    except Exception as e:
        print(f"{Colors.RED}❌ Erro em {filename}: {str(e)}{Colors.ENDC}")
        return False

if __name__ == "__main__":
    files = sys.argv[1:]
    if not files: sys.exit(0)
    print(f"\n{Colors.BOLD}{Colors.HEADER}=== JINC SDD GATEKEEPER v7 (Modo Nuclear) ==={Colors.ENDC}\n")
    results = [validate_sdd_contract(f) for f in files]
    sys.exit(0 if all(results) else 1)
