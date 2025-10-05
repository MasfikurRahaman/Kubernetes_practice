# Kubernetes Python Logger Practice

## Overview

This repository contains a **Python logging application** designed to run in a Kubernetes pod.  
It demonstrates proper logging best practices by sending logs to **stdout and stderr** rather than writing directly to disk. This ensures **Kubernetes can capture logs automatically**, avoiding issues like disk filling up due to open log files.

---

## Problem / Issue

During early DevOps experiments, we encountered a common Linux/Kubernetes issue:

1. A log file in a container was consuming large disk space (`/var/log/app.log`).
2. Deleting the file inside the container **did not free up disk space**.
3. `df -h` showed 100% full, but `du -sh` showed smaller usage.
4. Investigation revealed that the **file was still open by a running process**, so the inode was not released.  

In Kubernetes, this is often observed when applications write logs to files inside containers rather than stdout/stderr.

---

## How It Was Fixed

1. **Python logging refactor**:
   - The application now logs **INFO messages to stdout**.
   - **WARNING and ERROR messages go to stderr**.
   - This eliminates the need to write logs to disk inside the container.

2. **Dockerfile update**:
   - Uses `app_new.py` for the updated logger.
   - No `/var/log` volume needed.

3. **Kubernetes manifest update**:
   - Pod now uses the new Docker image `masum140/my-python-logger:2.0`.
   - Logs are captured automatically by `kubectl logs`.

4. **Old files preserved**:
   - Previous versions of the application, Dockerfile, and YAML are moved to an `old/` folder for reference.

---

## Permanent / Main Changes

| Component        | Change |
|-----------------|--------|
| Python App      | Logs redirected to stdout/stderr; simulates normal and warning logs |
| Dockerfile      | Updated to use new Python app; minimal container, Kubernetes-ready |
| Kubernetes YAML | Pod updated to use new Docker image with `imagePullPolicy: Always` |
| Repo structure  | Old files moved to `old/` folder for reference; new files clearly separated |

---

## Usage

1. Build Docker image:

```bash
docker build -t my-python-logger:2.0 .
docker tag my-python-logger:2.0 masum140/my-python-logger:2.0
docker push masum140/my-python-logger:2.0


###############################################################################################################################


Apply Kubernetes pod:

kubectl apply -f python-logger.yaml
kubectl get pods
kubectl logs -f python-logger


You will see the INFO logs on stdout and warnings/errors on stderr.

Key Takeaways

Never write logs to disk inside containers in production.

Always use stdout/stderr for containerized applications.

Kubernetes automatically captures logs, preventing disk usage issues.

Keep old versions in a separate folder for reference, but only the latest version should be deployed.
