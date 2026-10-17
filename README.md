# OC CI/CD Final Project — Python Task Manager

## Project name
**OC CI/CD Final Project — Python Task Manager**

## Objective
Demonstrate Continuous Integration (CI) with GitHub Actions and a Tekton/OpenShift Pipeline for a small Python application. The workflow runs Flake8 lint checks and Nose unit tests. The Tekton configuration includes a cleanup task and a Nose test task.

## Application
A minimal Flask API:
- `GET /` — service information
- `GET /health` — health status

## GitHub Actions
The workflow is `.github/workflows/workflow.yml`. It runs on pushes and pull requests to `main`, checks out the code, configures Python, installs dependencies, runs **Lint with flake8**, and **Run unit tests with nose**.

## Tekton / OpenShift
- `.tekton/tasks.yml` defines `cleanup`, `git-clone`, `flake8`, `nose`, `buildah`, and `deploy` tasks.
- `.tekton/pipeline.yml` connects the tasks.
- `.tekton/pvc.yml` is a sample PersistentVolumeClaim manifest for pipeline workspace storage.

The PVC requests `1Gi` using the `skills-network-learner` storage class, as required by question 5. Apply these manifests in your assigned Skills Network OpenShift project.

## Run locally
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m flake8 .
python -m nose -v
python app.py
```

## Push to GitHub
Create a repository, copy these files into it, then:
```bash
git init
git add .
git commit -m "Add Python CI/CD project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
Replace the placeholder remote URL with your real repository URL. After pushing, open the repository's **Actions** tab and capture the successful run.

## Submission evidence checklist
1. GitHub URL to this `README.md`.
2. GitHub URL to `.github/workflows/workflow.yml`.
3. GitHub URL to `.tekton/tasks.yml`.
4. Screenshot of actual OpenShift PVC details saved as `oc-pipelines-console-pvc-details.png`.
5. Copy the successful GitHub Actions run log text.
6. Screenshot of the actual OpenShift Pipeline named `oc-pipelines-oc-final`.
7. Screenshot of the actual successful OpenShift PipelineRun named `oc-pipelines-oc-green`.
8. Copy the actual OpenShift application logs.

**Important:** screenshots and logs must come from your own GitHub/OpenShift environment. This starter project cannot truthfully supply evidence of a pipeline that has not been run in your cluster.
# oc-cicd-final-project
