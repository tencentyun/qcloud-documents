## Creating a Cluster
1. Click the **New** button on the cluster list page.
![](https://mc.qcloudimg.com/static/img/51a7002062f738cc42385c36b1b0675c/Basic_Operations_of_Clusters_1.jpg)

2. Enter your basic information and click **Next**.
![](https://mc.qcloudimg.com/static/img/2b18f35cc7edf215513cdca76bd449bf/Basic_Operations_of_Clusters_2.jpg)


3. Select your model and click **Next**. All models with cloud disks as system disks are supported.
![](https://mc.qcloudimg.com/static/img/ec8a7a29da599184dd2a1cc9d23b688b/Basic_Operations_of_Clusters_3.jpg)

4. Enter CVM configurations and click "Complete".

![](https://mc.qcloudimg.com/static/img/c81f5445ad781c094e627492d90e72f3/Basic_Operations_of_Clusters_4.jpg)

5. The created cluster is displayed in the cluster list.

![](https://mc.qcloudimg.com/static/img/fff4cff64244230c40e30611c3fbbdbf/Basic_Operations_of_Clusters_5.jpg)

### Adding a CVM
1. Select the cluster you just created and click **Add Nodes**.
![](https://mc.qcloudimg.com/static/img/fe682f227654d4657a24b5dba81513ca/Basic_Operations_of_Clusters_6.jpg)

2. Specify the network, model and configuration. Click **Complete**. You can create CVMs in different subnets under different availability zones in the same region.
![](https://mc.qcloudimg.com/static/img/84a14c87342674ae8a51650f3d144311/Basic_Operations_of_Clusters_7.jpg)

3. The newly added CVM is displayed in the ID/Node Name list.

![](https://mc.qcloudimg.com/static/img/cdc42fbbb30ce1f72c28378dc3aa9fab/Basic_Operations_of_Clusters_8.jpg)

## Terminating a CVM
1. On the cluster list page, select the ID/Node Name of a cluster, click "Cluster List" and select the CVM you want to terminate.

![](https://mc.qcloudimg.com/static/img/22e4972eab8c13c68c1b7da8fa405e58/Basic_Operations_of_Clusters_9.jpg)

2. Click **Terminate** and then **OK**.

![](https://mc.qcloudimg.com/static/img/d01c1214bd6eecd6ac4a4d0cbde920ca/Basic_Operations_of_Clusters_10.jpg)

## Checking Node Information

Click the ID/Node Name of the cluster in the cluster list and select "Node List" to view CVM list information.

![](https://mc.qcloudimg.com/static/img/354a8ab39cc3d154e26e714ac990102a/Basic_Operations_of_Clusters_11.jpg)

## Logging in to Node
Currently, Tencent Cloud CVM is support by the nodes. For more information, please see [Log in to CVM](https://cloud.tencent.com/doc/product/213/5436).

##Creating Cluster Namespaces

1. Select and open a cluster from the cluster list. Select **Namespace List** tab and click **Create a Namespace**.
![](https://mc.qcloudimg.com/static/img/bc9107ded987a9882058f19903be5e88/Basic_Operations_of_Clusters_12.jpg)
![](https://mc.qcloudimg.com/static/img/0b1aaec41b2b26407b85521446ef18df/Basic_Operations_of_Clusters_13.jpg)

## Deleting Cluster Namespaces

1. Select and open a cluster from the cluster list. Select **Namespace List** tab and the namespace you want to delete.
2. Click **Delete** and **OK**.

>Note: All resources in the namespace are deleted as you delete the namespace. Please back up your data in advance.
