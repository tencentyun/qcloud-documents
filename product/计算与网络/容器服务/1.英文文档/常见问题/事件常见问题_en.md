## Common Errors and Solutions

### 1. Back-off restarting failed docker container
Description: The exceptional Docker container is being restarted.
Solution: Check if the Docker process running in the image has exited due to exception. If there is no process running in the image, you can add an execution script in the service creation page.

### 2. fit failure on node: Insufficient cpu
Description: Insufficient cluster CPU.
Solution: The reason for this error is that the node cannot provide enough computing cores. Modify the CPU limit from the service page or expand the cluster.

### 3. no nodes available to schedule pods
Description: Insufficient cluster resource.
Solution: The reason for this error is that the number of nodes is not sufficient to carry the pods. Modify the number of service pods or CPU limit from the service page.

### 4. pod failed to fit in any node
Description: No proper node for the pods to use.
Solution: This error is caused by inappropriate resource limit configuration which leads to a situation where there are no proper nodes to carry the pods. Modify the number of service pods or CPU limit from the service page.

### 5. Liveness probe failed: 
Description: Container health check failed
Solution: Check if the container processes in the image are normal, and whether the health check port is correctly configured.

### 6. Error syncing pod, skipping 
Error syncing pod, skipping failed to "StartContainer" for with CrashLoopBackOff: "Back-off 5m0s restarting failed container
Description: Contain process crashed or exited.
Solution: Check if there are frontend processes running in the container. If so, check whether these processes have any exceptional behaviors. For more information, please see Guide on How to Build Docker Image (https://cloud.tencent.com/document/product/457/7208).

Contact customer service if the solutions above cannot solve your issues.






