import datetime
import shutil
from pathlib import Path

VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"


def main():
    print(f"{AZUL}=== Organizador de Arquivos - Versão Pro ==={RESET}")

    default = str(Path.home() / "Downloads")
    print(f"Pasta padrão: {default}")
    entrada = input(
        "Digite o caminho completo da pasta (ou Enter para usar padrão): "
    ).strip()
    pasta_origem = Path(entrada if entrada else default)

    if not pasta_origem.exists() or not pasta_origem.is_dir():
        print(f"{VERMELHO}Erro: Pasta não encontrada → {pasta_origem}{RESET}")
        return

    print(f"{VERDE}Organizando: {pasta_origem}{RESET}\n")

    categorias = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff"],
        "Documentos": [
            ".pdf",
            ".doc",
            ".docx",
            ".txt",
            ".rtf",
            ".odt",
            ".xlsx",
            ".xls",
            ".pptx",
            ".csv",
        ],
        "Vídeos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
        "Áudio": [".mp3", ".wav", ".flac", ".m4a", ".ogg"],
        "Instaladores": [".exe", ".msi", ".msix"],
        "Outros": [],
    }

    ignorar = {".ini", ".part", ".crdownload", ".tmp", ".temp"}

    contagem = {cat: 0 for cat in categorias}
    movidos_total = 0

    data_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    log_nome = f"organizado_em_{data_hora}.txt"
    log_path = pasta_origem / log_nome
    with open(log_path, "w", encoding="utf-8") as log:
        log.write(f"Organização realizada em: {datetime.datetime.now()}\n")
        log.write(f"Pasta: {pasta_origem}\n\n")

    for arquivo in pasta_origem.iterdir():
        if not arquivo.is_file():
            continue

        extensao = arquivo.suffix.lower()
        nome = arquivo.name

        if extensao in ignorar or nome.startswith(".") or nome == "desktop.ini":
            print(f"{AMARELO}Ignorado: {nome}{RESET}")
            continue

        categoria = "Outros"
        for cat, exts in categorias.items():
            if extensao in exts:
                categoria = cat
                break

        pasta_destino = pasta_origem / categoria
        pasta_destino.mkdir(exist_ok=True)

        destino_final = pasta_destino / nome
        contador = 1
        while destino_final.exists():
            stem = Path(nome).stem
            ext = Path(nome).suffix
            destino_final = pasta_destino / f"{stem} ({contador}){ext}"
            contador += 1

        try:
            shutil.move(str(arquivo), str(destino_final))
            print(f"{VERDE}Movido:{RESET} {nome:50} → {categoria}")
            contagem[categoria] += 1
            movidos_total += 1

            with open(log_path, "a", encoding="utf-8") as log:
                log.write(f"Movido: {nome} → {categoria}\n")

        except Exception as e:
            print(f"{VERMELHO}Erro ao mover {nome}: {e}{RESET}")

    print(f"\n{VERDE}=== Resumo da Organização ==={RESET}")
    print(f"Arquivos movidos no total: {movidos_total}")
    for cat, qtd in contagem.items():
        if qtd > 0:
            print(f"  → {cat}: {qtd}")
    print(f"{AMARELO}Log salvo em: {log_nome}{RESET}")
    print(f"{VERDE}Organização concluída! 🚀{RESET}")


if __name__ == "__main__":
    main()
