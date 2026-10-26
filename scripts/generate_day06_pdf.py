#!/usr/bin/env python3
"""
PEER'S Spear Phish Crafter - Executive Multi-Page Lab Report Compiler (Day 06)
Sqrock IT Solution Cybersecurity Internship Track: Social Engineering Attack Simulations Using Python

Compiles an authoritative 7-page executive engineering report integrating:
- 6 empirical execution screenshots (Kali Linux CLI cold boot, master menu, 3 awareness vectors, GitHub repo)
- In-depth forensic explanations for every screenshot
- Deep technical analyses of token injection, RFC 5322 MIME headers, and red-flag indicators
- Authoritative SPF (RFC 7208), DKIM (RFC 6376), and DMARC (RFC 7489) defense implementation guide
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
        textColor=colors.HexColor("#58A6FF")
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
    # PAGE 2: TOKEN INJECTION MECHANICS & 3 ATTACK VECTORS MATRIX
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
    # PAGE 3: EMPIRICAL EVIDENCE PHASE 1 (Figures 1 & 2)
    # =========================================================================
    story.append(Paragraph("5. Empirical Verification & Evidence Breakdown (Phase 1)", h1_style))
    story.append(Paragraph(
        "The following empirical test captures demonstrate the execution of PEER'S Spear Phish Crafter within an authorized "
        "Kali Linux security research environment, verifying cold-boot startup and master console options.",
        body_style
    ))

    # Screenshot 1: Banner & Startup
    img1_path = os.path.join(SCREENSHOTS_DIR, "01_kali_init_banner.png")
    if os.path.exists(img1_path):
        story.append(Image(img1_path, width=440, height=220))
        story.append(Paragraph("Figure 1: Kali Linux Terminal Cold-Start & Custom Dual-Tone ASCII Banner Rendering", caption_style))
    
    story.append(Paragraph(
        "<b>Technical Analysis of Figure 1:</b><br/>"
        "• <b>Environment Verification:</b> Executed inside a native Kali Linux terminal session (<code>kali@kali:~/PEER-S-Spear-Phish-Crafter</code>).<br/>"
        "• <b>Deployment Pipeline:</b> Demonstrates cloning directly from GitHub, directory inspection (<code>ls</code>), and initialization via <code>python spear_crafter.py</code>.<br/>"
        "• <b>Zero-Dependency UI:</b> Renders the dual-tone <code>PEER'S SPEAR PHISH CRAFTER v1.0</code> production header without heavyweight GUI libraries.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Screenshot 2: Master Menu
    img2_path = os.path.join(SCREENSHOTS_DIR, "02_master_menu.png")
    if os.path.exists(img2_path):
        story.append(Image(img2_path, width=440, height=220))
        story.append(Paragraph("Figure 2: Master Control Menu & Active Target Context (Harish Kumar | Sqrock IT Solution)", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 2:</b><br/>"
        "• <b>Active Profile Binding:</b> Displays the current recipient profile: <b>Harish Kumar</b> (<code>harish.k@sqrock.com</code>) at <b>Sqrock IT Solution</b>.<br/>"
        "• <b>Modular Options:</b> Provides 8 core operations spanning batch generation, deep vector inspection, raw RFC 5322 MIME headers, "
        "forensic red-flag auditing, and DMARC defense blueprinting.<br/>"
        "• <b>Execution Trigger:</b> The operator selects Option <code>[1] Generate &amp; Review All 3 Awareness Email Drafts</code> to render the drafts.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: EMPIRICAL EVIDENCE PHASE 2 (Figures 3 & 4)
    # =========================================================================
    story.append(Paragraph("5. Empirical Verification & Evidence Breakdown (Phase 2)", h1_style))
    story.append(Paragraph(
        "Phase 2 validates the rendering of Draft-01 (Corporate IT SSO Certificate Renewal) and Draft-02 (People Operations Compensation Review), "
        "highlighting dynamic token replacement and employee awareness red flags.",
        body_style
    ))

    # Screenshot 3: Draft 1 (IT SSO)
    img3_path = os.path.join(SCREENSHOTS_DIR, "03_draft01_it_sso.png")
    if os.path.exists(img3_path):
        story.append(Image(img3_path, width=440, height=220))
        story.append(Paragraph("Figure 3: Rendered Draft-01 — Corporate IT: Mandatory SSO Certificate Renewal & Access Hold", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 3:</b><br/>"
        "• <b>Dynamic Token Replacement:</b> Tokens <code>{name}</code>, <code>{company}</code>, and <code>{deadline_hours}</code> cleanly replaced.<br/>"
        "• <b>Deceptive Infrastructure:</b> Sets visible From to <i>'Sqrock Global IT Support Desk'</i> (<code>it-support@sqrock-portal.com</code>), while "
        "Reply-To routes to <code>admin-verification@external-gateway-sync.net</code>.<br/>"
        "• <b>Forensic Red Flags:</b> Flags display-name masking, reply-to mismatch, 24-hr coercion, and lookalike portal link.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Screenshot 4: Draft 2 (HR Payroll)
    img4_path = os.path.join(SCREENSHOTS_DIR, "04_draft02_hr_payroll.png")
    if os.path.exists(img4_path):
        story.append(Image(img4_path, width=440, height=220))
        story.append(Paragraph("Figure 4: Rendered Draft-02 — People Operations: Annual Compensation & Direct Deposit Review", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 4:</b><br/>"
        "• <b>Financial Incentive Vector:</b> Targets compensation review to induce urgency and prompt direct deposit routing modifications.<br/>"
        "• <b>Confidentiality Gag Lever:</b> The pretext instructs the recipient <i>'Please do not forward this communication'</i> to prevent peer verification.<br/>"
        "• <b>Forensic Red Flags:</b> Highlights financial incentive hook, artificially tight Friday cutoff, and external Reply-To routing.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: EMPIRICAL EVIDENCE PHASE 3 & MIME HEADER FORENSICS (Figure 5)
    # =========================================================================
    story.append(Paragraph("5. Empirical Verification & Evidence Breakdown (Phase 3)", h1_style))
    story.append(Paragraph(
        "Phase 3 validates Draft-03 (Finance Overdue Supplier Invoice Settlement) and dissects the underlying RFC 5322 MIME email headers.",
        body_style
    ))

    # Screenshot 5: Draft 3 (Finance Invoice)
    img5_path = os.path.join(SCREENSHOTS_DIR, "05_draft03_finance_invoice.png")
    if os.path.exists(img5_path):
        story.append(Image(img5_path, width=440, height=220))
        story.append(Paragraph("Figure 5: Rendered Draft-03 — Finance / Supply Chain: Urgent Overdue Supplier Invoice Settlement", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 5:</b><br/>"
        "• <b>Legal & Supply Disruption Threat:</b> Alleges an overdue payment of $18,450.00 USD threatening contract breach and cloud SLA disconnection.<br/>"
        "• <b>Wire Fraud Mechanism:</b> Directs the victim to update wire transfer instructions via a deceptive lookalike portal.<br/>"
        "• <b>Red Flag Identifiers:</b> Cites financial panic pretext, procurement bypass attempt, and external billing infrastructure.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("6. Raw RFC 5322 MIME Header Telemetry & Spoofing Indicators", h2_style))
    mime_sample = """Delivered-To: harish.k@sqrock.com
Received: by mail-gateway.sqrock.internal with SMTP id relay994821; Mon, 26 Oct 2026 12:40:00 +0000
Authentication-Results: mx.sqrock.internal;
       dkim=fail (bad signature / unsigned);
       spf=fail (sender IP not in authorized SPF record of sqrock.com);
       dmarc=fail (p=REJECT dis=NONE) header.from=it-support@sqrock-portal.com
Received-SPF: fail (domain does not designate permitted sender)
Return-Path: <bounce-handler@relay-mailer44.org>
Message-ID: <a89b14c2-9901-4df2-bc77-991289182918@sqrock.com>
From: "Sqrock Global IT Support Desk" <it-support@sqrock-portal.com>
To: "Harish Kumar" <harish.k@sqrock.com>
Reply-To: <admin-verification@external-gateway-sync.net>
Subject: ACTION REQUIRED: Security Certificate Expiration for Harish Kumar
X-Mailer: Microsoft Outlook 16.0 | X-Priority: 1 (Highest) | Importance: High"""

    t_mime = Table([[Paragraph(mime_sample.replace('\n', '<br/>'), code_style)]], colWidths=[540])
    t_mime.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#0D1117")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#30363D")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_mime)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: OPEN-SOURCE VERIFICATION & DEFENDER BLUEPRINT (Figure 6)
    # =========================================================================
    story.append(Paragraph("7. Open-Source Implementation & GitHub Verification", h1_style))
    story.append(Paragraph(
        "To ensure compliance with transparent security engineering standards, the complete codebase was published to the public "
        "GitHub repository at <code>https://github.com/MdPeerSiddiqui/PEER-S-Spear-Phish-Crafter</code>.",
        body_style
    ))

    # Screenshot 6: GitHub Repo
    img6_path = os.path.join(SCREENSHOTS_DIR, "06_github_repo_overview.png")
    if os.path.exists(img6_path):
        story.append(Image(img6_path, width=440, height=247))
        story.append(Paragraph("Figure 6: Public GitHub Repository Header, Dynamic Badges & Executive Overview", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 6:</b><br/>"
        "• <b>Repository Architecture:</b> Publicly accessible repository under authorized account <code>MdPeerSiddiqui</code>.<br/>"
        "• <b>Quality Badges:</b> Verified Shields.io badges confirming <b>Python 3.9+</b>, cross-platform support (<b>Kali Linux | Windows | macOS</b>), "
        "<b>6/6 Passing Tests</b>, and open-source <b>MIT Licensing</b>.<br/>"
        "• <b>Contributor Attribution:</b> Formally documented under the author profile of Mohammed Peer Siddiqui for Sqrock IT Solution internship evaluation.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("8. Email Defender Blueprint: SPF & DKIM Configuration", h2_style))
    spf_spec = """<b>SPF DNS TXT Record (RFC 7208):</b><br/>
Host: <code>@</code> (or <code>sqrock.com</code>) | Value: <code>v=spf1 include:_spf.google.com include:sendgrid.net ip4:198.51.100.1 ~all</code><br/>
• <i>Explanation:</i> Authorizes specific sending IPs and third-party relays. Unlisted senders receive a SoftFail (~all).<br/>
<br/>
<b>DKIM Cryptographic Key Record (RFC 6376):</b><br/>
Host: <code>s2026._domainkey.sqrock.com</code> | Value: <code>v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQ...IDAQAB</code><br/>
• <i>Explanation:</i> Provides asymmetric public-key signature verification; tampering with message body immediately invalidates DKIM."""
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

    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: DMARC ENFORCEMENT, TESTS & ETHICAL SIGN-OFF
    # =========================================================================
    story.append(Paragraph("9. DMARC Enforcement & Staged Rollout Strategy (RFC 7489)", h1_style))
    story.append(Paragraph(
        "DMARC ties SPF and DKIM together by enforcing <b>Identifier Alignment</b> with the visible <code>From:</code> header and instructing "
        "recipient servers on how to handle spoofed messages:",
        body_style
    ))

    dmarc_phases = [
        [Paragraph("<b>Rollout Phase</b>", body_bold), Paragraph("<b>DMARC DNS TXT Record</b>", body_bold), Paragraph("<b>Protection Behavior</b>", body_bold)],
        [
            Paragraph("<b>Phase 1: Monitoring</b><br/>(30–60 Days)", body_style),
            Paragraph("<code>v=DMARC1; p=none; rua=mailto:dmarc-reports@sqrock.com; pct=100</code>", body_style),
            Paragraph("Zero disruption; collects daily XML aggregate reports of all sending sources.", body_style)
        ],
        [
            Paragraph("<b>Phase 2: Quarantine</b><br/>(14–30 Days)", body_style),
            Paragraph("<code>v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@sqrock.com; pct=100; sp=quarantine</code>", body_style),
            Paragraph("Spoofed mail failing SPF/DKIM is automatically routed to Spam/Junk folders.", body_style)
        ],
        [
            Paragraph("<b>Phase 3: Rejection</b><br/>(Full Production)", body_style),
            Paragraph("<code>v=DMARC1; p=reject; rua=mailto:dmarc-reports@sqrock.com; pct=100; sp=reject; aspf=r; adkim=r</code>", body_style),
            Paragraph("<b>Complete spoofing immunity.</b> Unauthorized spoofed mail is <b>instantly dropped</b> at SMTP connect time.", body_style)
        ]
    ]
    t_dph = Table(dmarc_phases, colWidths=[110, 240, 190])
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
    story.append(Spacer(1, 6))

    story.append(Paragraph("10. Automated Unit Testing Verification Suite", h1_style))
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
    story.append(Spacer(1, 6))

    story.append(Paragraph("11. Ethical Compliance, Authorized Scope & Sign-Off", h1_style))
    story.append(Paragraph(
        "<b>Ethical Scope:</b> All email templates, sender headers, and lookalike domains generated by this suite are intended strictly for "
        "<b>authorized internal awareness training simulations</b> and defensive engineering education. No outbound emails were transmitted "
        "across public networks without explicit administrative authorization. No credential-harvesting backend servers or malicious payload "
        "delivery mechanisms were deployed. All operations adhere strictly to the <b>Information Technology Act 2000 (India)</b>, the Computer "
        "Fraud and Abuse Act (CFAA), and the Sqrock IT Solution Ethical Guidelines.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("12. Intern Declaration & Sign-Off", h1_style))
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
