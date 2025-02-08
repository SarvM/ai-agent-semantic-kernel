# 🚀 Setting Up WSL2 on a Windows Machine for Python Development

## **Step 1: Enable WSL and Virtual Machine Platform**

### ✅ **Run the following command in PowerShell as Administrator**:

```powershell
wsl --install
```

- This command enables **WSL**, installs **Ubuntu (default)**, and sets WSL2 as the default version.

👉 If you need a different Linux distro (e.g., Debian, Kali), list available options:

```powershell
wsl --list --online
```

Then install your preferred distro:

```powershell
wsl --install -d Debian
```

📌 **(If you already have WSL1, upgrade it to WSL2 with these commands):**

```powershell
wsl -l -v  # To identify the version
wsl --set-version Ubuntu 2
```

---

## **Step 2: Install a Linux Distribution**

After installation, restart your PC and open **Ubuntu** (or your chosen Linux distro) from the Start Menu.

- It will prompt you to create a **new Linux user** (this is separate from your Windows account).
- Set a **username** and **password** (e.g., `yourname`).

---

## **Step 3: Update Linux Packages**

After logging into your WSL2 Linux terminal, update your system:

```bash
sudo apt update && sudo apt upgrade -y
```

---

## **Step 4: Install Python & Pip in WSL2**

Most distributions come with Python preinstalled. Check your version:

```bash
python3 --version
```

If Python is not installed, install it using:

```bash
sudo apt install python3 python3-pip -y
```

Ensure `pip` (Python package manager) is up to date:

```bash
sudo apt install python3-pip
```

---

Trust All /mnt/c/ Directories

```bash
git config --global --add safe.directory "*"
```

## **Step 5: Set Up a Python Virtual Environment (Recommended)**

To avoid conflicts, create a virtual environment for your projects:

```bash
sudo apt install python3-venv -y
python3 -m venv myenv
source myenv/bin/activate
```

When activated, you’ll see `(myenv)` in the terminal.

To deactivate:

```bash
deactivate
```

---

## **Step 6: Install VS Code and WSL Extension**

To write and run Python code efficiently:

1. **Install VS Code** from [official site](https://code.visualstudio.com/)
2. Install the **Remote - WSL Extension** from the **VS Code Extensions Marketplace**
3. Open VS Code and connect to WSL:
   - Press `Ctrl + Shift + P`
   - Select **"Remote-WSL: New Window"**
   - Open your project folder (`/home/yourname/project`)

---

## **Step 7: Install Essential Python Development Tools**

For REST API development:

```bash
pip install fastapi uvicorn flask requests
```

For AI/ML and **Semantic Kernel**:

```bash
pip install semantic-kernel openai langchain torch
```

---

## **Step 8: Enable Windows-WSL File Sharing (Optional)**

Your Linux files are in:

```bash
/home/yourname/
```

You can access them from Windows via:

```
\\wsl$\Ubuntu\home\yourname\
```

Similarly, access your **Windows files in WSL**:

```bash
cd /mnt/c/Users/YourName/
```

---

## **Step 9: Running a Python Web Server in WSL2**

Run a **FastAPI or Flask app**:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Then, open your browser and go to:

```
http://localhost:8000
```

---

## **Step 10: (Optional) Enable GPU Acceleration for AI/ML**

If you're working on AI/ML, install **NVIDIA CUDA support for WSL2**:

```bash
sudo apt install nvidia-cuda-toolkit -y
```

Check GPU support:

```bash
nvidia-smi
```
