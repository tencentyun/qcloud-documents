对于一个启用了 Kerberos 的正式生产系统，还需要考虑 KDC 的高可用。而 Kerberos 服务是支持配置为主备模式的，数据同步是通过 kprop 服务将主节点的数据同步到备节点。在购买了腾讯云 EMR 高可用安全集群后，Kerberos 默认是高可用的，用户无需任何配置。


本文主要介绍 Kerberos 服务高可用的相关配置和使用。

## 前提条件
- 已购买腾讯云 EMR 高可用集群。
- 购买集群时，已选择开启 Kerberos 认证。

## KDC 高可用配置介绍

配置`/etc/krb5.conf`文件，设置如下：
>!示例中配置了两个 KDC 地址，active kdc 和 backup kdc，这样能保证当其中任意一个 KDC 服务异常时，仍可以对集群提供正常的 KDC 服务。
>
```
[libdefaults]
dns_lookup_realm = false
ticket_lifetime = 24h
renew_lifetime = 7d
forwardable = true
rdns = false
default_realm = REALM
default_tgs_enctypes = des3-cbc-sha1
default_tkt_enctypes = des3-cbc-sha1
permitted_enctypes = des3-cbc-sha1

[realms]
REALM = {
kdc = active_kdc:88
admin_server = active_kdc
kdc = backup_kdc:88
admin_server = backup_kdc 
}

[domain_realm]
# .example.com = EXAMPLE.COM
```

## KDC 数据同步
-  kprop 配置
在两个 kdc server 上默认有`/var/kerberos/krb5kdc/kpropd.acl`配置文件。
```
host/active_kdc@REALM
host/backup_kdc@REALM
```
2. 执行`/var/kerberos/krb5kdc/kpropd.acl`文件
执行默认配置文件`/var/kerberos/krb5kdc/kpropd.acl`后，两个 kdc server 上会生成`/etc/krb5.keyta`文件。同时，两个 kdc server 也会启动 kprop 服务。
```
[root@10 krb5kdc]# service kprop status 
Redirecting to /bin/systemctl status kprop.service
kprop.service - Kerberos 5 Propagation
Loaded: loaded (/usr/lib/systemd/system/kprop.service; disabled; vendor preset: disabled)
Active: active (running) since Thu 2020-05-07 15:33:35 CST; 1h 9min ago
Process: 3752 ExecStart=/usr/sbin/_kpropd $KPROPD_ARGS (code=exited, status=0/SUCCESS)
Main PID: 3753 (kpropd)
CGroup: /system.slice/kprop.service
└─3753 /usr/sbin/kpropd
```
4. 周期性同步 kdc 数据指令
EMR agent 会周期性（默认5分钟）将 active kdc 的 principals 同步到 backup kdc，保证两个 kdc 上的数据是同步的。会在 active kdc 周期性执行如下同步指令：
```
kdb5_util dump /var/kerberos/krb5kdc/master.dump & kprop -f /var/kerberos/krb5kdc/master.dump -d -P 754 backup_kdc
```

## 结果验证

1. 在 active kdc 上执行如下命令。
```
kadmin.local "-q addprinc -randkey test"
```
2. 在 backup kdc 上可以看到新增的 principal，说明 kdc 之间已完成数据同步，这里需要等待一段时间（默认5分钟）。
```
kadmin.local "-q listprincs"|grep test
```

 
