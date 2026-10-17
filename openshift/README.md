# OpenShift setup notes

These commands assume `oc` is installed and you are logged into the correct cluster.

1. Select your assigned project:
   ```bash
   oc project YOUR_PROJECT
   ```
2. Apply the workspace PVC:
   ```bash
   oc apply -f .tekton/pvc.yml
   ```
3. Apply Tasks and Pipeline:
   ```bash
   oc apply -f .tekton/tasks.yml
   oc apply -f .tekton/pipeline.yml
   ```
4. Verify resources:
   ```bash
   oc get pvc oc-pipelines-console-pvc
   oc describe pvc oc-pipelines-console-pvc
   oc get tasks
   oc get pipeline oc-pipelines-oc-final
   ```

A PipelineRun also needs a workspace binding and a source checkout step or a pre-populated workspace. The included Pipeline expects source code to already exist in the bound workspace. Your course environment may provide a preconfigured pipeline or task for cloning the Git repository. Follow the course's OpenShift instructions for binding the repository and workspace before starting a run.

## Evidence capture
- PVC: OpenShift Developer/Administrator console → Storage → PersistentVolumeClaims → `oc-pipelines-console-pvc` → Details.
- Pipeline: Pipelines → Pipelines → `oc-pipelines-oc-final`.
- Successful run: Pipelines → PipelineRuns → open the successful run and capture task status. If your course requires the run name `oc-pipelines-oc-green`, create/name it accordingly in the console if supported.
- Logs: open the successful PipelineRun/task logs or the deployed application workload's Logs tab. Copy actual output; do not fabricate it.
