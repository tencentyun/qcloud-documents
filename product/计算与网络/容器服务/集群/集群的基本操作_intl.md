## Creating a Cluster
1. Click the **New** button on the cluster list page.
 ![](https://mc.qcloudimg.com/static/img/41f819632bb146b6d89fea7f2980cc08/Basic_Operations_of_Clusters_1.jpg)

1. Enter your basic information and click **Next**.
 ![](https://mc.qcloudimg.com/static/img/fe4f9f9bd9a129c2992d20366fd45e3b/Basic_Operations_of_Clusters_2.jpg)

1. Select your model and click **Next**. All models with cloud disks as system disks are supported.
 ![](https://mc.qcloudimg.com/static/img/7fc38e8d897735e0ab694ed9ff680f45/Basic_Operations_of_Clusters_3.jpg)

1. Enter CVM configurations and click "Complete".
 ![](https://mc.qcloudimg.com/static/img/a65dda393d4dfe2e89624ab82b7ea693/Basic_Operations_of_Clusters_4.jpg)

1. The created cluster is displayed in the cluster list.
 ![](https://mc.qcloudimg.com/static/img/0cec22abebd970383c0f23c1dcd19b39/Basic_Operations_of_Clusters_5.jpg)


## Adding a CVM
1. Select the cluster you just created and click **Add Nodes**.
![](https://mc.qcloudimg.com/static/img/bfe645cc457f645ba4f8095fd5bb87a8/Basic_Operations_of_Clusters_6.jpg)

2. Specify the network, model and configuration. Click **Complete**. You can create CVMs in different subnets under different availability zones in the same region.
![](https://mc.qcloudimg.com/static/img/d2b4c16a176604455130a3c65449b8cd/Basic_Operations_of_Clusters_7.jpg)

3. The newly added CVM is displayed in the ID/Node Name list.
![](https://mc.qcloudimg.com/static/img/058a7f64644733b636dbc502a46267bd/Basic_Operations_of_Clusters_8.jpg)


## Terminating a CVM
1. On the cluster list page, select the ID/Node Name of a cluster, click "Cluster List" and select the CVM you want to terminate.
![](https://mc.qcloudimg.com/static/img/5fcd8904cb18513005f5e82b1d139681/Basic_Operations_of_Clusters_9.jpg)

2. Click **Terminate** and then **OK**.
![](https://mc.qcloudimg.com/static/img/ed878ca1a732e0443f2277904121b2ad/Basic_Operations_of_Clusters_10.jpg)


## Checking Node Information
Click the ID/Node Name of the cluster in the cluster list and select "Node List" to view CVM list information.
![](https://mc.qcloudimg.com/static/img/7d876da931fe6e3ef5983fea830629c9/Basic_Operations_of_Clusters_11.jpg)


## Logging in to Node
Currently, Tencent Cloud CVM is support by the nodes. For more information, please see [Log in to CVM](https://cloud.tencent.com/doc/product/213/5436).


## Creating Cluster Namespaces
Select and open a cluster from the cluster list. Select **Namespace List** tab and click **Create a Namespace**.
![](https://mc.qcloudimg.com/static/img/46cc733241f25e727a4d9fc07335bdd4/Basic_Operations_of_Clusters_12.jpg)
![](https://mc.qcloudimg.com/static/img/0b1aaec41b2b26407b85521446ef18df/Basic_Operations_of_Clusters_13.jpg)


## Deleting Cluster Namespaces
1. Select and open a cluster from the cluster list. Select **Namespace List** tab and the namespace you want to delete.
2. Click **Delete** and **OK**.

>Note: All resources in the namespace are deleted as you delete the namespace. Please back up your data in advance.
