1. 准备工作流数据

    Hue 的任务调度基于工作流，我们先创建一个包含 Hive script 脚本的工作流，Hive script 脚本的内容如下:

    ``` sql
    create database if not exists hive_sample;
    show databases;
    use hive_sample;
    show tables;
    create table if not exists hive_sample (a int, b string);
    show tables;
    insert into hive_sample select 1, "a";
    select * from hive_sample;
    ```

    将以上内容保存为 hive_sample.sql 文件, Hive 工作流还需要一个 hive-site.xml 配置文件，这个配置文件可以在集群中安装了 Hive 组件的节点上找到。具体的路径在： /usr/local/service/hive/conf/hive-site.xml, 复制一个 hive-site.xml 文件，将其中对应配置修改为如下值

    ``` xml
    <property>
      <name>hive.exec.local.scratchdir</name>
      <value>/tmp/hive</value>
    </property>
    <property>
      <name>hive.downloaded.resources.dir</name>
      <value>/tmp/hive/${hive.session.id}_resources</value>
    </property>
    <property>
      <name>hive.querylog.location</name>
      <value>/tmp/hive</value>
    </property>
    <property>
      <name>hive.server2.logging.operation.log.location</name>
      <value>/tmp/hive/tmp/operation_logs</value>
    </property>
    ```
    
2. 创建工作流

    在 Hue 页面中选择 Workflows -> Editors -> Workflows

    ![创建工作流](https://mc.qcloudimg.com/static/img/d370180a4d6886b335e199cf045dcab9/5-8-2-1.png)

    单击“create”

    ![creat](https://mc.qcloudimg.com/static/img/51aab5e3987b1a627c9914667317bc89/5-8-2-2.png)

    进入当前 workflow 的 HDFS 空间

    ![进入HDFS](https://mc.qcloudimg.com/static/img/ad9c45d94cb125df03b434191b4ce806/5-8-2-3.png)

    上传 Hive script 文件和 hive-site.xml, 并在 lib 目录中加入 mySQL 的 jdbc jar 包

     ![加入包](https://mc.qcloudimg.com/static/img/18dc191755cdb726c862942c3dc9c51e/5-8-2-4.png  )

    在工作流编辑页面中拖一个 Hive

    ![编辑页面](https://mc.qcloudimg.com/static/img/9eca15617a835b1f0828ef9501810dda/5-8-2-5.png)

    选择刚刚上传的 Hive scipt 文件和 hive-site.xml 文件

    ![选择文件](https://mc.qcloudimg.com/static/img/8aba3d74764e60f739dcb0caf15ad1ac/5-8-2-6.png)

    保存当前 workflow

3. 创建定时任务

    Hue 的定时任务是 coordinator, 类似于 Linux 的 crontab，支持的调度粒度可以到分钟级别, 选择 Workflows -> Editors -> Coordinator -> Create，创建 coordinator

    ![创建定时](https://mc.qcloudimg.com/static/img/e0e18b6ee297fc42a30b741371a47098/5-8-2-7.png)

    单击 "choose a workflow...", 选择一个创建好的流程

    ![选择流程](https://mc.qcloudimg.com/static/img/7636daf7c05d7691291a93406e851783/5-8-2-8.png)

    选择需要调度的粒度和时间间隔，可以多选，用于支持多个时间间隔

    ![选择粒度](https://mc.qcloudimg.com/static/img/e8d8649600f3b22be693dbb8fa80d603/5-8-2-9.png)

4. 执行定时任务

    选择 coordinator 的执行时间区间，然后单击"submiT"

    ![执行定时](https://mc.qcloudimg.com/static/img/a145f4c79bac4a69797fb669bde921cf/5-8-2-10.png)

    在 coordinator 的监控页面可以看到 coordinator 的调度情况    

    ![监控](https://mc.qcloudimg.com/static/img/1f0f8cbc0164c31c6ac9a7b4e069ecdf/5-8-2-11.png)

除此以外 Hue 还支持管理 HDFS 上的数据、Hbase 数据管理，Yarn 任务管理等，更多资料请参考 [这里](http://gethue.com/blog/)
