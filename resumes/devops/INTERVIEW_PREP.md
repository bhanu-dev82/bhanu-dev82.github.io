# Mentorizee interview — study only what is on the resume

Interview: **Mohit Bhaskar Urkunde** (CEO & Director, Mentorizee Pvt Ltd, Pune).
Role: **DevOps teacher**. They asked for **Docker, AWS**, and similar basics.
Join: they want you **soon**. Say you can join immediately.

Do **not** claim Kubernetes, Jenkins, Terraform, or Ansible. They are **not** on the resume.

---

## How to talk about Docker and AWS (honest)

Your shipped apps use **Git, CI/CD, Linux, Firebase / GCP**.
Docker and AWS are on the resume as **teaching tools** (what students must learn), not as “I ran AWS at Netflix.”

If they go deep:

> “My production products run on GCP and Firebase. For this course I teach the same ideas on AWS and Docker — EC2, S3, IAM, Dockerfile, Compose — with labs students can repeat.”

That is safe. Inventing an AWS production story is not.

---

## Linux (they will ask)

Know:

- `pwd`, `ls -l`, `cd`, `mkdir`, `rm`, `cp`, `mv`, `cat`, `nano` / `vim`
- `grep`, `chmod`, `chown`, `ps`, `top`, `df -h`, `free -h`
- File permissions: `rwx` for user / group / other (`755`, `644`)
- SSH: `ssh -i key.pem user@ip`

Story from resume: Linux / IoT on V-Safe; you work on Linux daily.

---

## Git (they will ask)

Know:

- `clone`, `status`, `add`, `commit`, `push`, `pull`
- branch → change → pull request → review → merge
- `.gitignore`

Story from resume: **Wikimedia Scribe-Android** — PRs, code review, 7+ language layouts.

---

## Docker (they will ask)

One-liners:

| Idea | Say this |
|---|---|
| Container vs VM | VM = whole OS. Container = app + libs, shares the host kernel. Faster, lighter. |
| Image vs container | Image = recipe / snapshot. Container = a running copy of that image. |
| Why Docker | Same app runs on student laptop, lab PC, and server. “Works on my machine” goes away. |

Commands:

```bash
docker build -t myapp .
docker run -d -p 8080:80 --name web myapp
docker ps
docker logs web
docker exec -it web bash
docker stop web && docker rm web
```

Minimal Dockerfile you should be able to write on a board:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

Compose (two services): web + database in `docker-compose.yml`.
Volumes: keep data after the container stops.

Do **not** say you containerized PyMaster unless you actually did.

---

## AWS (they will ask)

Teach these four. That is enough for a first batch.

| Service | In one sentence | Lab |
|---|---|---|
| **EC2** | A virtual computer in the cloud | Launch Ubuntu, SSH in, install Docker |
| **S3** | Unlimited folders for files | Upload a file, make a public link |
| **IAM** | Who is allowed to do what | User vs role vs policy. Never share root. |
| **Security Group** | Firewall for EC2 | Allow SSH 22 and HTTP 80 only from needed IPs |
| **VPC** | Your private network | Public subnet = has internet. Private = no public IP. |

Map from your real work:

- Firebase Auth / IAM → “who can access what”
- Firebase Storage / S3 → “store files”
- GCP / EC2 → “run the server”
- Crashlytics → “watch production after release”

If they ask “have you used EKS / Lambda / Terraform?”: “Not on this resume. I can add a lab if the batch needs it.”

---

## CI/CD (on the resume — they may ask)

- **CI** = every push, tests/build run automatically
- **CD** = after green build, release to staging/prod
- **GitHub Actions**: YAML in `.github/workflows/` — `on: push`, jobs, steps
- Your story: PyMaster **dev / staging / prod** builds, then Play Store publish, Crashlytics after release

---

## Teaching (this is why they hire you)

Mohit already runs student workshops (including at **GHRCE**). Talk like a teacher:

1. Explain in one sentence  
2. Demo on screen  
3. Students do a 20-minute lab  
4. Recap mistakes  

Your proof: 1,200+ PyMaster exercises, trained healthcare workers, Board of Studies, conference talks.

If he asks why DevOps: “Students can code, but they cannot ship. Linux + Git + Docker + AWS is the missing lab.”

---

## Likely questions

1. What is DevOps? — Build, test, release, run, watch. Developers and ops as one loop.  
2. Difference Docker vs VM? — see table above.  
3. What is an image? — snapshot used to start containers.  
4. What is EC2 vs S3? — compute vs storage.  
5. What is IAM? — identity and permissions. Never use root daily.  
6. How would you teach Docker in 3 days? — Day 1 images/containers. Day 2 Dockerfile. Day 3 Compose + a small app.  
7. Can you join this week? — **Yes.**  
8. Willing to move to Pune? — Have a clear yes/no. Company is in Pune (Dhankawadi).  

---

## Do not say

- “I designed Kubernetes clusters”
- “I automated AWS with Terraform”
- “I ran Jenkins at scale”
- Fake user counts or fake AWS production metrics
