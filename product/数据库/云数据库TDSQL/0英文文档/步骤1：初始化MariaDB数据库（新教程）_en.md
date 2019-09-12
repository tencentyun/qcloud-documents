 In this step, we initialize the purchased MariaDB database.
1. At the upper left corner of [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Relational Databases" under the "Cloud Products" menu to go to the database product page.
![](//mc.qcloudimg.com/static/img/511cad3621447b36d204b87bf83bb09f/image.png)
2. On the relational database page, click "Instance List" under "TDSQL(MariaDB)" to find the TDSQL(MariaDB) instance in "**Uninitialized**" status to be operated in the destination region (here is Guangzhou).
![](//mc.qcloudimg.com/static/img/d947b9c5326ae79c36ff283335d56b65/image.png)
3. Click "Initialize" to initialize the MariaDB database instance.
![](//mc.qcloudimg.com/static/img/038c3fe9ba91793d68023f0fb5ec6df0/image.png)

4. Configure initialization parameters, and then click "OK" to start initialization.
 - **Supported character set**: Select the character set supported by the MariaDB database.
 - **Table name is case sensitive**: Set whether the table name is case sensitive. The default is "Yes".
 - **Enable strongsync**: Enable strongsync to ensure consistency of slave data when a master fails. It is not enabled by default, that is, synchronization mode is async.
 - **innodb_page_size**: Length of INNODB index data page. Default value for MariaDB is 16K. Modification of this value will affect the creation of the index. Smaller value means better performance.
![](//mc.qcloudimg.com/static/img/7b9c1afcae2239d041a467eda7af3414/image.png)
5. The status of the target MariaDB instance becomes "**Running**", which indicates successful initialization.
 ![](//mc.qcloudimg.com/static/img/f4c9216239116666bc51ee2d42a5df59/image.png)

