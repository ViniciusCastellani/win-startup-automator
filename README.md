# 🚀 Windows Automation Startup Optimizer

Este projeto automatiza a preparação do ambiente de trabalho em máquinas Windows. Ele gerencia estados de hardware (periféricos), serviços de sistema (Bluetooth) e orquestra a abertura de aplicações específicas (Matific e Elefante Letrado) garantindo que fiquem em modo tela cheia e devidamente organizadas.

## ✨ Funcionalidades Principais

* **Hardware Sync:** Ativa `NumLock` e `CapsLock` automaticamente caso estejam desligados.
* **Service Management:** Garante que o serviço de Bluetooth (`bthserv`) esteja rodando via PowerShell.
* **Orquestração de Janelas:** - Abre atalhos da área de trabalho de forma assíncrona.
* Monitora o carregamento dos processos.
* Aplica comandos de interface (Tela Cheia via F11).
* Gerencia o foco e minimização para transição suave entre apps.


* **Boot Optimization:** Inclui um delay preventivo para evitar conflitos com o carregamento inicial do Windows.

---

## 🛠️ Tecnologias Utilizadas

* **PyAutoGUI:** Automação de entradas de teclado e macros.
* **PyGetWindow:** Manipulação e filtragem de janelas ativas.
* **PyWin32 (Win32API):** Interação de baixo nível com o kernel do Windows.
* **Subprocess/OS:** Execução de comandos de sistema e gestão de arquivos.

---

## 📦 Instalação e Configuração

### 1. Clonando o repositório

```bash
git clone https://github.com/seu-usuario/windows-startup-automation.git
cd windows-startup-automation

```

### 2. Instalando Dependências

Recomenda-se o uso de um ambiente virtual:

```bash
python -m venv venv
source venv/scripts/activate  # No Windows
pip install -r requirements.txt

```

---

## 🔨 Gerando o Executável (.exe)

Para distribuir o software para máquinas sem Python instalado, utilizamos o **PyInstaller**.

1. **Gere o build:**
```bash
pyinstaller --onefile --noconsole startup.py

```


2. **Limpeza de resíduos:**
Após a conclusão, você verá as pastas `build/` e o arquivo `.spec`. Eles são temporários e podem ser removidos:
```powershell
Remove-Item -Recurse -Force build, *.spec

```


3. **Resultado:** O executável final estará pronto na pasta `dist/`.

---

## 🚀 Como usar na Inicialização do Windows

Para que a automação funcione sempre que o computador for ligado:

1. Pressione `Win + R`.
2. Digite `shell:startup` e pressione Enter.
3. Mova o arquivo `startup.exe` (ou um atalho para ele) para esta pasta.

> **Nota:** Certifique-se de que os atalhos `Matific.lnk` e `Elefante Letrado Login.lnk` estejam presentes na Área de Trabalho do usuário.

---

## 📂 Estrutura do Repositório

```text
.
├── startup.py           # Script principal de automação
├── requirements.txt     # Lista de dependências Python
├── .gitignore           # Filtro de arquivos para Git (Ignora build/ e dist/)
└── README.md            # Documentação do projeto

```
