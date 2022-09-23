当前 EMR-V2.1.0及以后的版本都支持 kerberos 创建安全类型集群，即集群中除 alluxio、zepplin、kylin 外所有已支持的开源组件以 Kerberos 的安全模式启动，在这种安全环境下，只有经过认证的客户端（Client）才能访问集群的服务（Service，例如 HDFS）。

>!impala 服务组件仅支持 EMR-V3.1.0 及以后的版本，以 kerberos 的安全模式启动。

## 重要概念

| 全称                    | 简称 | 作用                                                         |
| ----------------------- | ---- | ------------------------------------------------------------ |
| key distributed center  | KDC  | 整个安全认证过程的票据生成管理服务，其中包含两个服务：AS 和 TGS。 |
| authentication service  | AS   | 为 client 生成 TGT 的服务。                                  |
| ticket granting service | TGS  | 为 client 生成某个服务的 ticket。                            |
| account database        | AD   | 存储所有 client 的白名单，只有存在于白名单的 client 才能顺利申请到 TGT。 |
| ticket-granting ticket  | TGT  | 用于获取 ticket 的票据。                                     |
| client                  | -    | 想访问某个 server 的客户端。                                 |
| server                  | -    | 提供某种业务的服务。                                         |

## 其他概念

| 全称 | 作用 | 
|---------|---------|
| principal | 认证的主体，即“用户名”。 | 
|   realm |realm 有点像编程语言中的 namespace。在编程语言中，变量名只有在某个 namespace 里才有意义。同样的，一个 principal 只有在某个 realm 下才有意义。所以 realm 可以看成是 principal 的一个“容器”或者“空间”。相对应的，principal 的命名规则是 what_name_you_like@realm。在 kerberos，约定成俗用大写来命名 realm，例如：EXAMPLE.COM。    |
| password     |  某个用户的密码，对应于 kerberos 中的 master_key。password 可以存在一个 keytab 文件中。所以 kerberos 中需要使用密码的场景都可以用一个 keytab 作为输入。   |
|  credential   |   credential 是“证明某个人确定是他自己/某一种行为的确可以发生”的凭据。在不同的使用场景下，credential 的具体含义也略有不同： <li> 对于某个 principal 个体而言，他的 credential 就是他的 password。</li> <li> 在 kerberos 认证的环节中，credential 就意味着各种各样的 ticket。</li>   |

## 认证流程
client 访问 server 的过程中，想确保 client 和 server 都是可靠的，必然要引入第三方公证平台，因此有了 AS 和 TGS 这两个服务，AS 与 TGS 通常位于同一个服务进程中，对于 mit 的 kerberos 实现，均由 kdc 提供。

认证流程分为以下三步：
1. client 向 kerberos 服务请求，希望获取访问 server 的权限。kerberos 首先判断 client 是否可信赖，通过在 AD 中存储黑名单和白名单来区分 client。成功后，AS 返回 TGT 给 client。
2. client 得到了 TGT 后，继续向 kerberos 请求，希望获取访问 server 的权限。kerberos 通过 client 消息中的 TGT，判断 client 拥有权限，给 client 访问 server 的权限 ticket。
3. client 得到 ticket 后，就可以访问 server 了，但这个 ticket 只是针对这个 server，访问其他 server 需要重新向 TGS 申请。
![](https://main.qcloudimg.com/raw/dfc320a8b310df3ddbdda8ebcedaa7c0.png)
