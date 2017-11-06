EMR Phoenix 编译的是 4.8.1 版本，首先下载一个 phoenix-4.8.1-HBase-1.2 版本客户端

- 下载 Phoenix 客户端[点击下载](https://archive.apache.org/dist/phoenix/apache-phoenix-4.8.1-HBase-1.2/bin/)

- 客户端环境准备把下载好的客户端包拷贝并解压到 EMR 集群任意一个节点的任意一个目录下（推荐  Hadoop 主目录），进入解压后 Hbin 目录，拷贝 Hbase 配置文件 Hbase-site.xml 到此目录：

    ``` shell
    cp /usr/local/service/hbase/conf/hbase-site.xml 
    ```

切换成 Hadoop 用户，使用 Phoenix 的 python 命令行工具：

    ``` shell
    ./sqlline.py
    ```

成功后会显示成这种方式：

![配置成功](https://mc.qcloudimg.com/static/img/18a364f4f014c8df2edcd89ded877e34/5-4-1.png)