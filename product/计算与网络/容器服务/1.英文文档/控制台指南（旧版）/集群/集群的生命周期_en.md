## Cluster Lifecycle

### Status Description
| Status | Description |
|:--:|:--|
| Creating | The cluster is being created. Applying for cloud resources |
| Adjusting Scale | The number of nodes in the cluster has changed. Adding or terminating nodes |
| Running | The cluster is running |
| Upgrading | The cluster is being upgraded. Please wait for upgraded features |
| Deleting | The cluster is being deleted |
| Exception | Exceptions occurred in the cluster, for instance, unable to reach node network |

### Status Flow Chart
**Cluster Lifecycle**: Cluster status flow is shown below. Hexagons represent node status.

![Alt text](https://mc.qcloudimg.com/static/img/a21f83fb844568e72ccb319d24f01946/%7BBE75004B-997B-4939-B7DB-C769ED2712AF%7D.png)

## Node Lifecycle

### Status Description

| Status | Description |
|:--:|:--|
| Healthy | The node is running and is connected with the cluster |
| Exception | The node encountered exceptions and is not connected with the cluster |
| Other Status | Please see [CVM Lifecycle](https://cloud.tencent.com/document/product/213/4856) |
