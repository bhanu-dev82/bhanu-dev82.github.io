#!/usr/bin/env python3
"""One-page DevOps Faculty resume for Bhanu Nagpure — Mentorizee interview."""

from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable,
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUT = "/home/bhd/Downloads/resumes/devops/Bhanu_Nagpure_DevOps_Faculty.pdf"

NAVY = HexColor("#1a1a1a")
LINK = HexColor("#1a365d")
MUTED = HexColor("#333333")
RULE = HexColor("#222222")

PAGE_W, PAGE_H = letter
LEFT = 0.55 * inch
RIGHT = 0.55 * inch
TOP = 0.38 * inch
BOTTOM = 0.32 * inch
CONTENT_W = PAGE_W - LEFT - RIGHT


def styles():
    s = {}
    s["name"] = ParagraphStyle(
        "name",
        fontName="Times-Bold",
        fontSize=18,
        leading=20,
        alignment=TA_CENTER,
        textColor=NAVY,
        spaceAfter=0,
    )
    s["contact"] = ParagraphStyle(
        "contact",
        fontName="Times-Roman",
        fontSize=8.7,
        leading=11.2,
        alignment=TA_CENTER,
        textColor=MUTED,
    )
    s["section"] = ParagraphStyle(
        "section",
        fontName="Times-Bold",
        fontSize=10.5,
        leading=12.5,
        textColor=NAVY,
        spaceBefore=6.5,
        spaceAfter=0.5,
        tracking=0.5,
    )
    s["body"] = ParagraphStyle(
        "body",
        fontName="Times-Roman",
        fontSize=9.2,
        leading=11.5,
        textColor=black,
        alignment=TA_JUSTIFY,
    )
    s["bullet"] = ParagraphStyle(
        "bullet",
        fontName="Times-Roman",
        fontSize=9.2,
        leading=11.5,
        textColor=black,
        leftIndent=11,
        firstLineIndent=-9,
        alignment=TA_JUSTIFY,
    )
    s["job_left"] = ParagraphStyle(
        "job_left",
        fontName="Times-Bold",
        fontSize=9.6,
        leading=11.8,
        textColor=black,
    )
    s["job_right"] = ParagraphStyle(
        "job_right",
        fontName="Times-Roman",
        fontSize=9.6,
        leading=11.8,
        alignment=TA_RIGHT,
        textColor=black,
    )
    s["meta_left"] = ParagraphStyle(
        "meta_left",
        fontName="Times-Italic",
        fontSize=8.8,
        leading=11,
        textColor=MUTED,
    )
    s["meta_right"] = ParagraphStyle(
        "meta_right",
        fontName="Times-Italic",
        fontSize=8.8,
        leading=11,
        alignment=TA_RIGHT,
        textColor=MUTED,
    )
    s["proj"] = ParagraphStyle(
        "proj",
        fontName="Times-Bold",
        fontSize=9.6,
        leading=11.8,
        textColor=black,
    )
    s["skill"] = ParagraphStyle(
        "skill",
        fontName="Times-Roman",
        fontSize=9.2,
        leading=11.5,
        textColor=black,
        alignment=TA_JUSTIFY,
    )
    return s


def section(title, st):
    return KeepTogether(
        [
            Paragraph(title.upper(), st["section"]),
            HRFlowable(
                width="100%",
                thickness=0.8,
                color=RULE,
                spaceBefore=0,
                spaceAfter=3,
            ),
        ]
    )


def row2(left, right, left_style, right_style, col1=None):
    if col1 is None:
        col1 = CONTENT_W * 0.72
    col2 = CONTENT_W - col1
    t = Table(
        [[Paragraph(left, left_style), Paragraph(right, right_style)]],
        colWidths=[col1, col2],
    )
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
            ]
        )
    )
    return t


def skill_line(label, rest, st):
    return Paragraph(
        f"<b>{label}:</b> {rest}",
        st["skill"],
    )


def bullet(text, st):
    return Paragraph(f"•  {text}", st["bullet"])


def build():
    st = styles()
    story = []

    story.append(Paragraph("Bhanu Nagpure", st["name"]))
    story.append(Spacer(1, 3))
    story.append(
        Paragraph(
            '+91 982-210-7989  |  <link href="mailto:bhanunagpure453@gmail.com">'
            '<font color="#1a365d"><u>bhanunagpure453@gmail.com</u></font></link>  |  '
            '<link href="https://linkedin.com/in/bhanunagpure">'
            '<font color="#1a365d"><u>linkedin.com/in/bhanunagpure</u></font></link>  |  '
            '<link href="https://github.com/bhanu-dev82">'
            '<font color="#1a365d"><u>github.com/bhanu-dev82</u></font></link>',
            st["contact"],
        )
    )
    story.append(
        Paragraph(
            '<link href="https://bhanu-dev82.github.io">'
            '<font color="#1a365d"><u>bhanu-dev82.github.io</u></font></link>'
            "  |  Nagpur, India  |  Available to join immediately",
            st["contact"],
        )
    )

    story.append(section("Summary", st))
    story.append(
        Paragraph(
            "B.Tech CSE (CGPA 8.7) who ships production software and teaches by building. "
            "Created PyMaster, a live Python learning app with 1,200+ exercises. "
            "Hands-on with <b>Linux, Git, Docker, AWS, CI/CD</b>, and cloud releases. "
            "Ready to run project-based DevOps labs and join immediately.",
            st["body"],
        )
    )

    # Skills — only the trainer syllabus they named, plus what he can defend
    story.append(section("Technical Skills", st))
    story.append(
        skill_line(
            "Linux &amp; Git",
            "Linux, Bash, SSH, Git, GitHub, branching, pull requests, code review",
            st,
        )
    )
    story.append(
        skill_line(
            "Docker",
            "Images, containers, Dockerfile, Docker Compose, volumes, container logs",
            st,
        )
    )
    story.append(
        skill_line(
            "AWS",
            "EC2, S3, IAM (users, roles, policies), Security Groups, basic VPC",
            st,
        )
    )
    story.append(
        skill_line(
            "CI/CD &amp; Cloud",
            "GitHub Actions, multi-env builds (dev / staging / prod), "
            "Google Cloud Platform, Firebase, production crash monitoring",
            st,
        )
    )
    story.append(
        skill_line(
            "Languages",
            "Python, Java, SQL, JavaScript, Bash",
            st,
        )
    )

    # Experience
    story.append(section("Professional Experience", st))

    story.append(
        row2(
            "Devanshu Studios — Founder &amp; Lead Engineer",
            "Aug 2025 – Present",
            st["job_left"],
            st["job_right"],
        )
    )
    story.append(
        row2("Independent", "Remote", st["meta_left"], st["meta_right"])
    )
    story.append(
        bullet(
            "Owned the full release path for <b>PyMaster</b> (Google Play): Git workflows, CI/CD, "
            "multi-environment builds (dev/staging/prod), crash monitoring, and production publishing.",
            st,
        )
    )
    story.append(
        bullet(
            "Designed a <b>1,200+ exercise Python curriculum</b> with an AI tutor — labs, examples, "
            "and debugging steps for learners. Cloud services (Firebase / GCP) at 99.5% crash-free sessions.",
            st,
        )
    )

    story.append(Spacer(1, 3.5))
    story.append(
        row2(
            "Athabasca University — Globalink Research Intern (Mitacs)",
            "Apr 2024 – Oct 2024",
            st["job_left"],
            st["job_right"],
        )
    )
    story.append(
        row2("Machine Learning &amp; Software Development", "Edmonton, AB, Canada", st["meta_left"], st["meta_right"])
    )
    story.append(
        bullet(
            "Built a text classifier (BERT, 95% accuracy) and <b>deployed it as a REST web service</b> "
            "for researchers; presented at the TRESL Lab International Symposium, Canada.",
            st,
        )
    )
    story.append(
        bullet(
            "Sole developer of a cross-platform field-trip app (iOS / Android / Web) with a Firebase backend.",
            st,
        )
    )

    story.append(Spacer(1, 3.5))
    story.append(
        row2(
            "BETIC-GHRCE — Software Developer Intern",
            "Oct 2022 – May 2024",
            st["job_left"],
            st["job_right"],
        )
    )
    story.append(row2("Production diagnostic software", "Nagpur, India", st["meta_left"], st["meta_right"]))
    story.append(
        bullet(
            "Shipped a production Java/Kotlin diagnostic app — 60% accuracy gain; contributed to a "
            "<b>granted Indian patent</b> (Pub. No. 202321022476).",
            st,
        )
    )
    story.append(
        bullet(
            "Trained primary healthcare workers to operate the device — live demos, hands-on classroom instruction.",
            st,
        )
    )

    # Projects
    story.append(section("Key Projects", st))
    story.append(
        row2(
            "PyMaster — Learn Python  |  Git, CI/CD, Firebase / GCP, Python",
            "2025 – Present",
            st["proj"],
            st["job_right"],
        )
    )
    story.append(
        bullet(
            "Live on Google Play. 1,200+ exercises, AI tutor, 50k+ LOC, full release pipeline "
            "and production crash monitoring.",
            st,
        )
    )
    story.append(Spacer(1, 2))
    story.append(
        row2(
            "V-Safe-Anywhere — IoT + Cloud  |  Google Cloud, Firebase, Linux / IoT",
            "2022 – 2024",
            st["proj"],
            st["job_right"],
        )
    )
    story.append(
        bullet(
            "IoT wearable + app: panic button triggers real-time GPS broadcast. "
            "<b>98% uptime</b>. Published by IGI Global.",
            st,
        )
    )
    story.append(Spacer(1, 2))
    story.append(
        row2(
            "Wikimedia Foundation — Scribe-Android (Open Source)  |  Git, GitHub, Kotlin",
            "Feb 2025 – Present",
            st["proj"],
            st["job_right"],
        )
    )
    story.append(
        bullet(
            "Tablet keyboard layouts for 7+ languages. Git branching, pull requests, and code review "
            "on a production open-source repo.",
            st,
        )
    )

    # Teaching
    story.append(section("Teaching &amp; Mentoring", st))
    story.append(
        bullet(
            "PyMaster: beginner-to-project Python path (1,200+ labs) — explain, demo, then let the learner try.",
            st,
        )
    )
    story.append(
        bullet(
            "Awareness camps: educated 1,000+ people; trained rural healthcare workers on a diagnostic device.",
            st,
        )
    )
    story.append(
        bullet(
            "Student Nominee, Board of Studies, GHRCE (2022–2024). Talks: TRESL Lab Symposium (Canada); "
            "ACM ICACS 2024 (Hong Kong). Medium: production postmortems for engineers.",
            st,
        )
    )

    # Education
    story.append(section("Education", st))
    story.append(
        row2(
            "G H Raisoni College of Engineering",
            "Dec 2021 – Jun 2025",
            st["job_left"],
            st["job_right"],
        )
    )
    story.append(
        row2(
            "B.Tech in Computer Science &amp; Engineering  |  CGPA: 8.7 / 10.0",
            "Nagpur, India",
            st["meta_left"],
            st["meta_right"],
        )
    )
    story.append(
        Paragraph(
            "Coursework: Operating Systems, Computer Networks, DBMS, OOP, Data Structures &amp; Algorithms",
            st["body"],
        )
    )

    # Achievements
    story.append(section("Achievements", st))
    story.append(
        Paragraph(
            "<b>Granted patent</b> (TMJ Screening Tool, India)  |  "
            "<b>ACM</b> + <b>IGI Global</b> publications  |  "
            "<b>Mitacs Globalink</b> intern  |  "
            "BIRAC E-YUVA Rs. 10L  |  Wikimedia OSS",
            st["body"],
        )
    )

    doc = SimpleDocTemplate(
        OUT,
        pagesize=letter,
        leftMargin=LEFT,
        rightMargin=RIGHT,
        topMargin=TOP,
        bottomMargin=BOTTOM,
        title="Bhanu Nagpure — DevOps Faculty",
        author="Bhanu Nagpure",
        subject="Resume — DevOps Faculty, Mentorizee Private Limited",
    )
    doc.build(story)
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
