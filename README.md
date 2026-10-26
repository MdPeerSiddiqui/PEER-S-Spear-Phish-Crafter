# PEER'S Spear Phish Crafter 🎯✉️

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Windows%20%7C%20macOS-0078D4?style=for-the-badge&logo=linux&logoColor=white)](https://kali.org)
[![Security](https://img.shields.io/badge/Security-Spear%20Phishing%20%26%20DMARC%20Defense-red?style=for-the-badge&logo=shield)](https://sqrock.com)
[![Tests](https://img.shields.io/badge/Tests-6%2F6%20Passing-brightgreen?style=for-the-badge&logo=checkmarx)](https://github.com/MdPeerSiddiqui/PEER-S-Spear-Phish-Crafter)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

> **Security-Awareness Training Email Generator & Forensic DMARC Defense Suite**  
> Developed by **Md Peer Siddiqui** for the **Sqrock IT Solution Cybersecurity Internship (Day 06: Spear Phishing Email Craft & Defense)**.

---

## 🎯 Executive Overview

Unlike untargeted mass spam, **Spear Phishing** leverages target-specific Open-Source Intelligence (OSINT) to craft deceptive communications with authentic organizational context. By embedding a victim's real name, role, department, reporting chain, and corporate infrastructure, adversaries bypass human vigilance.

**PEER'S Spear Phish Crafter** is an enterprise-grade Python CLI suite designed to:
1. Dynamically generate personalized phishing-awareness training drafts across 3 critical enterprise vectors.
2. Render both visual email body copy and raw **RFC 5322 MIME headers** to demonstrate spoofing mechanics.
3. Perform forensic red-flag analysis to educate employees on subtle domain mismatches and reply-to diversions.
4. Establish an authoritative **SPF (RFC 7208), DKIM (RFC 6376), and DMARC (RFC 7489) defense matrix** to immunize organizational domains against spoofing.

---

## 🚀 Key Features

* **🎭 3 Realistic Security-Awareness Attack Vectors:**
  * **[DRAFT-01] Corporate IT / SSO Certificate Renewal:** Simulates an Active Directory certificate migration warning threatening 24-hour account suspension.
  * **[DRAFT-02] People Operations / Payroll Review:** Simulates an urgent compensation harmonization update requiring bank routing re-verification.
  * **[DRAFT-03] Supply Chain / Overdue Vendor Invoice:** Simulates an overdue cloud infrastructure invoice with legal escalation threats.
* **✉️ Dual-Mode Email Renderer:** Displays clean visual email body text alongside raw RFC 5322 MIME headers (`From`, `Reply-To`, `Return-Path`, `Message-ID`, `X-Mailer`, `Authentication-Results`).
* **🔍 Forensic Red-Flag Analyzer:** Identifies display-name spoofing, envelope return-path diversion, urgency triggers, and lookalike domain syntax.
* **🛡️ SPF, DKIM & DMARC Defense Blueprint:** Provides exact DNS TXT records and a staged implementation roadmap (Monitoring ➔ Quarantine ➔ Strict Rejection `p=reject`).
* **📁 Standardized JSON Deliverable Export:** Automatically compiles the 3 awareness drafts and defender matrix into `templates/spear_phish_templates.json`.
* **📄 Executive PDF Lab Report Compiler:** Built-in ReportLab generator creating an authoritative 7-page technical report.
* **⚡ 100% Deterministic Unit Testing:** Includes 6 automated test cases verifying template rendering, MIME headers, and DMARC rules (**6/6 passed in 0.005s**).

---

## 📦 Installation & Setup

### For Kali Linux / Debian / Ubuntu:
```bash
# 1. Clone the repository
git clone https://github.com/MdPeerSiddiqui/PEER-S-Spear-Phish-Crafter.git
cd PEER-S-Spear-Phish-Crafter

# 2. Set up a Python virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the crafter
python3 spear_crafter.py
```

### For Windows (PowerShell):
```powershell
# 1. Clone the repository
git clone https://github.com/MdPeerSiddiqui/PEER-S-Spear-Phish-Crafter.git
cd PEER-S-Spear-Phish-Crafter

# 2. Set up virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the crafter
python spear_crafter.py
```

---

## 🎮 CLI Master Control Menu

```text
========================================================================
 ⚡ SECURITY-AWARENESS TRAINING EMAIL GENERATOR & DMARC DEFENSE SUITE ⚡
 Developed by: Md Peer Siddiqui | Sqrock IT Solution Internship (Day 06)
========================================================================

 Master Options:
  [1] Generate & Review All 3 Awareness Email Drafts
  [2] Inspect Specific Awareness Vector (Deep Body & Forensics)
  [3] Inspect Raw RFC 5322 MIME Email Headers
  [4] Run Email Header Spoofing & Red Flag Forensics
  [5] View SPF, DKIM & DMARC Defender Blueprint Guide
  [6] Export Deliverable JSON (spear_phish_templates.json)
  [7] Customize Target Profile Parameters (Name, Org, Domain)
  [8] Compile Executive Multi-Page PDF Lab Report (Day 06)
  [0] Exit Suite
```

---

## 🧪 Automated Testing

The suite includes 6 automated unit tests validating scenario schema completeness, dynamic token substitution, MIME header syntax, and DMARC policies.

Run tests via:
```bash
python -m unittest tests/test_spear_crafter.py -v
```

**Test Output:**
```
test_custom_target_profile_rendering (tests.test_spear_crafter.TestSpearPhishCrafter) ... ok
test_dmarc_defense_policy_records (tests.test_spear_crafter.TestSpearPhishCrafter) ... ok
test_export_deliverable_json (tests.test_spear_crafter.TestSpearPhishCrafter) ... ok
test_render_mime_headers (tests.test_spear_crafter.TestSpearPhishCrafter) ... ok
test_render_scenario_body_token_replacement (tests.test_spear_crafter.TestSpearPhishCrafter) ... ok
test_scenarios_data_count_and_keys (tests.test_spear_crafter.TestSpearPhishCrafter) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.005s

OK
```

---

## 📁 Repository Structure

```
PEER-S-Spear-Phish-Crafter/
├── spear_crafter.py          # Core interactive CLI email generator & analyzer
├── requirements.txt          # Python dependencies (colorama, reportlab)
├── README.md                 # Complete documentation & usage guide
├── LICENSE                   # MIT License
├── .gitignore                # Environment exclusions
├── templates/
│   └── spear_phish_templates.json  # Exported 3 drafts + DMARC guide deliverable
├── tests/
│   └── test_spear_crafter.py # Automated unit test suite
├── scripts/
│   └── generate_day06_pdf.py # Executive ReportLab PDF compiler
└── reports/
    └── Day06_Spear_Phishing_Report_Sqrock_MdPeerSiddiqui.pdf
```

---

## 🛡️ Ethical Compliance & Disclaimer

> **NOTICE:** This tool and its simulation models are developed strictly for **authorized educational, awareness training, and academic research purposes** under the **Sqrock IT Solution Cybersecurity Internship Program**.  
> The scripts and simulated emails are designed solely for defensive awareness to train employees to recognize social engineering tactics. Unauthorized transmission of spear-phishing emails, header forgery against unowned domains, or credential harvesting is illegal under the **Information Technology Act 2000 (India)** and the **Computer Fraud and Abuse Act (CFAA)**.

---

## 👤 Author

* **Md Peer Siddiqui**
* **Cybersecurity Intern at Sqrock IT Solution**
* **GitHub:** [@MdPeerSiddiqui](https://github.com/MdPeerSiddiqui)
* **LinkedIn:** [Md Peer Siddiqui](https://linkedin.com)
