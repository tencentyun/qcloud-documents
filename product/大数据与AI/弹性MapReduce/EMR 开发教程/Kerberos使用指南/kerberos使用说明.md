本文使用 mit 的 kerberos 来作为 kdc 服务。假设 kdc 服务已安装并启动，使用 kerberos，首先要创建域（realm），再添加相关角色的 principal（包括 server 和 client），然后生成 keytab 文件。

## 创建数据库
使用`kdb5_util`命令创建数据库，存放 principal 相关的信息。
```
kdb5_util -r EXAMPLE.COM create -s
Initializing database '/var/krb5/principal' for realm 'EXAMPLE.COM'
master key name 'K/M@EXAMPLE.COM'
You will be prompted for the database Master Password.
It is important that you NOT FORGET this password.
Enter KDC database master key: <Type the key>
Re-enter KDC database master key to verify: <Type it again>
```

## 添加 principal
```
 kadmin.local
 kadmin.local: add_principal -pw testpassword test/host@EXAMPLE.COM

 WARNING: no policy specified fortest/host@EXAMPLE.COM; defaulting to no policy
 Principal "test/host@EXAMPLE.COM" created.
```

## 生成密钥表文件
```
 kadmin.local
 kadmin.local: ktadd -k /var/krb5kdc/test.keytab test/host@EXAMPLE.COM

 Entry for principal test/host@EXAMPLE.COM with kvno 2, encryption type des3-cbc-sha1 added to keytab WRFILE:/var/krb5kdc/test.keytab.
```
这里，我们创建了新的用户：test/host@EXAMPLE.COM ，并且将这个用户的密钥放置到 `/var/krb5kdc/test.keytab` 文件中。

## 启动 kdc
```
 service krb5-kdc start
 * Starting Kerberos KDC krb5kdc       
```

## kinit 验证
```
kinit -k -t /etc/krb5.keytab test-client/host@EXAMPLE.COM
```
kinit 对应的是向 kdc 获取 TGT 的步骤。它会向`/etc/krb5.conf`中指定的 kdc server 发送请求。如果 TGT 请求成功，使用 klist 即可看到。
```
klist
Ticket cache: FILE:/tmp/krb5cc_1000
Default principal: test-client/host@EXAMPLE.COM

Valid starting       Expires              Service principal
2019-01-15T17:50:25  2019-01-16T17:50:25  krbtgt/EXAMPLE.COM@EXAMPLE.COM
renew until 2019-01-16T00:00:25
```

## 在项目中使用
使用 kinit 验证成功后，可以把 keytab 文件复制到需要使用的 server 和 client 的服务器上，并配置相应的 principal 进行使用。

