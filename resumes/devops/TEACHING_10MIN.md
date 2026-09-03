# 10-minute Docker class — speak this

Open this on your phone. If they say “any topic”, say: **“I’ll take Docker.”**

Draw the four pictures. Speak slower than you think.

---

## 0:00  Opening

I’ll take **Docker** — first lab I would run with a DevOps batch. Problem, idea, a small demo, then a student lab.

---

## 0:00–1:00  Hook

Every student hits this: **it works on my machine.**

Laptop: Python 3.12, Flask, app runs.  
College PC: Python 3.10, Flask missing, app crashes.

The app is not wrong. The **environment** is different.

DevOps makes “run the app” repeatable. Docker packs the app **and** the environment.

*Draw: three boxes — laptop / college PC / server.*

---

## 1:00–3:00  VM vs container

Old way: **virtual machine** — full guest OS. Heavy. Slow. Lots of RAM.

Docker: **container**. Shares the host **kernel**. Only packs app + libraries.

A VM virtualises **hardware**. A container virtualises the **process**. That’s why it is small and starts in seconds.

*Draw: two stacks — VM has Guest OS, container does not.*

---

## 3:00–5:00  Image vs container

Students mix these two words. I don’t let that slide.

**Image** = recipe. Read-only. Blueprint.  
**Container** = running copy. One image, many containers.

```
docker pull python:3.11
docker images
docker run -d --name web python:3.11
docker ps
docker logs web
docker stop web && docker rm web
```

*Draw: IMAGE --docker run--> CONTAINER 1, 2, 3*

---

## 5:00–8:00  Dockerfile (write line by line)

The environment becomes **code**. Same file on every laptop.

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

- `FROM` — don’t start empty  
- `WORKDIR` — cd /app  
- copy requirements **first**, then `RUN pip` — **layer cache**  
- `COPY . .` — app code  
- `EXPOSE` — documents the port  
- `CMD` — what starts  

```bash
docker build -t myapp:1.0 .
docker run -d -p 8000:8000 --name api myapp:1.0
```

`-p 8000:8000` is host port → container port. Students forget this and think the app is dead.

*Draw: browser → localhost:8000 → container :8000*

---

## 8:00–9:00  Compose + DevOps loop

Real apps: web + database. **Compose** starts both: `docker compose up`.

I do **not** start with Kubernetes. Docker first, then cloud.

```
Git → docker build → run locally → same image on AWS EC2
```

That is the CI/CD story later.

---

## 9:00–10:00  Recap + lab + stop

Three lines:

1. Docker packs **app + environment**  
2. **Image** = recipe, **container** = running copy  
3. **Dockerfile** makes the environment code  

**Lab (30 min):** 20-line Python app → Dockerfile → build → run `-p` → open browser → change one line → rebuild and see cache.

That’s how I teach: explain, demo, they do it.

Questions?

---

## If you freeze

Say only this, then continue:

> “Docker packs the app and its environment. Image is the recipe. Container is the running copy. Dockerfile is how we write that recipe.”
