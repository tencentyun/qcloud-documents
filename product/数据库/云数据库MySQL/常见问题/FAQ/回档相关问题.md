### MySQL 回档时是否会把当前表数据覆盖？
回档操作会产生新的数据库或表至原实例中。回档完后，您可以看到原来的数据库或表，以及新建的数据库或表。回档后的库表名是原库表名_bak。

### MySQL 误删了数据如何恢复？
通过回档恢复解决。不过回档仅支持回档到 5 天内的任意时间节点。

可以参考 [数据回档](https://cloud.tencent.com/document/product/236/7276) 教程 。
### MySQL 如何批量回档？
请参考 [批量回档](https://cloud.tencent.com/document/product/236/8466#.E6.89.B9.E9.87.8F.E5.9B.9E.E6.A1.A3)。

### MySQL 执行某个存储过程中误删了部分未备份的数据，能否还原数据？
可以使用控制台的回档功能 。
可以恢复五天之内任意时间点的数据 。
![](//mc.qcloudimg.com/static/img/06dc8e407e02ea57a9754f07a92118f3/image.png)

### MySQL 回档过程中，如何实时查询回档进度？
回档过程中，可实时查询回档的进度。
详细操作请参考 [数据回档](https://cloud.tencent.com/document/product/236/7276) 文档。

### MySQL 回档过程中是否可以实时查询回档日志？
回档过程中，可实时查询回档的进度。
详细请参考 [数据回档](https://cloud.tencent.com/document/product/236/7276)  文档。

### MySQL 如何实例回档？
详细操作可以参考 [数据回档](https://cloud.tencent.com/document/product/236/7276) 教程 。
