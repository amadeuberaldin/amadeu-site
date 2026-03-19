# 🌐 Amadeu Beraldin — Personal Technical Website

This repository contains the source code for my personal website:

👉 https://amadeuberaldin.com.br

---

## 📌 About the Project

This site is not a traditional portfolio.

It is designed as a **public technical notebook**, where I document:

- ideas
- experiments
- infrastructure setups
- real systems I build and operate

The goal is to make the **process visible**, not just the final result.

---

## 🧱 Architecture

The website is deployed using a self-hosted infrastructure:

- VPS with public IP
- WireGuard VPN (for secure internal access)
- Caddy (automatic HTTPS with Let's Encrypt)
- Static frontend (HTML, CSS, JS)

---

## 🔐 Security Model

- SSH доступ restricted to VPN only
- Public exposure limited to HTTP/HTTPS
- Firewall rules hardened (iptables)
- No sensitive data stored in repository

---

## 🚀 Deployment

The site is deployed manually using a simple script:

```bash
./scripts/deploy.sh

This sends the frontend files to the server using scp.

---

📂 Repository Structure

frontend/ — static website files

scripts/ — deployment script

docs/ — (future) documentation

---

🧠 Philosophy

Learning technology means building real systems.

This project is part of a broader effort to:

understand infrastructure deeply

build reproducible systems

document everything

---

🔗 Related Projects

Homelab: https://github.com/amadeuberaldin/homelab

VPN Infrastructure: https://github.com/amadeuberaldin/wireguard-vpn-infrastructure

Server Automation: https://github.com/amadeuberaldin/server-automation

AI Agent Infrastructure: https://github.com/amadeuberaldin/ai-agent-infrastructure

---

⚠️ Notes

This repository does not contain:

private keys

real server credentials

sensitive configuration data


---
