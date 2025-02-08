### **Set Up SSH Key for GitHub in WSL2**

Follow these steps to configure SSH authentication for GitHub in **WSL2**:

---

### **1. Check for Existing SSH Keys**

First, check if you already have an SSH key:

```bash
ls -l ~/.ssh/id_rsa.pub
```

- If the file **exists**, you can use it. Skip to **Step 3**.
- If **not found**, proceed to **Step 2** to generate a new SSH key.

---

### **2. Generate a New SSH Key**

Run the following command, replacing `"your-email@example.com"` with your GitHub email:

```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```

- When prompted, **press Enter** to accept the default location (`~/.ssh/id_rsa`).
- Optionally, set a **passphrase** for added security.

---

### **3. Start the SSH Agent and Add Your Key**

Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

Then add your SSH key:

```bash
ssh-add ~/.ssh/id_rsa
```

---

### **4. Add Your SSH Key to GitHub**

Copy your SSH public key:

```bash
cat ~/.ssh/id_rsa.pub
```

- Copy the displayed key.

Then, **add it to GitHub**:

1. Go to **GitHub** → Click your **profile picture** → **Settings**.
2. Navigate to **"SSH and GPG keys"**.
3. Click **"New SSH Key"**, paste your key, and click **"Add SSH Key"**.

---

### **5. Test SSH Connection with GitHub**

Run the following command to test the connection:

```bash
ssh -T git@github.com
```

If successful, you should see:

```
Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
```

---

### **6. Configure Git to Use SSH (Optional)**

Set Git to use SSH instead of HTTPS for cloning:

```bash
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

Now, you can clone repositories using SSH:

```bash
git clone git@github.com:your-username/your-repository.git
```

---

Let me know if you need further assistance! 🚀
