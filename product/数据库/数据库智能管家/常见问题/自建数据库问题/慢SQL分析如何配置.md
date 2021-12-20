
### 步骤1：开启自建数据库慢日志记录
首先检查是否开启了慢日志记录，使用 root 帐号登录到自建数据库实例上执行如下命令：
```
mysql> show variables like 'slow%';
+---------------------+----------------------------------------+
| Variable_name       | Value                                  |
+---------------------+----------------------------------------+
| slow_launch_time    | 2                                      |
| slow_query_log      | ON                                     |
| slow_query_log_file | /data/mysql/VM_83_217_centos-slow.log  |
+---------------------+----------------------------------------+
```

如上，若 `slow_query_log` 一项的值为 `ON`，说明已经开启；若为 `OFF`，需要执行如下命令开启慢日志记录：
```
mysql> set global slow_query_log='ON';
```
>?该开启命令在实例重启后会失效，如需要将该配置持久化，可以修改数据库实例的配置文件（默认配置文件 `/etc/my.cnf`），在 mysqld 下添加如下内容：
>```
root@xxx ~ # vim /etc/my.cnf
[mysqld]
slow_query_log=ON
```

### 步骤2：修改慢日志文件访问权限
开启慢日志记录之后，agent 需要能够读取慢日志文件，慢 SQL 分析功能才能够正常使用。
首先在数据库实例上执行 `show variables like 'slow%'` 命令，查看慢日志记录文件所在位置：
```
mysql> show variables like 'slow%';
+----------------------+----------------------------------------+
| Variable_name        | Value                                  |
+----------------------+----------------------------------------+
| slow_launch_time     | 2                                      |
| slow_query_log       | ON                                     |
| slow_query_log_file  | /data/mysql/VM_83_217_centos-slow.log  |
+----------------------+----------------------------------------+
```

`slow_query_log_file`的值即为慢日志文件所在位置，需要将其上层目录修改为可访问权限，对于该 log 文件需要设置为可读权限：

```
root@xxx ~ # chmod 755 /data
对于上面的慢日志文件，其上层目录分别为 /data/mysql 和 /data，需要依次设置权限
root@xxx ~ # chmod 755 /data/mysql
然后该日志文件需要设置为可读
root@xxx ~ # chmod 644 /data/mysql/VM_83_217_centos-slow.log
```

### 步骤3：打开慢日志采集开关
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance?product=mysql)，在左侧导航选择【实例管理】页，在上方选择对应数据库。
2. 在实例管理页面，打开该数据库实例的慢日志采集开关，若开关可以正常打开且无报错，说明慢日志分析功能配置成功。
![](https://main.qcloudimg.com/raw/62156ebffeb2b0965552ca027abe100f.png)
