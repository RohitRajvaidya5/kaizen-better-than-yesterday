# Authentication & Authorization
---

## Fundamentals

- [ ] 🔷 What is Authentication?
- [ ] 🔷 What is Authorization?
- [ ] 🔷 Authentication vs Authorization
- [ ] 🔷 Identity
- [ ] 🔷 User Credentials
- [ ] 🔷 Authentication Factors
- [ ] 🔷 Principle of Least Privilege
- [ ] 🔷 Security Terminology
- [ ] 🟣 Identity Federation

---

## Password Authentication

- [ ] 🔷 Username & Password
- [ ] 🔷 Password Policies
- [ ] 🔷 Strong Passwords
- [ ] 🔷 Password Hashing
- [ ] 🔷 Password Salting
- [ ] 🔷 Password Verification
- [ ] 🔷 Password Reset
- [ ] 🔷 Forgot Password Flow
- [ ] 🔷 Change Password
- [ ] 🟣 Passwordless Authentication

---

## Password Hashing

- [ ] 🔷 bcrypt
- [ ] 🔷 Argon2
- [ ] 🔷 PBKDF2
- [ ] 🔷 Hash vs Encryption
- [ ] 🔷 Salt
- [ ] 🔷 Pepper
- [ ] 🔷 Hash Verification
- [ ] 🟣 Key Stretching

---

## Sessions

- [ ] 🔷 Session Authentication
- [ ] 🔷 Session ID
- [ ] 🔷 Session Cookies
- [ ] 🔷 Session Storage
- [ ] 🔷 Session Expiration
- [ ] 🔷 Logout
- [ ] 🔷 Session Invalidation
- [ ] 🟣 Distributed Sessions

---

## Cookies

- [ ] 🔷 Cookies
- [ ] 🔷 HttpOnly Cookie
- [ ] 🔷 Secure Cookie
- [ ] 🔷 SameSite Cookie
- [ ] 🔷 Cookie Expiration
- [ ] 🔷 Cookie Security
- [ ] 🟣 Signed Cookies

---

## Token Authentication

- [ ] 🔷 Bearer Token
- [ ] 🔷 Token Authentication
- [ ] 🔷 Access Token
- [ ] 🔷 Refresh Token
- [ ] 🔷 Token Expiration
- [ ] 🔷 Token Revocation
- [ ] 🔷 Stateless Authentication
- [ ] 🟣 Token Introspection

---

## JWT (JSON Web Token)

- [ ] 🔷 JWT Structure
- [ ] 🔷 Header
- [ ] 🔷 Payload
- [ ] 🔷 Signature
- [ ] 🔷 JWT Claims
- [ ] 🔷 Standard Claims
- [ ] 🔷 Custom Claims
- [ ] 🔷 JWT Signing
- [ ] 🔷 JWT Verification
- [ ] 🔷 JWT Expiration
- [ ] 🔷 Refresh Tokens
- [ ] 🟣 JWT Blacklisting

---

## OAuth 2.0

- [ ] 🔷 What is OAuth2?
- [ ] 🔷 Resource Owner
- [ ] 🔷 Client
- [ ] 🔷 Authorization Server
- [ ] 🔷 Resource Server
- [ ] 🔷 Authorization Code Flow
- [ ] 🔷 Client Credentials Flow
- [ ] 🔷 Password Grant
- [ ] 🔷 Refresh Token Flow
- [ ] 🟣 Device Authorization Flow

---

## OpenID Connect (OIDC)

- [ ] 🟣 What is OpenID Connect?
- [ ] 🟣 ID Token
- [ ] 🟣 UserInfo Endpoint
- [ ] 🟣 Discovery Endpoint
- [ ] 🟣 OIDC Authentication Flow

---

## API Keys

- [ ] 🔷 API Keys
- [ ] 🔷 API Key Authentication
- [ ] 🔷 API Key Rotation
- [ ] 🔷 API Key Expiration
- [ ] 🟣 Scoped API Keys

---

## Multi-Factor Authentication (MFA)

- [ ] 🔷 Two-Factor Authentication (2FA)
- [ ] 🔷 One-Time Password (OTP)
- [ ] 🔷 Time-based OTP (TOTP)
- [ ] 🔷 Backup Codes
- [ ] 🟣 Hardware Security Keys (FIDO2)

---

## Authorization Models

- [ ] 🔷 Role-Based Access Control (RBAC)
- [ ] 🔷 Roles
- [ ] 🔷 Permissions
- [ ] 🔷 User Roles
- [ ] 🔷 Permission Checks
- [ ] 🟣 Attribute-Based Access Control (ABAC)
- [ ] 🟣 Policy-Based Access Control (PBAC)

---

## Access Control

- [ ] 🔷 Protected Routes
- [ ] 🔷 Public Routes
- [ ] 🔷 Private Routes
- [ ] 🔷 Resource Ownership
- [ ] 🔷 Permission Validation
- [ ] 🔷 Admin Access
- [ ] 🟣 Fine-Grained Permissions

---

## Authentication in FastAPI

- [ ] 🔷 Depends()
- [ ] 🔷 OAuth2PasswordBearer
- [ ] 🔷 OAuth2PasswordRequestForm
- [ ] 🔷 JWT Authentication
- [ ] 🔷 Password Hashing
- [ ] 🔷 Current User
- [ ] 🔷 Protected Endpoints
- [ ] 🔷 Role-Based Authorization
- [ ] 🟣 Custom Authentication Backends

---

## Authentication in Django

- [ ] 🔷 Django Authentication
- [ ] 🔷 User Model
- [ ] 🔷 Custom User Model
- [ ] 🔷 Authentication Backend
- [ ] 🔷 Login
- [ ] 🔷 Logout
- [ ] 🔷 Django Permissions
- [ ] 🔷 Django Groups
- [ ] 🟣 Custom Authentication Backends

---

## Authentication in DRF

- [ ] 🔷 SessionAuthentication
- [ ] 🔷 BasicAuthentication
- [ ] 🔷 TokenAuthentication
- [ ] 🔷 JWT Authentication
- [ ] 🔷 Custom Authentication
- [ ] 🔷 Current User
- [ ] 🔷 Login API
- [ ] 🔷 Logout API
- [ ] 🟣 OAuth2 Integration

---

## Social Authentication

- [ ] 🟣 Google Login
- [ ] 🟣 GitHub Login
- [ ] 🟣 Microsoft Login
- [ ] 🟣 Facebook Login
- [ ] 🟣 Apple Login

---

## Security Best Practices

- [ ] 🔷 HTTPS
- [ ] 🔷 Secure Password Storage
- [ ] 🔷 Input Validation
- [ ] 🔷 SQL Injection Prevention
- [ ] 🔷 XSS Prevention
- [ ] 🔷 CSRF Protection
- [ ] 🔷 CORS
- [ ] 🔷 Rate Limiting
- [ ] 🔷 Account Lockout
- [ ] 🔷 Login Attempt Limiting
- [ ] 🔷 Secret Management
- [ ] 🔷 Environment Variables
- [ ] 🟣 Certificate Pinning

---

## Session & Token Security

- [ ] 🔷 Token Expiration
- [ ] 🔷 Refresh Token Rotation
- [ ] 🔷 Logout Everywhere
- [ ] 🔷 Session Timeout
- [ ] 🔷 Secure Cookie Flags
- [ ] 🔷 Revoke Tokens
- [ ] 🟣 Sliding Sessions

---

## Secrets Management

- [ ] 🔷 Secret Keys
- [ ] 🔷 Environment Variables
- [ ] 🔷 .env Files
- [ ] 🔷 Secret Rotation
- [ ] 🔷 Keep Secrets Out of Git
- [ ] 🟣 Secret Managers (Vault, AWS Secrets Manager)

---

## Common Authentication Flows

- [ ] 🔷 User Registration
- [ ] 🔷 User Login
- [ ] 🔷 Email Verification
- [ ] 🔷 Forgot Password
- [ ] 🔷 Reset Password
- [ ] 🔷 Change Password
- [ ] 🔷 Logout
- [ ] 🔷 Refresh Access Token
- [ ] 🟣 Passwordless Login

---

## Authentication Testing

- [ ] 🔷 Login Testing
- [ ] 🔷 Registration Testing
- [ ] 🔷 JWT Testing
- [ ] 🔷 Permission Testing
- [ ] 🔷 Role Testing
- [ ] 🔷 Expired Token Testing
- [ ] 🔷 Refresh Token Testing
- [ ] 🟣 Security Penetration Testing

---

## Authentication Best Practices

- [ ] 🔷 Hash Passwords
- [ ] 🔷 Never Store Plain Text Passwords
- [ ] 🔷 Use HTTPS
- [ ] 🔷 Use Short-Lived Access Tokens
- [ ] 🔷 Rotate Refresh Tokens
- [ ] 🔷 Validate Every Request
- [ ] 🔷 Use RBAC
- [ ] 🔷 Log Authentication Events
- [ ] 🔷 Protect Secrets
- [ ] 🔷 Secure Cookies
- [ ] 🔷 Principle of Least Privilege
- [ ] 🟣 Zero Trust Security

---

## Authentication & Authorization Interview Questions

- [ ] 🔷 Authentication vs Authorization
- [ ] 🔷 Session vs JWT
- [ ] 🔷 JWT vs OAuth2
- [ ] 🔷 Access Token vs Refresh Token
- [ ] 🔷 JWT Structure
- [ ] 🔷 JWT Claims
- [ ] 🔷 Password Hashing vs Encryption
- [ ] 🔷 bcrypt vs Argon2
- [ ] 🔷 RBAC vs ABAC
- [ ] 🔷 OAuth2 Flows
- [ ] 🔷 CSRF vs CORS
- [ ] 🔷 Cookie vs Local Storage
- [ ] 🔷 HttpOnly Cookie
- [ ] 🔷 Secure Cookie
- [ ] 🔷 SameSite Cookie
- [ ] 🔷 Token Expiration
- [ ] 🔷 Refresh Token Rotation
- [ ] 🔷 API Keys
- [ ] 🔷 Principle of Least Privilege
- [ ] 🟣 OpenID Connect
- [ ] 🟣 Zero Trust Architecture
