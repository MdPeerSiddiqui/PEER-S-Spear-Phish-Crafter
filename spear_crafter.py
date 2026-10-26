#!/usr/bin/env python3
"""
PEER'S SPEAR PHISH CRAFTER v1.0
Security-Awareness Training Email Generator & Forensic Analysis Engine
Author: Md Peer Siddiqui
Internship Track: Social Engineering Attack Simulations Using Python (Day 06)
Host Organization: Sqrock IT Solution
"""

import os
import sys
import json
import datetime
import uuid

try:
    import colorama
    from colorama import Fore, Style
    colorama.init(autoreset=True)
except ImportError:
    class DummyColor:
        def __getattr__(self, name):
            return ""
    Fore = DummyColor()
    Style = DummyColor()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
DEFAULT_OUTPUT_JSON = os.path.join(TEMPLATES_DIR, "spear_phish_templates.json")

# Default Target Profile (can be customized dynamically via menu)
DEFAULT_TARGET = {
    "name": "Harish Kumar",
    "email": "harish.k@sqrock.com",
    "company": "Sqrock IT Solution",
    "domain": "sqrock.com",
    "department": "Cloud Infrastructure & Security",
    "location": "Bangalore, India",
    "manager_name": "Rajesh Mehta",
    "role": "Senior Cloud Security Engineer",
    "deadline_hours": 24
}

# The 3 Core Awareness Scenarios
SCENARIOS_DATA = [
    {
        "id": "DRAFT-01",
        "title": "Corporate IT: Mandatory SSO Certificate Renewal & Access Hold",
        "category": "Enterprise IT Helpdesk / Identity Access Management",
        "sender_display": "Sqrock Global IT Support Desk",
        "spoofed_from": "it-support@{domain_spoofed}",
        "reply_to": "admin-verification@external-gateway-sync.net",
        "return_path": "bounce-handler@relay-mailer44.org",
        "subject": "ACTION REQUIRED: Security Certificate Expiration for {name} ({company})",
        "urgency_tier": "HIGH (24-Hour Account Lockout Threat)",
        "psychological_triggers": ["Corporate Authority", "Urgency / Fear of Disruption", "Compliance"],
        "body_template": """Dear {name},

Our centralized Active Directory and Okta Single Sign-On (SSO) gateway migration has flagged your endpoint profile as pending mandatory certificate synchronization.

Due to corporate compliance policy, failure to bind your hardware multi-factor authenticator within {deadline_hours} hours will result in automated suspension of your {company} VPN, Slack, and internal Git repository access.

[MANDATORY ACTION REQUIRED]:
Please navigate to the internal gateway portal below and authenticate your active session token:

👉 https://login.{domain_spoofed}/sso/auth/verify-token?id=99281-sqr

Once synchronized, your endpoint access credentials will be renewed for the next 180 days.

Regards,
Central IT Security Operations
{company} — Infrastructure & Identity Management
Internal Support Extension: #4401""",
        "red_flags": [
            "Display Name Spoofing: 'Sqrock Global IT Support Desk' masks external spoofed domain.",
            "Reply-To Mismatch: Inbound mail directs replies to 'admin-verification@external-gateway-sync.net'.",
            "Urgency / Coercion: Threatens immediate suspension of core tools (VPN, Git, Slack) within 24 hours.",
            "Deceptive Link Target: Link subdomain imitates internal portal ('login.{domain_spoofed}')."
        ]
    },
    {
        "id": "DRAFT-02",
        "title": "People Operations: Annual Compensation & Direct Deposit Review",
        "category": "Corporate HR & Payroll",
        "sender_display": "People Operations & Payroll Management",
        "spoofed_from": "payroll-review@{domain_spoofed}",
        "reply_to": "hr-dispatch@talent-benefits-secure.io",
        "return_path": "notifications@hr-payroll-system.org",
        "subject": "CONFIDENTIAL: Updated Q4 Compensation Review & Direct Deposit Routing for {name}",
        "urgency_tier": "HIGH (Payroll Processing Cutoff)",
        "psychological_triggers": ["Financial Incentive / Ambition", "Authority", "Urgency"],
        "body_template": """Hi {name},

As part of {company}'s Q4 compensation harmonization across the {department} division, your updated executive compensation structure and revised tax bracket deductions have been finalized.

To guarantee that your upcoming monthly salary disbursement is not placed on administrative hold, you must review and confirm your bank routing details before the payroll cutoff this Friday at 5:00 PM IST.

[CONFIDENTIAL DOCUMENT ACCESS]:
Your personalized breakdown has been uploaded to the encrypted HR portal:

👉 https://payroll.{domain_spoofed}/confidential/compensation-statement?emp=HK-9921

Please do not forward this communication. All salary adjustments are strictly confidential under {company} employee agreements.

Warm regards,
People Operations & Benefits Desk
{company} Human Resources Division""",
        "red_flags": [
            "Social Engineering Vector: Targets financial compensation to induce immediate compliance without verification.",
            "Urgency Trigger: Artificially short deadline tied to monthly salary disbursement hold.",
            "Confidentiality Gag: Explicit instruction 'do not forward' prevents victim from verifying with colleagues.",
            "External Reply-To Header: Directs queries to untrusted domain 'talent-benefits-secure.io'."
        ]
    },
    {
        "id": "DRAFT-03",
        "title": "Finance / Supply Chain: Urgent Overdue Supplier Invoice Settlement",
        "category": "Vendor & Supply Chain Finance",
        "sender_display": "Global Accounts Payable & Procurement",
        "spoofed_from": "billing-accounts@{domain_spoofed}",
        "reply_to": "vendor-reconciliation@wire-hold-finance.biz",
        "return_path": "mailer-daemon@finance-invoice-gateway.net",
        "subject": "OVERDUE NOTICE: Immediate Payment Hold on Invoice #INV-2026-8819 for {company}",
        "urgency_tier": "CRITICAL (Legal / Supply Disruption)",
        "psychological_triggers": ["Fear of Supply Stoppage", "Legal Coercion", "Urgency"],
        "body_template": """ATTENTION: {name} (Cc: Accounts Payable / Procurement)

Our automated accounting system indicates that Payment Requisition #INV-2026-8819 ($18,450.00 USD) for contracted cloud infrastructure services provided to {company} is now 14 days overdue.

A temporary hold has been placed on your organization's service renewal. Continued delay will result in legal escalation and suspension of vendor SLA deliverables.

[INVOICE AUDIT & REMITTANCE]:
Review the reconciliation audit and updated electronic wire transfer instructions attached below:

👉 https://invoices.{domain_spoofed}/remittance/audit-statement?ref=INV-8819-HOLD

If payment has already been initiated, update the remittance transaction hash immediately through the secure portal above to avoid service disconnection.

Sincerely,
Accounts Receivable & Dispute Settlement Desk
Global Vendor Services Group""",
        "red_flags": [
            "Financial Scare Pretext: Alleges overdue invoice ($18,450.00) threatening service disconnection.",
            "False Legal Escalation: Cites contract breaches to intimidate recipient into bypassing procurement controls.",
            "Wire Instruction Modification: Directs recipient to unverified payment update link.",
            "Mismatched Sender Infrastructure: Originates from external non-standard billing domain."
        ]
    }
]


def print_banner():
    banner = rf"""{Fore.CYAN}{Style.BRIGHT}
  ____  ____  _____    _    ____    ____  _   _ ___ ____  _   _ 
 / ___||  _ \| ____|  / \  |  _ \  |  _ \| | | |_ _/ ___|| | | |
 \___ \| |_) |  _|   / _ \ | |_) | | |_) | |_| || |\___ \| |_| |
  ___) |  __/| |___ / ___ \|  _ <  |  __/|  _  || | ___) |  _  |
 |____/|_|   |_____/_/   \_\_| \_\ |_|   |_| |_|___|____/|_| |_|
                                                                
   ____ ____      _    _____ _____ _____ ____                   
  / ___|  _ \    / \  |  ___|_   _| ____|  _ \                  
 | |   | |_) |  / _ \ | |_    | | |  _| | |_) |                 
 | |___|  _ <  / ___ \|  _|   | | | |___|  _ <                  
  \____|_| \_\/_/   \_\_|     |_| |_____|_| \_\                 
{Fore.YELLOW}{Style.BRIGHT} ⚡ SECURITY-AWARENESS TRAINING EMAIL GENERATOR & DMARC DEFENSE SUITE ⚡
{Fore.WHITE} Developed by: Md Peer Siddiqui | Sqrock IT Solution Internship (Day 06)
{Fore.CYAN}========================================================================{Style.RESET_ALL}
"""
    print(banner)


def render_scenario_body(scenario, target):
    """
    Renders the formatted text email body replacing all dynamic tokens.
    """
    domain_spoofed = target["domain"].replace(".com", "-portal.com")
    text = scenario["body_template"].format(
        name=target["name"],
        company=target["company"],
        department=target["department"],
        location=target["location"],
        manager_name=target["manager_name"],
        role=target["role"],
        deadline_hours=target["deadline_hours"],
        domain_spoofed=domain_spoofed
    )
    subject = scenario["subject"].format(
        name=target["name"],
        company=target["company"],
        domain_spoofed=domain_spoofed
    )
    spoofed_from = scenario["spoofed_from"].format(domain_spoofed=domain_spoofed)

    return {
        "id": scenario["id"],
        "title": scenario["title"],
        "category": scenario["category"],
        "subject": subject,
        "from_header": f'"{scenario["sender_display"]}" <{spoofed_from}>',
        "to_header": f'"{target["name"]}" <{target["email"]}>',
        "reply_to": scenario["reply_to"],
        "return_path": scenario["return_path"],
        "urgency_tier": scenario["urgency_tier"],
        "psychological_triggers": scenario["psychological_triggers"],
        "body": text,
        "red_flags": scenario["red_flags"]
    }


def render_mime_headers(rendered_data, target):
    """
    Generates standard RFC 5322 MIME email headers showcasing spoofing mechanics.
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    date_str = now.strftime("%a, %d %b %Y %H:%M:%S +0000")
    msg_id = f"<{uuid.uuid4()}@{target['domain']}>"
    
    headers = f"""{Fore.LIGHTBLACK_EX}Delivered-To: {target['email']}
Received: by mail-gateway.sqrock.internal with SMTP id relay994821;
        {date_str}
Authentication-Results: mx.sqrock.internal;
       dkim=fail (bad signature / unsigned);
       spf=fail (sender IP not in authorized SPF record of {target['domain']});
       dmarc=fail (p=REJECT dis=NONE) header.from={rendered_data['from_header']}
Received-SPF: fail (domain of spoofed origin does not designate permitted sender)
Return-Path: <{rendered_data['return_path']}>
Message-ID: {msg_id}
Date: {date_str}
From: {rendered_data['from_header']}
To: {rendered_data['to_header']}
Reply-To: <{rendered_data['reply_to']}>
Subject: {rendered_data['subject']}
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8; format=flowed
Content-Transfer-Encoding: 7bit
X-Mailer: Microsoft Outlook 16.0 (Enterprise Client Build 14326.20454)
X-Priority: 1 (Highest)
X-MSMail-Priority: High
Importance: High{Style.RESET_ALL}"""
    return headers


def display_rendered_email(rendered_data, target):
    """
    Prints the rendered email draft cleanly in terminal.
    """
    print(f"\n{Fore.CYAN}{Style.BRIGHT}========================================================================")
    print(f" ✉️ AWARENESS EMAIL DRAFT: [{rendered_data['id']}] {rendered_data['title']}")
    print(f"========================================================================{Style.RESET_ALL}")
    print(f" {Fore.YELLOW}Category        :{Style.RESET_ALL} {rendered_data['category']}")
    print(f" {Fore.YELLOW}From Header     :{Style.RESET_ALL} {Fore.RED}{rendered_data['from_header']}{Style.RESET_ALL}")
    print(f" {Fore.YELLOW}To Recipient    :{Style.RESET_ALL} {rendered_data['to_header']}")
    print(f" {Fore.YELLOW}Reply-To Routing:{Style.RESET_ALL} {Fore.MAGENTA}{rendered_data['reply_to']}{Style.RESET_ALL}")
    print(f" {Fore.YELLOW}Subject Line    :{Style.RESET_ALL} {Fore.WHITE}{Style.BRIGHT}{rendered_data['subject']}{Style.RESET_ALL}")
    print(f" {Fore.YELLOW}Urgency Level   :{Style.RESET_ALL} {Fore.RED}{rendered_data['urgency_tier']}{Style.RESET_ALL}")
    print(f" {Fore.YELLOW}Psych Triggers  :{Style.RESET_ALL} {', '.join(rendered_data['psychological_triggers'])}")
    print(f"{Fore.CYAN}{'-'*72}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{rendered_data['body']}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'-'*72}{Style.RESET_ALL}")
    print(f"\n {Fore.RED}{Style.BRIGHT}🚩 Forensic Red Flags for Employee Awareness:{Style.RESET_ALL}")
    for rf in rendered_data["red_flags"]:
        print(f"   {Fore.RED}• {rf}{Style.RESET_ALL}")


def display_dmarc_defense_guide(domain="sqrock.com"):
    """
    Prints the comprehensive SPF, DKIM, and DMARC configuration and deployment guide.
    """
    print(f"\n{Fore.CYAN}{Style.BRIGHT}========================================================================")
    print(f" 🛡️ EMAIL DEFENDER BLUEPRINT: SPF, DKIM & DMARC DEPLOYMENT GUIDE")
    print(f" Protected Domain: {domain}")
    print(f"========================================================================{Style.RESET_ALL}")

    print(f"""
{Fore.YELLOW}{Style.BRIGHT}1. SENDER POLICY FRAMEWORK (SPF - RFC 7208){Style.RESET_ALL}
• Purpose: Specifies which mail servers (IP addresses / MX records) are authorized to send email on behalf of {domain}.
• DNS Record Type: TXT
• Host / Name    : @ (or {domain})
• Recommended TXT Value:
  {Fore.GREEN}{Style.BRIGHT}v=spf1 include:_spf.google.com include:sendgrid.net ip4:198.51.100.1 ~all{Style.RESET_ALL}
• Explanation:
  - 'v=spf1'      : Protocol version indicator.
  - 'include:...' : Grants sending rights to Google Workspace / transactional relays.
  - '~all'        : SoftFail (marks unlisted senders as suspicious without outright dropping).
  - '-all'        : HardFail (recommended once DMARC is enforced; rejects unlisted IPs).

{Fore.YELLOW}{Style.BRIGHT}2. DOMAINKEYS IDENTIFIED MAIL (DKIM - RFC 6376){Style.RESET_ALL}
• Purpose: Adds an asymmetric cryptographic digital signature to email headers, proving the email body was not altered in transit.
• DNS Record Type: TXT
• Host / Selector: s2026._domainkey.{domain}
• Recommended TXT Value:
  {Fore.GREEN}{Style.BRIGHT}v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3...IDAQAB{Style.RESET_ALL}
• Explanation:
  - Private key resides on the authorized mail server and signs every outbound message.
  - Public key is published in DNS; receiving mail servers verify the cryptographic signature against the body hash.

{Fore.YELLOW}{Style.BRIGHT}3. DOMAIN-BASED MESSAGE AUTHENTICATION, REPORTING & CONFORMANCE (DMARC - RFC 7489){Style.RESET_ALL}
• Purpose: Ties SPF and DKIM together by enforcing Alignment (the 'From:' domain must match SPF and DKIM domains) and instructing receivers on how to treat spoofed mail.
• DNS Record Type: TXT
• Host / Name    : _dmarc.{domain}
• Staged Implementation Path:
  Phase 1 (Monitoring Only):
    {Fore.WHITE}v=DMARC1; p=none; rua=mailto:dmarc-reports@{domain}; pct=100{Style.RESET_ALL}
  Phase 2 (Quarantine Suspicious Mail into Spam):
    {Fore.YELLOW}v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@{domain}; pct=100; sp=quarantine{Style.RESET_ALL}
  Phase 3 (Full Strict Rejection - Production Defense):
    {Fore.GREEN}{Style.BRIGHT}v=DMARC1; p=reject; rua=mailto:dmarc-reports@{domain}; ruf=mailto:dmarc-forensics@{domain}; pct=100; sp=reject; aspf=r; adkim=r{Style.RESET_ALL}

• Key Tags:
  - 'p=reject'   : Instructs receiving servers (Gmail, Outlook) to DROP unauthorized spoofed emails completely.
  - 'rua=...'    : Designates destination email for daily XML aggregate compliance reports.
  - 'aspf=r'     : Relaxed SPF domain alignment check (requires base domain match).
  - 'adkim=r'    : Relaxed DKIM domain alignment check.
""")


def export_deliverable_json(target, filepath=DEFAULT_OUTPUT_JSON):
    """
    Exports the 3 rendered email drafts and defender setup guide into JSON format.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    rendered_drafts = [render_scenario_body(sc, target) for sc in SCENARIOS_DATA]
    
    dmarc_guide = {
        "domain": target["domain"],
        "spf_policy": {
            "record_type": "TXT",
            "host": "@",
            "value": f"v=spf1 include:_spf.google.com ~all",
            "standard": "RFC 7208"
        },
        "dkim_policy": {
            "record_type": "TXT",
            "host": f"s2026._domainkey.{target['domain']}",
            "value": "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQ...",
            "standard": "RFC 6376"
        },
        "dmarc_policy": {
            "record_type": "TXT",
            "host": f"_dmarc.{target['domain']}",
            "monitoring_record": f"v=DMARC1; p=none; rua=mailto:dmarc-reports@{target['domain']}; pct=100",
            "enforcement_record": f"v=DMARC1; p=reject; rua=mailto:dmarc-reports@{target['domain']}; pct=100; sp=reject; aspf=r; adkim=r",
            "standard": "RFC 7489"
        }
    }

    deliverable = {
        "metadata": {
            "tool": "PEER'S Spear Phish Crafter v1.0",
            "intern_name": "Md Peer Siddiqui",
            "organization": "Sqrock IT Solution",
            "track": "Social Engineering Attack Simulations Using Python (Day 06)",
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()
        },
        "target_context": target,
        "spear_phishing_awareness_drafts": rendered_drafts,
        "email_authentication_defense_matrix": dmarc_guide
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(deliverable, f, indent=2)

    return filepath


def interactive_menu():
    """
    Master interactive CLI control loop.
    """
    target = dict(DEFAULT_TARGET)

    while True:
        try:
            print_banner()
            print(f" Current Target Profile: {Fore.GREEN}{Style.BRIGHT}{target['name']}{Style.RESET_ALL} | {Fore.YELLOW}{target['company']}{Style.RESET_ALL} ({target['email']})\n")
            print(" Master Options:")
            print(f"  {Fore.CYAN}[1]{Style.RESET_ALL} Generate & Review All 3 Awareness Email Drafts")
            print(f"  {Fore.CYAN}[2]{Style.RESET_ALL} Inspect Specific Awareness Vector (Deep Body & Forensics)")
            print(f"  {Fore.CYAN}[3]{Style.RESET_ALL} Inspect Raw RFC 5322 MIME Email Headers")
            print(f"  {Fore.CYAN}[4]{Style.RESET_ALL} Run Email Header Spoofing & Red Flag Forensics")
            print(f"  {Fore.CYAN}[5]{Style.RESET_ALL} View SPF, DKIM & DMARC Defender Blueprint Guide")
            print(f"  {Fore.CYAN}[6]{Style.RESET_ALL} Export Deliverable JSON ({Fore.YELLOW}spear_phish_templates.json{Style.RESET_ALL})")
            print(f"  {Fore.CYAN}[7]{Style.RESET_ALL} Customize Target Profile Parameters (Name, Org, Domain)")
            print(f"  {Fore.CYAN}[8]{Style.RESET_ALL} Compile Executive Multi-Page PDF Lab Report (Day 06)")
            print(f"  {Fore.CYAN}[0]{Style.RESET_ALL} Exit Suite")

            choice = input(f"\n{Fore.GREEN}SPEAR-CRAFTER > {Style.RESET_ALL}").strip()

            if choice == "1":
                for sc in SCENARIOS_DATA:
                    rendered = render_scenario_body(sc, target)
                    display_rendered_email(rendered, target)
                input(f"\n{Fore.WHITE}Press [ENTER] to return to menu...{Style.RESET_ALL}")

            elif choice == "2":
                print(f"\n{Fore.CYAN}Available Awareness Vectors:{Style.RESET_ALL}")
                for i, sc in enumerate(SCENARIOS_DATA, 1):
                    print(f"  [{i}] {sc['title']}")
                sub = input(f"\n{Fore.YELLOW}Select vector number (1-3) > {Style.RESET_ALL}").strip()
                if sub in ("1", "2", "3"):
                    sc = SCENARIOS_DATA[int(sub) - 1]
                    rendered = render_scenario_body(sc, target)
                    display_rendered_email(rendered, target)
                else:
                    print(f"{Fore.RED}[!] Invalid vector selection.{Style.RESET_ALL}")
                input(f"\n{Fore.WHITE}Press [ENTER] to return to menu...{Style.RESET_ALL}")

            elif choice == "3":
                print(f"\n{Fore.CYAN}Select Vector to Inspect Raw MIME Headers:{Style.RESET_ALL}")
                for i, sc in enumerate(SCENARIOS_DATA, 1):
                    print(f"  [{i}] {sc['title']}")
                sub = input(f"\n{Fore.YELLOW}Select vector number (1-3) > {Style.RESET_ALL}").strip()
                if sub in ("1", "2", "3"):
                    sc = SCENARIOS_DATA[int(sub) - 1]
                    rendered = render_scenario_body(sc, target)
                    headers = render_mime_headers(rendered, target)
                    print(f"\n{Fore.CYAN}{Style.BRIGHT}========================================================================")
                    print(f" 📄 RAW RFC 5322 MIME EMAIL HEADERS: [{rendered['id']}]")
                    print(f"========================================================================{Style.RESET_ALL}")
                    print(headers)
                else:
                    print(f"{Fore.RED}[!] Invalid vector selection.{Style.RESET_ALL}")
                input(f"\n{Fore.WHITE}Press [ENTER] to return to menu...{Style.RESET_ALL}")

            elif choice == "4":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}========================================================================")
                print(f" 🔍 EMAIL HEADER FORENSICS & SPOOFING RED FLAG AUDIT")
                print(f"========================================================================{Style.RESET_ALL}")
                for sc in SCENARIOS_DATA:
                    rendered = render_scenario_body(sc, target)
                    print(f"\n {Fore.YELLOW}{Style.BRIGHT}[{rendered['id']}] {rendered['title']}:{Style.RESET_ALL}")
                    print(f"   • {Fore.WHITE}From Header :{Style.RESET_ALL} {rendered['from_header']}")
                    print(f"   • {Fore.WHITE}Reply-To    :{Style.RESET_ALL} {rendered['reply_to']}")
                    print(f"   • {Fore.RED}Identified Red Flags:{Style.RESET_ALL}")
                    for rf in rendered["red_flags"]:
                        print(f"     {Fore.RED}└──► {rf}{Style.RESET_ALL}")
                input(f"\n{Fore.WHITE}Press [ENTER] to return to menu...{Style.RESET_ALL}")

            elif choice == "5":
                display_dmarc_defense_guide(target["domain"])
                input(f"\n{Fore.WHITE}Press [ENTER] to return to menu...{Style.RESET_ALL}")

            elif choice == "6":
                out_path = export_deliverable_json(target)
                print(f"\n{Fore.GREEN}{Style.BRIGHT}[✓] Awareness Drafts & DMARC Guide successfully exported to:{Style.RESET_ALL}")
                print(f"    {out_path}")
                input(f"\n{Fore.WHITE}Press [ENTER] to return to menu...{Style.RESET_ALL}")

            elif choice == "7":
                print(f"\n{Fore.CYAN}{Style.BRIGHT}--- CUSTOMIZE TARGET PROFILE PARAMETERS ---{Style.RESET_ALL}")
                name = input(f"Enter target full name (current: '{target['name']}') > ").strip()
                if name: target["name"] = name
                
                comp = input(f"Enter target company (current: '{target['company']}') > ").strip()
                if comp:
                    target["company"] = comp
                    target["domain"] = comp.lower().replace(" ", "") + ".com"
                    target["email"] = f"{target['name'].lower().replace(' ', '.')}@{target['domain']}"
                
                dept = input(f"Enter department (current: '{target['department']}') > ").strip()
                if dept: target["department"] = dept
                
                print(f"\n{Fore.GREEN}[✓] Target profile updated successfully!{Style.RESET_ALL}")
                input(f"\n{Fore.WHITE}Press [ENTER] to return to menu...{Style.RESET_ALL}")

            elif choice == "8":
                pdf_script = os.path.join(BASE_DIR, "scripts", "generate_day06_pdf.py")
                if os.path.exists(pdf_script):
                    print(f"\n{Fore.CYAN}[*] Compiling Executive PDF Lab Report...{Style.RESET_ALL}")
                    os.system(f'"{sys.executable}" "{pdf_script}"')
                else:
                    print(f"\n{Fore.RED}[!] PDF generation script not found at {pdf_script}{Style.RESET_ALL}")
                input(f"\n{Fore.WHITE}Press [ENTER] to return to menu...{Style.RESET_ALL}")

            elif choice == "0":
                print(f"\n{Fore.CYAN}[*] Exiting PEER'S Spear Phish Crafter. Train defenders, stay vigilant!{Style.RESET_ALL}\n")
                sys.exit(0)

            else:
                print(f"{Fore.RED}[!] Invalid selection. Please choose an option from 0 to 8.{Style.RESET_ALL}")
                input(f"\n{Fore.WHITE}Press [ENTER] to continue...{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}[!] Execution interrupted by user. Exiting cleanly...{Style.RESET_ALL}\n")
            sys.exit(0)


if __name__ == "__main__":
    interactive_menu()
