# Mentorizee DevOps faculty interview — 1-hour pack

**Read this file. That is enough.**  
Interview with **Mohit Bhaskar Urkunde**, CEO, Mentorizee Pvt Ltd (Pune).  
Role: **DevOps teacher**. They care if you can **explain**, not if you ran Netflix-scale AWS.

**If they say “explain any topic for 10 minutes” → choose Docker.**

---

## Use your 60 minutes like this

| Time | Do this |
|------|---------|
| 0–20 min | Read **section A** out loud twice (the 10-min talk) |
| 20–40 min | Read **section C** (Q&A). Say answers out loud |
| 40–50 min | Skim **section B** backups (AWS / Git / Linux) in case they pick the topic |
| 50–60 min | Read **section D** (join / Pune / why teaching) |

Do **not** study Kubernetes, Jenkins, Terraform, Ansible.

Honest line if they go deeper than the resume:

> “My shipped products run on GCP and Firebase. For this course I teach the same ideas on Docker and AWS — with labs students can repeat.”

---

# A. 10-minute teaching demo — Docker

This is your main weapon. Speak slowly. Draw while you talk. Pause after each block.

## What you say at the start (10 seconds)

> “I’ll take **Docker** — it’s the first real DevOps lab I would run with students. I’ll explain the problem, the idea, a small demo, and a lab I’d give them.”

Then start. Do **not** ask “is Docker okay?” unless they already assigned a topic.

---

## Minute 0–1  ·  Hook (the problem)

> “Every student hits this: **it works on my machine.**
>
> On my laptop the app runs. On the college PC it crashes. Python 3.10 vs 3.12. A library missing. Windows vs Linux.
>
> The app is not wrong. The **environment** is different.
>
> DevOps is about making ‘run the app’ **repeatable**. Docker is how we pack the app **and** its environment together.”

**Draw this:**

```
Student laptop          College PC           Server
 Python 3.12              Python 3.10          no Python
 flask installed          flask missing        Ubuntu
   APP RUNS                APP CRASHES          ???
```

---

## Minute 1–3  ·  VM vs container (draw boxes)

> “Old solution: a **virtual machine**. Full guest operating system inside your computer. Heavy. Slow to start. 4–8 GB RAM for one app.
>
> Docker uses a **container**. Not a full OS. It shares the host’s **kernel**. It only packs the app + libraries it needs.
>
> Same isolation idea. Much lighter. Starts in seconds. That’s why we teach Docker before cloud.”

**Draw this:**

```
VIRTUAL MACHINE                    CONTAINER (Docker)

+------------------+               +------------------+
| App              |               | App              |
| Libraries        |               | Libraries        |
| Guest OS         |               +------------------+
+------------------+               | Host OS + kernel |
| Host OS          |               +------------------+
+------------------+
   heavy, slow                        light, fast
```

Say this sentence clearly (they will remember it):

> “A VM virtualises **hardware**. A container virtualises the **process**. That’s why containers are small and start fast.”

---

## Minute 3–5  ·  Image vs container (the analogy)

> “Two words students mix up. I never let that slide.
>
> **Image** = the recipe. Read-only snapshot. Class in Java. Blueprint.
>
> **Container** = a running copy of that image. Object. The cooked meal.
>
> One image → many containers. That’s how we scale later on AWS.”

**Draw this:**

```
  IMAGE (recipe)          docker run
  python:3.11             --------->   CONTAINER 1  (running)
  + my app.py                          CONTAINER 2  (running)
                                       CONTAINER 3  (stopped)
```

Commands (write them on the board):

```bash
docker pull python:3.11          # get an image
docker images                    # list images
docker run -d --name web python:3.11   # start a container
docker ps                        # running containers
docker ps -a                     # all, including stopped
docker stop web
docker rm web
docker rmi python:3.11           # delete image
```

---

## Minute 5–8  ·  Dockerfile (this is the “wow” part)

> “We don’t click buttons. We write a file called **Dockerfile**. It’s the recipe. Same file on every student’s laptop. That’s the point of DevOps: **the environment is code.**”

Write this slowly, line by line. Explain each line as you write it.

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

| Line | What you say |
|------|----------------|
| `FROM` | Base image. Don’t start from empty. Start from Python already installed. `-slim` = smaller. |
| `WORKDIR` | `cd /app` inside the container. |
| `COPY requirements.txt` | Copy **only** the dependency file first. |
| `RUN pip install` | Install packages **when we build**. Not when the student runs. |
| `COPY . .` | Now copy the app code. |
| `EXPOSE 8000` | Documentation: this app listens on 8000. Does not publish by itself. |
| `CMD` | Default command when the container starts. |

Then the two commands that matter:

```bash
docker build -t myapp:1.0 .
docker run -d -p 8000:8000 --name api myapp:1.0
```

**Draw the port mapping:**

```
Browser  -->  localhost:8000  -->  container port 8000
                 (host)                (app)
```

> “`-p 8000:8000` means: host port → container port. Students forget this and think the app is dead. It’s running, they just didn’t publish the port.”

**Layers (10 seconds, impresses the interviewer):**

> “Each instruction is a **layer**. If only `app.py` changes, Docker reuses the `pip install` layer. That’s why we copy `requirements.txt` **before** the full code. Fast rebuilds. I teach this on day 1 so they don’t write slow Dockerfiles.”

---

## Minute 8–9  ·  Compose + where it sits in DevOps

> “Real apps are not one container. Web + database.
>
> **Docker Compose** is a YAML file that starts both with one command: `docker compose up`.
>
> I don’t teach Kubernetes first. Kubernetes is an orchestra. Docker is one instrument. Students must hear one instrument first.”

Tiny compose (don’t write the whole file unless asked):

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
```

Where it fits:

```
Git  →  Docker build  →  run container  →  same image on AWS EC2
 code     package            test locally      production
```

> “That’s CI/CD later. GitHub Actions can run `docker build` on every push. Same image I ran on my laptop, I put on EC2.”

---

## Minute 9–10  ·  Recap + the lab + stop

> “Three sentences to remember:
>
> 1. Docker packs the **app and its environment**.
> 2. **Image** is the recipe. **Container** is the running copy.
> 3. **Dockerfile** makes the environment code — so it is repeatable.
>
> **Lab I would give after this talk (30 minutes):**
> Take a 20-line Flask or Python HTTP app. Write a Dockerfile. Build. Run with `-p`. Hit it in the browser. Then change one line of code, rebuild, and see the layer cache.
>
> That’s how I teach: explain, demo, then they do it. Questions?”

**Then shut up.** Smile. Let them ask.

---

## If they interrupt / ask during the 10 minutes

| They say | You say |
|----------|---------|
| “What is a volume?” | “Container filesystem dies when the container is removed. A volume is a folder on the host that survives. Databases need volumes.” |
| “What is Docker Hub?” | “App Store for images. `python:3.11` comes from there. Like Play Store, but for environments.” |
| “Difference COPY vs ADD?” | “I teach COPY. ADD can unpack tars and fetch URLs. Extra magic confuses beginners.” |
| “CMD vs ENTRYPOINT?” | “CMD = default command, easy to override. ENTRYPOINT = the main program. Day-2 topic.” |
| “Is this production?” | “This is the teaching core. Production adds health checks, non-root user, small images, CI. I add those in week 2.” |

---

## Whiteboard checklist (draw these 4 things)

1. Three machines / three environments (the problem)
2. VM box vs container box
3. Image → `docker run` → containers
4. `-p host:container` arrow

If you draw only those four, the 10 minutes looks like a class, not a speech.

---

# B. Backup 10-minute talks (if they pick the topic)

Only one of these. Don’t prepare all perfectly. Skim.

---

## If they say AWS (10 min)

**Title:** “AWS for a first DevOps batch — four services, one story.”

Story: *Student has a Python app. Put it on the internet.*

| Minute | Say |
|--------|-----|
| 0–1 | Cloud = rent computers, don’t buy a server. Pay for what you use. |
| 1–3 | **EC2** = a virtual computer. Ubuntu in a data centre. You SSH in. This is where Docker will run. |
| 3–5 | **S3** = unlimited folders for files. Images, backups, static websites. Not a computer. Don’t run apps on S3. |
| 5–7 | **IAM** = who is allowed to do what. User = human. Role = a service. Policy = the permission JSON. **Never use the root account daily.** |
| 7–9 | **Security Group** = firewall for EC2. Allow 22 (SSH) from my IP. Allow 80/443 from the world. Deny everything else. |
| 9–10 | Lab: launch EC2 → SSH → install Docker → run the same container from the Docker class → open port 80. Recap: compute, storage, identity, firewall. |

Draw:

```
You --SSH:22-->  EC2 (Ubuntu + Docker + app:80)
                      |
                     IAM role
                      |
                     S3 (photos, backups)
```

Map from **your** work (honest):

> “PyMaster uses Firebase Auth and Storage. Same two ideas: IAM is Auth, S3 is Storage. EC2 is ‘run the server’. I teach AWS because that’s the industry syllabus. The ideas are the same on GCP.”

Do **not** invent EKS, Lambda, Terraform stories.

---

## If they say Git (10 min)

1. Why: history + teamwork. Without Git, “final_final_v3.zip”.
2. Three places: working folder → staging (`git add`) → commit (`git commit`) → remote (`git push`).
3. Branch = safe copy of the work. Main stays clean.
4. Pull request = “please review, then merge.” This is how Wikimedia works — **your real story**.
5. Lab: init, add, commit, branch, PR on GitHub.

---

## If they say Linux (10 min)

1. Server OS is Linux. AWS EC2 Ubuntu. Docker host is Linux. Must teach it first.
2. Everything is a file. `ls -l` shows permissions `rwx` for user/group/other.
3. Commands: `pwd cd ls cat grep chmod ps top df`.
4. SSH is how you enter EC2.
5. Lab: break a permission (`chmod 000 file`), watch it fail, fix to `644`.

---

## If they say CI/CD (10 min)

1. CI = every push, the machine builds/tests. Not “it works on my laptop”.
2. CD = after green build, release to staging, then prod.
3. GitHub Actions: a YAML file in `.github/workflows/`. `on: push` → jobs → steps.
4. Your story: PyMaster **dev / staging / prod** builds, then Play Store, then Crashlytics.
5. Next step in a DevOps course: Action runs `docker build` and pushes the image.

---

# C. Common interview questions

Say answers **out loud** once. Short. Then stop.

---

## C1. DevOps basics

**What is DevOps?**  
“A way of working: build, test, release, run, and watch in one loop. Developers and ops are not two teams throwing code over a wall. For students: Git + Linux + Docker + AWS + CI/CD is that loop.”

**CI vs CD?**  
“CI — integrate and test on every push. CD — deliver that green build to staging/production. CI is the exam. CD is publishing the result.”

**Why Docker in DevOps?**  
“It makes the environment identical on laptop, lab, and server. CI can build an image. Production runs the same image.”

**What is a pipeline?**  
“A sequence: test → build image → deploy. Automated. No ‘please run it on your PC’.”

**Monolithic vs microservices? (only if asked)**  
“Monolith = one app, one deploy. Microservices = many small services. I start students with one container. Microservices later. Docker Compose is the bridge.”

---

## C2. Docker questions (very likely after your talk)

**Image vs container?**  
“Image is the snapshot/recipe. Container is a running instance of that image.”

**Container vs VM?**  
“VM has a guest OS. Container shares the host kernel. Containers start faster and use less RAM.”

**What happens on `docker run`?**  
“Docker creates a writable layer on top of the image, connects networking, maps ports if you asked, and starts the process in `CMD`.”

**Why `COPY requirements.txt` before `COPY . .`?**  
“Layer cache. Dependencies change less than code. Rebuilds stay fast.”

**CMD vs RUN?**  
“`RUN` happens at **build** time (pip install). `CMD` happens at **start** time (python app.py).”

**What is Docker Compose?**  
“A YAML file to run more than one container together. Web + DB. One command: `docker compose up`.”

**What is a volume?**  
“Persistent disk for a container. Without it, database data dies when the container is removed.”

**How do you see logs?**  
“`docker logs container_name`. Students debug with this before they change code.”

**How do you enter a running container?**  
“`docker exec -it name bash`.”

**Is Docker the same as Kubernetes?**  
“No. Docker runs containers on one machine. Kubernetes schedules containers across many machines. I teach Docker first.”

**Name some Dockerfile instructions.**  
`FROM, WORKDIR, COPY, RUN, EXPOSE, CMD, ENV, USER`

**What is a tag?**  
“A label on an image: `myapp:1.0`. `latest` is just a name. I teach students to use versions, not only `latest`.”

---

## C3. AWS questions

**What is EC2?**  
“Elastic Compute Cloud. A virtual computer. You pick CPU, RAM, disk, OS. SSH in. Run Docker there.”

**What is S3?**  
“Object storage. Files, not a filesystem you `cd` into. Good for backups, images, static sites. Not for running programs.”

**EC2 vs S3?**  
“EC2 is compute. S3 is storage. Don’t mix them.”

**What is IAM?**  
“Identity and Access Management. Users, groups, roles, policies. Least privilege: give only what is needed.”

**User vs role?**  
“User is a person with a password or access keys. Role is assumed by a service — for example EC2 reading S3 — with temporary credentials. Better than putting keys in code.”

**What is a Security Group?**  
“Virtual firewall on EC2. Allow/deny ports. Stateful. I teach: SSH 22 from my IP only, HTTP 80 from anywhere.”

**What is a VPC?**  
“Your private network in AWS. Public subnet has a route to the internet. Private subnet does not. Beginners start in the default VPC, then I explain why we make our own.”

**What is an AMI?**  
“Amazon Machine Image. The template used to launch EC2. Like a Docker image, but for a whole VM.”

**How would you put a Docker app on AWS?**  
“Launch Ubuntu EC2, open 22 and 80 in the security group, SSH, install Docker, `docker run -p 80:8000 myapp`. Same image they built locally. That’s the week-1 project.”

**Root account?**  
“Lock it. Enable MFA. Create an IAM admin user for daily work. I repeat this every batch because students ignore it.”

**Have you used Lambda / EKS / Terraform?**  
“Not something I put on this resume. I can add a lab if the batch is ready. Core course is EC2, S3, IAM, Security Groups, then Docker on EC2.”

---

## C4. Linux + Git

**Why Linux for DevOps?**  
“Servers run Linux. EC2 images are Linux. Docker is native on Linux. Students must be comfortable in a terminal.”

**What does `ls -l` show?**  
“Type, permissions, owner, size, date, name. Permissions are `rwx` for user, group, others.”

**What is `chmod 755`?**  
“Owner rwx, group rx, others rx. Typical for folders and scripts. `644` is files: owner rw, others r.”

**How do you find a process using port 8000?**  
“`ss -tulpn | grep 8000` or `lsof -i :8000`. Then I show `docker ps` — often it’s the container.”

**Git: add vs commit vs push?**  
“add = stage. commit = snapshot locally. push = send commits to GitHub.”

**What is a merge conflict?**  
“Two people changed the same lines. Git stops. You pick the final text, then commit. I demo this live. It’s the best Git lesson.”

**Your Git story from the resume?**  
“Wikimedia Scribe-Android. I opened pull requests, took review, and merged keyboard layouts for 7+ languages. That’s the workflow I teach: branch, PR, review, merge.”

---

## C5. Teaching questions (they hired a teacher)

**How do you teach a weak student?**  
“Small lab, one goal. Pair them. I walk the room. I don’t lecture for 60 minutes. PyMaster is built that way: one exercise, then the next.”

**How do you know they learned Docker?**  
“They show me: a Dockerfile they wrote, `docker ps` output, browser hitting the mapped port. If they can’t demo it, they didn’t learn it.”

**3-day Docker plan?**  
- Day 1: problem, VM vs container, `run` / `ps` / `logs`  
- Day 2: Dockerfile, build, ports, layers  
- Day 3: Compose, volume, a small two-service lab  

**How do you handle a student who only knows C / Python?**  
“I don’t start with theory. I start with their `app.py`. We put it in Docker. They see the same app, new environment. Then names: image, container.”

**Online vs classroom?**  
“Same loop: I demo, they do, we recap mistakes. Online needs more screenshots and a shared repo. I already write labs (PyMaster has 1,200+).”

**How do you keep content current?**  
“Syllabus stays: Linux, Git, Docker, AWS, CI/CD. Commands change a little. I redo the lab myself before each batch.”

**Why you, not a 5-year DevOps engineer?**  
“I ship software and I already teach. I can translate. Students don’t need war stories from a 10,000-node cluster. They need a lab they can finish today.”

---

## C6. Resume questions (he will open your PDF)

**Tell me about yourself. (90 seconds)**  
“I’m Bhanu. B.Tech CSE from GHRCE, 8.7 CGPA. I build and ship: PyMaster is a live Python learning app with 1,200+ exercises — so I already think in labs. I interned in Canada with Mitacs, I have a granted patent, I contribute to Wikimedia. For this role I want to teach the missing piece students don’t get in college: Linux, Git, Docker, AWS, and how to actually release. I can join immediately.”

**PyMaster CI/CD — what did you actually do?**  
“I owned the release path: Git, multi-environment builds — dev, staging, production — then Play Store publish, then Crashlytics to watch crashes. That’s the same idea as a DevOps pipeline: build, promote, monitor.”

**You listed AWS but your apps use GCP. Why?**  
“Industry batches are AWS. I teach AWS as the syllabus. My production work is GCP/Firebase — Auth, Storage, hosting. The ideas map: IAM, object storage, compute. I won’t pretend I ran a 50-service EKS cluster.”

**99.5% crash-free / 98% uptime — if they ask how?**  
“Crashlytics on PyMaster: almost all sessions had no crash. V-Safe: the Firebase path for SOS stayed up across the project. I use them as monitoring examples, not as fake SRE metrics.”

**Why teaching DevOps, you look like an app developer?**  
“Because I felt the gap. Students can write code. They cannot ship. I built a learning product. I trained healthcare workers on a device. I want to do that for DevOps labs.”

---

## C7. Company / HR

**What do you know about Mentorizee?**  
“Ed-tech from Pune. Hands-on, mentor-led, project-based training for students and early professionals. You run workshops in colleges — including GHRCE. You want trainers who can join soon and teach industry tools like Docker and AWS, not only slides.”

**Why us?**  
“You teach by doing. That’s how I already work. I can start now and run labs, not wait three months to design a 200-page PPT.”

**Can you join immediately?**  
“Yes.”  
(If they ask a date: “This week / as soon as you want.”)

**Pune / relocate?**  
Have one sentence ready. Examples:  
- “Yes, I can come to Pune.”  
- “I can start remote this week and come to Pune on ___.”  
Don’t freeze. They expect join-soon.

**Salary?**  
Don’t throw a number first. “I’m flexible for the right teaching role. What range do you have for this faculty seat?”  
If they push: pick a range you can live with. For a Pune ed-tech trainer, think in monthly CTC you already discussed with family. Don’t invent a fake 20 LPA.

**Do you have doubts?**  
Ask 1–2, not 6:  
1. “Is the first batch Docker + AWS, and how many weeks?”  
2. “Classroom, online, or both — and when do you want the first class?”

---

# D. Day-of rules

1. **Pick Docker** if they let you choose. You rehearsed it.  
2. **Draw.** Talking without boxes looks like memorising.  
3. **Never say Kubernetes / Terraform / Jenkins** unless they ask. Then: “Not on my resume. I can learn the lab version for a later module.”  
4. **Don’t lie about AWS production.** Teach it. Don’t fake it.  
5. **Join immediately.** That’s a requirement.  
6. If you blank: repeat the three sentences — *pack the environment; image vs container; Dockerfile is the recipe.* Then continue.  
7. After the 10 minutes, ask: “Should I also outline the student lab?” That shows you’re a teacher.

---

## One cheat card (memorise these 12 lines)

```
DevOps = build, test, release, run, watch — as one loop
Docker  = app + environment, repeatable
Image   = recipe          Container = running copy
VM      = guest OS        Container = shares kernel
Dockerfile FROM WORKDIR COPY RUN EXPOSE CMD
docker build -t myapp .
docker run -d -p 8000:8000 myapp
EC2 = computer    S3 = files    IAM = who    SG = firewall
CI = every push builds     CD = then we release
My story = PyMaster labs + Git PRs at Wikimedia + join now
```

That’s the interview.
