#!/usr/bin/env python3
"""
Architecture Auto-Sync - Antigravity Kit
========================================
Lê os manifestos YAML (SDD) de todas as skills, agentes e workflows,
compilando um mapa atualizado em .agents/ARCHITECTURE.md.
"""

import os
import yaml

# O script identifica a raiz do projeto independentemente de onde é chamado
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AGENTS_DIR = os.path.join(ROOT_DIR, '.agents')
OUTPUT_FILE = os.path.join(AGENTS_DIR, 'ARCHITECTURE.md')

def extract_sdd_metadata(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    meta = yaml.safe_load(parts[1])
                    if isinstance(meta, dict):
                        return meta.get('name'), meta.get('description')
    except Exception:
        pass
    return None, None

def generate_markdown():
    md = "# 🗺️ Mapa Arquitetural JINC Skills\n\n"
    md += "> **Nota:** Este documento é compilado automaticamente a cada commit. Modificações manuais serão sobrescritas.\n\n"

    # Define a ordem de importância para a leitura
    target_folders = ['agents', 'skills', 'workflows', 'rules']

    for folder in target_folders:
        folder_path = os.path.join(AGENTS_DIR, folder)
        if not os.path.exists(folder_path):
            continue

        md += f"## 📂 `{folder}/`\n\n"
        
        has_files = False
        for file in sorted(os.listdir(folder_path)):
            if file.endswith('.md'):
                has_files = True
                filepath = os.path.join(folder_path, file)
                name, desc = extract_sdd_metadata(filepath)
                
                if name and desc:
                    md += f"- **`{name}`** (`{file}`): {desc}\n"
                else:
                    md += f"- `{file}`: *(Aguardando conformidade SDD)*\n"
        
        if not has_files:
            md += "*Nenhum manifesto registrado nesta camada.*\n"
        md += "\n"

    return md

if __name__ == "__main__":
    print("🔄 Sincronizando arquitetura...")
    new_content = generate_markdown()
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"✅ ARCHITECTURE.md gerado com sucesso em .agents/ARCHITECTURE.md")
