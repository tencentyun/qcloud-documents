## Adding an existing CVM
### Overview
Tencent CCS supports adding both new and existing CVMs to the cluster.
Currently, existing CVMs can only be added to the cluster within the same VPC. The reuse of CVM resources in the basic network and different VPCs will be available in the future.

### Operation method
1. Select ID/Node Name of a cluster on the cluster list page, click **Node List**, and select Add Existing Node.

![Alt text](https://mc.qcloudimg.com/static/img/0cec75d91713f2b61f96dc8b6f70aa6d/Image+003.png)

2. Select an appropriate CVM to add to the cluster.

![Alt text](https://mc.qcloudimg.com/static/img/65e0be4baeed62090ac7e5c7111b8b3d/Image+004.png)

3. Set node login method, and click **Finish**.

![Alt text](https://mc.qcloudimg.com/static/img/cd2e37ee6af64ad695a7780f4b7eb980/Image+005.png)

### Limits
1. Currently, only the CVM under the same VPC can be added.
2. If you add existing CVM to the cluster, the operating system of CVM will be reinstalled.
