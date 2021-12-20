## Hadoop 命令
### 未获取 ticket
当已启用 kerberos 时，执行 hadoop 命令时都需要提前获取 ticket。如果没有获取 ticket，则会出现如下错误信息：
```
hadoop fs -ls /
19/04/19 19:59:03 WARN ipc.Client: Exception encountered while connecting to the server : javax.security.sasl.SaslException: GSS initiate failed [Caused by GSSException: No valid credentials provided (Mechanism level: Failed to find any Kerberos tgt)]
ls: Failed on local exception: java.io.IOException: javax.security.sasl.SaslException: GSS initiate failed [Caused by GSSException: No valid credentials provided (Mechanism level: Failed to find any Kerberos tgt)]; Host Details : local host is: "172.30.0.27/172.30.0.27"; destination host is: "172.30.0.27":4007; 
```

### 获取 ticket
前提：hadoop@EMR 的 principal 已添加。
```
kinit -kt /var/krb5kdc/emr.keytab hadoop@EMR
```
执行命令即可正常访问。
```
hadoop fs -ls /

Found 8 items
-rw-r--r--   3 hadoop supergroup       3809 2019-03-06 11:10 /README.md
drwxr-xr-x   - hadoop supergroup          0 2019-01-14 21:43 /apps
drwxrwx---   - hadoop supergroup          0 2019-01-17 19:46 /emr
drwxr-xr-x   - hadoop supergroup          0 2019-01-23 20:02 /hbase
drwxr-xr-x   - hadoop supergroup          0 2019-03-07 11:10 /spark-history
drwx-wx-wx   - hadoop supergroup          0 2019-03-06 20:23 /tmp
drwxr-xr-x   - hadoop supergroup          0 2019-01-17 14:43 /user
drwxr-xr-x   - hadoop supergroup          0 2019-01-17 19:43 /usr
```

## Java 代码访问 HDFS
### 使用本地 ticket
>!需要提前执行 kinit 获取 ticket，ticket 过期后程序会访问异常。
>
```java
public static void main(String[] args) throws IOException {
	Configuration conf = new Configuration();
	conf.addResource(new Path("/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml"));
	conf.addResource(new Path("/usr/local/service/hadoop/etc/hadoop/core-site.xml"));
	UserGroupInformation.setConfiguration(conf);
	UserGroupInformation.loginUserFromSubject(null);
	FileSystem fileSystem = FileSystem.get(conf);
	FileStatus[] fileStatus = fileSystem.listStatus(new Path("/"));
	for (int i = 0; i < fileStatus.length; i++) {
		System.out.println(fileStatus[i].getPath());
	}
}
```

### 使用 keytab 文件
```java
public static void main(String[] args) throws IOException {
	Configuration conf = new Configuration();
	conf.addResource(new Path("/usr/local/service/hadoop/etc/hadoop/hdfs-site.xml"));
	conf.addResource(new Path("/usr/local/service/hadoop/etc/hadoop/core-site.xml"));
	UserGroupInformation.setConfiguration(conf);
	UserGroupInformation.loginUserFromKeytab("hadoop@EMR", "/var/krb5kdc/emr.keytab");
	FileSystem fileSystem = FileSystem.get(conf);
	FileStatus[] fileStatus = fileSystem.listStatus(new Path("/"));
	for (int i = 0; i < fileStatus.length; i++) {
		System.out.println(fileStatus[i].getPath());
	}
}
```
