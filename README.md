# 🧾 Contact QR Code Generator

![QR Code Generator](https://github.com/Anandpal-123/qr-code-generator/actions/workflows/qr_generator.yml/badge.svg)    

This project generates **QR codes for contact details** (Name, Email, Phone) using Python.  
It is automated with **GitHub Actions** to generate QR codes on every push and upload them as artifacts.

---

## 📂 Features
- Generate QR codes for multiple contacts
- Save each QR code as an image (`.png`)
- Automated GitHub Actions workflow:
  - Installs dependencies
  - Runs the generator script
  - Uploads QR codes as artifacts

---

## 🚀 How It Works
1. Define your contact details in [`generate_qr.py`](generate_qr.py)  
2. Push code to the `qr_code` branch  
3. GitHub Actions will:
   - Run the Python script
   - Generate QR codes
   - Upload them as artifacts

---

## 🛠️ Run Locally
If you want to test locally:

```bash
# Clone this repository
git clone https://github.com/your-username/qr-code-generator.git
cd contact-qr-code-generator

# Install dependencies
pip install qrcode[pil]

# Run the script
python generate_qr.py