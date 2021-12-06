## 什么是自定义 DNS 

为了方便运维管理，您的作业可能会使用域名的方式访问外部资源（消息队列 CKafka、云数据库 MySQL等），您可以使用自定义 DNS 的方式进行域名解析。自定义 DNS 的原理请参考 Kubernetes 官网文档 [自定义 DNS 服务](https://kubernetes.io/zh/docs/tasks/administer-cluster/dns-custom-nameservers/)。您一般会使用两种方式来完成域名解析。

1. host 映射。如下示例，您可以使用 `kafka.example.com` 来访问 IP 为`172.17.0.2`的 CKafka 实例。
``` 
172.17.0.2 kafka.example.com 172.17.0.3 mysql.example.com 
``` 
2. DNS 域名解析。如下示例，假设您的 DNS 服务器地址为 `172.17.0.253` 和 `172.17.0.254`，您的作业中对任何 `*.example.com` 形式的域名访问，都会通过您的 DNS 服务器解析。您可以在 DNS 服务器中配置 `172.17.0.2 kafka.example.com` 的映射关系，那么 `kafka.example.com` 就能解析到地址 `172.17.0.2`。
```
 example.com { forward . 172.17.0.253 172.17.0.254 } 
```

## 如何自定义 DNS 

您可以在集群详情页里设置自定义 DNS。请注意：若您同时配置了 host 映射和 DNS 域名解析，优先选择 DNS 域名解析。 

### 操作步骤

1. 在 **[集群管理](https://console.cloud.tencent.com/oceanus/cluster) > 集群信息**中可设置自定义 DNS。
![](https://qcloudimg.tencent-cloud.cn/raw/d10aa240b3bbaf44bea0a20e761c6d74.png)
2. 在弹窗中设置 host 或域名，单击**确认**保存设置，保存后可以再次进行修改。
![](https://qcloudimg.tencent-cloud.cn/raw/a541dd9a30150e22bea18548ee2d6b00.png)



   
