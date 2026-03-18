# Organizador Automático de Arquivos em Python 🚀

Um script simples e útil que organiza sua pasta de **Downloads** (ou qualquer outra) automaticamente, separando arquivos por tipo em segundos!

**Antes** (pasta bagunçada com tudo misturado):  
![Antes](<img width="1897" height="1010" alt="pasta bagunçada" src="https://github.com/user-attachments/assets/9d50edb8-b022-4072-9167-f8b00bdc0c5c" />
)

**Depois** (organizado em pastas como Imagens, Documentos, etc.):  
![Depois](<img width="818" height="143" alt="pastas organizadas1" src="https://github.com/user-attachments/assets/58540b19-6f36-40a5-b22b-5e0928390779" />
)
(<img width="1302" height="987" alt="documentos organizados" src="https://github.com/user-attachments/assets/d352bd47-ad33-4041-8f4c-816c9657af0a" />
)
(<img width="1398" height="898" alt="imagens organizados" src="https://github.com/user-attachments/assets/8bd8d9ab-e197-40ce-b727-408589933432" />
)
(<img width="1142" height="902" alt="outros organizados" src="https://github.com/user-attachments/assets/b57535af-e1e7-456f-af27-9968080de2bb" />
)

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
