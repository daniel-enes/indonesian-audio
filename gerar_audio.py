import argparse
import asyncio
from pathlib import Path

import edge_tts


VOICES = {
    "feminina": "id-ID-GadisNeural",
    "masculina": "id-ID-ArdiNeural",
}


async def gerar_audio(
    texto: str,
    voz: str,
    velocidade: str,
    arquivo_saida: Path,
) -> None:
    comunicacao = edge_tts.Communicate(
        text=texto,
        voice=voz,
        rate=velocidade,
    )

    await comunicacao.save(str(arquivo_saida))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gera áudios MP3 para exercícios de indonésio."
    )

    parser.add_argument(
        "--texto",
        default="exercicios/01-viagem.txt",
        help="Caminho do arquivo TXT com o texto em indonésio.",
    )

    parser.add_argument(
        "--voz",
        choices=VOICES.keys(),
        default="feminina",
        help="Voz utilizada na narração.",
    )

    parser.add_argument(
        "--velocidade",
        default="-30%",
        help="Velocidade da fala. Exemplo: -10%%, +0%% ou +10%%.",
    )

    parser.add_argument(
        "--saida",
        default="audios/01-viagem.mp3",
        help="Caminho do arquivo MP3 gerado.",
    )

    args = parser.parse_args()

    arquivo_texto = Path(args.texto)
    arquivo_saida = Path(args.saida)

    if not arquivo_texto.is_file():
        raise SystemExit(
            f"Arquivo de texto não encontrado: {arquivo_texto}"
        )

    texto = arquivo_texto.read_text(encoding="utf-8").strip()

    if not texto:
        raise SystemExit("O arquivo de texto está vazio.")

    arquivo_saida.parent.mkdir(parents=True, exist_ok=True)

    voz = VOICES[args.voz]

    try:
        asyncio.run(
            gerar_audio(
                texto=texto,
                voz=voz,
                velocidade=args.velocidade,
                arquivo_saida=arquivo_saida,
            )
        )
    except Exception as erro:
        raise SystemExit(
            f"Não foi possível gerar o áudio: {erro}"
        ) from erro

    print(f"Áudio gerado com sucesso: {arquivo_saida}")
    print(f"Voz: {args.voz} ({voz})")
    print(f"Velocidade: {args.velocidade}")


if __name__ == "__main__":
    main()
