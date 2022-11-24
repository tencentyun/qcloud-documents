## 操作场景
 
本文针对腾讯内部自研上云用户接入微服务引擎托管的 PolarisMesh 治理中心。

## 接入机制说明

### 北极星SDK二次寻址

北极星内部版本SDK接入时，由于SDK默认开启了二次寻址机制（且无法关闭），二次寻址机制依赖**polaris.discover**以及**polaris.healthcheck**这2个服务。因此需要在公有云北极星引擎实例创建出来后，需在控制台手动创建**polaris.discover**以及**polaris.healthcheck**这两个服务，使得SDK能够成功寻址。

### 为何需要用户手动创建

用户接入方式存在多VPC、公网接入两类场景。不同的接入侧用户需要看到不同的服务端IP，无法自动创建相关北极星系统服务

### L5agent 使用北极星

#### L5的SID在北极星中如何创建

由于l5api仅支持访问L5 SID，因此访问非L5 SID格式的服务名，需要创建CL5 SID格式的服务别名指向该服务，这里请直接从内部北极星将服务对应的L5别名SID信息直接复制，然后在公有云北极星中创建响应的服务别名

- 复制SID信息
![](https://qcloudimg.tencent-cloud.cn/raw/81d75a94d0f82138bd91de6c19c34057.png)

- 如果对应的环境类型（即命名空间）在公有云北极星引擎中不存在，则先进行手动创建
![](https://qcloudimg.tencent-cloud.cn/raw/c97b1a669c8912e1cd1b04fb67766c89.png)

- 在公有云北极星引擎实例中创建L5格式的服务别名
![](https://qcloudimg.tencent-cloud.cn/raw/c71c1b754b02120262a2551dc7bebe48.png)


#### SID和命名空间的对应关系

L5 SDI的格式：ModID:CmdID

<b>强烈建议用户命名空间选择default或者Production，ModID取值范围为： [2, 192,000,000]</b>

如果用户确实有需要使用其他命名空间，请按照以下方式进行其他命名空间的换算：
ModID 数值右移6位，如果结果 >= 3000001，则需要计算 ModID & 63 的结果值，根据结果值对应的命名空间信息如下，否则会出现L5寻址失败的问题：

```json
{
	1: "Production",
	2: "Development",
	3: "Pre-release",
	4: "Test",
	5: "Polaris",
	6: "default",
}
```

## 微服务引擎操作场景
本文主要面向腾讯内部自研上云用户如何迁移至微服务引擎托管的 PolarisMesh 治理中心。

## 前提条件
- 已创建 PolarisMesh 服务治理中心，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**治理中心**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
3. 单击目标引擎的“ID”，进入基本信息页面。


### 引擎实例未开启客户端公网访问

#### L5Agent 接入

1. 查看引擎的接入地址，在实例的基本信息页面中，记住访问地址中的每个VPC内网IP地址以及访问端口
![](https://qcloudimg.tencent-cloud.cn/raw/fb9e4d3a42c3795682cf030409feedf0.png)
2. 修改L5Agent的配置文件 l5_config.ini
```toml
[L5CONFIG]
ServerIp={对应 vpc 的内网接入地址}
ServerPort=7779
```
4. 重启L5agent，启动前要把/data/L5Backup/l5server_list.backup删掉


#### 北极星内部SDK接入

##### 创建 polaris.discover 以及 polaris.healthcheck 服务

1. 在实例的基本信息页面中，记住访问地址中的每个VPC内网IP地址以及访问端口
![](https://qcloudimg.tencent-cloud.cn/raw/ac156fe7007b43ebd91bba186e71e87d.png)
2. 针对每一个内网VPC的IP地址，在命名空间 **Polaris** 下创建服务 **polaris.discover-{vpc 名称}** 以及 **polaris.healthcheck-{vpc 名称}**
 ![](https://qcloudimg.tencent-cloud.cn/raw/6f1ace02cca38bd57d420c8585f2a2a6.png)
3. 点击服务 **polaris.discover-{vpc 名称}**，进入到服务的实例页面，根据对应上述第一步所记录的VPC内网IP地址以及端口协议**grpc**、**trpc**分别创建实例
 ![](https://qcloudimg.tencent-cloud.cn/raw/55cde3efcee6abe11117ca2dc94790b4.png)
4. 点击服务 **polaris.healthcheck-{vpc 名称}**，进入到服务的实例页面，根据对应上述第一步所记录的VPC内网IP地址以及端口协议**grpc**、**trpc**分别创建实例
![](https://qcloudimg.tencent-cloud.cn/raw/d123c305d51ba2f345dcbbaf74e41be8.png)
5. 按照上述步骤的操作，最终服务**polaris.discover-{vpc 名称}**的实例列表如下
 ![](https://qcloudimg.tencent-cloud.cn/raw/271aa62d54d96e8e148114bedf17a529.png)
6. 按照上述步骤的操作，最终服务**polaris.healthcheck-{vpc 名称}**的实例列表如下
![](https://qcloudimg.tencent-cloud.cn/raw/7ab5e26730fff7183ef3d695ac8f23e1.png)
 
注意：如果只是单VPC接入的场景，则无需参考 **polaris.discover-{vpc 名称}** 这种命名规则，直接使用 **polaris.discover** 即可，**polaris.healthcheck-{vpc 名称}** 也直接使用 **polaris.healthcheck** 即可
 
##### 创建路由规则

###### 创建路由规则示例

###### polaris.discover-{vpc 名称}

![](https://qcloudimg.tencent-cloud.cn/raw/92f1a7af341c558f50fc234f7d72bb91.png)

###### polaris.healthcheck-{vpc 名称}

![](https://qcloudimg.tencent-cloud.cn/raw/92f1a7af341c558f50fc234f7d72bb91.png)

##### SDK接入相关配置文件说明

###### polaris-go

- **polaris.yaml**中按照下面示例进行配置二次寻址
```yaml
global:
 serverConnector:
   addresses:
   - {对应 vpc 的内网接入地址}:8091
 system:
   #服务发现集群
   discoverCluster:
     namespace: Polaris
     service: polaris.discover-{vpc 名称}
   #健康检查集群
   healthCheckCluster:
     namespace: Polaris
     service: polaris.healthcheck-{vpc 名称}
```

###### polaris-java

- polaris.yaml 中按照下面示例进行配置二次寻址
```yaml
 global:
   serverConnector:
     addresses:
       - {对应 vpc 的内网接入地址}:8091
   system:
     #服务发现集群
     discoverCluster:
       namespace: Polaris
       service: polaris.discover-{vpc 名称}
       sameAsBuiltin: false
	  #健康检查集群
     healthCheckCluster:
       namespace: Polaris
       service: polaris.healthcheck-{vpc 名称}
       sameAsBuiltin: false
```

###### polaris-cpp

- polaris.yaml 中按照下面示例进行配置二次寻址
```yaml
global:
  serverConnector:
    addresses:
      - {对应 vpc 的内网接入地址}:8091
  system:
    #服务发现集群
    discoverCluster:
      namespace: Polaris
      service: polaris.discover-{vpc 名称}
    #健康检查集群
    healthCheckCluster:
      namespace: Polaris
      service: polaris.healthcheck-{vpc 名称}
```

######  spring-cloud-tencent

- 修改 bootstrap.yaml 或者 bootstrap.properties 文件
```
spring:
  cloud:
    polaris:
      address: {对应 vpc 的内网接入地址}:8091
```

- 在**resources**下创建**polaris.yml**文件

- 按照下面示例进行配置二次寻址
```yaml
global:
  system:
    #服务发现集群
    discoverCluster:
      namespace: Polaris
      service: polaris.discover-{vpc 名称}
      sameAsBuiltin: false
	#健康检查集群
    healthCheckCluster:
      namespace: Polaris
      service: polaris.healthcheck-{vpc 名称}
      sameAsBuiltin: false
```

###### trpc

```yaml
plugins:                                             #插件配置
  registry:
    polaris:                                         #北极星名字注册服务的配置
      heartbeat_interval: 3000                       #名字注册服务心跳上报间隔
      protocol: grpc                                 #名字服务远程交互协议类型
      address_list: {对应 vpc 的内网接入地址}:8091      #北极星接入地址，实际上就是内网CLB接入地址
	   cluster_service:
        discover: polaris.discover-{vpc 名称}        #修改发现server集群名
        health_check: polaris.healthcheck-{vpc 名称} #修改心跳server集群名
      
  selector:                                          #针对trpc框架服务发现的配置
    polaris:                                         #北极星服务发现的配置
      address_list: {对应 vpc 的内网接入地址}:8091      #北极星接入地址，实际上就是内网CLB接入地址
      protocol: grpc                                 #名字服务远程交互协议类型
      cluster_service:
        discover: polaris.discover-{vpc 名称}        #修改发现server集群名
        health_check: polaris.healthcheck-{vpc 名称} #修改心跳server集群名
```

### 引擎实例开启客户端公网访问

#### L5Agent 接入

1. 查看引擎的接入地址，在实例的基本信息页面中，记住访问地址中的公网IP地址以及访问端口
![](https://qcloudimg.tencent-cloud.cn/raw/2e7e813be530b1d4f5fc6fe501452b03.png)
2. 修改L5Agent的配置文件 l5_config.ini
```toml
[L5CONFIG]
ServerIp={对应公网接入地址}
ServerPort=7779
```
4. 重启L5agent，启动前要把/data/L5Backup/l5server_list.backup删掉

#### 北极星内部SDK接入

##### 创建 polaris.discover 以及 polaris.healthcheck 服务

1. 在实例的基本信息页面中，记住访问地址中的公网IP地址以及访问端口
 ![](https://qcloudimg.tencent-cloud.cn/raw/47e0ef859b9dccfde2b3754fd05699cd.png)
2. 在命名空间**Polaris**下创建服务**polaris.discover**以及**polaris.healthcheck**
 ![](https://qcloudimg.tencent-cloud.cn/raw/9380435875dcc61976065e7a6c2f6ad8.png)
3. 点击服务**polaris.discover**，进入到服务的实例页面，根据客户端公网访问IP地址以及端口协议**grpc**、**trpc**分别创建实例
 ![](https://qcloudimg.tencent-cloud.cn/raw/4160a80cca8e48af28f580dcc11ba862.png)
4. 点击服务**polaris.healthcheck**，进入到服务的实例页面，根据客户端公网访问IP地址以及端口协议**grpc**、**trpc**分别创建实例
![](https://qcloudimg.tencent-cloud.cn/raw/67719dc73f4579dc5fec14c20dd678c2.png)
5. 按照上述步骤的操作，最终服务**polaris.discover**的实例列表如下
 ![](https://qcloudimg.tencent-cloud.cn/raw/1cf3e2176a6fa7638f07b13dfe5ac3b3.png)
6. 按照上述步骤的操作，最终服务**polaris.healthcheck**的实例列表如下
![](https://qcloudimg.tencent-cloud.cn/raw/1f7ce0960f4e2a1d73294ec39abed404.png)
 
##### 创建路由规则

###### polaris.discover

![](https://qcloudimg.tencent-cloud.cn/raw/92f1a7af341c558f50fc234f7d72bb91.png)

###### polaris.healthcheck

![](https://qcloudimg.tencent-cloud.cn/raw/92f1a7af341c558f50fc234f7d72bb91.png)

##### SDK接入相关配置文件说明

###### polaris-go

- polaris.yaml 中按照下面示例进行配置二次寻址
```yaml
global:
 serverConnector:
   addresses:
     - {对应公网接入地址}:8091
 system:
   #服务发现集群
   discoverCluster:
     namespace: Polaris
     service: polaris.discover
   #健康检查集群
   healthCheckCluster:
     namespace: Polaris
     service: polaris.healthcheck
```

###### polaris-java

- polaris.yaml 中按照下面示例进行配置二次寻址
```yaml
global:
  serverConnector:
    addresses:
      - {对应公网接入地址}:8091
  system:
    #服务发现集群
    discoverCluster:
      namespace: Polaris
      service: polaris.discover
      sameAsBuiltin: false
	#健康检查集群
    healthCheckCluster:
      namespace: Polaris
      service: polaris.healthcheck
      sameAsBuiltin: false
```

###### polaris-cpp

- polaris.yaml 中按照下面示例进行配置二次寻址
```yaml
global:
  serverConnector:
    addresses:
      - {对应公网接入地址}:8091
  system:
    #服务发现集群
    discoverCluster:
      namespace: Polaris
      service: polaris.discover
    #健康检查集群
    healthCheckCluster:
      namespace: Polaris
      service: polaris.healthcheck
```

###### spring-cloud-tencent

- 修改 bootstrap.yaml 或者 bootstrap.properties 文件
```
spring:
  cloud:
    polaris:
      address: {对应公网接入地址}:8091
```

- 在**resources**下创建**polaris.yml**文件

- 按照下面示例进行配置二次寻址
```yaml
global:
  system:
    #服务发现集群
    discoverCluster:
      namespace: Polaris
      service: polaris.discover
      sameAsBuiltin: false
	#健康检查集群
    healthCheckCluster:
      namespace: Polaris
      service: polaris.healthcheck
      sameAsBuiltin: false
```

###### trpc

```yaml
plugins:                                             #插件配置
  registry:
    polaris:                                         #北极星名字注册服务的配置
      heartbeat_interval: 3000                       #名字注册服务心跳上报间隔
      protocol: grpc                                 #名字服务远程交互协议类型
      address_list: {对应公网接入地址}:8091      #北极星接入地址，实际上就是内网CLB接入地址
      cluster_service:
        discover: polaris.discover                   #修改发现server集群名
        health_check: polaris.healthcheck            #修改心跳server集群名
      
  selector:                                          #针对trpc框架服务发现的配置
    polaris:                                         #北极星服务发现的配置
      address_list: {对应公网接入地址}:8091      #北极星接入地址，实际上就是内网CLB接入地址
      protocol: grpc                                 #名字服务远程交互协议类型
      cluster_service:
        discover: polaris.discover                   #修改发现server集群名
        health_check: polaris.healthcheck            #修改心跳server集群名
```

## 常见问题排查

### L5

> 使用 ./L5GetRoute1 查询失败

***现象***

./L5GetRoute1 xxx xxx 10
ApiGetRoute failed, ret: -9998, usec=181283,avg_usec=181283,err: FILE[static_route.cpp] LINE[153][GetRoute],NOT FOUND,invalid mod[xxx] cmd[xxx]

***排除方向***

- 检查 l5config.ini 中对于 ServerIp 的信息是否填写正确
- 确保对应的服务下有健康的服务实例
- L5的SID所对应的命名空间是否正确
- 是否已经在北极星中创建了格式为SID的服务别名