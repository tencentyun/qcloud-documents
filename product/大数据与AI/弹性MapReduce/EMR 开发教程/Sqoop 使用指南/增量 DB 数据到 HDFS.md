ed 更新模式，append 模式用在数据只增加但没有更新的场景，lastmodified 模式用在数据不但有增加且有更新的模式。

- 使用 append 模式

    在表 sqoop_test 表中新增一条数据, 如下：

    ``` sql
    mysql select * from sgoop_test
    +----+--------+---------------------+---------+
    | id | title  | time                | content |
    +----+--------+---------------------+---------+
    |  1 | first  | 2017-09-30 15:53:03 | hdfs    |
    |  2 | second | 2017-09-30 15:53:30 | mr      |
    |  3 | third  | 2017-09-30 15:53:43 | yarn    |
    |  4 | forth  | 2017-09-30 16:28:05 | hive    |
    +----+--------+---------------------+---------+
    4 rows in set (0.00 sec)
    ```

    执行数据导入

    ``` shell
    ./sqoop-import --connect jdbc:mysql://172.31.20.31/test --username root --password ****** --table sqoop_test --check-column id --incremental append
    --last-value 3 --target-dir /sqoopTest
    #--last-value参数指定以前导入的row的最大值。
    ```

    导出成功后您可以在 HDFS 查看导出的数据，如果不想手动指定 –last-value 的值，可以使用 sqoop job 的方
    式，Sqoop 会自动保存上次导入成功的 last-value 值。如果要使用 sqoop job。需要启动 sqoop-metastore 进程，
    操作步骤如下：

    1. 在 sqoop-sit.xml 中开启服务

        ``` xml
        <property>
          <name>sqoop.metastore.client.enable.autoconnect</name>
          <value>ture</value>
        </property>
        ```

    2. 启动服务

        ``` shell
        ./sqoop-metastore &
        ```

        执行导入

        ``` shell
        ./sqoop job --create job1 -- import --connect jdbc:mysql://172.31.20.31/test
        --username root --password ******** --table sqoop_test --check-column id
        --incremental append --last-value 4 --target-dir /sqoopTest
        ```

        创建JOB 后，查看JOB 信息

        ```shell
        [hadoop@172 bin]$ ./sqoop job --list
        Warning: /usr/local/service/sqoop/bin/../../hcatalog does not exist! HCatalog jobs will fail.
        Please set $HACT_HOME to the root of your catalog installation
        Warning: /usr/local/service/sqoop/bin/../../accumulo does not exist! Accumulo imports will fail.
        Please set $ACCUMULO_HOME to the root of your Accumulo installation.
        Warning: /usr/local/service/sqoop/bin/../../zookeeper does not exist! Accumulo imports will fail.
        Please set $ZOOKEEPER_HOME to the root of your Zookeeper installation.
        17/09/30 17:05:16 INFO sqoop.Sqoop Running Sqoop version: 1.4.6
        SLF4J: Class path contains multiple SLF4J bindings.
        SLF4J: Found binding in [jar:file:/usr/local/service/hadoop/share/hadoop/common/lib/slf4j-log4j12-1.7.1   .jar!/org/slf4j/impl/StaticLoggerBinder.class]
        SLF4J: Found binding in [jar:file: /usr/local/service/hbase/lib/slf4j-log4j12-1.7.10.jar!/org/slf4j/impl/StaticLoggerBinder.class]
        Staticloggerbinder . class ]
        SLF4J: See http:/www.slf4j.org/codes.html#multiple_bindings for an explanation.
        SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
        Available jobs:
           job 1
        [hadoop@172 bin]$
        ```

        新增数据
        
        ``` sql
        insert into sqoop_test_values(null,’fifth’,’spark’);
        ```

        执行JOB

        ``` shell
        ./sqoop job --exec job1
        ```

        任务执行成功后，您可以去 HDFS 查看新导入过来的数据。

- 使用 lastmodified 模式

    查询出最近的更新时间

    ``` sql
    select max(time) from sqoop_test
    ```

    创建Job

    ```shell
    ./sqoop job --create job2 -- import --connect jdbc:mysql://172.31.20.31/test
    --username root --password ********* --table sqoop_test --merge-key id
    --check-column time --incremental lastmodified --last-value ’2017-09-30
    17:11:37’ --target-dir /sqoopTest
    ```

    更新老数据

    ``` shell
    mysql> update sqoop_test set time=now(), content='AAAAA' where id = 1
        -> ;
    Query OK, 1 row affected (0.00 sec)
    Rows matched: 1 changed: 1 warnings: 0
    mysql> insert into sqoop_test values(null, 'seventh', now(), 'hbase')
    Query OK, 1 row affected (0.00 sec)
    mysql select * from sgoop_test;
    +----+---------+---------------------+---------+
    | id | title   | time                | content |
    +----+---------+---------------------+---------+
    |  1 | first   | 2017-09-30 17:30:57 | AAAAA   |
    |  2 | second  | 2017-09-30 15:53:30 | mr      |
    |  3 | third   | 2017-09-30 15:53:43 | yarn    |
    |  4 | forth   | 2017-09-30 16:28:05 | hive    |
    |  5 | fifth   | 2017-09-30 17:07:04 | spark   |
    |  6 | sixth   | 2017-09-30 17:11:37 | kyin    |
    |  7 | seventh | 2017-09-30 17:31:21 | hbase   |
    +----+---------+---------------------+---------+   
    7 rows in set (0.00 sec)
    ```

    执行JOB

    ``` shell
    ./sqoop job --exec job1
    ```
