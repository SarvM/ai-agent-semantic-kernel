
To install **Microsoft Semantic Kernel** on **WSL2 with Python**, follow these steps:

---

### **1. Ensure WSL2 and Python are Installed**
- Open **WSL2 terminal** (`Ubuntu` or your chosen distro).
- Check if Python is installed:  
  ```bash
  python3 --version
  ```
  If not, install it:
  ```bash
  sudo apt update && sudo apt install python3 python3-pip -y
  ```

---

### **2. Create a Virtual Environment (Optional but Recommended)**
```bash
python3 -m venv sk_env
source sk_env/bin/activate  # Activate virtual environment
```

---

### **3. Install Microsoft Semantic Kernel**
```bash
pip install semantic-kernel
```

---

### **4. Verify Installation**
```python
python3 -c "import semantic_kernel; print(semantic_kernel.__version__)"
```



