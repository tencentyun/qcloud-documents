

## 操作场景
当您在生产环境中已经使用了自建的 Nacos 集群，并希望在腾讯云中部署灾备集群时；或者对集群的高可用、稳定性以及网络上的跨地域延迟有要求时，可以参考本指引配置多活容灾与就近访问方案，以提供跨云、跨 IDC 机房之间的应用访问，或者腾讯云内的跨集群之间的应用访问。

## 操作原理
Nacos 的核心功能为服务注册发现与配置管理，故 Nacos 多活容灾方案需要包括数据同步与服务注册发现同步：

- 数据同步：Nacos 的配置数据、用户信息、命名空间数据、访问控制等信息在数据库中持久化存储，因此首先需要使用 TSE Nacos 的数据同步功能实现源数据库到 TSE Nacos 数据库的全量迁移与实时增量同步，以保证每个 Nacos 集群都会有全量配置数据。
- 服务注册发现同步：采用 Java agent 的形式，在不改变业务代码的情况下，通过字节码增强的方式，实现服务的双注册和发现，以此提供服务同时在不同集群间路由的能力。

例如：当您在自建 IDC 机房和腾讯云分别部署了一整套应用和 Nacos 集群，可以通过本方案配置多活容灾与就近访问。即 IDC 机房内的 consumer 应用调用 provider 应用时，优先访问 IDC 内的 provider 应用，如果找不到该应用，则访问腾讯云中的 provider 应用。

**Nacos 多活部署架构图**
![](https://qcloudimg.tencent-cloud.cn/raw/7d3e66b5f196daf9b02550c8e0168112.png)


## 前提条件
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)，新建一个 nacos 实例，并获取客户端访问地址。详细操作请参见 [引擎管理](https://cloud.tencent.com/document/product/1364/63997)。
![](https://qcloudimg.tencent-cloud.cn/raw/343ea18a5103e2a7529e1dcc74426d67.png)
2. 访问 [Github 地址](https://github.com/polarismesh/polaris-java-agent/releases)，下载 Polaris Java Agent（支持 Nacos 双注册双发现）。
![](https://qcloudimg.tencent-cloud.cn/raw/53bb8ef2c64e23114e0b86d1c5eb2f35.png)

## 操作步骤
### 步骤1：开启数据同步
通过 TSE Nacos 的配置数据同步能力，将源 Nacos 数据库导入与同步至 TSE Nacos 集群。请参考 [Nacos 数据同步](https://cloud.tencent.com/document/product/1364/84650)。

[](id:step2)
### 步骤2：配置自建集群中的服务双注册发现
1. 将提前下载好的 polaris java agent zip 包上传到您的服务所部署的路径下并解压，确认该位置可以被正常访问。
2. 将原本注册在自建集群中的服务依次重新部署并双注册至 TSE Nacos 集群，部署时需要添加如下参数：
```
java   
-javaagent:/*/polaris-java-agent-v*/polaris-agent-core-bootstrap.jar   
-Dplugins.enable=nacos-all-plugin   
-Dnacos.cluster.name=*   
-Dother.nacos.server.addr=**.**.**.**   
-Drouter.nearby.level=nacos_cluster -jar xx.jar
```
>? 四处 `*` 分别代表 polaris java agent 所在的路径、版本号、集群名称、另一个 Nacos 集群的客户端访问地址。
>
**Java Agent 参数配置**
polaris java agent 提供以下以下配置项，所有的配置项通过系统变量（-D参数）的方式进行配置。
<table>
<thead>
<tr>
<th align="center">配置项</th>
<th align="center">描述</th>
<th align="center">必填</th>
<th align="center">可选值</th>
<th align="center">默认值</th>
</tr>
</thead>
<tbody><tr>
<td align="center">plugins.enable</td>
<td align="center">选择需要加载的插件</td>
<td align="center">是</td>
<td align="center">nacos-all-plugin</td>
<td align="center">nacos-all-plugin</td>
</tr>
<tr>
<td align="center">nacos.cluster.name</td>
<td align="center">Nacos 集群名称/标签，唯一标识即可</td>
<td align="center">是</td>
<td align="center">唯一标识即可</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">other.nacos.server.addr</td>
<td align="center">另一个 Nacos 集群的访问地址</td>
<td align="center">是</td>
<td align="center"></td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">router.nearby.level</td>
<td align="center">就近路由级别</td>
<td align="center">否</td>
<td align="center">null：不开启就近路由，采用客户端配置的路由策略，默认为轮询策略。<br>nacos_cluster：开启集群级别的就近路由，优先路由至相同 nacos.cluster.name 下的服务。</td>
<td align="center">null</td>
</tr>
</tbody></table>
3. 部署成功后，在 TSE Nacos 原生控制台的服务管理页面可以看到注册的服务。Nacos 原生控制台的访问方式请参见 [访问控制](https://cloud.tencent.com/document/product/1364/63998)。此时服务在自建 Nacos 集群和 TSE Nacos 集群中均进行了注册。
4. 观察自建的 Nacos 集群和 TSE 的 Nacos 集群，依次验证下注册、发现、反注册，看是否均符合预期。待所有服务均重新部署完毕后，在自建 Nacos 集群和 TSE Nacos 集群的控制台均能看到所有服务以及其下的实例信息。

### 步骤3：配置 TSE Nacos 集群中的服务双注册发现
重复 [步骤2](#step2) 中的操作，将原本注册至 TSE Nacos 集群中的服务依次重新部署，并双注册至自建 Nacos 集群。请注意将 Java Agent 参数配置项中的 `nacos.cluster.name` 与 `other.nacos.server.addr` 修改为合适的值。

完成以上步骤后，您已经成功配置了自建 Nacos 集群与 TSE Nacos 集群之间的多活方案，建议您保持 TSE Nacos 数据同步任务的持续运行，并保持在自建 Nacos 集群更新配置数据，以保证集群之间的数据一致。

