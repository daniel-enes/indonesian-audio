# Indonesian Audio

Projeto em Python para gerar arquivos de áudio em indonésio (MP3) a
partir de arquivos de texto, utilizando o pacote
[`edge-tts`](https://github.com/rany2/edge-tts).

A ferramenta pode ser usada para criar materiais de compreensão
auditiva, permitindo escolher entre vozes masculinas e femininas e
ajustar a velocidade da fala.

## Requisitos

-   Ubuntu ou outra distribuição Linux.
-   Python 3.
-   Conexão com a internet para gerar os áudios, pois o `edge-tts`
    utiliza o serviço online de síntese de voz da Microsoft.
-   `python3-venv` instalado para criar ambientes virtuais.

## Estrutura do projeto

``` text
indonesian-audio/
├── .venv/                 # Ambiente virtual Python (não versionar)
├── exercicios/            # Arquivos TXT com textos em indonésio
│   ├── 01-viagem.txt
│   └── 02-futebol.txt
├── audios/                # Áudios MP3 gerados (opcionalmente não versionar)
├── gerar_audio.py         # Script de geração de áudio
└── README.md
```

A estrutura pode variar conforme os exercícios adicionados ao projeto.

## 1. Preparar o ambiente

Clone o repositório e entre na pasta do projeto:

``` bash
git clone <URL_DO_REPOSITORIO>
cd indonesian-audio
```

Crie um ambiente virtual:

``` bash
python3 -m venv .venv
```

Se o comando informar que o módulo `venv` não está disponível no Ubuntu,
instale o pacote necessário:

``` bash
sudo apt update
sudo apt install python3-venv
```

Ative o ambiente virtual:

``` bash
source .venv/bin/activate
```

Instale ou atualize o `pip` e instale a dependência:

``` bash
python -m pip install --upgrade pip
python -m pip install edge-tts
```

Sempre que abrir um novo terminal para trabalhar no projeto, ative
novamente o ambiente virtual:

``` bash
cd ~/indonesian-audio
source .venv/bin/activate
```

Ajuste o caminho caso o repositório esteja em outra pasta.

## 2. Preparar um texto em indonésio

Crie um arquivo `.txt` dentro da pasta `exercicios/`. Por exemplo:

``` bash
mkdir -p exercicios audios
nano exercicios/01-viagem.txt
```

Digite ou cole o texto em indonésio, salve o arquivo e feche o editor.

O script lê o arquivo como UTF-8, portanto caracteres acentuados e
outros caracteres Unicode são aceitos.

## 3. Gerar um áudio MP3

O comando básico é:

``` bash
python gerar_audio.py
```

Sem argumentos, o programa utiliza os seguintes valores padrão:

-   **Texto:** `exercicios/01-viagem.txt`
-   **Voz:** feminina (`id-ID-GadisNeural`)
-   **Velocidade:** `-30%`
-   **Arquivo de saída:** `audios/01-viagem.mp3`

Para gerar um áudio de outro texto, indique os argumentos desejados.

### Exemplo: voz masculina

``` bash
python gerar_audio.py \
  --texto exercicios/02-futebol.txt \
  --voz masculina \
  --velocidade=-30% \
  --saida audios/02-futebol.mp3
```

O sinal de igual em `--velocidade=-30%` evita que o `argparse`
interprete o valor negativo como uma nova opção.

### Exemplo: voz feminina

``` bash
python gerar_audio.py \
  --texto exercicios/01-viagem.txt \
  --voz feminina \
  --velocidade=-30% \
  --saida audios/01-viagem-feminina.mp3
```

### Exemplo: velocidade normal

``` bash
python gerar_audio.py \
  --texto exercicios/01-viagem.txt \
  --velocidade=+0% \
  --saida audios/01-viagem-normal.mp3
```

### Exemplo: fala mais rápida

``` bash
python gerar_audio.py \
  --texto exercicios/01-viagem.txt \
  --velocidade=+10% \
  --saida audios/01-viagem-rapida.mp3
```

## 4. Opções do programa

  ----------------------------------------------------------------------------
  Argumento               Descrição               Valor padrão
  ----------------------- ----------------------- ----------------------------
  `--texto`               Caminho do arquivo      `exercicios/01-viagem.txt`
                          `.txt` com o texto em   
                          indonésio               

  `--voz`                 Voz usada na narração:  `feminina`
                          `feminina` ou           
                          `masculina`             

  `--velocidade`          Ajuste relativo da      `-30%`
                          velocidade da fala, por 
                          exemplo `-30%`, `+0%`   
                          ou `+10%`               

  `--saida`               Caminho e nome do       `audios/01-viagem.mp3`
                          arquivo MP3 gerado      
  ----------------------------------------------------------------------------

Para consultar as opções disponíveis:

``` bash
python gerar_audio.py --help
```

As vozes configuradas no código são:

-   `feminina`: `id-ID-GadisNeural`
-   `masculina`: `id-ID-ArdiNeural`

A lista de vozes disponíveis pode mudar. Para consultar as vozes de
indonésio reconhecidas pelo `edge-tts`, execute:

``` bash
edge-tts --list-voices | grep 'id-ID'
```

Se uma voz deixar de estar disponível, atualize o identificador no
dicionário `VOICES` do arquivo `gerar_audio.py`.

## 5. Reproduzir o áudio

No Ubuntu, abra o arquivo gerado com:

``` bash
xdg-open audios/01-viagem.mp3
```

O arquivo também pode ser aberto pelo gerenciador de arquivos ou por um
reprodutor de áudio instalado no sistema.

## 6. Fluxo sugerido para praticar compreensão auditiva

1.  Leia o glossário do exercício, sem consultar a transcrição completa.
2.  Ouça o MP3 sem olhar o texto original.
3.  Anote em português o que conseguiu compreender.
4.  Ouça novamente e tente identificar as partes que faltaram.
5.  Compare sua compreensão com a transcrição e a tradução.
6.  Revise as palavras novas e recupere palavras estudadas
    anteriormente.

## 7. Observações

-   A geração do áudio requer conexão com a internet.
-   O projeto utiliza `edge-tts`, que acessa o serviço online de síntese
    de voz da Microsoft; não é um sintetizador totalmente local.
-   A velocidade definida no programa é um ajuste de síntese. O
    resultado percebido pode variar conforme a voz e o texto.
-   Os nomes de vozes e a disponibilidade do serviço podem mudar com o
    tempo.
-   Evite versionar o ambiente virtual `.venv/`, pois ele é específico
    da máquina.
-   Os arquivos de áudio podem ocupar espaço no repositório. Decida se
    deseja versioná-los ou mantê-los localmente.

## 8. `.gitignore` sugerido

Crie um arquivo `.gitignore` na raiz do projeto para não enviar o
ambiente virtual nem arquivos temporários:

``` gitignore
.venv/
__pycache__/
*.py[cod]
```

Se preferir não enviar os MP3s ao GitHub, adicione também:

``` gitignore
audios/
```

Se decidir versionar os áudios de exemplo, não adicione essa última
regra.

## Referências

-   [Repositório do edge-tts](https://github.com/rany2/edge-tts)
-   [Documentação e opções de uso do
    edge-tts](https://github.com/rany2/edge-tts#command-line)
