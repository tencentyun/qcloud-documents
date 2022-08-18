## 概述

Kerberos 是大数据生态系统中广泛应用的统一认证服务，GooseFS 作为大数据和数据湖场景下的加速存储服务，支持集群节点和用户访问接入 Kerberos 认证服务中。本文将详细介绍如何配置 GooseFS 接入 Kerberos 认证服务以及如何使用 Hadoop Delegation Token 认证。

## GooseFS 接入 Kerberos 的认证架构

![](https://qcloudimg.tencent-cloud.cn/raw/f3fa3d97e385d113faf053cb989edef7.png)

## GooseFS Kerberos 认证优势

- 与 HDFS 接入 Kerberos 的认证架构和流程基本一致，在 HDFS 上启用了 Kerberos 认证流程的应用可以很容易地迁移到 GooseFS。
- 支持 Hadoop 的 Delegation Token 认证机制，因此可以很好地兼容 Hadoop 生态的应用作业。

## 配置 GooseFS 接入 Kerberos 认证

### 前提条件

- GooseFS 1.3.0 及以上版本。
- 确保环境中已存在 Kerberos KDC 服务，并且 GooseFS 以及应用客户端能够正常访问 Kerberos KDC 服务相关端口。

### 在 Kerberos KDC 中创建 GooseFS 相关的身份信息

首先，我们需要在 Kerberos KDC 中创建 GooseFS 集群 Server 与 Client 相关的 Kerberos 身份信息，然后才能继续后续的接入配置。这里我们在 **Kerberos KDC 服务器**上借助 `kadmin.local` 交互式工具来完成创建：
>! `kadmin.local` 工具需要 root/sudo 权限执行。
>

```shell
$ sudo kadmin.local
```

如果执行成功，则进入了 kadmin 的交互式 shell 环境中：

```shell
Authenticating as principal root/admin@GOOSEFS.COM with password.
kadmin.local:  
```

其中，`kadmin.local` 表示该交互式执行环境的命令提示符。

#### 创建 GooseFS Server / Client 相关的身份信息

如下通过一个简单测试集群以及应用场景样例来介绍整个 Kerberos 的配置过程。
1. 集群环境说明
采用单 Master 双 Worker 的 Standalone 部署架构：
 - Master（JobMaster）：172.16.0.1
 - Worker1（JobWorker1）：172.16.0.2
 - Worker2（JobWorker2）：172.16.0.3
 - Client：172.16.0.4
2. 在 `kadmin.local` 中创建 Server 和 Client 身份认证相关信息：
```shell
kadmin.local: addprinc -randkey goosefs/172.16.0.1@GOOSEFS.COM
kadmin.local: addprinc -randkey client/172.16.0.4@GOOSEFS.COM
```
>! 此处使用 `-randkey` 选项的原因在于 GooseFS 无论 Server 还是 Client 登录均使用 `keytab` 文件认证，不使用明文密码。若身份信息需要用于 password 登录场景，则可以去掉该选项。
>
3. 生成导出每个身份对应的 `keytab` 文件：
```shell
kadmin.local: xst -k goosefs_172_16_0_1.keytab goosefs/172.16.0.1@GOOSEFS.COM
kadmin.local: xst -k client_172_16_0_4.keytab client/172.16.0.4@GOOSEFS.COM
```

### 配置 GooseFS Server/Client 接入使用 Kerberos 认证

1. 将上述导出 `keytab` 文件分发到对应的机器上，此处建议的路径是 `${GOOSEFS_HOME}/conf/`：
```shell
$ scp goosefs_172_16_0_1.keytab <username>@172.16.0.1:${GOOSEFS_HOME}/conf/
$ scp goosefs_172_16_0_1.keytab <username>@172.16.0.2:${GOOSEFS_HOME}/conf/
$ scp goosefs_172_16_0_1.keytab <username>@172.16.0.3:${GOOSEFS_HOME}/conf/
$ scp client_172_16_0_4.keytab <username>@172.16.0.4:${HOME}/.goosefs/
```
2. 在对应机器上，将 Server Principal KeyTab 文件的所属用户/用户组修改为 GooseFS Server 启动时所使用的用户及用户组（其目的是为了让 GooseFS 启动时有足够的权限读取）。
```shell
$ chown <GooseFS_USER>:<GOOSEFS_USERGROUP> goosefs_172_16_0_1.keytab
$ # 同时修改 Unix 访问权限位
$ chmod 0440 goosefs_172_16_0_1.keytab
```
3. 将 Client 的 KeyTab 的所属用户/用户组修改为发起 GooseFS 请求的客户端账户。其目的同样是为了保证 Client 有足够的权限读取该文件。
```shell
$ chown <client_user>:<client_usergroup> client_172_16_0_4.keytab
$ # 同时修改 Unix 访问权限位
$ chmod 0440 client_172_16_0_4.keytab
```

#### Server 和 Client 端 GooseFS 配置

1. Master/Worker Server 的 goosefs-site.properties
```properties

# Security properties
# Kerberos properties
goosefs.security.authorization.permission.enabled=true
goosefs.security.authentication.type=KERBEROS
goosefs.security.kerberos.unified.instance.name=172.16.0.1
goosefs.security.kerberos.server.principal=goosefs/172.16.0.1@GOOSEFS.COM
goosefs.security.kerberos.server.keytab.file=${GOOSEFS_HOME}/conf/goosefs_172_16_0_1.keytab

```
配置完成 GooseFS Server 端的认证配置后，重启整个集群以使得配置生效。
2. Client 的 goosefs-site.properties
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
>! Client 端需要指定 Server 的 principal。其原因为在 Kerberos 认证体系中，KDC 需要知道当前 Client 所访问的 Service，而 GooseFS 是通过 Server 的 principal 区分 Client 当前请求的 Service。
>

至此，GooseFS 接入 Kerberos 的基础认证完毕，后续客户端发起的请求都将经过 Kerberos 进行身份认证。

