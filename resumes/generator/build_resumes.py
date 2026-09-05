#!/usr/bin/env python3
"""Role-specialised, ATS-friendly one-page resumes for Bhanu Nagpure.

Generates a clean, single-column PDF per target role from one shared
data model so each variant stays in sync. Reuses the ReportLab styling
approach of resumes/devops/build_resume.py.

Roles: SDE / Backend, Android, Flutter, ML/AI Engineer, DevOps.
"""

import os

from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.normpath(os.path.join(HERE, ".."))

PAGE_W, PAGE_H = letter
LEFT = RIGHT = 0.5 * inch
TOP = 0.3 * inch
BOTTOM = 0.2 * inch
CONTENT_W = PAGE_W - LEFT - RIGHT


# ---------------------------------------------------------------- data ----

CONTACT = (
    "+91 982-210-7989  |  bhanunagpure453@gmail.com  |  "
    "linkedin.com/in/bhanunagpure  |  github.com/bhanu-dev82"
)
CONTACT2 = "bhanu-dev82.github.io  |  Nagpur, India  |  Open to on-site / remote / hybrid"

EDUCATION = {
    "school": "G H Raisoni College of Engineering",
    "dates": "Dec 2021 - Jun 2025",
    "degree": "B.Tech in Computer Science & Engineering  |  CGPA: 8.7 / 10.0",
    "place": "Nagpur, India",
    "coursework": "Operating Systems, Computer Networks, DBMS, OOP, Data Structures &amp; Algorithms",
}

PUBLICATIONS = [
    (
        "<b>Journal:</b> \"V-Safe-Anywhere: Empowering Women's Safety with Wearable AI and IoT.\" "
        "<i>IGI Global</i>, Mar 2024.",
        "https://www.igi-global.com/chapter/v-safe-anywhere/342150",
    ),
    (
        "<b>Conference:</b> \"Autonomous Floating Garbage Collection Device using Computer Vision and "
        "Robotics.\" <i>8th ICACS 2024, ACM</i>, Hong Kong, Oct 2024.",
        "https://dl.acm.org/doi/10.1145/3693939.3693957",
    ),
    (
        "<b>Conference:</b> \"Development of a Mobile Field Trip Application.\" <i>3rd Annual TRESL Lab "
        "International Symposium</i>, Athabasca, Canada, Jul 2024.",
        None,
    ),
]

PATENTS = [
    "<b>Patent (Granted):</b> \"Smart Chairside TMJ Examination &amp; Muscle Activity Detector Tool,\" India (Pub. No. 202321022476).",
    "<b>Patent (Pending):</b> \"AI-Based Portable Device for Dental Disease Detection,\" DPIIT, India (App. No. 202421006731, Published Aug 2025).",
]

AWARDS = [
    ("3rd Place", "Avishkar 2024"),
    ("Runner-up", "DIPEX 2023 &amp; SHRISTI 2023"),
    ("BIREC E-YUVA Grant", "Rs. 10 lakh seed funding"),
    ("Winner", "MEDHA 2022 &amp; MEDIC-2022"),
]


def link(text, url):
    if not url:
        return text
    return (
        f'<link href="{url}"><font color="#1a365d"><u>{text}</u></font></link>'
    )


ROLES = {}


def role(key, **kw):
    ROLES[key] = kw


role(
    "sde",
    accent=HexColor("#1a365d"),
    fileslug="Bhanu_Nagpure_SDE",
    plausible_targets="Software Engineer / Backend / SDE-I",
    headline="Software Engineer",
    summary=(
        "Software engineer (B.Tech CSE, CGPA 8.7) who owns the whole product lifecycle - architecture, "
        "backend, and shipping. Shipped <b>3 apps to Google Play (2 live, 1 in closed testing)</b> with offline-first sync, "
        "event-driven async engines, REST/Firebase backends and CI/CD pipelines. Globalink intern "
        "(Mitacs, Canada); <b>IGI Global</b> and <b>ACM</b> publications; <b>granted patent</b>; Wikimedia OSS."
    ),
    skills=[
        ("Languages", "Java (primary), Python, Kotlin, C++, SQL, JavaScript"),
        ("Data Structures &amp; Algorithms", "Arrays, Linked Lists, Trees, Graphs, Hash Maps, Heaps, Dynamic Programming, Sorting &amp; Searching, complexity analysis"),
        ("Backend &amp; Systems", "REST APIs, Firebase (Firestore, Auth, Storage, Crashlytics), SQL &amp; NoSQL, asynchronous pipelines, offline-first sync, event-driven architecture"),
        ("Concurrency &amp; Architecture", "Java threading, Kotlin Coroutines &amp; Flow, WorkManager; Clean Architecture, MVVM/MVI, SOLID, Hilt, Repository pattern"),
        ("DevOps &amp; Cloud", "Git, GitHub Actions CI/CD, Gradle, Google Cloud Platform, Firebase, Docker, Linux"),
    ],
    experience=[
        {
            "title": "Devanshu Studios - Founder &amp; Software Engineer",
            "dates": "Aug 2025 - Present",
            "org": "Independent",
            "place": "Remote",
            "bullets": [
                "Took complete ownership of building and shipping <b>PyMaster</b> (Play Store): 50k+ LOC production platform, <b>Clean Architecture</b>, multi-env build system (dev/staging/prod), Riverpod 2.0 and a Gemini AI tutor - <b>99.5% crash-free sessions</b>; designed unit-testable data / domain / presentation layers with Repository + Hilt DI, Proto DataStore and EncryptedSharedPreferences.",
                "Engineered an <b>offline-first async sync engine</b>: event queue persists user progress locally and batch-uploads to Firebase on reconnect - <b>zero data loss</b> under intermittent connectivity with deterministic conflict resolution.",
                "Owned the full <b>production lifecycle</b>: CI/CD pipeline, Play Console publishing, A/B testing, Crashlytics incident response, RevenueCat billing (subscriptions + IAP) and AdMob native-ad mediation; shipped <b>Chakuli</b> (live: Gemma 4, Qwen3.5, Phi, SmolLM on a dual <b>LiteRT + GGUF</b> runtime) and led <b>Keepary</b> through Play closed testing (on-device ML Kit OCR, RevenueCat Pro).",
            ],
        },
        {
            "title": "Athabasca University - Globalink Research Intern (Mitacs)",
            "dates": "Apr 2024 - Oct 2024",
            "org": "Machine Learning &amp; Software Development",
            "place": "Edmonton, AB, Canada",
            "bullets": [
                "Built a text-ideology classifier in Java/Python using <b>BERT/Transformers</b> reaching <b>95% prediction accuracy</b>; deployed as a REST-backed web service for researcher validation.",
                "Sole developer of a cross-platform (iOS, Android, Web) field-trip app - Firebase Auth/Storage backend, OpenStreetMaps integration; presented at the <b>TRESL Lab International Symposium</b>, Canada (Jul 2024).",
            ],
        },
        {
            "title": "BETIC-GHRCE - Software Developer Intern",
            "dates": "Oct 2022 - May 2024",
            "org": "",
            "place": "Nagpur, India",
            "bullets": [
                "Built a production Java/Kotlin diagnostic app with MediaPipe FaceMesh - <b>60%</b> accuracy improvement and <b>30%</b> inference speedup via camera-pipeline optimisation; contributed to a <b>granted Indian patent</b> (TMJ Screening Tool).",
            ],
        },
        {
            "title": "Wikimedia Foundation - Open Source Contributor",
            "dates": "Feb 2025 - Present",
            "org": "Scribe-Android (Kotlin)",
            "place": "Remote",
            "bullets": [
                "Implemented tablet keyboard layouts for 7+ languages; refactored the core <b>KeyHandler</b> module to reduce coupling and improve testability; resolved critical UI bugs.",
            ],
        },
    ],
    projects=[
        {
            "title": "PyMaster - Learn Python",
            "stack": "Dart, Kotlin, Firebase, Riverpod 2.0, Gemini AI, RevenueCat",
            "dates": "2025 - Present",
            "bullets": [
                "<b>Live on Google Play.</b> 1,200+ exercises, gamified leagues, Gemini AI tutor and offline-first sync - 50k+ LOC at 99.5% crash-free. Multi-env Flavors, RevenueCat IAP, AdMob mediation.",
            ],
        },
        {
            "title": "Chakuli - Offline AI Chatbot",
            "stack": "Kotlin, LiteRT-LM + GGUF, Jetpack Compose, WorkManager, Proto DataStore",
            "dates": "2025 - Present",
            "bullets": [
                "<b>Live on Google Play.</b> Runs Gemma 4, Qwen3.5, Phi 3.5 Mini and SmolLM entirely on-device on a dual LiteRT + GGUF runtime - zero cloud inference. Compose UI, Hilt DI, CameraX, Agent Skills, encrypted key storage.",
            ],
        },
        {
            "title": "Rote Playoffs - Agent Procedure Benchmark (WeMakeDevs x Modiqo)",
            "stack": "Python, Rote CLI, controlled A/B benchmarking, deterministic grading",
            "dates": "Sep 2026",
            "bullets": [
                "Shipped <b>38 agent procedures</b> (all 1.00, top-5 of 123 makers); measured procedure reuse in a controlled study: <b>9.9x faster</b>, <b>15.3x fewer output tokens</b>, replicated across 6 tasks with frozen ground truth.",
            ],
        },
    ],
)

role(
    "android",
    accent=HexColor("#0a7d3d"),
    fileslug="Bhanu_Nagpure_Android",
    plausible_targets="Android Developer / Mobile Developer",
    headline="Android Developer",
    summary=(
        "Android engineer with <b>2+ years</b> building and shipping production apps on Google Play. Deep "
        "expertise in <b>Kotlin, Jetpack Compose, and the Android SDK</b>, with a proven track record across "
        "<b>on-device AI</b> (LiteRT-LM, Gemma/Phi), custom camera pipelines (CameraX), MVVM + Hilt "
        "architecture, WorkManager and Play Store publishing. International research intern (Mitacs, Canada)."
    ),
    skills=[
        ("Languages &amp; UI", "Kotlin, Java, SQL; Jetpack Compose (Material 3), custom layouts, Material Design"),
        ("Architecture", "MVVM/MVI, Clean Architecture, Hilt (DI), Repository pattern, SOLID"),
        ("Concurrency &amp; Persistence", "Coroutines &amp; Flow, WorkManager, Room, Proto DataStore, EncryptedSharedPreferences, Retrofit, REST APIs"),
        ("On-Device AI", "Dual runtime (LiteRT-LM + GGUF), Gemma 4, Qwen3.5, Phi 3.5 Mini, MediaPipe FaceMesh, Google ML Kit"),
        ("Firebase &amp; Monetisation", "Firebase (Auth, Firestore, Storage, Crashlytics), RevenueCat (IAP), Google AdMob mediation"),
        ("Tools", "Git, Gradle (Kotlin DSL), Android Studio, CI/CD, Google Cloud Platform, Linux"),
    ],
    experience=[
        {
            "title": "Devanshu Studios - Founder &amp; Lead Android Engineer",
            "dates": "Aug 2025 - Present",
            "org": "Independent",
            "place": "Remote",
            "bullets": [
                "Shipped <b>Chakuli - Offline AI Chatbot</b> (live on Google Play): a privacy-first Android assistant running <b>Gemma 4, Qwen3.5, Phi 3.5 Mini and SmolLM</b> entirely on-device via a dual <b>LiteRT + GGUF</b> runtime - zero cloud calls for AI inference; owned the full production lifecycle (CI/CD, Crashlytics, RevenueCat, AdMob mediation).",
                "Built the full <b>Jetpack Compose</b> (Material 3) UI, <b>Hilt</b> DI, <b>Proto DataStore</b>, <b>WorkManager</b> background model downloads, custom <b>CameraX</b> pipeline, Agent Skills system and encrypted key storage.",
                "Architected and shipped <b>PyMaster</b> - an Android/Flutter Python learning platform (50k+ LOC) with Gemini AI tutor, RevenueCat IAP and Firebase backend, live on Play Store.",
            ],
        },
        {
            "title": "BETIC-GHRCE - Software Developer Intern",
            "dates": "Oct 2022 - May 2024",
            "org": "",
            "place": "Nagpur, India",
            "bullets": [
                "Built an <b>Android (Kotlin/Java)</b> app for TMJ-disorder screening integrating <b>MediaPipe FaceMesh</b> and <b>Google ML Kit</b>, improving diagnostic classification accuracy by <b>60%</b>.",
                "Boosted camera performance by <b>30%</b> via optimised ML Kit integration enabling real-time facial landmark detection - contributed to a filed patent (Pub. No. 202321022476).",
            ],
        },
        {
            "title": "Wikimedia Foundation - Open Source Contributor",
            "dates": "Feb 2025 - Present",
            "org": "Scribe-Android (Kotlin)",
            "place": "Remote",
            "bullets": [
                "Developed tablet-specific keyboard layouts in <b>Kotlin</b> for 7+ languages; resolved UI bugs and refactored the core <b>KeyHandler</b> module for maintainability and test coverage.",
            ],
        },
    ],
    projects=[
        {
            "title": "Chakuli - Offline AI Chatbot",
            "stack": "Kotlin, Jetpack Compose, LiteRT + GGUF, Hilt, CameraX",
            "dates": "2025 - Present",
            "bullets": [
                "On-device Android AI assistant running <b>Gemma 4, Qwen3.5, Phi 3.5 Mini, SmolLM</b> via a dual <b>LiteRT + GGUF</b> runtime - no internet required for inference, full data privacy; Agent Skills system, encrypted storage, foreground WorkManager model downloads, Protobuf DataStore persistence.",
            ],
        },
        {
            "title": "OCanPredict - OSMF Screening App",
            "stack": "Kotlin, Java, MediaPipe FaceMesh, Firebase",
            "dates": "Dec 2022 - Jul 2023",
            "bullets": [
                "Android diagnostic app using <b>MediaPipe FaceMesh</b> for real-time OSMF screening, boosting efficiency by <b>40%</b>; won multiple national awards and contributed to a granted patent.",
            ],
        },
    ],
)

role(
    "flutter",
    accent=HexColor("#02569b"),
    fileslug="Bhanu_Nagpure_Flutter",
    plausible_targets="Flutter Developer / Cross-Platform Mobile Developer",
    headline="Flutter Developer",
    summary=(
        "Flutter engineer with <b>2+ years of end-to-end product experience</b>, having independently designed, "
        "built and shipped <b>3 apps (2 live, 1 in closed testing) to Google Play</b>. Expert in <b>Flutter, Dart, Riverpod 2.0 and Clean "
        "Architecture</b>, with deep cross-platform (iOS, Android, Web) experience and strong command of Firebase, "
        "RevenueCat and production-grade app architecture."
    ),
    skills=[
        ("Flutter &amp; Dart", "Flutter SDK, Dart, Riverpod 2.0, BLoC/Cubit, Clean Architecture, Flutter Flavors, go_router"),
        ("Cross-Platform", "iOS, Android, Web - single codebase; platform channels; native integrations"),
        ("Backend &amp; Data", "Firebase (Auth, Firestore, Storage, Crashlytics), REST APIs, OpenStreetMaps, Hive"),
        ("Monetisation &amp; AI", "RevenueCat (IAP/subscriptions), Google AdMob (mediation), Gemini LLM (on-device)"),
        ("Languages", "Dart, Kotlin, Python, Java, SQL"),
        ("Tools", "Git, GitHub, Android Studio, Xcode, Gradle (Kotlin DSL), CI/CD, Google Cloud Platform, Linux"),
    ],
    experience=[
        {
            "title": "Devanshu Studios - Founder &amp; Lead Flutter Engineer",
            "dates": "Aug 2025 - Present",
            "org": "Independent",
            "place": "Remote",
            "bullets": [
                "Architected and shipped <b>PyMaster</b> (Live on Play Store) - a <b>50k+ LOC Flutter</b> Python learning platform with Clean Architecture, <b>Riverpod 2.0</b> and Flutter Flavors for dev/staging/prod environments.",
                "Integrated <b>Gemini LLM</b> as a native AI tutor; built an <b>offline-first sync engine</b> (Riverpod + Hive) that batch-queues progress and uploads to Firebase on reconnect - zero data loss.",
                "Implemented the full <b>monetisation stack</b>: RevenueCat (subscriptions &amp; IAP), Google AdMob native-ad mediation, Firebase Google Sign-In - managing the entire lifecycle from code to Play Console.",
                "Shipped <b>Chakuli</b> (live on Play) - on-device AI chatbot, Gemma 4/Qwen3.5 on a dual LiteRT + GGUF runtime.",
                "Leading <b>Keepary</b> through Play closed testing - a Flutter scan-to-PDF scanner with on-device <b>ML Kit OCR</b>, local vault + search, compress-to-target-size, <b>RevenueCat Pro</b> and capped AdMob - no account, no cloud.",
            ],
        },
        {
            "title": "Athabasca University - Globalink Research Intern",
            "dates": "Apr 2024 - Aug 2024",
            "org": "Mitacs",
            "place": "Edmonton, AB, Canada",
            "bullets": [
                "Led end-to-end development of a <b>cross-platform (iOS, Android, Web)</b> field-trip app using <b>Flutter</b>, Firebase (Auth, Firestore, Storage) and <b>OpenStreetMaps</b>; presented at the <b>3rd Annual TRESL Lab Symposium</b>, Canada.",
            ],
        },
        {
            "title": "Wikimedia Foundation - Open Source Contributor",
            "dates": "Feb 2025 - Present",
            "org": "Scribe-Android (Kotlin)",
            "place": "Remote",
            "bullets": [
                "Developed tablet keyboard layouts (Kotlin) for 7+ languages; resolved UI bugs and refactored the KeyHandler module for maintainability and test coverage.",
            ],
        },
    ],
    projects=[
        {
            "title": "Keepary - Document Scanner (Closed Testing)",
            "stack": "Flutter, Riverpod, ML Kit OCR, RevenueCat, AdMob",
            "dates": "2026 - Present",
            "bullets": [
                "Scan-to-PDF with on-device OCR, local vault + search, merge/split/compress, ID-card mode and QR - <b>no account, no cloud</b>; Pro via RevenueCat (searchable PDF, encryption).",
            ],
        },
        {
            "title": "PyMaster - Learn Python Coding",
            "stack": "Flutter, Dart, Riverpod 2.0, Firebase, RevenueCat, Gemini AI",
            "dates": "2025 - Present",
            "bullets": [
                "Production Flutter app on Google Play: <b>1,200+ interactive exercises</b>, gamified league system and a <b>Gemini-powered AI Tutor</b> for context-aware debugging - <b>99.5% crash-free</b>.",
                "Full ownership: Clean Architecture, <b>Riverpod 2.0</b>, Flutter Flavors, CI/CD pipeline and Play Console publishing.",
            ],
        },
        {
            "title": "V-Safe-Anywhere: Women's Safety Wearable",
            "stack": "Flutter, Firebase, IoT, Google Cloud",
            "dates": "Nov 2022 - Apr 2024",
            "bullets": [
                "Flutter app paired with a custom IoT wearable: a panic button triggers <b>instant live GPS broadcast</b> to pre-saved contacts via Firebase - <b>98% uptime</b>. " + link("Published by IGI Global", "https://www.igi-global.com/chapter/v-safe-anywhere/342150") + ".",
            ],
        },
        {
            "title": "Mobile Field Trip Application",
            "stack": "Flutter, Firebase, OpenStreetMaps",
            "dates": "Apr 2024 - Aug 2024",
            "bullets": [
                "Cross-platform Flutter app (iOS, Android, Web) for academic field assignments; Firebase Auth &amp; Storage, OpenStreetMaps integration. Presented at the TRESL Lab Symposium, Canada.",
            ],
        },
    ],
)

role(
    "ml",
    accent=HexColor("#6b21a8"),
    fileslug="Bhanu_Nagpure_ML_Engineer",
    plausible_targets="Machine Learning / AI Engineer",
    headline="Machine Learning &amp; AI Engineer",
    summary=(
        "Machine-learning engineer with <b>international research experience</b> (Mitacs Globalink, Canada) and "
        "hands-on production AI: <b>95%-accuracy</b> text classification with BERT/Transformers, <b>on-device LLM "
        "inference</b> (LiteRT-LM, Gemma/Phi), and computer vision (MediaPipe, ML Kit, YOLOv5). Published in "
        "<b>IGI Global</b> and <b>ACM</b>; <b>2 patent applications (1 granted)</b>. Strong in Python, "
        "PyTorch/TensorFlow, and shipping AI into production mobile products."
    ),
    skills=[
        ("ML &amp; Deep Learning", "PyTorch, TensorFlow, HuggingFace Transformers, BERT, Scikit-learn, fine-tuning, evaluation (accuracy/precision/recall)"),
        ("NLP &amp; Generative AI", "Text classification, tokenization, Gemini API (Flash Lite), context-aware prompt/system design"),
        ("Computer Vision", "OpenCV, YOLOv5, MediaPipe FaceMesh, Google ML Kit, optimised inference pipelines"),
        ("On-Device AI", "Dual runtime (LiteRT-LM + GGUF), Gemma 4, Qwen3.5, Phi 3.5 Mini, SmolLM, offline inference"),
        ("Languages", "Python (research), Java, Kotlin, Dart, C++, SQL"),
        ("MLOps &amp; Deployment", "Flask/REST service deployment, Firebase, Git, CI/CD, model lifecycle"),
    ],
    experience=[
        {
            "title": "Devanshu Studios - Founder &amp; AI Engineer",
            "dates": "Aug 2025 - Present",
            "org": "Independent",
            "place": "Remote",
            "bullets": [
                "Built <b>Chakuli</b>, an on-device LLM chatbot running <b>Gemma 4, Qwen3.5, Phi 3.5 Mini and SmolLM</b> via a dual <b>LiteRT + GGUF</b> runtime - full AI inference offline, zero cloud calls, preserving user privacy.",
                "Designed a <b>mastery-based adaptive practice engine</b> that detects weak topics and generates focused AI sessions; integrated a <b>Gemini AI tutor</b> with per-track system prompts.",
            ],
        },
        {
            "title": "Athabasca University - ML Research Intern (Mitacs Globalink)",
            "dates": "Aug 2024 - Oct 2024",
            "org": "",
            "place": "Edmonton, AB, Canada",
            "bullets": [
                "Built a text-ideology classifier using <b>BERT/Transformers</b> in Java/Python reaching <b>95% prediction accuracy</b>; deployed as a <b>REST-backed web service</b> for researcher validation.",
            ],
        },
        {
            "title": "BETIC-GHRCE - ML &amp; Software Developer Intern",
            "dates": "Oct 2022 - May 2024",
            "org": "",
            "place": "Nagpur, India",
            "bullets": [
                "Applied <b>MediaPipe FaceMesh</b> + <b>Google ML Kit</b> to a medical diagnostic app, improving accuracy by <b>60%</b> and inference speed by <b>30%</b> through camera-pipeline optimisation.",
                "Contributed to a <b>granted patent</b> (TMJ Screening Tool, Pub. No. 202321022476) using the same on-device computer-vision stack.",
            ],
        },
        {
            "title": "IIT Bombay - Design for Health Fellow",
            "dates": "Mar 2022 - Oct 2022",
            "org": "",
            "place": "Mumbai, India",
            "bullets": [
                "Led a team prototyping a xerostomia diagnostic device, reducing assessment time by <b>80%</b>; software layer on IoT hardware, presented at IIT Bombay.",
            ],
        },
    ],
    projects=[
        {
            "title": "Rote Playoffs - Agent Procedure Benchmark",
            "stack": "Python, controlled A/B benchmarking, deterministic grading, telemetry",
            "dates": "Sep 2026",
            "bullets": [
                "Measured procedure reuse in agentic LLM workflows across 6 tasks: <b>9.9x faster</b>, <b>15.3x fewer output tokens</b>, 9.8/10 with-Play correctness; frozen ground truth, deterministic grader.",
            ],
        },
        {
            "title": "Chakuli - On-Device AI Chatbot",
            "stack": "LiteRT + GGUF, Gemma 4/Qwen3.5/Phi/SmolLM, Kotlin, Compose",
            "dates": "2025 - Present",
            "bullets": [
                "Offline AI assistant with zero-cloud LLM inference and an Agent Skills system; foreground WorkManager manages multi-GB model downloads with exponential backoff.",
            ],
        },
        {
            "title": "Text Ideology Classifier",
            "stack": "Python, Transformers/BERT, Java, Flask",
            "dates": "2024",
            "bullets": [
                "<b>95% prediction accuracy</b>; deployed as a REST web service for researcher validation at Athabasca University.",
            ],
        },
        {
            "title": "Autonomous Garbage Collection Robot",
            "stack": "Python, YOLOv5, OpenCV, IoT",
            "dates": "2023",
            "bullets": [
                "YOLOv5 computer-vision pipeline for autonomous waste detection - <b>60%</b> reduction in manual effort. " + link("Published at ACM ICACS 2024, Hong Kong", "https://dl.acm.org/doi/10.1145/3693939.3693957") + ".",
            ],
        },
    ],
)

role(
    "devops",
    accent=HexColor("#b36000"),
    fileslug="Bhanu_Nagpure_DevOps",
    plausible_targets="DevOps / Platform / Release Engineer",
    headline="DevOps &amp; Platform Engineer",
    summary=(
        "Production engineer who owns the path from code to release. Shipped <b>3 apps to Google Play (2 live, 1 in closed testing)</b> "
        "with a third in closed testing. Runs <b>multi-env build and release pipelines</b> (dev/staging/prod), <b>CI/CD</b>, cloud backends "
        "(Firebase / GCP) and crash monitoring. Hands-on with <b>Linux, Git, Docker, AWS and CI/CD</b>, with a "
        "B.Tech CSE (CGPA 8.7) and experience on production open-source (Wikimedia)."
    ),
    skills=[
        ("Linux &amp; Git", "Linux, Bash, SSH, Git/GitHub, branching, pull requests, code review"),
        ("Containers", "Docker, Dockerfile, Docker Compose, images, volumes, container logs"),
        ("Cloud (AWS)", "EC2, S3, IAM (users, roles, policies), Security Groups, basic VPC"),
        ("CI/CD &amp; Release", "GitHub Actions, multi-env builds (dev/staging/prod), Play Console release automation, Google Cloud Platform, Firebase"),
        ("Observability", "Firebase Crashlytics, Analytics, A/B testing, incident response"),
        ("Languages", "Python, Java, Kotlin, SQL, JavaScript, Bash"),
    ],
    experience=[
        {
            "title": "Devanshu Studios - Founder &amp; Software Engineer",
            "dates": "Aug 2025 - Present",
            "org": "Independent",
            "place": "Remote",
            "bullets": [
                "Set up the full <b>CI/CD</b> pipeline for PyMaster, Chakuli and Keepary - multi-env build system (dev/staging/prod) via Flutter Flavors and Gradle, automated Play Console releases, closed-testing track management and A/B testing.",
                "Run <b>production monitoring</b>: Firebase Crashlytics incident response, Analytics-driven decisions - sustained <b>99.5% crash-free</b> sessions.",
                "Built and operated cloud backends (Firebase / GCP) and an <b>offline-first sync engine</b> with deterministic conflict resolution for reliable data transfer.",
                "Integrated and operated the monetisation stack (RevenueCat, AdMob mediation) and model-download delivery for on-device AI.",
            ],
        },
        {
            "title": "Wikimedia Foundation - Open Source Contributor",
            "dates": "Feb 2025 - Present",
            "org": "Scribe-Android (Kotlin)",
            "place": "Remote",
            "bullets": [
                "Worked the full Git/GitHub workflow (branching, pull requests, code review) on a production open-source Android repo; refactored the KeyHandler module for testability.",
            ],
        },
        {
            "title": "Athabasca University - Globalink Research Intern (Mitacs)",
            "dates": "Apr 2024 - Oct 2024",
            "org": "",
            "place": "Edmonton, AB, Canada",
            "bullets": [
                "Deployed a <b>95%-accuracy</b> ML model as a <b>REST-backed web service</b> on Firebase for researcher validation; managed cloud Auth/Storage backend for a cross-platform field-trip app.",
            ],
        },
    ],
    projects=[
        {
            "title": "PyMaster - Production Release Pipeline",
            "stack": "GitHub Actions, Flutter Flavors, Firebase, Gradle",
            "dates": "2025 - Present",
            "bullets": [
                "Enabled <b>1-click reproducible builds</b> for dev/staging/prod with environment-collated configs, automated testing and controlled Play Store rollouts - <b>99.5% crash-free</b>.",
            ],
        },
        {
            "title": "V-Safe-Anywhere - Cloud &amp; IoT Backend",
            "stack": "Firebase, Google Cloud, IoT, Flutter",
            "dates": "2022 - 2024",
            "bullets": [
                "Operated a Firebase-backed live GPS broadcast system at <b>98% uptime</b>; " + link("published by IGI Global", "https://www.igi-global.com/chapter/v-safe-anywhere/342150") + ".",
            ],
        },
    ],
)

ROLE_ORDER = ["sde", "android", "flutter", "ml", "devops"]

# -------------------------------------------------------------- styling ----

def styles(accent, scale=1.0):
    s = {}
    s["name"] = ParagraphStyle(
        "name", fontName="Helvetica-Bold", fontSize=17, leading=19,
        alignment=TA_CENTER, textColor=HexColor("#111111"), spaceAfter=0,
    )
    s["headline"] = ParagraphStyle(
        "headline", fontName="Helvetica", fontSize=9.2, leading=11.5,
        alignment=TA_CENTER, textColor=accent, spaceBefore=1.5, spaceAfter=0.5,
    )
    s["contact"] = ParagraphStyle(
        "contact", fontName="Helvetica", fontSize=8.2, leading=10.4,
        alignment=TA_CENTER, textColor=HexColor("#333333"),
    )
    s["section"] = ParagraphStyle(
        "section", fontName="Helvetica-Bold", fontSize=9.9, leading=11.5,
        textColor=HexColor("#111111"), spaceBefore=3.0, spaceAfter=0,
    )
    s["body"] = ParagraphStyle(
        "body", fontName="Helvetica", fontSize=8.7, leading=10.3,
        textColor=black, alignment=TA_JUSTIFY,
    )
    s["bullet"] = ParagraphStyle(
        "bullet", fontName="Helvetica", fontSize=8.7, leading=10.3,
        textColor=black, leftIndent=10, firstLineIndent=-8, alignment=TA_JUSTIFY,
    )
    s["skill"] = ParagraphStyle(
        "skill", fontName="Helvetica", fontSize=8.6, leading=10.1,
        textColor=black, alignment=TA_JUSTIFY,
    )
    s["job_left"] = ParagraphStyle(
        "job_left", fontName="Helvetica-Bold", fontSize=9.3, leading=11, textColor=black,
    )
    s["job_right"] = ParagraphStyle(
        "job_right", fontName="Helvetica", fontSize=8.9, leading=11,
        alignment=TA_RIGHT, textColor=black,
    )
    s["meta_left"] = ParagraphStyle(
        "meta_left", fontName="Helvetica-Oblique", fontSize=8.5, leading=10,
        textColor=HexColor("#333333"),
    )
    s["meta_right"] = ParagraphStyle(
        "meta_right", fontName="Helvetica-Oblique", fontSize=8.5, leading=10,
        alignment=TA_RIGHT, textColor=HexColor("#333333"),
    )
    s["award"] = ParagraphStyle(
        "award", fontName="Helvetica", fontSize=8.6, leading=10.3,
        textColor=black, alignment=TA_JUSTIFY,
    )
    if scale != 1.0:
        for st in s.values():
            st.fontSize = max(6.3, st.fontSize * scale)
            st.leading = st.leading * scale
    return s


def section(title, r):
    return KeepTogether(
        [
            Paragraph(title.upper(), r["section"]),
            HRFlowable(width="100%", thickness=0.9, color=HexColor("#222222"),
                       spaceBefore=0, spaceAfter=2.5),
        ]
    )


def row2(left, right, ls, rs, col1=None):
    if col1 is None:
        col1 = CONTENT_W * 0.72
    t = Table([[Paragraph(left, ls), Paragraph(right, rs)]],
              colWidths=[col1, CONTENT_W - col1])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
    ]))
    return t


def bullet(text, r):
    return Paragraph(f"\u2022  {text}", r["bullet"])


def job_block(job, r):
    parts = [job["title"], job["dates"]]
    parts.append((" &middot; ".join(x for x in [job.get("org"), job.get("place")] if x) or ""))
    blocks = [row2(job["title"], job["dates"], r["job_left"], r["job_right"])]
    if job.get("org") or job.get("place"):
        meta = " &middot; ".join(x for x in [job.get("org"), job.get("place")] if x)
        blocks.append(row2(meta, "", r["meta_left"], r["meta_right"]))
    blocks.append(Spacer(1, 1))
    return KeepTogether([blocks[0]] + (blocks[1:-1] if len(blocks) > 2 else blocks[1:])
                        + [bullet(b, r) for b in job["bullets"]] + [Spacer(1, 2)])


def build_one(data, out_pdf, scale=1.0):
    accent = data["accent"]
    r = styles(accent, scale)
    story = []

    # Header
    story.append(Paragraph("BHANU NAGPURE", r["name"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph(data["headline"], r["headline"]))
    story.append(Spacer(1, 1))
    story.append(Paragraph(CONTACT, r["contact"]))
    story.append(Paragraph(CONTACT2, r["contact"]))

    # Summary
    story.append(section("Summary", r))
    story.append(Paragraph(data["summary"], r["body"]))

    # Skills
    story.append(section("Technical Skills", r))
    for label, rest in data["skills"]:
        story.append(Paragraph(f"<b>{label}:</b> {rest}", r["skill"]))

    # Experience
    story.append(section("Professional Experience", r))
    for job in data["experience"]:
        story.append(job_block(job, r))

    # Projects
    story.append(section("Key Projects", r))
    for p in data["projects"]:
        story.append(row2(f"<b>{p['title']}</b> &nbsp;|&nbsp; {p['stack']}", p["dates"],
                          r["job_left"], r["job_right"]))
        for b in p["bullets"]:
            story.append(bullet(b, r))
        story.append(Spacer(1, 2))

    # Education
    story.append(section("Education", r))
    story.append(row2(EDUCATION["school"], EDUCATION["dates"],
                      r["job_left"], r["job_right"]))
    story.append(row2(EDUCATION["degree"], EDUCATION["place"],
                      r["meta_left"], r["meta_right"]))
    story.append(Paragraph(EDUCATION["coursework"], r["body"]))

    # Publications, Patents & Awards
    story.append(section("Publications, Patents &amp; Awards", r))
    for text, url in PUBLICATIONS:
        story.append(bullet(link(text, url), r))
    story.append(bullet("; ".join(PATENTS), r))
    story.append(bullet(
        "<b>Awards:</b> " + " &nbsp;|&nbsp; ".join(
            f"{name} &middot; {cat}" for name, cat in AWARDS), r))

    doc = SimpleDocTemplate(
        out_pdf, pagesize=letter, leftMargin=LEFT, rightMargin=RIGHT,
        topMargin=TOP, bottomMargin=BOTTOM,
        title=f"Bhanu Nagpure - {data['headline']}" + " - Resume",
        author="Bhanu Nagpure",
        subject=f"Resume - {data['plausible_targets']}",
    )
    doc.build(story)
    print(f"Wrote {out_pdf} (scale {scale:.2f}, {doc.page} page)")
    return doc


def main():
    for key in ROLE_ORDER:
        data = ROLES[key]
        folder = os.path.join(OUT_DIR, key)
        os.makedirs(folder, exist_ok=True)
        out = os.path.join(folder, data["fileslug"] + ".pdf")
        for scale in (1.0, 0.97, 0.94, 0.91, 0.88, 0.85):
            doc = build_one(data, out, scale)
            if doc.page <= 1:
                break


if __name__ == "__main__":
    main()
