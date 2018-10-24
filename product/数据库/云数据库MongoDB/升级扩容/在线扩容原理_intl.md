Procedure for Online Expansion
1. Initiate expansion operation on the WEB console or via API
2. The system creates an appropriate number of secondary nodes according to the new specifications.
3. Add the new secondary nodes into the cluster instance for data synchronization.
4. After the data synchronization is completed for the last secondary node, kick off the original nodes one by one. Secondary nodes are first kicked off before primary nodes.
5. When there is no primary node in the cluster, a new primary node will be selected.
![](https://mc.qcloudimg.com/static/img/c5f2b406c73f6fd9c21b216d1cf0d350/zaixiuankuorong.png)

