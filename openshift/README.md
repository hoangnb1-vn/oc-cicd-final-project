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

The pipeline clones the repository itself. When starting a PipelineRun, bind
`shared-workspace` to PVC `oc-pipelines-console-pvc`. Push the project changes
to the configured Git repository before running: the checkout must contain
the Dockerfile, requirements, application, and tests.

### Question 6: pipeline diagram (2 points)

Apply `.tekton/tasks.yml` first, then `.tekton/pipeline.yml`, or import their
YAML documents through the OpenShift console's **Import YAML** form.
All six Tasks are supplied locally; no ClusterTasks are referenced.

Open **Pipelines > Pipelines > oc-pipelines-oc-final > Details** and capture
the diagram with every task visible:

`cleanup -> git-clone -> flake8 -> nose -> buildah -> deploy`

Save the actual console screenshot as `oc-pipelines-oc-final.png` and upload
it for question 6. Creating this Pipeline does not start a PipelineRun.

Before running the full pipeline, confirm that the `pipeline` service account
can deploy workloads/routes, push to the project image registry, and run the
Buildah step as UID 0 with SETFCAP under the lab's existing pipelines-scc.
Buildah uses VFS storage and chroot isolation without privileged containers.
The default image
target uses namespace `sn-labs-hoangnb1`; adjust the `image` parameter if your
assigned namespace changes. If the lab disallows this Buildah configuration, use its
provided supported build task rather than changing cluster security policies.

## Evidence capture

### Question 8: actual application logs (2 points)

The application listens on port `8000` and writes a startup banner containing
`SERVICERUNNING`. Apply the latest Tasks and run the pipeline against the latest
GitHub `main` commit to rebuild and deploy the updated application first.
After the PipelineRun succeeds, capture the application container logs:

```bash
oc logs -n sn-labs-hoangnb1 deployment/oc-final --all-containers=true --timestamps=true > oc-pipeline-application-logs
cat oc-pipeline-application-logs
```

Verify that the actual output includes `SERVICERUNNING` and port `8000`, then
copy the entire file contents into the text answer for question 8. Do not
substitute PipelineRun build logs or manually written sample logs.

### Question 7: successful PipelineRun (2 points)

1. Push the updated repository, including `Dockerfile`, to GitHub branch `main`.
2. Apply the latest Tasks and Pipeline in the assigned project.
3. Import `.tekton/pipelinerun.yml` through **Import YAML > Create**, or run
   `oc create -f .tekton/pipelinerun.yml`. Use **create**, not **apply**, because
   this manifest uses `generateName` to allow retries without deleting runs.
4. Open **Pipelines > PipelineRuns**, select the newly generated
   `oc-pipelines-oc-green-...` run, and monitor its details and logs.
5. Only capture submission evidence when the run is **Succeeded** and all six
   tasks are green. Save the screenshot as `oc-pipelines-oc-green.png`.

The question specifies the screenshot filename, not a fixed PipelineRun name.
If a task fails, inspect its Logs and Events before retrying with a new run.
This repository does not contain evidence of a successful cluster execution.

### Question 5: PVC details (2 points)

The manifest `.tekton/pvc.yml` requests `1Gi` with storage class
`skills-network-learner`.

In the assigned Skills Network OpenShift project:

1. Apply `.tekton/pvc.yml` using the command above, or paste its contents
   into the OpenShift console's **Import YAML** form and create the resource.
2. Open **Storage > PersistentVolumeClaims > oc-pipelines-console-pvc > Details**.
3. Verify that the details show storage class `skills-network-learner` and
   requested capacity `1Gi` (the console may format this as `1 GiB`).
4. Capture the real details page with both fields visible. Save the screenshot
   as `oc-pipelines-console-pvc-details.png` and upload it for question 5.

If a claim with this name already exists with another storage class, do not
delete it blindly: storage class cannot normally be changed on an existing
claim. Create a separate correctly configured claim with a different name,
or follow the lab's reset instructions if that exact name is required.

- PVC: OpenShift Developer/Administrator console → Storage → PersistentVolumeClaims → `oc-pipelines-console-pvc` → Details.
- Pipeline: Pipelines → Pipelines → `oc-pipelines-oc-final`.
- Successful run: Pipelines → PipelineRuns → open the successful run and capture task status. If your course requires the run name `oc-pipelines-oc-green`, create/name it accordingly in the console if supported.
- Logs: open the successful PipelineRun/task logs or the deployed application workload's Logs tab. Copy actual output; do not fabricate it.
