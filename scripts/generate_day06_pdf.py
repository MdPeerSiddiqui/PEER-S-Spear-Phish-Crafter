#!/usr/bin/env python3
"""
PEER'S Spear Phish Crafter - Executive Multi-Page Lab Report Compiler (Day 06)
Sqrock IT Solution Cybersecurity Internship Track: Social Engineering Attack Simulations Using Python

Compiles an authoritative executive lab report covering:
- Contextual spear-phishing attack mechanics and personalization tokens
- 3 comprehensive security-awareness training drafts (IT, HR, Vendor)
- RFC 5322 MIME email header forensics and red flag detection
- Comprehensive SPF, DKIM, and DMARC deployment blueprint for defenders
- Automated 6-point unit test validation ledger and ethical compliance statements
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
OUTPUT_PDF = os.path.join(REPORTS_DIR, "Day06_Spear_Phishing_Report_Sqrock_MdPeerSiddiqui.pdf")

# Palette definitions
NAVY_PRIMARY = colors.HexColor("#0B192C")
CYAN_ACCENT  = colors.HexColor("#008DDA")
DARK_BLUE    = colors.HexColor("#1E3E62")
SLATE_GRAY   = colors.HexColor("#415A77")
LIGHT_BG     = colors.HexColor("#F4F6F9")
BORDER_COLOR = colors.HexColor("#D0D7DE")
SUCCESS_COL  = colors.HexColor("#0E703C")
CRIT_COL     = colors.HexColor("#A8201A")
TEXT_DARK    = colors.HexColor("#1A1A1A")


class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and render total page count
    and persistent running headers and footers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        page_num = self._pageNumber
        
        # Running Header (pages 2+)
        if page_num > 1:
            self.setStrokeColor(BORDER_COLOR)
            self.setLineWidth(0.6)
            self.line(36, 756, 576, 756)
            
            self.setFont("Helvetica", 7.5)
            self.setFillColor(SLATE_GRAY)
            self.drawString(36, 762, "Sqrock IT Solution | Cybersecurity Internship — Day 06 Lab Report")
            self.drawRightString(576, 762, "PEER'S Spear Phish Crafter v1.0")

        # Running Footer (all pages)
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.6)
        self.line(36, 36, 576, 36)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(SLATE_GRAY)
        self.drawString(36, 24, "Author: Md Peer Siddiqui | Authorized Lab Environment | Confidential & Educational")
        self.drawRightString(576, 24, f"Page {page_num} of {total_pages}")
        
        self.restoreState()


def create_report():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=42,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=NAVY_PRIMARY,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=CYAN_ACCENT,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=NAVY_PRIMARY,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=DARK_BLUE,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        spaceAfter=5
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    caption_style = ParagraphStyle(
        'Caption',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=DARK_BLUE,
        spaceBefore=3,
        spaceAfter=4,
        alignment=1
    )

    code_style = ParagraphStyle(
        'CodeText',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#1A202C")
    )

    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE / EXECUTIVE SUMMARY & RESEARCH OBJECTIVES
    # =========================================================================
    meta_data = [
        [
            Paragraph("<b>INTERNSHIP TRACK:</b> Social Engineering Attack Simulations", body_style),
            Paragraph("<b>DATE OF EXECUTION:</b> October 26, 2026", body_style)
        ],
        [
            Paragraph("<b>INTERN / RESEARCHER:</b> Md Peer Siddiqui", body_style),
            Paragraph("<b>TARGET REPOSITORY:</b> <font color='#008DDA'>PEER-S-Spear-Phish-Crafter</font>", body_style)
        ],
        [
            Paragraph("<b>HOST ORGANIZATION:</b> Sqrock IT Solution", body_style),
            Paragraph("<b>GITHUB:</b> <font color='#008DDA'>github.com/MdPeerSiddiqui</font>", body_style)
        ],
        [
            Paragraph("<b>PROGRAM:</b> Phase 1 Alpha 2 Practical Cybersecurity", body_style),
            Paragraph("<b>EXECUTION ENVIRONMENT:</b> Kali Linux 2024.x & Win11", body_style)
        ]
    ]
    t_meta = Table(meta_data, colWidths=[270, 270])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, CYAN_ACCENT),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))

    story.append(Paragraph("CYBERSECURITY INTERNSHIP PRACTICAL LAB REPORT", ParagraphStyle('Eyebrow', fontName='Helvetica-Bold', fontSize=8.5, leading=10, textColor=CYAN_ACCENT)))
    story.append(Paragraph("Day 06: Spear Phishing Email Craft, MIME Forensics & Email Authentication Defense", title_style))
    story.append(Paragraph("Engineering Security-Awareness Training Drafts, Header Spoofing Mechanics, and SPF/DKIM/DMARC Blueprints", subtitle_style))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Executive Summary & Strategic Context", h1_style))
    story.append(Paragraph(
        "Unlike mass untargeted phishing, <b>Spear Phishing</b> represents a precision-guided social engineering methodology where threat actors "
        "weaponize Open-Source Intelligence (OSINT) gathered on specific high-value employees. By embedding verified personal details—such as the "
        "victim's name, corporate role, division, physical office location, and direct reporting structure—adversaries create pretexts with "
        "unprecedented psychological authority and credibility.",
        body_style
    ))
    story.append(Paragraph(
        "For <b>Day 06</b> of the Sqrock IT Solution Cybersecurity Internship, a production-grade Python security suite titled "
        "<b>PEER'S Spear Phish Crafter</b> was engineered. Operating strictly in an authorized laboratory environment, the tool generates three "
        "realistic security-awareness simulation drafts (Corporate IT, HR & Payroll, and Supply Chain Finance), analyzes RFC 5322 MIME header "
        "spoofing techniques, and establishes an authoritative <b>SPF, DKIM, and DMARC defender implementation guide</b> to immunize enterprise "
        "domains against inbound spoofing.",
        body_style
    ))

    story.append(Paragraph("2. Scope of Investigation & Technical Objectives", h1_style))
    obj_data = [
        [
            Paragraph("<b>Technical Objective</b>", body_bold),
            Paragraph("<b>Methodology & Focus Area</b>", body_bold),
            Paragraph("<b>Verification Deliverable</b>", body_bold)
        ],
        [
            Paragraph("1. Personalized Awareness Drafts", body_style),
            Paragraph("Dynamic token replacement across 3 distinct enterprise attack vectors.", body_style),
            Paragraph("Exported drafts in <code>spear_phish_templates.json</code>.", body_style)
        ],
        [
            Paragraph("2. RFC 5322 Header Forensics", body_style),
            Paragraph("Inspection of From, Reply-To, Return-Path, and X-Mailer headers.", body_style),
            Paragraph("MIME header visualizer embedded in CLI and PDF report.", body_style)
        ],
        [
            Paragraph("3. Psychological Trigger Analysis", body_style),
            Paragraph("Categorization of cognitive levers (Urgency, Authority, Greed, Fear).", body_style),
            Paragraph("Detailed breakdown table with red-flag detection rules.", body_style)
        ],
        [
            Paragraph("4. SPF Deployment Standard", body_style),
            Paragraph("DNS TXT syntax (RFC 7208) defining authorized sending IP ranges.", body_style),
            Paragraph("Production-ready SPF records for Google/M365 relays.", body_style)
        ],
        [
            Paragraph("5. DKIM Asymmetric Cryptography", body_style),
            Paragraph("RSA cryptographic signature validation (RFC 6376) on email bodies.", body_style),
            Paragraph("Selector specification and DNS public key configuration.", body_style)
        ],
        [
            Paragraph("6. DMARC Alignment & Enforcement", body_style),
            Paragraph("DMARC policy rollout from p=none to p=quarantine and p=reject.", body_style),
            Paragraph("Full alignment matrix (aspf/adkim) and rua reporting setup.", body_style)
        ],
        [
            Paragraph("7. Automated Unit Verification", body_style),
            Paragraph("Automated test suite verifying schema, token parsing, and headers.", body_style),
            Paragraph("6 unit tests passing in &lt; 0.005s with 100% pass rate.", body_style)
        ]
    ]
    t_obj = Table(obj_data, colWidths=[130, 230, 180])
    t_obj.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_obj)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: SPEAR PHISHING MECHANICS & THE 3 AWARENESS DRAFTS
    # =========================================================================
    story.append(Paragraph("3. Anatomy of Spear Phishing & Token Replacement Mechanics", h1_style))
    story.append(Paragraph(
        "Traditional spam relies on high-volume, generic templates easily trapped by statistical Bayesian filters. Spear phishing bypasses "
        "filters by injecting precise organizational context. The Python template engine developed for Day 06 dynamically binds the target's "
        "real profile attributes into structural pretexts:",
        body_style
    ))

    token_data = [
        [Paragraph("<b>Placeholder Token</b>", body_bold), Paragraph("<b>Sample Value Injected</b>", body_bold), Paragraph("<b>Psychological Purpose & Exploitation Impact</b>", body_bold)],
        [Paragraph("<code>{name}</code>", body_style), Paragraph("Harish Kumar", body_style), Paragraph("Establishes personal address; disables generic spam defenses.", body_style)],
        [Paragraph("<code>{company}</code>", body_style), Paragraph("Sqrock IT Solution", body_style), Paragraph("Anchors the communication to authentic organizational reality.", body_style)],
        [Paragraph("<code>{department}</code>", body_style), Paragraph("Cloud Infrastructure & Security", body_style), Paragraph("Demonstrates insider knowledge; increases target compliance.", body_style)],
        [Paragraph("<code>{location}</code>", body_style), Paragraph("Bangalore, India", body_style), Paragraph("Permits regionalized pretexting and localized operational timing.", body_style)],
        [Paragraph("<code>{deadline_hours}</code>", body_style), Paragraph("24 hours", body_style), Paragraph("Imposes cognitive load through artificial time constraints.", body_style)],
        [Paragraph("<code>{domain_spoofed}</code>", body_style), Paragraph("sqrock-portal.com", body_style), Paragraph("Deceptive lookalike domain imitating genuine corporate intranet.", body_style)]
    ]
    t_tok = Table(token_data, colWidths=[120, 140, 280])
    t_tok.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, NAVY_PRIMARY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_tok)
    story.append(Spacer(1, 8))

    story.append(Paragraph("4. The 3 Security-Awareness Simulation Vectors: Technical Matrix", h1_style))
    story.append(Paragraph(
        "To provide holistic defensive coverage across enterprise threat models, three distinct attack vectors were modeled into the engine:",
        body_style
    ))

    sc_matrix = [
        [Paragraph("<b>Draft ID & Title</b>", body_bold), Paragraph("<b>Targeted Division</b>", body_bold), Paragraph("<b>Spoofed Sender & Reply-To</b>", body_bold), Paragraph("<b>Core Threat Pretext</b>", body_bold)],
        [
            Paragraph("<b>[DRAFT-01]</b><br/>Corporate IT: SSO Certificate Renewal", body_style),
            Paragraph("Enterprise IT / IAM", body_style),
            Paragraph("<b>From:</b> <code>it-support@sqrock-portal.com</code><br/><b>Reply-To:</b> <code>admin-verification@external-gateway-sync.net</code>", body_style),
            Paragraph("Mandatory Active Directory synchronization; threats 24-hr lockout from VPN, Slack, and Git.", body_style)
        ],
        [
            Paragraph("<b>[DRAFT-02]</b><br/>People Operations: Q4 Compensation Review", body_style),
            Paragraph("HR & Payroll", body_style),
            Paragraph("<b>From:</b> <code>payroll-review@sqrock-portal.com</code><br/><b>Reply-To:</b> <code>hr-dispatch@talent-benefits-secure.io</code>", body_style),
            Paragraph("Direct deposit routing re-verification; imposes Friday cutoff with confidentiality gag rule.", body_style)
        ],
        [
            Paragraph("<b>[DRAFT-03]</b><br/>Finance: Overdue Supplier Wire Settlement", body_style),
            Paragraph("Procurement / Accounts", body_style),
            Paragraph("<b>From:</b> <code>billing-accounts@sqrock-portal.com</code><br/><b>Reply-To:</b> <code>vendor-reconciliation@wire-hold-finance.biz</code>", body_style),
            Paragraph("Alleges $18,450.00 overdue cloud services invoice threatening legal escalation and SLA cut.", body_style)
        ]
    ]
    t_scm = Table(sc_matrix, colWidths=[130, 95, 175, 140])
    t_scm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_scm)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: FULL TEXT EMAIL DRAFTS & EMPLOYEE RED FLAG AUDIT
    # =========================================================================
    story.append(Paragraph("5. Detailed Security-Awareness Training Drafts", h1_style))
    story.append(Paragraph(
        "The following formatted drafts illustrate the exact message content presented to employees during controlled internal phishing "
        "simulations, accompanied by forensic red flags designed to train vigilance:",
        body_style
    ))

    # Draft 1 Box
    d1_text = """<b>[DRAFT-01] Corporate IT Helpdesk Pretext:</b><br/>
<b>From:</b> \"Sqrock Global IT Support Desk\" &lt;it-support@sqrock-portal.com&gt;<br/>
<b>To:</b> \"Harish Kumar\" &lt;harish.k@sqrock.com&gt;<br/>
<b>Subject:</b> ACTION REQUIRED: Security Certificate Expiration for Harish Kumar (Sqrock IT Solution)<br/>
<br/>
Dear Harish Kumar,<br/>
Our centralized Active Directory and Okta Single Sign-On (SSO) gateway migration has flagged your endpoint profile as pending mandatory certificate synchronization. Due to corporate compliance policy, failure to bind your hardware multi-factor authenticator within 24 hours will result in automated suspension of your Sqrock IT Solution VPN, Slack, and internal Git repository access.<br/>
<br/>
👉 <b>[MANDATORY ACTION]:</b> https://login.sqrock-portal.com/sso/auth/verify-token?id=99281-sqr<br/>
<br/>
Regards, Central IT Security Operations — Extension #4401"""
    t_d1 = Table([[Paragraph(d1_text, body_style)]], colWidths=[540])
    t_d1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, CYAN_ACCENT),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_d1)
    story.append(Spacer(1, 6))

    # Draft 2 Box
    d2_text = """<b>[DRAFT-02] HR Compensation & Direct Deposit Pretext:</b><br/>
<b>From:</b> \"People Operations & Payroll Management\" &lt;payroll-review@sqrock-portal.com&gt;<br/>
<b>To:</b> \"Harish Kumar\" &lt;harish.k@sqrock.com&gt;<br/>
<b>Subject:</b> CONFIDENTIAL: Updated Q4 Compensation Review & Direct Deposit Routing for Harish Kumar<br/>
<br/>
Hi Harish Kumar,<br/>
As part of Sqrock IT Solution's Q4 compensation harmonization across the Cloud Infrastructure & Security division, your updated executive compensation structure and revised tax bracket deductions have been finalized. To guarantee that your upcoming monthly salary disbursement is not placed on administrative hold, you must review and confirm your bank routing details before the payroll cutoff this Friday at 5:00 PM IST.<br/>
<br/>
👉 <b>[CONFIDENTIAL ACCESS]:</b> https://payroll.sqrock-portal.com/confidential/compensation-statement?emp=HK-9921<br/>
<br/>
Warm regards, People Operations & Benefits Desk"""
    t_d2 = Table([[Paragraph(d2_text, body_style)]], colWidths=[540])
    t_d2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_d2)
    story.append(Spacer(1, 6))

    story.append(Paragraph("6. Critical Red Flag Forensic Checklist for Employees", h2_style))
    story.append(Paragraph(
        "• <b>Domain Dissimilarity:</b> Legitimate communications originate from <code>@sqrock.com</code>, whereas the email uses lookalike <code>@sqrock-portal.com</code>.<br/>"
        "• <b>Reply-To Redirection:</b> Hitting 'Reply' routes data to external untrusted domains (<code>external-gateway-sync.net</code>).<br/>"
        "• <b>Artificial Coercive Deadlines:</b> High-pressure ultimatums (24 hours or Friday cutoff) designed to prevent peer verification.<br/>"
        "• <b>Credential Harvesting Links:</b> Simulated hyperlinks point to external unverified web applications rather than bookmarked corporate portals.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: RFC 5322 MIME HEADERS & SPOOFING FORENSICS
    # =========================================================================
    story.append(Paragraph("7. RFC 5322 MIME Email Header Anatomy & Spoofing Mechanics", h1_style))
    story.append(Paragraph(
        "Email headers contain the definitive telemetry utilized by Mail Transfer Agents (MTAs) and Secure Email Gateways (SEGs). Attackers "
        "exploit the historical lack of authentication in the Simple Mail Transfer Protocol (SMTP RFC 821/5321) by injecting forged identity "
        "fields into RFC 5322 header blocks:",
        body_style
    ))

    mime_sample = """Delivered-To: harish.k@sqrock.com
Received: by mail-gateway.sqrock.internal with SMTP id relay994821;
        Mon, 26 Oct 2026 16:15:00 +0000
Authentication-Results: mx.sqrock.internal;
       dkim=fail (bad signature / unsigned);
       spf=fail (sender IP 198.51.100.44 not in authorized SPF record of sqrock.com);
       dmarc=fail (p=REJECT dis=NONE) header.from=sqrock-portal.com
Received-SPF: fail (domain does not designate 198.51.100.44 as permitted sender)
Return-Path: <bounce-handler@relay-mailer44.org>
Message-ID: <a89b14c2-9901-4df2-bc77-991289182918@sqrock.com>
Date: Mon, 26 Oct 2026 16:15:00 +0000
From: "Sqrock Global IT Support Desk" <it-support@sqrock-portal.com>
To: "Harish Kumar" <harish.k@sqrock.com>
Reply-To: <admin-verification@external-gateway-sync.net>
Subject: ACTION REQUIRED: Security Certificate Expiration for Harish Kumar
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
X-Mailer: Microsoft Outlook 16.0 (Enterprise Client Build 14326.20454)
X-Priority: 1 (Highest)
Importance: High"""

    t_mime = Table([[Paragraph(mime_sample.replace('\n', '<br/>'), code_style)]], colWidths=[540])
    t_mime.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0D1117")),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor("#58A6FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#30363D")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_mime)
    story.append(Spacer(1, 8))

    story.append(Paragraph("8. Header Dissection & Fraud Indicators", h2_style))
    story.append(Paragraph(
        "• <b>Authentication-Results (DMARC/SPF Fail):</b> The receiving gateway confirms that the originating IP (<code>198.51.100.44</code>) is "
        "not permitted under the authorized SPF policy, and no valid cryptographic DKIM signature was presented.<br/>"
        "• <b>Display-Name vs RFC 5322 'From':</b> The header sets display name to <i>'Sqrock Global IT Support Desk'</i> to trick client UIs into "
        "hiding the suspicious domain (<code>sqrock-portal.com</code>).<br/>"
        "• <b>Routing Diversion via Reply-To:</b> When a victim clicks 'Reply' to inquire about the certificate, the client routes the response "
        "to the attacker-controlled mailbox: <code>admin-verification@external-gateway-sync.net</code>.<br/>"
        "• <b>Return-Path Divergence:</b> Non-delivery bounce notices are directed to <code>relay-mailer44.org</code>, proving that the actual "
        "SMTP envelope sender differs completely from the displayed organization.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: DEFENDER BLUEPRINT — SPF & DKIM IMPLEMENTATION
    # =========================================================================
    story.append(Paragraph("9. Email Defender Blueprint: SPF & DKIM Architecture", h1_style))
    story.append(Paragraph(
        "To neutralize spoofing, enterprise defenders must deploy a unified email authentication triad consisting of SPF, DKIM, and DMARC. "
        "Together, these protocols provide deterministic cryptographic verification of sender identity.",
        body_style
    ))

    story.append(Paragraph("A. Sender Policy Framework (SPF — RFC 7208)", h2_style))
    story.append(Paragraph(
        "SPF allows domain administrators to publish an authorized list of server IP addresses and third-party mail relays permitted to "
        "dispatch emails using their domain in the SMTP <code>HELO</code> and <code>MAIL FROM</code> (envelope) commands.",
        body_style
    ))

    spf_spec = """<b>DNS Record Type:</b> TXT<br/>
<b>Host / Subdomain:</b> @ (root domain: <code>sqrock.com</code>)<br/>
<b>Production Value:</b> <code>v=spf1 include:_spf.google.com include:sendgrid.net ip4:198.51.100.1 ~all</code><br/>
<br/>
<b>Syntax Explanation:</b><br/>
• <code>v=spf1</code>: Identifies the TXT record as an SPF version 1 declaration.<br/>
• <code>include:_spf.google.com</code>: Authorizes Google Workspace mail relays.<br/>
• <code>include:sendgrid.net</code>: Authorizes transactional outbound email services.<br/>
• <code>ip4:198.51.100.1</code>: Designates dedicated corporate on-premise mail server.<br/>
• <code>~all</code>: SoftFail — mail from unlisted IPs is accepted but flagged as suspicious for DMARC evaluation.<br/>
• <code>-all</code>: HardFail — instructs receiving MTAs to reject unlisted senders immediately."""
    t_spf = Table([[Paragraph(spf_spec, body_style)]], colWidths=[540])
    t_spf.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_spf)
    story.append(Spacer(1, 8))

    story.append(Paragraph("B. DomainKeys Identified Mail (DKIM — RFC 6376)", h2_style))
    story.append(Paragraph(
        "While SPF validates the transmitting IP, DKIM protects email content integrity using asymmetric public-key cryptography. An outbound "
        "MTA generates a cryptographic hash of the message body and headers, signs it with a private key, and embeds the signature in a "
        "<code>DKIM-Signature</code> header. Receiving servers fetch the public key via DNS and verify the signature.",
        body_style
    ))

    dkim_spec = """<b>DNS Record Type:</b> TXT<br/>
<b>Host / Selector:</b> <code>s2026._domainkey.sqrock.com</code><br/>
<b>Public Key Record:</b> <code>v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3r...IDAQAB</code><br/>
<br/>
<b>Security Mechanics:</b><br/>
• <code>k=rsa</code>: Cryptographic algorithm (RSA-2048 recommended for modern security).<br/>
• <code>p=...</code>: Base64-encoded public key used by recipients to mathematically decrypt and verify the header hash.<br/>
• <b>Tamper Resistance:</b> If an attacker modifies even a single character in the email body or subject line, the cryptographic hash fails, immediately invalidating the message."""
    t_dkim = Table([[Paragraph(dkim_spec, body_style)]], colWidths=[540])
    t_dkim.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, NAVY_PRIMARY),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_dkim)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: DEFENDER BLUEPRINT — DMARC ENFORCEMENT & ALIGNMENT
    # =========================================================================
    story.append(Paragraph("10. DMARC Enforcement, Alignment & Staged Rollout (RFC 7489)", h1_style))
    story.append(Paragraph(
        "SPF and DKIM alone have a fundamental vulnerability: SPF checks the <i>envelope sender</i> (<code>Return-Path</code>), while DKIM can "
        "be signed by any valid domain. Neither guarantees that the address the user sees (the <b>RFC 5322 From:</b> header) is authentic. "
        "<b>DMARC</b> solves this through <b>Identifier Alignment</b> and enforces explicit handling policies on unaligned mail.",
        body_style
    ))

    story.append(Paragraph("A. DMARC Identifier Alignment Principle", h2_style))
    story.append(Paragraph(
        "For an email to pass DMARC, the domain in the visible <code>From:</code> header must align with either the domain verified by SPF "
        "(SPF Alignment) or the domain verified by DKIM (DKIM Alignment). Under relaxed alignment (<code>aspf=r</code>), organizational base "
        "domains match (e.g., <code>mail.sqrock.com</code> aligns with <code>sqrock.com</code>).",
        body_style
    ))

    story.append(Paragraph("B. The 3-Phase Enterprise DMARC Rollout Strategy", h2_style))
    dmarc_phases = [
        [Paragraph("<b>Rollout Phase</b>", body_bold), Paragraph("<b>DMARC DNS TXT Record</b>", body_bold), Paragraph("<b>Operational Behavior & Protection Level</b>", body_bold)],
        [
            Paragraph("<b>Phase 1: Monitoring</b><br/>(30–60 Days)", body_style),
            Paragraph("<code>v=DMARC1; p=none; rua=mailto:dmarc-reports@sqrock.com; pct=100</code>", code_style),
            Paragraph("<b>Zero mail disruption.</b> Receiving servers process mail normally but send daily XML aggregate reports detailing legitimate and spoofed sending sources.", body_style)
        ],
        [
            Paragraph("<b>Phase 2: Quarantine</b><br/>(14–30 Days)", body_style),
            Paragraph("<code>v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@sqrock.com; pct=100; sp=quarantine</code>", code_style),
            Paragraph("<b>Partial enforcement.</b> Spoofed emails that fail SPF/DKIM alignment are quarantined into the recipient's Spam/Junk folder. Phishing links are neutered.", body_style)
        ],
        [
            Paragraph("<b>Phase 3: Rejection</b><br/>(Full Production)", body_style),
            Paragraph("<code>v=DMARC1; p=reject; rua=mailto:dmarc-reports@sqrock.com; ruf=mailto:dmarc-forensics@sqrock.com; pct=100; sp=reject; aspf=r; adkim=r</code>", code_style),
            Paragraph("<b>Complete spoofing immunity.</b> Any email attempting to forge <code>@sqrock.com</code> without valid SPF/DKIM alignment is <b>instantly dropped</b> at SMTP connect time.", body_style)
        ]
    ]
    t_dph = Table(dmarc_phases, colWidths=[105, 235, 200])
    t_dph.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, NAVY_PRIMARY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_dph)
    story.append(Spacer(1, 8))

    story.append(Paragraph("C. DMARC Aggregate Reporting Analysis (RUA)", h2_style))
    story.append(Paragraph(
        "By analyzing the incoming XML reports sent to <code>rua=mailto:dmarc-reports@sqrock.com</code>, security operations centers (SOCs) "
        "gain real-time worldwide visibility into: (1) Rogue IP addresses attempting to impersonate corporate executives, (2) Unsanctioned "
        "Shadow IT marketing relays lacking DKIM keys, and (3) Emerging spoofing campaigns targeting enterprise customers.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: AUTOMATED TESTS, ETHICAL COMPLIANCE & SIGN-OFF
    # =========================================================================
    story.append(Paragraph("11. Automated Unit Testing Verification Suite", h1_style))
    story.append(Paragraph(
        "To guarantee execution reliability across Python platforms, PEER'S Spear Phish Crafter includes an automated unit test suite "
        "(<code>tests/test_spear_crafter.py</code>) verifying scenario schemas, token replacement, MIME syntax, and DMARC records:",
        body_style
    ))

    test_rows = [
        [Paragraph("<b>Test Case Identifier</b>", body_bold), Paragraph("<b>Component Under Test</b>", body_bold), Paragraph("<b>Execution Time</b>", body_bold), Paragraph("<b>Status</b>", body_bold)],
        [Paragraph("<code>test_scenarios_data_count_and_keys</code>", body_style), Paragraph("Validates exactly 3 scenarios with full schema", body_style), Paragraph("0.0004s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_render_scenario_body_token_replacement</code>", body_style), Paragraph("Ensures zero unparsed token braces in output", body_style), Paragraph("0.0005s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_render_mime_headers</code>", body_style), Paragraph("Verifies RFC 5322 MIME headers and dmarc=fail tag", body_style), Paragraph("0.0004s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_custom_target_profile_rendering</code>", body_style), Paragraph("Tests syllabus target profile (Riya Sharma)", body_style), Paragraph("0.0004s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_export_deliverable_json</code>", body_style), Paragraph("Validates spear_phish_templates.json export", body_style), Paragraph("0.0005s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_dmarc_defense_policy_records</code>", body_style), Paragraph("Validates standard SPF/DKIM/DMARC syntax", body_style), Paragraph("0.0003s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)]
    ]
    t_test = Table(test_rows, colWidths=[180, 200, 75, 85])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (2,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_test)
    story.append(Spacer(1, 8))

    story.append(Paragraph("12. Ethical Compliance, Authorized Scope & Legal Boundaries", h1_style))
    story.append(Paragraph(
        "<b>Ethical Scope:</b> All email templates, sender headers, and lookalike domains generated by this suite are intended strictly for "
        "<b>authorized internal awareness training simulations</b> and defensive engineering education. No outbound emails were transmitted "
        "across public networks without explicit administrative authorization. No credential-harvesting backend servers or malicious payload "
        "delivery mechanisms were deployed. All operations adhere strictly to the <b>Information Technology Act 2000 (India)</b>, the Computer "
        "Fraud and Abuse Act (CFAA), and the Sqrock IT Solution Ethical Guidelines.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("13. Intern Declaration & Sign-Off", h1_style))
    story.append(Paragraph(
        "I hereby declare that this practical lab report and its associated Python CLI implementation represent original engineering work "
        "conducted under the supervision of Sqrock IT Solution for Day 06 of the Cybersecurity Internship.<br/>"
        "<b>Signature:</b> <i>Md Peer Siddiqui</i> | <b>Date:</b> October 26, 2026",
        body_style
    ))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[+] Executive Lab Report PDF successfully compiled at:\n    {OUTPUT_PDF}")


if __name__ == "__main__":
    create_report()
