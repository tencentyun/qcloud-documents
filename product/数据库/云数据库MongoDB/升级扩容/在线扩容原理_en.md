Procedure for Online Expansion
1. Initiate expansion operation on the WEB console or via API.
2. The system will create a corresponding number of Secondary nodes based on the new specifications.
3. Add the newly created Secondary nodes to the cluster instance one after another, and synchronize the data.
4. After data synchronization is completed for the last Secondary node , the original nodes will be removed one by one starting from Secondary nodes to Primary nodes.
5. When there is no primary node in the cluster, a new one will be elected.
![](https://mc.qcloudimg.com/static/img/c5f2b406c73f6fd9c21b216d1cf0d350/zaixiuankuorong.png)
