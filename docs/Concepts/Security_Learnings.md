# Security
---

## Security Fundamentals

- [ ] 🔷 What is Application Security?
- [ ] 🔷 CIA Triad (Confidentiality, Integrity, Availability)
- [ ] 🔷 Authentication vs Authorization
- [ ] 🔷 Principle of Least Privilege
- [ ] 🔷 Defense in Depth
- [ ] 🔷 Zero Trust Basics
- [ ] 🔷 Threat Modeling
- [ ] 🔷 Security by Design
- [ ] 🟣 STRIDE Model

---

## OWASP Top 10

- [ ] 🔷 Broken Access Control
- [ ] 🔷 Cryptographic Failures
- [ ] 🔷 Injection
- [ ] 🔷 Insecure Design
- [ ] 🔷 Security Misconfiguration
- [ ] 🔷 Vulnerable Components
- [ ] 🔷 Authentication Failures
- [ ] 🔷 Software & Data Integrity Failures
- [ ] 🔷 Logging & Monitoring Failures
- [ ] 🔷 Server-Side Request Forgery (SSRF)

---

## Authentication

- [ ] 🔷 Password Authentication
- [ ] 🔷 Password Hashing
- [ ] 🔷 bcrypt
- [ ] 🔷 Argon2
- [ ] 🔷 JWT
- [ ] 🔷 OAuth2
- [ ] 🔷 Session Authentication
- [ ] 🔷 Multi-Factor Authentication (MFA)
- [ ] 🔷 API Keys
- [ ] 🟣 OpenID Connect (OIDC)

---

## Authorization

- [ ] 🔷 Role-Based Access Control (RBAC)
- [ ] 🔷 Permission-Based Access
- [ ] 🔷 Resource Ownership
- [ ] 🔷 Route Protection
- [ ] 🔷 Object-Level Authorization
- [ ] 🟣 Attribute-Based Access Control (ABAC)

---

## Password Security

- [ ] 🔷 Password Policies
- [ ] 🔷 Password Hashing
- [ ] 🔷 Password Salting
- [ ] 🔷 Password Reset Flow
- [ ] 🔷 Password Expiration
- [ ] 🔷 Account Lockout
- [ ] 🔷 Brute Force Protection
- [ ] 🟣 Passwordless Authentication

---

## Cryptography

- [ ] 🔷 Hashing
- [ ] 🔷 Encryption
- [ ] 🔷 Symmetric Encryption
- [ ] 🔷 Asymmetric Encryption
- [ ] 🔷 AES
- [ ] 🔷 RSA
- [ ] 🔷 SHA-256
- [ ] 🔷 Digital Signatures
- [ ] 🔷 Certificates
- [ ] 🟣 Elliptic Curve Cryptography (ECC)

---

## HTTPS & TLS

- [ ] 🔷 HTTP vs HTTPS
- [ ] 🔷 SSL vs TLS
- [ ] 🔷 TLS Handshake
- [ ] 🔷 Certificates
- [ ] 🔷 Certificate Authorities (CA)
- [ ] 🔷 HSTS
- [ ] 🔷 Secure Communication
- [ ] 🟣 Mutual TLS (mTLS)

---

## Common Web Vulnerabilities

- [ ] 🔷 SQL Injection (SQLi)
- [ ] 🔷 Cross Site Scripting (XSS)
- [ ] 🔷 Cross Site Request Forgery (CSRF)
- [ ] 🔷 Clickjacking
- [ ] 🔷 Command Injection
- [ ] 🔷 Path Traversal
- [ ] 🔷 File Inclusion
- [ ] 🔷 XML External Entity (XXE)
- [ ] 🔷 Insecure Deserialization
- [ ] 🔷 Server-Side Request Forgery (SSRF)
- [ ] 🟣 HTTP Request Smuggling

---

## Input Validation

- [ ] 🔷 Input Validation
- [ ] 🔷 Output Encoding
- [ ] 🔷 Data Sanitization
- [ ] 🔷 Whitelisting
- [ ] 🔷 Blacklisting
- [ ] 🔷 File Validation
- [ ] 🔷 Request Validation
- [ ] 🟣 Content Security Policy (CSP)

---

## Secure Headers

- [ ] 🔷 Content-Security-Policy
- [ ] 🔷 X-Frame-Options
- [ ] 🔷 X-Content-Type-Options
- [ ] 🔷 Referrer-Policy
- [ ] 🔷 Permissions-Policy
- [ ] 🔷 Strict-Transport-Security
- [ ] 🟣 Cross-Origin-Embedder-Policy

---

## Cookies & Sessions

- [ ] 🔷 Cookies
- [ ] 🔷 HttpOnly
- [ ] 🔷 Secure Cookies
- [ ] 🔷 SameSite
- [ ] 🔷 Session Management
- [ ] 🔷 Session Timeout
- [ ] 🔷 Session Fixation
- [ ] 🟣 Distributed Sessions

---

## API Security

- [ ] 🔷 HTTPS
- [ ] 🔷 JWT Authentication
- [ ] 🔷 OAuth2
- [ ] 🔷 API Keys
- [ ] 🔷 Rate Limiting
- [ ] 🔷 Input Validation
- [ ] 🔷 Request Signing
- [ ] 🔷 API Versioning
- [ ] 🟣 API Gateway Security

---

## CORS & CSRF

- [ ] 🔷 Same Origin Policy
- [ ] 🔷 Cross-Origin Resource Sharing (CORS)
- [ ] 🔷 CORS Headers
- [ ] 🔷 Preflight Requests
- [ ] 🔷 CSRF
- [ ] 🔷 CSRF Tokens
- [ ] 🔷 CSRF Protection
- [ ] 🟣 Cross-Origin Isolation

---

## Rate Limiting

- [ ] 🔷 Rate Limiting
- [ ] 🔷 Fixed Window
- [ ] 🔷 Sliding Window
- [ ] 🔷 Token Bucket
- [ ] 🔷 Leaky Bucket
- [ ] 🔷 Redis Rate Limiting
- [ ] 🟣 Distributed Rate Limiting

---

## File Upload Security

- [ ] 🔷 File Type Validation
- [ ] 🔷 File Size Limits
- [ ] 🔷 MIME Type Validation
- [ ] 🔷 File Scanning
- [ ] 🔷 Secure Storage
- [ ] 🔷 Random File Names
- [ ] 🟣 Virus Scanning

---

## Secrets Management

- [ ] 🔷 Environment Variables
- [ ] 🔷 .env Files
- [ ] 🔷 Secret Rotation
- [ ] 🔷 API Secrets
- [ ] 🔷 Database Credentials
- [ ] 🔷 Git Secrets
- [ ] 🟣 HashiCorp Vault

---

## Logging & Auditing

- [ ] 🔷 Security Logging
- [ ] 🔷 Audit Logs
- [ ] 🔷 Login Tracking
- [ ] 🔷 Failed Login Attempts
- [ ] 🔷 Sensitive Data Masking
- [ ] 🔷 Monitoring
- [ ] 🟣 SIEM Integration

---

## Docker Security

- [ ] 🔷 Non-Root Containers
- [ ] 🔷 Official Images
- [ ] 🔷 Docker Secrets
- [ ] 🔷 Image Scanning
- [ ] 🔷 Read-Only File System
- [ ] 🔷 Least Privilege Containers
- [ ] 🟣 Seccomp Profiles

---

## Linux Security

- [ ] 🔷 File Permissions
- [ ] 🔷 chmod
- [ ] 🔷 chown
- [ ] 🔷 sudo
- [ ] 🔷 SSH Keys
- [ ] 🔷 Firewall (ufw)
- [ ] 🔷 Fail2Ban
- [ ] 🟣 SELinux

---

## Database Security

- [ ] 🔷 SQL Injection Prevention
- [ ] 🔷 Parameterized Queries
- [ ] 🔷 Least Privilege Database Users
- [ ] 🔷 Database Encryption
- [ ] 🔷 Backup Encryption
- [ ] 🔷 Audit Logs
- [ ] 🟣 Row-Level Security

---

## Security in Django

- [ ] 🔷 CSRF Protection
- [ ] 🔷 XSS Protection
- [ ] 🔷 ORM SQL Injection Protection
- [ ] 🔷 Authentication System
- [ ] 🔷 Permissions
- [ ] 🔷 Security Middleware
- [ ] 🔷 Secret Key Management
- [ ] 🟣 Custom Security Middleware

---

## Security in FastAPI

- [ ] 🔷 OAuth2
- [ ] 🔷 JWT Authentication
- [ ] 🔷 Password Hashing
- [ ] 🔷 Dependency-Based Authorization
- [ ] 🔷 CORS Middleware
- [ ] 🔷 Input Validation
- [ ] 🔷 Pydantic Validation
- [ ] 🟣 API Gateway Integration

---

## Dependency Security

- [ ] 🔷 pip-audit
- [ ] 🔷 Safety
- [ ] 🔷 Dependabot
- [ ] 🔷 Vulnerability Scanning
- [ ] 🔷 Package Updates
- [ ] 🟣 Software Bill of Materials (SBOM)

---

## Security Testing

- [ ] 🔷 Authentication Testing
- [ ] 🔷 Authorization Testing
- [ ] 🔷 SQL Injection Testing
- [ ] 🔷 XSS Testing
- [ ] 🔷 CSRF Testing
- [ ] 🔷 API Security Testing
- [ ] 🔷 Dependency Scanning
- [ ] 🟣 Penetration Testing

---

## Security Best Practices

- [ ] 🔷 Use HTTPS Everywhere
- [ ] 🔷 Hash Passwords
- [ ] 🔷 Validate Input
- [ ] 🔷 Escape Output
- [ ] 🔷 Principle of Least Privilege
- [ ] 🔷 Secure Secrets
- [ ] 🔷 Rotate Credentials
- [ ] 🔷 Keep Dependencies Updated
- [ ] 🔷 Log Security Events
- [ ] 🔷 Monitor Failed Logins
- [ ] 🔷 Use Parameterized Queries
- [ ] 🔷 Regular Security Audits
- [ ] 🟣 Zero Trust Architecture

---

## Security Interview Questions

- [ ] 🔷 Authentication vs Authorization
- [ ] 🔷 JWT vs Session Authentication
- [ ] 🔷 OAuth2 vs JWT
- [ ] 🔷 Hashing vs Encryption
- [ ] 🔷 bcrypt vs Argon2
- [ ] 🔷 SQL Injection Prevention
- [ ] 🔷 XSS vs CSRF
- [ ] 🔷 CORS
- [ ] 🔷 SameSite Cookies
- [ ] 🔷 HttpOnly Cookies
- [ ] 🔷 HTTPS vs HTTP
- [ ] 🔷 SSL vs TLS
- [ ] 🔷 RBAC
- [ ] 🔷 Rate Limiting
- [ ] 🔷 API Security
- [ ] 🔷 OWASP Top 10
- [ ] 🔷 Secure Headers
- [ ] 🔷 Secrets Management
- [ ] 🟣 Zero Trust
- [ ] 🟣 mTLS
- [ ] 🟣 Threat Modeling
- [ ] 🟣 SSRF Protection
