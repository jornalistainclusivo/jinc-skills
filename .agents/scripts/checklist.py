#!/usr/bin/env python3
"""
Antigravity Kit - SDD Contract Validator
========================================
Valida a estrutura YAML (Frontmatter) de Agentes e Skills
garantindo a conformidade com o Desenvolvimento Orientado a Especificações.
"""

import sys
import yaml
from pathlib import Path
from pydantic import BaseModel, ValidationError

# ANSI colors
class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# ==========================================
# 1. Contratos Estritos (Schemas SDD)
# ==========================================

class SkillSchema(BaseModel):
    name: str
    description: str

class AgentSchema(BaseModel):
    name: str
    focus: str
    skills_used: str | list[str]

# ==========================================
# 2. Motor de Extração
# ==========================================

def extract_yaml_frontmatter(file_path: Path) -> dict:
    """Extrai e higieniza o bloco YAML de um arquivo Markdown."""
    try:
        content = file_path.read_text(encoding='utf-8')
        if not content.startswith('---'):
            return {}
        
        yaml_block = content.split('---')[1]
        metadata = yaml.safe_load(yaml_block) or {}
        
        # Higienização contra artefatos da IDE Antigravity
        metadata.pop("$typeName", None)
        return metadata
    except Exception as e:
        print(f"{Colors.RED}[ERRO DE LEITURA] {file_path.name}: {e}{Colors.ENDC}")
        return {}

# ==========================================
# 3. Lógica de Validação
# ==========================================

def validate_directory(target_dir: Path, schema_class, entity_name: str) -> int:
    """Valida arquivos .md contra o schema Pydantic."""
    print(f"\n{Colors.BOLD}{Colors.CYAN}🔍 Validando {entity_name} em: {target_dir}{Colors.ENDC}")
    
    if not target_dir.exists():
        print(f"{Colors.YELLOW}  ⚠️ Diretório não encontrado.{Colors.ENDC}")
        return 0

    # FILTRO ARQUITETURAL CORRIGIDO:
    if entity_name == "Skills":
        # Nas skills, apenas o manifesto SKILL.md importa para o SDD
        md_files = list(target_dir.rglob('SKILL.md'))
    else:
        # Nos agentes, varre .md ignorando a documentação global do ecossistema
        md_files = [f for f in target_dir.rglob('*.md') if f.name.upper() not in ['README.MD', 'ARCHITECTURE.MD', 'AGENTS.MD', 'GEMINI.MD']]
    
    if not md_files:
        print(f"{Colors.YELLOW}  ⚠️ Nenhum manifesto encontrado.{Colors.ENDC}")
        return 0

    errors = 0
    for file in md_files:
        data = extract_yaml_frontmatter(file)
        if not data:
            print(f"{Colors.RED}  ❌ {file.name} ({file.parent.name}): Frontmatter YAML ausente ou inválido.{Colors.ENDC}")
            errors += 1
            continue
            
        try:
            schema_class(**data)
            print(f"{Colors.GREEN}  ✅ {file.name} ({file.parent.name}){Colors.ENDC}")
        except ValidationError as e:
            print(f"{Colors.RED}  ❌ {file.name} ({file.parent.name}): Quebra de Contrato SDD{Colors.ENDC}")
            for err in e.errors():
                print(f"{Colors.RED}     -> Campo '{err['loc'][0]}': {err['msg']}{Colors.ENDC}")
            errors += 1
            
    return errors

def main():
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}      JINC SKILLS - SDD CONTRACT VALIDATOR{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}")

    # Determina o diretório base (.agents)
    base_dir = Path('.agents') if Path('.agents').exists() else Path('.')
    
    total_errors = 0
    total_errors += validate_directory(base_dir / "skills", SkillSchema, "Skills")
    total_errors += validate_directory(base_dir / "agents", AgentSchema, "Agentes")
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*60}{Colors.ENDC}")
    if total_errors > 0:
        print(f"{Colors.RED}❌ Falha: {total_errors} erro(s) estrutural(is) detectado(s). Corrija antes de commitar.{Colors.ENDC}\n")
        sys.exit(1)
    else:
        print(f"{Colors.GREEN}✅ Sucesso: Todos os contratos SDD estão em conformidade.{Colors.ENDC}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
