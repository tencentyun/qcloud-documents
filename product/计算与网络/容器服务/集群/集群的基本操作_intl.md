## Creating a Cluster
1. Click the **New** button on the cluster list page.
![Alt text](https://mc.qcloudimg.com/static/img/9392ef717e58c9acae2d7a6522d0ecf5/Image+001.png)

2. Enter your basic information and click **Next**.
![Alt text](https://mc.qcloudimg.com/static/img/0d5d80fceb147d451533ece2d510b7b9/Image+002.png)


3. Select your model and click **Next**. All models with cloud disks as system disks are supported.
![Alt text](https://mc.qcloudimg.com/static/img/0b5cb08e7bbaad58621f980842576c78/Image+003.png)

4. Enter CVM configurations and click "Complete".

![Alt text](https://mc.qcloudimg.com/static/img/2e633dbaa3ba8a2a996404646f20b195/Image+004.png)

5. The created cluster is displayed in the cluster list.

![Alt text](https://mc.qcloudimg.com/static/img/5f35f95bb86c3464bf4152bd47d81926/Image+006.png)

### Adding a CVM
1. Select the cluster you just created and click **Add Nodes**.
![Alt text](https://mc.qcloudimg.com/static/img/2e548b3ffc6ce089a3f4474cc432fbbb/Image+041.png)

2. Specify the network, model and configuration. Click **Complete**. You can create CVMs in different subnets under different availability zones in the same region.
![Alt text](https://mc.qcloudimg.com/static/img/7dc7b7a12fda0e6a3db8b23c31c18957/Image+042.png)

3. The newly added CVM is displayed in the ID/Node Name list.

![Alt text](https://mc.qcloudimg.com/static/img/f5d9b2eccd3304adc38f1989ed9fa60d/Image+043.png)

## Terminating a CVM
1. On the cluster list page, select the ID/Node Name of a cluster, click "Cluster List" and select the CVM you want to terminate.

![Alt text](https://mc.qcloudimg.com/static/img/61ceaf3d01c31dfd57159be526bdc2d4/Image+044.png)

2. Click **Terminate** and then **OK**.

![Alt text](https://mc.qcloudimg.com/static/img/93e97bf9c181c470a05f59962c7804d1/Image+045.png)

## Checking Node Information

Click the ID/Node Name of the cluster in the cluster list and select "Node List" to view CVM list information.

![Alt text](https://mc.qcloudimg.com/static/img/dce49afd7da5acf8e16ff2dff5faf4d2/Image+046.png)

## Logging in to Node
Currently, Tencent Cloud CVM is support by the nodes. For more information, please see [Log in to CVM](https://www.qcloud.com/doc/product/213/5436).

##Creating Cluster Namespaces

1. Select and open a cluster from the cluster list. Select **Namespace List** tab and click **Create a Namespace**.
![Alt text](https://mc.qcloudimg.com/static/img/a36cb53b22284df29ec3b2c710654001/Image+002.png)
![Alt text](https://mc.qcloudimg.com/static/img/8a8d7575aa04540385f70d70955f544f/Image+001.png)

## Deleting Cluster Namespaces

1. Select and open a cluster from the cluster list. Select **Namespace List** tab and the namespace you want to delete.
2. Click **Delete** and **OK**.

>Note: All resources in the namespace are deleted as you delete the namespace. Please back up your data in advance.