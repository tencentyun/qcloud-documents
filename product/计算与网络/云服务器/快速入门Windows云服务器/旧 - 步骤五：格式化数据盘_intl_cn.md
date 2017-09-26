当您购买了数据盘时，需要格式化才可使用。未购买数据盘的用户可以跳过此步骤。您也可以根据需要进行多分区操作。

这里以Windows 2012R2为例进行格式化说明。

1) 通过步骤四介绍的方法登录Windows云服务器。

2) 点击【开始】（Start）-【服务器管理器】（Server Manager）-【工具】（Tools）-【计算机管理】（Computer Management）-【存储】（Storage）-【磁盘管理】（Disk Management）。

3) 在需要格式化的新数据盘名称上，右键点击【联机】（Online），当硬盘状态变为“没有初始化”（Not initialized）时，再次右键点击【初始化磁盘】（Initialize Disk），选择分区形式（GPT或MBR），点击确定。此时数据盘状态变为“联机”（Online）。
![](//mccdn.qcloud.com/static/img/3c62dd8d230b5499da6c917089ed0d41/image.jpg)
![](//mccdn.qcloud.com/static/img/693871277717dd1dc7756854b4e9e694/image.jpg)

4) 在数据盘未分区的空间上右键点击【新建简单卷】（New Simple Volume...）；根据向导提示进行操作，输入分区磁盘的大小，点击【下一步】；选择文件系统，格式化分区，点击【下一步】；完成新建简单卷，点击【完成】按钮。
![](//mccdn.qcloud.com/static/img/fbb1e9cb80721560b4a758b8017b019e/image.jpg)
![](//mccdn.qcloud.com/static/img/70bfd169da281a95b8b1368639fb52de/image.jpg)
![](//mccdn.qcloud.com/static/img/3604c5457164497ddddbb121ef252341/image.jpg)
![](//mccdn.qcloud.com/static/img/2332c03f9f1f03892fea31b648303473/image.jpg)

5) 在计算机界面可以看到新分区的数据盘：
 ![](//mccdn.qcloud.com/static/img/8475471ad2cc2212c063c493655a79da/image.jpg)