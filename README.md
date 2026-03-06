# 🚀 Windows Startup Automation

Automation for preparing the work environment on Windows machines.

This project automates common tasks performed after user login, ensuring system services are running and specific educational applications are launched automatically in fullscreen mode.

The goal is to reduce manual intervention and standardize the usage environment on shared computers (e.g., labs or classrooms).

---

# ✨ Features

### 🔧 Hardware Sync
Ensures keyboard state keys are correctly configured:

- Enables **Caps Lock** if it is off
- Enables **Num Lock** if it is off

---

### 📡 Service Management
Automatically checks and starts the **Bluetooth** service (`bthserv`) using PowerShell.

---

### 🖥️ Application Automation

The system automatically detects desktop shortcuts and launches:

- **Matific**
- **Elefante Letrado**

Features:

- **Case-insensitive** detection
- Flexible matching based on **regex**
- Does not depend on the exact shortcut name

Supported examples:

```
Matific.lnk
MATIFIC Escola.lnk
Login - Elefante Letrado.lnk
Elefante.lnk
```

---

### 🪟 Window Orchestration

After launching the programs:

- Waits for the window to load
- Puts the application in **fullscreen mode (F11)**
- Minimizes the first app to allow smooth switching between applications

---

### ⏱️ Boot Stabilization

Includes a **preventive initial delay** to avoid conflicts with services still loading during Windows login.

---

# 🛠️ Technologies Used

- **Python**
- **PyAutoGUI** — keyboard automation
- **PyGetWindow** — window management
- **Win32 API (ctypes)** — keyboard state detection
- **Subprocess / OS** — system command execution

---

# 📦 Development Setup

## 1. Clone the repository

```bash
git clone https://github.com/your-username/windows-startup-automation.git
cd windows-startup-automation
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔨 Building the Executable (.exe)

For distribution on machines without Python installed, we use **PyInstaller**.

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --noconsole startup.py
```

After the build:

- The executable will be located at:

```
dist/startup.exe
```

Temporary files can be removed:

```powershell
Remove-Item -Recurse -Force build, *.spec
```

---

# 🚀 Running Automatically on Windows

To run the script automatically at startup:

1. Press **Win + R**
2. Type:

```
shell:startup
```

3. Place the **startup.exe** file (or a shortcut to it) in this folder.

The script will run automatically after user login.

---

# ⚠️ Notes

- Application shortcuts must be on the **user's Desktop**
- Windows may display a **SmartScreen** warning when running the `.exe`

To proceed:

```
More info → Run anyway
```

---

# 📂 Repository Structure

```
.
├── startup.py
├── requirements.txt
├── .gitignore
└── README.md
```
