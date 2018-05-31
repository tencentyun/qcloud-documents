A cluster is a collection of cloud resources required by containers to run, including several CVMs, load balancers and other Tencent Cloud resources.

## Cluster Information

**Cluster Type**: VPC container clusters are supported.

**Cluster Configuration**: When creating the cluster, you can configure CVM model, operating system, system disk and data disk size, login password, etc.

**Cluster Structure**: Prepaid CVMs and postpaid CVMs are supported.

## Cluster Management
You can create clusters, expand/reduce nodes, delete clusters and operate clusters directly by using kubernetes APIs.

## Retained Resources for Cluster
Some resources are retained for each node in a cluster to keep kubernetes running normally. Specific rules are as follows:

CPU

| Total CPU capacity on node (unit: core) | 1 | 2 | 4 | 8 | 16 | 32 |
| --------------- | ---- | ---- | ---- | ---- | ---- | ---- |
| Retained CPU capacity on node (unit: core) | 0.06 | 0.07 | 0.08 | 0.09 | 0.11 | 0.14 |

Memory

| Total memory capacity on node (in Gib) | 1 | 2 | 4 | 8 | 12 | 16 | 24 | 32 | 48 |
| ---------------- | --- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- |
| Retained memory capacity on node (in Mib) | 160 | 320 | 420 | 830 | 1200 | 1300 | 1660 | 1830 | 2420 |

Moreover, 100 Mib of memory will be retained for each node to avoid the OOM error.

## Related Documentation
- [Basic Operations of Cluster](https://cloud.tencent.com/document/product/457/9091)
- [Cluster Lifecycle](https://cloud.tencent.com/document/product/457/9092)
- [Cluster Quota Limit](https://cloud.tencent.com/document/product/457/9087)
- [Network Configuration of Cluster Nodes and Containers](https://cloud.tencent.com/document/product/457/9083)
- [Disk Configuration of Cluster Node](https://cloud.tencent.com/document/product/457/9086)
- [Public IP of Cluster Node](https://cloud.tencent.com/document/product/457/9085)
- [Security Group Configuration of Cluster Node](https://cloud.tencent.com/document/product/457/9084)

