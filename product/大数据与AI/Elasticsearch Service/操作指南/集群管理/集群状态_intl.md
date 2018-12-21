You can view the status of the cluster both in the **Cluster List** page and the **Basic Info** section of the cluster details page.
![Cluster list page](https://main.qcloudimg.com/raw/3126ad8ef939ee985f7c326080620219.png)
![Cluster details page](https://main.qcloudimg.com/raw/3fa85f997895ed2e21b1abe9f7c1f9ee.png)
Cluster status indicates whether the cluster is changing or in use, including normal, processing, etc. The meaning of a specific status is as follows:

| Status | Meaning |
|---------|---------|
| Normal | Cluster creation is completed and there are no configuration changes, cluster restart, etc., and the cluster can be accessed and used normally. |
| Processing | Operations such as cluster creation, cluster configuration change, and cluster restart are in progress, during which access to some services (such as Kibana, data storage and query) will be affected. |

Health status is one of the most important indicators used to monitoring the ES cluster, which is used to indicate whether the cluster is working normally overall. The categories of health status are as follows:

| Color | Health Status |
|-------|-------------|
| Green | All primary and replica shards are fully functional. |
| Yellow | All primary shards are functional, but at least one replica shard is not.|
| Red | At least one primary shard is not functional. |

For more information, see [here](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/_cluster_health.html).

