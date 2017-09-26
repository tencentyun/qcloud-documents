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

![Alt text](https://mc.qcloudimg.com/static/img/c480588db03d554a36df294316a981da/Image+051.png)

## Node Lifecycle

### Status Description

| Status | Description |
|:--:|:--|
| Healthy | The node is running and is connected with the cluster |
| Exception | The node encountered exceptions and is not connected with the cluster |
| Other Status | Please see [CVM Lifecycle](https://www.qcloud.com/document/product/213/4856) |
