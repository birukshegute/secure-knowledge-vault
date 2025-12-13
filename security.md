# Security Policy

## 1. Overview
This project is a Django-based web application deployed on AWS infrastructure.
It handles authenticated user data and user-generated content and is designed
with a security-first mindset appropriate for cloud-hosted applications.

Primary security goals:
- Protect confidentiality of user data
- Preserve data integrity
- Prevent unauthorized access
- Minimize cloud misconfiguration risk

---

## 2. Threat Model (High-Level)

The following threats are considered in scope:

- Unauthorized access to user accounts
- Broken authentication or session management
- Injection attacks (SQL injection, XSS)
- Cross-Site Request Forgery (CSRF)
- File upload abuse and malicious payloads
- Privilege escalation within the application
- AWS IAM misconfiguration
- Excessive network exposure (open ports, weak security groups)
- Data exposure through logs or backups

Out-of-scope:
- Physical access attacks
- Zero-day vulnerabilities in underlying cloud provider infrastructure

---

## 3. Security Controls (Planned / Implemented)

### Application-Level
- Django built-in authentication and authorization
- Secure password hashing (Django defaults)
- CSRF protection enabled
- Input validation and output escaping
- Encrypted sensitive data at rest
- Secure session cookies

### Infrastructure-Level (AWS)
- Least-privilege IAM roles
- Security groups restricting inbound/outbound traffic
- No hardcoded secrets in source code
- Environment variables used for secrets
- Public access limited to required services only

---

## 4. Data Protection
- User credentials are never stored in plaintext
- Sensitive fields are encrypted at rest
- HTTPS is enforced for data in transit (where applicable)
- Logs are reviewed to prevent sensitive data leakage

---

## 5. Security Testing
Security testing will be performed throughout development and deployment.

Planned activities include:
- Manual vulnerability testing (authentication, input handling)
- Network scanning of cloud resources
- Validation of IAM permissions and security group rules
- Review and remediation of identified issues

Findings and mitigations will be documented as the project evolves.

---

## 6. Known Limitations
- No multi-factor authentication (MFA) in initial release
- Single-instance deployment (no high availability)
- No managed WAF or DDoS protection enabled
- Rate limiting may be limited in early versions

These limitations are acknowledged and documented intentionally.

---

## 7. Responsible Use
This project is intended for educational and demonstration purposes.
All security testing is performed only against infrastructure owned
or explicitly controlled by the author.

Unauthorized testing of third-party systems is strictly prohibited.
