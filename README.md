# IronVault v3.0 🔐

**IronVault** is a lightweight, logic-driven encryption suite designed for secure data management on resource-constrained hardware. Developed and optimized on a **ThinkPad R400** running **Void Linux**, it serves as the primary security layer for sensitive research data related to my **MEXT 2027 scholarship** application.

---

## 🚀 The Motivation
Standard encryption tools often come with heavy dependencies or environment conflicts on legacy systems. After experiencing build issues on Windows 7, I migrated my development workflow to **Void Linux**. IronVault was built to be:
* **Environment Agnostic:** Runs seamlessly on minimal Linux distributions.
* **Hardware-Linked:** Features logic optimized for the specific architecture of the ThinkPad R Series.
* **Dependency-Lite:** Written in Python with a focus on core security logic to avoid bloat.

---

## 🛠️ Key Features
* **Vault File Creation:** Securely package sensitive directories into a single `.bin` database.
* **HWID Verification:** Integrated logic to recognize hardware identity, ensuring data remains secure even if the storage medium is moved.
* **Logic-Driven Encryption:** Prioritizes custom security logic flows over generic third-party wrappers.
* **Void Linux and Windows 7 Optimized:** Fully compatible with `runit` and rolling-release environments.

---

## 💻 Tech Stack
* **Language:** Python 3.8.10 (Last Windows7 release, would work in morden environment)
* **Environment:** Void Linux (ThinkPad R400)
* **Logic Focus:** Security architecture and hardware-locked features

---

## 📥 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone (https://github.com/thedarkxh/darkest-data-encoder.git)
   '''bash
2. **Open the folder**
3. **Run main.py**
4. **Select Options:**

    1. **Vault File:** Encrypt and package data.

    2. **Extract File:** Decrypt and retrieve data.


***Note: Keep your key at safe place if you don't plan to loose your file.***
**This project is only for fun**
