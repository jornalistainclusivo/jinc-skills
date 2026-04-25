#!/usr/bin/env python3
import sys, os, re

class Colors:
    HEADER, GREEN, RED, ENDC, BOLD = '\033[95m', '\033[92m', '\033[91m', '\033[0m', '\033[1m'

EXEMPT_FILES = ['readme.md', 'architecture.md', 'changelog.md']

def validate_sdd_contract(filepath: str) -> bool:
    if not os.path.exists(filepath): return False
    filename = os.path.basename(filepath).lower()
    
    if filename in EXEMPT_FILES or '/.agents/rules/' in filepath.replace('\\', '/').lower():
        print(f"{Colors.HEADER}⏭️ Isento: {filename}{Colors.ENDC}")
        return True

    try:
        # Lendo as primeiras 20 linhas para máxima performance e foco
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            head = [next(f).lower() for _ in range(20)]
        
        content = "".join(head)
        
        # Procura por name e description ignorando espaços extras e aspas
        has_name = re.search(r'name\s*:\s*', content)
        has_desc = re.search(r'description\s*:\s*', content)

        if has_name and has_desc:
            print(f"{Colors.GREEN}✅ Validado: {filename}{Colors.ENDC}")
            return True
        else:
            print(f"{Colors.RED}❌ Falha em {filename}:")
            if not has_name: print(f"   - Faltando 'name:'")
            if not has_desc: print(f"   - Faltando 'description:'")
            print(f"   --- DEBUG: O que o script leu nas primeiras linhas: ---")
            print(f"{content.strip()}")
            print(f"   --------------------------------------------------------{Colors.ENDC}")
            return False
    except StopIteration:
        return validate_sdd_contract_full(filepath) # Caso o arquivo seja muito pequeno
    except Exception as e:
        print(f"{Colors.RED}❌ Erro em {filename}: {str(e)}{Colors.ENDC}")
        return False

def validate_sdd_contract_full(filepath):
    # Fallback para arquivos minúsculos
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read().lower()
    return 'name:' in content and 'description:' in content

if __name__ == "__main__":
    files = sys.argv[1:]
    if not files: sys.exit(0)
    print(f"\n{Colors.BOLD}{Colors.HEADER}=== JINC SDD GATEKEEPER v7 (Nuclear Edition) ==={Colors.ENDC}\n")
    results = [validate_sdd_contract(f) for f in files]
    sys.exit(0 if all(results) else 1)
