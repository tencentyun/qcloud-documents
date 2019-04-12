以下为初始化 TDSQL 实例的具体操作流程。
## TDSQL 控制台
1. 用户登录进入 [管理中心](https://console.cloud.tencent.com/)，将鼠标依次移动至【云产品】>【基础产品】>【数据库】，单击【分布式数据库】进入 [ TDSQL 控制台](https://console.cloud.tencent.com/dcdb)。
	![](https://mc.qcloudimg.com/static/img/23475689f7192fd8a0fc681d9e4cea2e/r1.png)
2. 在控制台中，可看到创建完成但未初始化的 TDSQL 实例，单击实例右方的【初始化】。
	![](https://mc.qcloudimg.com/static/img/3f1382a09e8636e052ca766e71d40465/image.png)

3. 弹出实例初始化界面，根据需要选择配置后，单击【确定】，进行初始化。
 - 支持字符集：选择 MySQL 数据库支持的字符集。

 - 表名大小写敏感：数据库表名大小写是否敏感。

	-  开启强同步：开启强同步可以保证在主机故障时备机数据的一致性，至少需要 2 个节点方可正常运行，默认为不开启，即数据同步方式为异步。

	- innodb_page_size：该数值为 Innodb 索引数据页长度， MariaDB 默认值为 16  K。修改该值将影响索引创建，该值越小，性能越好，但若更改为 4 KB 将导致单个索引不能超过 768 字节。
	
	![](https://mc.qcloudimg.com/static/img/6f9711414968945d27a8533c914e0317/r3.png)
	
4. 等待约两分钟后，实例状态转换为“运行中”，表明初始化完成，下一步即可进行连接数据库操作。
	![](https://mc.qcloudimg.com/static/img/87b5573dc8220c19069aa8d8b08cbcb3/r4.png)
