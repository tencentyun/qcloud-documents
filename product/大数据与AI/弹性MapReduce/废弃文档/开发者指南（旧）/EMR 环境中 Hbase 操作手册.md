## 管理员类操作
登录 Hbase 的 shell 环境，登录方式为登录任意一台 EMR 集群机器（Common 类型的节点除外）。
登录后进入到目录 `/usr/local/service/hbase` 下, 执行`bin/hbase shell`,进入 shell ，可以执行以下命令：
列出 HBase 中的所有表：
```
hbase(main):001:0> list
TABLE
SYSTEM.CATALOG
SYSTEM.FUNCTION
SYSTEM.SEQUENCE
SYSTEM.STATS
4 row(s) in 0.1870 seconds
```
 创建表：
```
hbase(main):005:0* create 'test', 'cf'
0 row(s) in 1.2600 seconds
=> Hbase::Table - test
```
 插入数据：
```
hbase(main):006:0> put 'test', 'row1', 'cf:a', 'value1'
0 row(s) in 0.1730 seconds
```
 获取一条数据：
```
hbase(main):007:0> get 'test', 'row1'
COLUMN           CELL
cf:a             timestamp=1489644953264, value=value1
1 row(s) in 0.0320 seconds
```
 禁用表和启用表
```
hbase(main):008:0> disable 'test'
0 row(s) in 2.2760 seconds
hbase(main):009:0> enable 'test'
0 row(s) in 1.2560 seconds
```
更多资料可以参考 [Apache Hbase Shell](http://hbase.apache.org/book.html#shell) 。
### 查询数据
管理员操作情况下，进入 shell 控制台后可以通过 scan 或者 get 查询 “test” 集群的数据。
```
hbase(main):010:0> scan 'test'
ROW COLUMN+CELL
row1 column=cf:a, timestamp=1489644953264, value=value1
1 row(s) in 0.1020 seconds
```
更多相关命令请参考 [Apache Hbase Shell](http://hbase.apache.org/book.html#shell) 。
### 通过 API 方式访问 Hbase 集群
通过 Hbase 提供的标准 API 访问 Hbase 集群，可参考如下代码：
```
public static void createTable(String tableName, String[] familys) throws IOException {
  Admin admin = null;
  Connection con = null;
  try{
    Configuration config = HBaseConfiguration.create();
// 填写zookeeper 地址，多个地址用英文逗号隔开
    config.set("hbase.zookeeper.quorum", "10.66.133.178:2181");
// 设置重试参数
    config.setInt("hbase.client.retries.number", 1);
    TableName TABLE = TableName.valueOf(tableName);
    con = ConnectionFactory.createConnection(config);
    admin = con.getAdmin();
    if (admin.tableExists(TABLE)){
      System.out.println("table already exists!");
    } else {
      HTableDescriptor tableDesc = new HTableDescriptor(TABLE);
      for (int i = 0; i < familys.length; i++) {
       tableDesc.addFamily(new HColumnDescriptor(familys[i]));
      }
      admin.createTable(tableDesc);
      System.out.println("create table " + tableName + " ok.");
    }
  }catch(IOException e){
    e.printStackTrace();
  }finally{
    admin.close();
    con.close();
  }
}
```
更多资料请参考 [Apache Hbase APIs](https://hbase.apache.org/book.html#_examples)。
### Hbase 和 MapReduce
请参考 [Hbase and MapReduce](https://hbase.apache.org/book.html#mapreduce)。
### 通过 Phoenix 以 SQL 的形式访问 Hbase 集群
下载 Phoenix 安装包：
```
wget https://mirrors.tuna.tsinghua.edu.cn/apache/phoenix/
      apache-phoenix-4.8.2-HBase-1.2/bin/
      apache-phoenix-4.8.2-HBase-1.2-bin.tar.gz
```
解压 Phoenix 安装包：
```
tar -xvf apache-phoenix-4.8.2-HBase-1.2-bin.tar.gz
```
安装  Phoenix ：
```    
cd apache-phoenix-4.8.2-HBase-1.2/bin
```
SQL 控制台操作：
```
./sqlline.py 10.0.1.5:2181
// 10.0.1.5:2181 为zookeeper 地址
```
创建表：
```
0: jdbc:phoenix:10.0.1.5:2181> CREATE TABLE IF NOT EXISTS us_population (
. . . . . . . . . . . . . . .> state CHAR(2) NOT NULL,
. . . . . . . . . . . . . . .> city VARCHAR NOT NULL,
. . . . . . . . . . . . . . .> population BIGINT
. . . . . . . . . . . . . . .> CONSTRAINT my_pk PRIMARY KEY (state, city));
No rows affected (1.643 seconds)
```
查询：
```
0: jdbc:phoenix:10.0.1.5:2181>
select TABLE_SCHEM,TABLE_NAME,COLUMN_NAME from SYSTEM.CATALOG limit 10;
```
查询结果如下：
![](//mc.qcloudimg.com/static/img/5636b538cf1d4d70f769d22df9cb9dd5/image.png)
	`10 rows selected (0.305 seconds)`
更多 Phoenix 相关资料请参考 [Phoenix](http://phoenix.apache.org/Phoenix-in-15-minutes-or-less.html) 。
### 通过 Hue 操作 Hbase
登录 Hue，并进入如下页面:
![](//mc.qcloudimg.com/static/img/a5f5a6421305d6593390eaf3dd388a05/image.png)
Hbase 表列表，如下图：
![](//mc.qcloudimg.com/static/img/784abba01f5ab6b3b0bb2da0ae9cdee9/image.png)
勾选表可以对表进行启用、禁用、删除操作。
单击【New Table】按钮可以创建新表，如下图：
![](//mc.qcloudimg.com/static/img/7937f38f16ed880a874c505aa2e92638/image.png)
 输入表名和要添加的列族然后单击【Submit】按钮即可。
在 Hbase 列表单击其中的一个表可以对表的数据进行管理，如下图：
![](//mc.qcloudimg.com/static/img/b5afa5b5f749dfee33cc070e4d0c3a07/image.png)
在该页面可以删除单元格也可以添加单元格数据。
还可以通过搜索框查找快速定位想要查询的数据。


