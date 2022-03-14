本文介绍 Hadoop 如何修改配置接入 kerberos。如果是通过腾讯云 EMR 购买的安全集群，系统会自动配置好，无需自行配置。

## 前提条件
- kdc 服务已搭建成功。
- Hadoop 相关的 principals 已创建完成。
- keytab 文件分发到了各台服务器上（假设 keytab 文件路径为 `/var/krb5kdc/emr.keytab`）。

## Hadoop 接入 kerberos
Hadoop 主要包含 HDFS 和 Yarn 服务，需要分别修改这两部分配置并重启服务进程。

### HDFS 接入
#### 修改 core-site.xml
```properties
hadoop.security.authentication: kerberos
hadoop.security.authorization: true
```

#### 修改 hdfs-site.xml
```properties
dfs.namenode.kerberos.principal: hadoop/_HOST@EMR
dfs.namenode.keytab.file: /var/krb5kdc/emr.keytab
dfs.namenode.kerberos.internal.spnego.principal: HTTP/_HOST@EMR
dfs.secondary.namenode.kerberos.principal: hadoop/_HOST@EMR
dfs.secondary.namenode.keytab.file: /var/krb5kdc/emr.keytab
dfs.secondary.namenode.kerberos.internal.spnego.principal: HTTP/_HOST@EMR
dfs.journalnode.kerberos.principal: hadoop/_HOST@EMR
dfs.journalnode.keytab.file: /var/krb5kdc/emr.keytab
dfs.journalnode.kerberos.internal.spnego.principal: HTTP/_HOST@EMR
dfs.datanode.kerberos.principal: hadoop/_HOST@EMR
dfs.datanode.keytab.file: /var/krb5kdc/emr.keytab
dfs.datanode.data.dir.perm: 700
dfs.web.authentication.kerberos.keytab: /var/krb5kdc/emr.keytab
dfs.web.authentication.kerberos.principal: HTTP/_HOST@EMR
ignore.secure.ports.for.testing: true
```

>!ignore.secure.ports.for.testing 选项必须设置为 true，否则必须配置 sasl 模式，且 webhdfs 必须启用 HTTPS。

#### 修改 httpfs-site.xml（如果启用 httpfs）
```properties
httpfs.authentication.type: kerberos
httpfs.hadoop.authentication.type: kerberos
httpfs.authentication.kerberos.principal: HTTP/_HOST@EMR
httpfs.hadoop.authentication.kerberos.principal: hadoop/_HOST@EMR
httpfs.authentication.kerberos.keytab: /var/krb5kdc/emr.keytab
httpfs.hadoop.authentication.kerberos.keytab: /var/krb5kdc/emr.keytab
```

### Yarn 接入
#### 修改 yarn-site.xml
```properties
yarn.resourcemanager.keytab: /var/krb5kdc/emr.keytab
yarn.resourcemanager.principal: hadoop/_HOST@EMR
yarn.nodemanager.keytab: /var/krb5kdc/emr.keytab
yarn.nodemanager.principal: hadoop/_HOST@EMR
```

#### 修改 mapred-site.xml
```properties
mapreduce.jobhistory.keytab: /var/krb5kdc/emr.keytab
mapreduce.jobhistory.principal: hadoop/_HOST@EMR
```

