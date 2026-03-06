# 🚀 Windows Startup Automation

Automação para preparação do ambiente de trabalho em máquinas Windows.

Este projeto automatiza tarefas comuns realizadas após o login do usuário, garantindo que serviços do sistema estejam ativos e aplicações educacionais específicas sejam abertas automaticamente em modo tela cheia.

O objetivo é reduzir intervenção manual e padronizar o ambiente de uso em computadores compartilhados (por exemplo, laboratórios ou salas de aula).

---

# ✨ Funcionalidades

### 🔧 Hardware Sync
Garante que as teclas de estado estejam corretamente configuradas:

- Ativa **Caps Lock** caso esteja desligado
- Ativa **Num Lock** caso esteja desligado

---

### 📡 Service Management
Verifica e inicia automaticamente o serviço de **Bluetooth** (`bthserv`) utilizando PowerShell.

---

### 🖥️ Automação de Aplicações

O sistema detecta automaticamente atalhos na área de trabalho e executa:

- **Matific**
- **Elefante Letrado**

Características:

- Detecção **case-insensitive**
- Busca flexível baseada em **regex**
- Não depende do nome exato do atalho

Exemplos suportados:

```

Matific.lnk
MATIFIC Escola.lnk
Login - Elefante Letrado.lnk
Elefante.lnk

````

---

### 🪟 Orquestração de Janelas

Após abrir os programas:

- Aguarda o carregamento da janela
- Coloca o aplicativo em **modo tela cheia (F11)**
- Minimiza o primeiro app para permitir alternância suave entre aplicações

---

### ⏱️ Boot Stabilization

Inclui um **delay inicial preventivo** para evitar conflitos com serviços ainda carregando durante o login do Windows.

---

# 🛠️ Tecnologias Utilizadas

- **Python**
- **PyAutoGUI** — automação de teclado
- **PyGetWindow** — manipulação de janelas
- **Win32 API (ctypes)** — verificação de estados de teclado
- **Subprocess / OS** — execução de comandos do sistema

---

# 📦 Instalação para Desenvolvimento

## 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/windows-startup-automation.git
cd windows-startup-automation
````

---

## 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 🔨 Gerando o Executável (.exe)

Para distribuição em máquinas sem Python instalado utilizamos **PyInstaller**.

Instale o PyInstaller:

```bash
pip install pyinstaller
```

Gerar executável:

```bash
pyinstaller --onefile --noconsole startup.py
```

Após o build:

* O executável estará em:

```
dist/startup.exe
```

Arquivos temporários podem ser removidos:

```powershell
Remove-Item -Recurse -Force build, *.spec
```

---

# 🚀 Executando automaticamente no Windows

Para rodar o script automaticamente ao iniciar o computador:

1. Pressione **Win + R**
2. Digite:

```
shell:startup
```

3. Coloque o arquivo **startup.exe** (ou um atalho para ele) nesta pasta.

O script será executado automaticamente após o login do usuário.

---

# ⚠️ Observações

* Os atalhos das aplicações devem estar na **Área de Trabalho do usuário**
* O Windows pode exibir um alerta **SmartScreen** ao executar o `.exe`

Para continuar:

```
More info → Run anyway
```

---

# 📂 Estrutura do Repositório

```
.
├── startup.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📜 Licença

Projeto distribuído para fins educacionais e de automação de ambiente Windows.

```

---

# Descrição da Release (GitHub)

Título da release:

```

v1.0.0 - Initial Release

````

Descrição:

```markdown
## Windows Startup Automation v1.0.0

Primeira versão estável da ferramenta de automação de inicialização para Windows.

Este executável automatiza a preparação do ambiente de trabalho após o login do usuário, garantindo que periféricos e serviços estejam ativos e que aplicações educacionais sejam abertas automaticamente em tela cheia.

---

## Funcionalidades

- Ativa automaticamente **Caps Lock** e **Num Lock**
- Inicia o serviço **Bluetooth (bthserv)**
- Detecta e abre automaticamente os aplicativos:
  - Matific
  - Elefante Letrado
- Busca de atalhos baseada em **regex** (não depende do nome exato)
- Coloca os aplicativos em **modo tela cheia**
- Gerencia foco e minimização de janelas
- Delay inicial para evitar conflitos durante o boot

---

## Como usar

1. Baixe `startup.exe`
2. Execute o arquivo
3. Para execução automática, coloque o executável em:

````

shell:startup

```

---

## Requisitos

- Windows 10 ou superior

Python **não é necessário** para executar o programa.

---

## Observação

O Windows pode exibir um aviso do **SmartScreen** porque o executável não é assinado digitalmente.

Clique:

```

More info → Run anyway

```
```
