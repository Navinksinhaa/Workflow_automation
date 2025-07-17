# 🚀 Workflow Automation - Mini Airflow Clone

A lightweight, scalable, and developer-friendly workflow automation system inspired by Apache Airflow, built with:

- ⚡ **FastAPI** – RESTful control plane for triggering and monitoring jobs
- 🧵 **Celery** – Distributed job queueing and execution
- 🧠 **Redis** – Fast in-memory message broker
- 🐳 **Docker Compose** – Simple orchestration of the full stack

---

## 🔧 Stack Overview

```mermaid
flowchart LR
    A[User/API Trigger - FastAPI] --> B[Redis Broker]
    B --> C[Celery Worker]
    C --> D[Task Execution]
    D --> E[Result Backend / Monitor API]
