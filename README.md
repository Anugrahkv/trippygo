# TrippyGo – Secure Full-Stack Web Application

## 📌 Objective
TrippyGo is a custom travel management web application built from the ground up to demonstrate secure development lifecycles and full-stack architecture. Developed utilizing Python and the Django framework, this project prioritizes modern data protection standards, input sanitization, and the active mitigation of critical web vulnerabilities.

## 🛠️ Technology Stack
* **Backend:** Python, Django Framework
* **Database:** SQLite (integrated via Django ORM)
* **Frontend:** HTML, CSS
* **Security Focus:** OWASP Top 10 Mitigation, Secure Authentication Workflows

## 🔒 Security Implementations & Architecture
Since this application processes user data, defense-in-depth principles were integrated directly into the MVC (Model-View-Controller) architecture:

* **Injection Prevention:** Utilized Django's built-in Object-Relational Mapping (ORM) and strict form field validation to systematically eliminate SQL Injection (SQLi) vulnerabilities.
* **XSS Mitigation:** Enforced context-aware output encoding and input sanitization to prevent Cross-Site Scripting (XSS) attacks.
* **Identity & Access Management:** Implemented robust user authentication workflows, utilizing cryptographic session management and secure password hashing algorithms (PBKDF2).
* **CSRF Protection:** Integrated Cross-Site Request Forgery (CSRF) tokens across all state-changing forms to ensure request origin integrity.

## 💻 Core Application Features
* Secure user registration, login, and session state management.
* Dynamic backend database handling for reliable travel data storage.
* Scalable application framework designed and validated within a simulated production environment.

## 🚀 Local Deployment Instructions
To run this application locally for testing and code review:

**1. Clone the repository:**
```bash
git clone [https://github.com/Anugrahkv/TrippyGo.git](https://github.com/Anugrahkv/TrippyGo.git)
cd TrippyGo
