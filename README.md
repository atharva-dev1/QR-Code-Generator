# 📌 QR Code Generator in Python

A simple yet powerful **QR Code Generator** built using Python.
This project can generate QR codes for **links, text, images, contact info, and more** — all in seconds!

<img width="1920" height="1080" alt="Screenshot (60)" src="https://github.com/user-attachments/assets/097b3e31-37ee-4e9d-8dd2-16728ead274f" />


<img width="1920" height="1080" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/8c0ea575-eafa-4de0-94a4-a34ed99da958" />


---

## 🚀 Features

✔ Generate QR codes for:

* 🔗 **URLs / Links**
* 📝 **Plain Text**
* 🖼️ **Image Paths**
* 📱 **Contact Information (vCard)**
* 📄 **Any custom data**

✔ Save QR Codes as image files (PNG/JPG)
✔ Beginner-friendly and clean code
✔ Fast and lightweight
✔ Works offline
✔ Customizable QR size and colors (optional)

---

## 🛠️ Technologies Used

* **Python 3**
* **qrcode** library
* **Pillow (PIL)** for image processing

---

## 📦 Installation

### 1️⃣ Clone this repository

```bash
git clone https://github.com/YOUR-USERNAME/qr-code-generator.git
cd qr-code-generator
```

### 2️⃣ Install dependencies

```bash
pip install qrcode pillow
```

---

## ▶️ How to Use

### Basic QR Code Generation

```python
import qrcode

data = "https://example.com"

qr = qrcode.make(data)
qr.save("myqrcode.png")
```

### Advanced QR Code (With Custom Size & Color)

```python
import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data("Hello, this is my advanced QR code!")
qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, fill_color="black", back_color="white")
img.save("advanced_qrcode.png")
```

---

## 📁 Project Structure

```
📂 qr-code-generator
│── main.py
│── README.md
│── /output
│     └── generated_qr.png
```

---

## 🧪 Examples

| Input                       | Output                                |
| --------------------------- | ------------------------------------- |
| Link → `https://google.com` | Generates a QR code that opens Google |
| Text → `"Hello World!"`     | Generates a QR with the message       |
| Image path                  | Encodes file path as scannable data   |
| vCard                       | Scannable contact card                |

---

## 📝 Future Improvements

🔹 Add a GUI (Tkinter)
🔹 Add QR code scanner feature
🔹 Add color themes
🔹 Export as PDF
🔹 Integrate into a web app (Flask/Django)

---

## 🤝 Contributing

Contributions, issues, and suggestions are welcome!
Feel free to open a pull request.

---

## ⭐ Show Your Support

If you like this project, **leave a star ⭐ on GitHub**!

---

## 👨‍💻 Author

**Atharva Sharma**
Beginner Python Developer | Learning everyday 🚀
