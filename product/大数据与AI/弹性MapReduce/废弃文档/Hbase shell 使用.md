Hbase Shell  在 EMR 集群的机器中可直接使用。方法如下：

- 环境准备

    1. ssh 登录 EMR 集群任意一台 CVM
    2. 切换到 Hadoop 用户
    3. EMR 集群已经帮用户设定了相应的环境变量，直接通过 Hbase Shell 使用

    ``` shell
    su hadoop
    hbase shell
    ```

- 查看帮助

    ``` shell
    hbase(main):001:0>help
    ```

- 创建表

    ``` shell
    base(main):001:0> create ’user_info’,{NAME => ’i’}
    ```

- 插入数据

    ``` shell
    hbase(main):003:0* put ’user_info’,’1660063’,’i:name’,’sundy’
    hbase(main):004:0> put ’user_info’,’1660063’,’i:gender’,’Male’
    hbase(main):005:0> put ’user_info’,’1660063’,’i:age’,’26’
    hbase(main):006:0> put ’user_info’,’1660063’,’i:address’,’City CD’
    ```

- 查询表数据

    ``` shell
    scan’user_info’,{STARTROW=>’1660063’,STOPROW=>’1660063’,COLUMNS=>[’i:name’,’i:address’]}
    ```

- 表禁用启用操作

    ``` shell
    hbase(main):013:0> disable’user_info’
    hbase(main):013:0> enable’user_info’
    ```

- 删除表

    ``` shell
    hbase(main):014:0> drop ’user_info’
    ```