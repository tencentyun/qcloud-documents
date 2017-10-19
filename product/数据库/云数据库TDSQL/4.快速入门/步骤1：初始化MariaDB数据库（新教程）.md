 在此步骤中，我们将对已经购买的MariaDB数据库执行初始化操作。
1. 在[腾讯云控制台](https://console.cloud.tencent.com/)的左上角，单击【云产品】下的【关系型数据库】，进入数据库产品页面。
![](//mc.qcloudimg.com/static/img/511cad3621447b36d204b87bf83bb09f/image.png)
1. 在关系型数据库页面中，单击【TDSQL(MariaDB)】下的【实例列表】，找到目标地域（此例中以广州为例）中要操作的状态为“**未初始化**”的MariaDB数据库实例。
![](//mc.qcloudimg.com/static/img/d947b9c5326ae79c36ff283335d56b65/image.png)
1. 单击【初始化】对要操作的MariaDB 数据库实例执行初始化。
![](//mc.qcloudimg.com/static/img/038c3fe9ba91793d68023f0fb5ec6df0/image.png)

1. 配置初始化参数，然后单击【确定】开始初始化。
 - ** 支持的字符集**：选择MariaDB数据库支持的字符集。
 - **表名大小写敏感**：表名是否大小写敏感，默认为是。
 - **开启强同步**：开启强同步可以保证在主机故障时备机数据的一致性。默认为不开启，即同步方式为异步同步。
 - **innodb_page_size**：该数值为Innodb索引数据页长度，MariaDB默认值为16K。修改该值将影响索引创建，该值越小，性能越好。
![](//mc.qcloudimg.com/static/img/7b9c1afcae2239d041a467eda7af3414/image.png)
1. 目标MariaDB实例的状态变为“**运行中**”，说明已初始化成功。
 ![](//mc.qcloudimg.com/static/img/f4c9216239116666bc51ee2d42a5df59/image.png)
