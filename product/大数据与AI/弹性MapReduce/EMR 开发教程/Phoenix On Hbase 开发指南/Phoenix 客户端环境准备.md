Phoenix 查询引擎支持使用 SQL 进行 HBase 数据的查询，会将 SQL 查询转换为一个或多个 HBase API，协同处理器与自定义过滤器的实现，并编排执行。使用 Phoenix 进行简单查询，其性能量级是毫秒，对于百万级别的行数来说，其性能量级是秒。EMR 中选择 Hbase 组件的集群，默认编译并启动 Phoenix 引擎。

EMR Phoenix 编译的是4.8.1版本，首先下载一个 phoenix-4.8.1-HBase-1.2 版本客户端。
- [下载 Phoenix 客户端](https://archive.apache.org/dist/phoenix/apache-phoenix-4.8.1-HBase-1.2/bin/)
- 客户端环境准备把下载好的客户端包拷贝并解压到 EMR 集群任意一个节点的任意一个目录下（推荐 Hadoop 主目录），进入解压后 bin 目录，拷贝 Hbase 配置文件 Hbase-site.xml 到此目录：
``` shell
cp /usr/local/service/hbase/conf/hbase-site.xml 目的路径
```
 切换成 Hadoop 用户，使用 Phoenix 的 Python 命令行工具：
``` 
./sqlline.py
```
执行成功后显示如下：
![配置成功](https://mc.qcloudimg.com/static/img/18a364f4f014c8df2edcd89ded877e34/5-4-1.png)
