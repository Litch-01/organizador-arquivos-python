# Organizador Automático de Arquivos em Python 🚀

Um script simples e útil que organiza sua pasta de **Downloads** (ou qualquer outra) automaticamente, separando arquivos por tipo em segundos!

**Antes** (pasta bagunçada com tudo misturado):  
![Antes](antes.png)

**Depois** (organizado em pastas como Imagens, Documentos, etc.):  
![Depois](depois.png)

## O que ele faz?
- Pergunta qual pasta organizar (default: Downloads)
- Separa por categorias:
  - Imagens (.jpg, .png, .webp...)
  - Documentos (.pdf, .docx, .txt...)
  - Vídeos (.mp4, .avi...)
  - Áudio (.mp3...)
  - Instaladores (.exe, .msi...)
  - Outros (o que não encaixar)
- Ignora arquivos indesejados (desktop.ini, .part, .crdownload...)
- Cria subpastas automaticamente
- Evita sobrescrever arquivos (adiciona (1), (2) se necessário)
- Mostra progresso com **cores** no terminal
- Gera um log txt com tudo que foi movido

## Tecnologias usadas
- Python 3 (padrão, sem dependências externas)
- Bibliotecas nativas: `os`, `shutil`, `pathlib`, `datetime`

## Como rodar (em 30 segundos)
1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USERNAME/organizador-arquivos-python.git
