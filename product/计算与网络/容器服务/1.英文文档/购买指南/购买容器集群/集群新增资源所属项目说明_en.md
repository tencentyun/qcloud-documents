## Project of New Resources in a Cluster
### Overview
To conduct financial accounting by projects, please take the following into the consideration:

1. Clusters are not project-specific, but CVMs, load balancers and other resources in a cluster are project-specific.
2. Project of new resources in a cluster: Only the new resources in the cluster are allocated to the project.

### Notes
1. It is recommended to allocate all the resources in a cluster to the same project.
2. If it is necessary to distribute CVMs in a cluster to different projects, go to the CVM Console to migrate projects.
3. If CVMs belong to different projects, they belong to different `security group instances`. Please try to configure the same `security group rules` for the CVMs in the same cluster.
