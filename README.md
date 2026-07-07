# Automated Threat Intelligence Log Parser

A high-performance, fault-tolerant Python security automation script that ingests raw server logs, extracts network indicators using pattern-matching, and queries live global threat intelligence databases to identify and isolate malicious actors in real-time.

---

## 🚀 Core Features & Architecture

The script operates as a secure, three-phase data pipeline designed for production SecOps environments:

* **High-Speed Log Parsing:** Utilizes optimized Regular Expressions (`re`) with precise word boundaries (`\b`) to scrape raw, messy server access logs and cleanly isolate IPv4 patterns.
* **API Budget Optimization:** Implements rapid type-casting deduplication (`list(set())`) to ensure individual host addresses are queried exactly once, conserving daily API allocations.
* **Defensive Schema Auditing:** Rejects insecure, silent data recovery fallbacks. Features an active blueprint validation layer to catch API structural layout modifications or schema drift, preventing threat-detection blindness.
* **Decoupled Security Architecture:** Zero hardcoded credentials. Adheres to modern application security compliance standards by pulling sensitive API keys directly out of the operating system's environment memory layer.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.x installed on your machine along with the standard package manager `pip`.

### 2. Clone and Install Dependencies
Navigate to your project directory and install the necessary HTTP communications suite:
```bash
pip install requests
