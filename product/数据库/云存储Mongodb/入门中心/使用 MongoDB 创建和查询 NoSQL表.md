本文档主要介绍使用腾讯云 MongoDB 创建和查询 NoSQL 表。
以下步骤进行前，需要您在腾讯云 CVM 通过 shell 连接上 MongoDB，具体详情请参考 [Shell连接示例](https://www.qcloud.com/document/product/240/3978)。
### 创建 NoSQL 表
1. 首先，输入命令`show dbs`检查可用数据库的列表。
![](https://mc.qcloudimg.com/static/img/54bbefc9c59f22fd8ac11f4140d05f4f/showdbs.png)
2. 输入命令`use 数据库名` 切换到指定数据库，若无该数据库，MongoDB 将自动创建。
>**注意：**
>新创建的数据库不在`show dbs`显示列表中。要显示数据库，需要至少插入一个文档，空的数据库不显示。

	![](https://mc.qcloudimg.com/static/img/6c2b453eca2fbcff9f0dc7be0bf393d5/usetest.png)
3. 输入以下命令即可在该数据库下创建一个名为 newtest 的表。下列 id，name，by 均为该表中数据。
```
db.newtest.insert({id:1,name:"test",by:"tencentcloud"})
```
![](https://mc.qcloudimg.com/static/img/10a8cde0ee1ede52d99bd56f80a5c6ab/dbinsert.png)
4. 输入`show tables`或`show collections`即可查看该数据库中的表。
![](https://mc.qcloudimg.com/static/img/2f2c6868e0b01671678497f652538f58/showtables.png)

### 查询 NoSQL 表
1. 创建表成功后，可通过输入以下命令查询刚刚创建的 newtest 表内数据。
```
db.newtest.find()
```
![](https://mc.qcloudimg.com/static/img/d4a5637e7771848c41b6ad833b24d0a9/find.png)
2. 若需以格式化方式显示结果，可输入以下命令。
```
db.newtest.find().pretty()
```
![](https://mc.qcloudimg.com/static/img/36cd64b68f5d95f1a551c57bbf3cfb0a/findp.png)

### 删除 NoSQL 表
1. 若需要删除上述创建的 newtest 表中数据可输入以下命令。
```
db.newtest.remove({id:1})
```
>**注意：**
>命令`remove(参数)`括号中参数为指定删除条件，若无指定删除条件无法删除数据。

	![](https://mc.qcloudimg.com/static/img/20f22097a8a50428a6d21f378b5b2d65/remove.png)
2. 若需要删除 newtest 表，可输入以下命令。
```
db.newtest.drop();
```
![](https://mc.qcloudimg.com/static/img/9865dc8175f4ef3152e8c40874a91a8c/drop.png)