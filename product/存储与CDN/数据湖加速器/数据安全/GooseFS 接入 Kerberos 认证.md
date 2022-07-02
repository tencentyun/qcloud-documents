# GooseFS 接入 Kerberos 认证

## 概述

Kerberos 是大数据生态系统中广泛应用的统一认证服务，GooseFS 作为大数据和数据湖场景下的加速存储，支持集群节点和用户访问接入 Kerberos 认证服务中。本文将详细地介绍如何配置 GooseFS 接入 Kerberos 认证服务以及如何使用 Hadoop Delegation Token 认证。

## GooseFS 接入 Kerberos 的认证架构

![GooseFS Kerbero 认证流程](/Users/yuyang/qcloud-documents/product/存储与CDN/数据湖加速器/数据安全/pics/GooseFS Kerberos 认证基本流程.png)

### GooseFS Kerberos 认证优势

- 与 HDFS 接入 Kerberos 的认证架构和流程基本一致，在 HDFS 上启用了 Kerberos 认证流程的应用可以很容易地迁移到 GooseFS 上来；
- 支持 Hadoop 的 Delegation Token 认证机制，因此可以很好地兼容 Hadoop 生态的应用作业。

## 配置 GooseFS 接入 Kerberos 认证

### 前置条件

- GooseFS 1.3.0 及以上版本；
- 环境中有已经存在的 Kerberos KDC 服务，并且 GooseFS 以及应用客户端能够正常访问到这个 Kerberos KDC 服务相关端口。

### 在 Kerberos KDC 中创建 GooseFS 相关的身份信息

首先我们需要在 Kerberos KDC 中创建 GooseFS 集群 Server 与 Client 相关的 Kerberos 身份信息，才能继续后续的接入配置。这里我们在 **Kerberos KDC 服务器**上借助 `kadmin.local` 这个交互式工具来完成创建（注意：这个工具需要 root/sudo 权限执行）：

```shell
$ sudo kadmin.local
```

如果执行成功，则进入了 kadmin 的交互式 shell 环境中：

```shell
Authenticating as principal root/admin@GOOSEFS.COM with password.
kadmin.local:  
```

其中，`kadmin.local` 该交互式执行环境的命令提示符。

#### 创建 GooseFS Server / Client 相关的身份信息

这里通过一个简单测试集群以及应用场景样例来说明整个 Kerberos 的配置过程。

##### 集群环境说明

采用单 Master 双 Worker 的 Standalone 部署架构：

- Master（JobMaster）：172.16.0.1
- Worker1（JobWorker1）：172.16.0.2
- Worker2（JobWorker2）：172.16.0.3
- Client：172.16.0.4

##### 在 `kadmin.local` 中创建 Server 和 Client 身份认证相关信息

```shell
kadmin.local: addprinc -randkey goosefs/172.16.0.1@GOOSEFS.COM
kadmin.local: addprinc -randkey client/172.16.0.4@GOOSEFS.COM
```

注意，这里使用 `-randkey` 选项的原因在于 GooseFS 无论 Server 还是 Client 登陆都使用 `keytab` 文件来认证，不使用明文密码。若身份信息需要用于 password 登陆场景，则可以去掉该选项。

##### 生成导出每个身份对应的 `keytab` 文件：

```shell
kadmin.local: xst -k goosefs_172_16_0_1.keytab goosefs/172.16.0.1@GOOSEFS.COM
kadmin.local: xst -k client_172_16_0_4.keytab client/172.16.0.4@GOOSEFS.COM
```

### 配置 GooseFS Server/Client 接入使用 Kerberos 认证

将上述导出 `keytab` 文件分发到对应的机器上，这里建议的路径是 `${GOOSEFS_HOME}/conf/`：

```shell
$ scp goosefs_172_16_0_1.keytab <username>@172.16.0.1:${GOOSEFS_HOME}/conf/
$ scp goosefs_172_16_0_1.keytab <username>@172.16.0.2:${GOOSEFS_HOME}/conf/
$ scp goosefs_172_16_0_1.keytab <username>@172.16.0.3:${GOOSEFS_HOME}/conf/
$ scp client_172_16_0_4.keytab <username>@172.16.0.4:${HOME}/.goosefs/
```

然后在对应机器上修改 Server Principal KeyTab 文件的所属用户/用户组为 GooseFS Server 启动时的用户及用户组（这样做是为了让 GooseFS 启动时有足够的权限读取）：

```shell
$ chown <GooseFS_USER>:<GOOSEFS_USERGROUP> goosefs_172_16_0_1.keytab
$ # 同时修改 Unix 访问权限位
$ chmod 0440 goosefs_172_16_0_1.keytab
```

Client 的 KeyTab 文件则需要修改为发起 GooseFS 请求的客户端账户，同样也是为了保证 Client 有足够的权限读取该文件：

```shell
$ chown <client_user>:<client_usergroup> client_172_16_0_4.keytab
$ # 同时修改 Unix 访问权限位
$ chmod 0440 client_172_16_0_4.keytab
```

#### Server 和 Client 端 GooseFS 配置

##### Master/Worker Server 的 goosefs-site.properties

```properties

# Security properties
# Kerberos properties
goosefs.security.authorization.permission.enabled=true
goosefs.security.authentication.type=KERBEROS
goosefs.security.kerberos.unified.instance.name=172.16.0.1
goosefs.security.kerberos.server.principal=goosefs/172.16.0.1@GOOSEFS.COM
goosefs.security.kerberos.server.keytab.file=${GOOSEFS_HOME}/conf/goosefs_172_16_0_1.keytab

```

配置好 GooseFS Server 端的认证配置后，需要重启整个集群以使得配置生效。

##### Client 的 goosefs-site.properties

```properties
# Security properties
# Kerberos properties
goosefs.security.authorization.permission.enabled=true
goosefs.security.authentication.type=KERBEROS
goosefs.security.kerberos.unified.instance.name=172.16.0.1
goosefs.security.kerberos.server.principal=goosefs/172.16.0.1@GOOSEFS.COM
goosefs.security.kerberos.client.principal=client/172.16.0.4@GOOSEFS.COM
goosefs.security.kerberos.client.keytab.file=${GOOSEFS_HOME}/conf/client_172_16_0_4.keytab

```

**注意**：Client 端需要指定 Server 的 principal，这是因为在 Kerberos 认证体系中，KDC 需要知道当前 Client 所访问的 Service，GooseFS 中是通过 Server 的 principal 来区分 Client 当前请求 Service 的。

至此，GooseFS 接入 Kerberos 的基础认证完毕，后续客户端发起的请求都将经过 Kerberos 进行身份认证。

### Auth-To-Local 配置

GooseFS 支持配置 Kerberos 的 principal name 到操作系统用户的转换规则，并且与 Hadoop 中的 auth_to_local 配置语法相同，因此具备良好的兼容性。配置选项为 `goosefs.security.auth_to_local`，具体的配置语法可参考 Hadoop 的 [auth_to_local](https://www.cloudera.com/documentation/enterprise/5-3-x/topics/cdh_sg_kerbprin_to_sn.html) 规则。以下给出一个简单的配置示例：

```properties

goosefs.security.authorization.permission.enabled=true
goosefs.security.authentication.type=KERBEROS
goosefs.security.kerberos.unified.instance.name=172.16.0.1
goosefs.security.kerberos.server.principal=hadoop/172.16.0.1@GOOSEFS.COM
goosefs.security.kerberos.server.keytab.file=${GOOSEFS_HOME}/conf/goosefs_172_16_0_1.keytab

goosefs.security.kerberos.client.principal=client/localhost@GOOSEFS.COM
goosefs.security.kerberos.client.keytab.file=${GOOSEFS_HOME}/conf/client_localhost.keytab

goosefs.security.auth_to_local=RULE:[2:$1@$0](.*localhost@GOOSEFS.COM)s/.*/user1/g DEFAULT

```

**注意**：`goosefs.security.auth_to_local` 这个配置是一个集群端配置，因此每次修改以后，需要重启集群才能生效。每条规则之间使用空格分隔。

## 配置使用 Hadoop Delegation Token 认证


## FAQ
