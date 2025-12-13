# Secure Knowledge Vault

A cloud-hosted Django web application designed to demonstrate secure backend
development, AWS infrastructure usage, and practical cybersecurity principles.

This project focuses on building, deploying, attacking, and hardening a real
application using modern cloud and security best practices.

---

## Project Goals
- Build a secure, production-style Django backend
- Deploy and manage cloud infrastructure on AWS
- Apply security controls at the application and infrastructure levels
- Perform controlled offensive security testing
- Patch and harden the system based on findings
- Document the full security lifecycle

---

## Technology Stack

### Backend
- Python
- Django
- Django ORM
- Gunicorn

### Frontend
- Server-rendered Django templates
- Minimal JavaScript
- Utility-first CSS (e.g. Tailwind)

### Cloud & Infrastructure
- AWS EC2
- AWS S3
- AWS IAM
- AWS CloudWatch
- AWS Lambda (asynchronous processing)
- Terraform (Infrastructure as Code)

### Security
- Django authentication & authorization
- Encrypted data at rest
- Least-privilege IAM
- Network isolation using security groups
- Manual security testing and remediation

---

## High-Level Architecture

User (Browser)
      |
      |  HTTPS
      v
  Nginx (EC2)
      |
      v
 Gunicorn (WSGI)
      |
      v
 Django Application
      |
      +--> Database (SQLite initially / PostgreSQL later)
      |
      +--> Amazon S3 (File Storage)
               |
               v
         AWS Lambda (Background Processing)

---

## Key Features (v1 Scope)
- User authentication and authorization
- Secure note creation, editing, and deletion
- Encrypted storage of sensitive content
- File upload and background processing
- Logging and monitoring
- Infrastructure provisioned via Terraform

> Feature scope is intentionally limited to ensure completion and security focus.

---

## Security Approach
Security is treated as a first-class concern throughout the project lifecycle.

- Threat modeling performed during design
- Secure defaults enforced at the framework level
- Cloud resources configured with least privilege
- Vulnerabilities intentionally tested and documented
- Fixes applied and verified

See [`SECURITY.md`](SECURITY.md) for full details.

---

## Project Status
This project is under active development.

Milestones include:
- Local development
- Cloud deployment
- Security testing
- Hardening and documentation

---

## Disclaimer
This project is for educational and demonstration purposes only.
All security testing is performed against infrastructure owned and controlled
by the author.

---

## Author
Biruk Shegute Sufa
