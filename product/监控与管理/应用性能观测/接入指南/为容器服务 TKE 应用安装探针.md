

您可以使用在容器服务（TKE） 中的应用市场服务 - tapm-operator，快速安装应用性能观测 APM 的探针。即可监控追踪容器服务中的应用，查看应用相关的监控指标、链路及日志。本文将会为您介绍如何在容器服务（TKE）侧安装 APM 探针。

>?当前仅支持 Java 语言- Opentelementry 增强探针。后续将会支持更多探针和语言，敬请期待。



## 操作步骤


### 首次通过 TKE 应用市场接入 APM

若您从未通过 TKE 应用市场接入 APM ，请参考以下操作步骤：

**前置步骤**
1. 创建 TKE 集群，您可查看 [容器服务（TKE）相关文档](https://cloud.tencent.com/document/product/457)，了解并使用容器服务。
2. 在 [应用性能观测控制台](https://console.cloud.tencent.com/apm/monitor/team)，创建 APM 业务系统。参考文档 [新建业务系统](https://cloud.tencent.com/document/product/1463/63511)。

**在容器服务（TKE）侧应用市场安装 tapm-operator**

1. 进入 [腾讯云容器服务（TKE）控制台-应用](https://console.cloud.tencent.com/tke2/helm)。
2. 选择您的容器集群，在容器集群下新建应用。
 - 输入应用名称。
 - 输入命名空间。
 - 来源项选择**应用市场**。
 - Chart 选择应用场景**监控**。
 - 选择应用性能观测 APM 的应用**tapm-operator**。
 - Chart 版本需选择最新版本。
![](https://qcloudimg.tencent-cloud.cn/raw/0e944af78a7e0821fc13e7afaaad7aed.png)
 - 修改 yaml 文件参数。
单击下方的参数编辑按钮，进入参数配置页面。
![](https://qcloudimg.tencent-cloud.cn/raw/a92ffa7d01062ccf5d7cf25154ba08a7.png)
根据下列描述修改 env 参数：
<table>
<tr>
<th width="20%">参数</th>
<th width="27%">描述</th>
<th width="53%">获取方式和格式说明</th>
</tr>
<tr>
<td>  APM_TOKEN</td>
<td>您的 APM  实例对应的上报 Token</td>
<td> 1. 在应用性能观测控制台-探针部署页面<br>选择 Java 语言-Opentelementry增强探上报方式。<br><br><img src="https://qcloudimg.tencent-cloud.cn/raw/1a9ed8112203421e565af4c108626c7e.png" width="70%"><br><br>2. 单击<b>下一步</b>，获取 Token。<br><img src="https://qcloudimg.tencent-cloud.cn/raw/c17e16415c3e201154a41f9a4b03b43f.png" width="70%"> </td>
</tr>
<tr>
<td>CLUSTER_ID</td>
<td>  APM_TOKEN</td>
<td>您可以在 <a href="https://console.cloud.tencent.com/tke2/cluster">容器服务控制台-集群列表</a> 中查看。 </td>
</tr>
<tr>
<td>TKE_REGION</td>
<td>此应用的 Kubernetes 集群所在地域</td>
<td>地域格式需要参考腾讯云规范地域格式，例如：广州地域为 ap-guangzhou，详见 <a href="https://cloud.tencent.com/document/product/213/6091">地域说明</a> 文档。 </td>
</tr>
</table>

### 二次通过 TKE 应用市场接入 APM

若您已经通过 TKE 应用市场的方式成功接入 APM，只需新增应用信息即可，请参考以下操作步骤：

**操作说明**
您需要将新增的应用所在的 pod 打上 label，具体添加步骤可参考下列方法一或方法二：

```
-  java-agent-app-name: service-name    // 服务名，例如：order-service
-  java-agent-injected: "true"                   // pod 是否需要注入，默认写 true
```



####  方法一

**在 TKE 创建或修改 Deployment 配置时加上 label**


1. 进入 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster)，单击相关集群，进入工作负载-Deployment ，选择新建或修改 Deployment 。
![](https://qcloudimg.tencent-cloud.cn/raw/5fa3ed1ba4068155966ec30711eae2d4.png)
2. 在 Labels  配置项中新增 label 。
```
 - java-agent-app-name = service-name   
 - java-agent-injected = true
```

![](https://qcloudimg.tencent-cloud.cn/raw/0484128dcb29edafd304803620312f74.png)
3. 单击**创建 Deployment**，即新增完成。

####  方法二
若已创建 Deployment，可直接点击 Deployment 名称修改 YAML 文件，按照如下格式修改。
```
-  java-agent-app-name: service-name 
-  java-agent-injected: "true"  
```

![](https://qcloudimg.tencent-cloud.cn/raw/c262ae8caa3fe588dc9dcc7001a5bcf4.png) 



### 跨地域上报

以上步骤会将数据上传到 APM，地域默认为容器集群所在的地域。请注意，APM 暂不支持部分容器集群所在的地域上报，如您有此类情况或者有特殊需求，可以修改或新增 label 进行跨地域上报。

**新增/修改 Label 信息说明：**
backend-service: APM 接入点信息
例如： APM 控制台数据接入信息为 `pl.ap-beijing.apm.tencentcs.com`
则需要新增/修改 Label 信息为：`backend-service：pl.ap-beijing.apm.tencentcs.com`
![](https://qcloudimg.tencent-cloud.cn/raw/6cd9c98e00813c390859b1644a33c926.png)

#### 方法一

在 TKE 创建或修改 Deployment 配置时加上 label。
1. 进入 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster)，点击相关集群，进入工作负载-Deployment ，选择新建或修改 Deployment 。
![](https://qcloudimg.tencent-cloud.cn/raw/5fa3ed1ba4068155966ec30711eae2d4.png)      
2. 在 Labels 处新增 label 。
以 `backend-service：pl.ap-beijing.apm.tencentcs.com` 为例：
![](https://qcloudimg.tencent-cloud.cn/raw/bd6f5b01ff45d856bfe59959ca7d8a72.png)

#### 方法二

若已创建 Deployment，可直接点击 Deployment 名称修改 YAML 文件，按照如下格式修改。
以 `backend-service：pl.ap-beijing.apm.tencentcs.com` 为例：
![](https://qcloudimg.tencent-cloud.cn/raw/d5c8f16925fa38aab4faeab9f79442aa.png)

### 查看应用性能数据

完成以上步骤后，您就可以在应用性能监控APM页面观测到您在容器中部署的应用情况，以及该应用相关的容器基础资源监控。
1. 在应用详情页，可选择想观测的应用，查看应用所在容器 Deployment 及 pod 的监控信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/d3e8b765adee6e4bbe877e4d006352c4.png)
2. 在链路详情中，可点击查看该 Span 归属应用所在 pod 的基础监控信息。
![](https://qcloudimg.tencent-cloud.cn/raw/5799b33603fa6afe7c754cef9d21e3ea.png)
![](https://qcloudimg.tencent-cloud.cn/raw/f3f5d8bb4937ce9101d392df2e46ac76.png)



