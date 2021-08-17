## 操作场景
本文介绍如何通过腾讯云容器服务控制台进行触发器的创建、修改、删除和查看触发日志。

触发器的使用可分为以下三步，您可参考本文开始使用触发器：
1. 选择具体镜像仓库创建触发器，配置触发表达式和服务更新参数。
2. 通过腾讯云 CI 或者 docker push 镜像到镜像仓库，确认提交的镜像是否满足触发表达式的条件。
3. 查看触发器日志，检查触发动作是否执行成功。


## 前提条件
已登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)。

## 操作步骤
### 创建镜像仓库触发器
1. 选择左侧导航栏中的**镜像仓库**>**[我的镜像](https://console.cloud.tencent.com/tke2/registry/user/self)**。
2. 在“我的镜像”页面中，单击镜像名称。如下图所示：
![](https://main.qcloudimg.com/raw/9dfa87ff95bb322396b0f58ba7a0f1e5.png)
3. 在镜像详情页面中，选择**触发器**>**添加触发器**。如下图所示：
![](https://main.qcloudimg.com/raw/74d7e4c51d36274c76a0ec8754ed0e49.png)
4. 根据以下提示，填写信息设置触发器属性。如下图所示：
![](https://main.qcloudimg.com/raw/fe8cd7a11a9cd9f15cfe5f3d64f2fe3f.png)
 - **触发器名称**：创建的触发器名称。英文字母开头，2 - 64 个字符以内 。
 - **触发条件**：分为三种触发条件。
    - **全部触发**：镜像仓库内，有新的 Tag（镜像版本）生成，或 Tag 发生更新时，触发动作。
    - **指定 Tag 触发**：镜像仓库内，有指定 Tag 生成或更新时，触发动作。
    - **正则触发**：镜像仓库内，有符合正则表达式的 Tag 生成或更新时，触发动作。
 - **触发动作**：更新容器的镜像。
 - **选择服务/镜像**：单击**请选择容器镜像**，在下拉列表中选择地域、集群、Namespace、服务、容器镜像属性。
5. 单击**保存**，即可完成触发器的创建。

### 修改镜像仓库触发器
1. 选择左侧导航栏中的**镜像仓库**>**[我的镜像](https://console.cloud.tencent.com/tke2/registry/user/self)**。
2. 在“我的镜像”页面中，单击镜像名称进入镜像详情页面。
3. 选择**触发器**页签进入触发器列表页，单击需修改触发器所在行右侧的<img src="https://main.qcloudimg.com/raw/49d854093c5e79c092343e0c72c5e752.png" style="margin:-3px 0px">。如下图所示：
![](https://main.qcloudimg.com/raw/052a56afc7e904acc5a4928346bc030b.png)
4. 在展开的触发器信息编辑页面修改信息，并单击**保存**。


### 删除镜像仓库触发器
1. 选择左侧导航栏中的**镜像仓库**>**[我的镜像](https://console.cloud.tencent.com/tke2/registry/user/self)**。
2. 在“我的镜像”页面中，单击镜像名称进入镜像详情页面。
3. 选择**触发器**页签进入触发器列表页，单击需修改触发器所在行右侧的<img src="https://main.qcloudimg.com/raw/895cf2643dc453e284eaba324484bc24.png" style="margin:-3px 0px">。如下图所示：
![](https://main.qcloudimg.com/raw/7ec505facf4cf19c69bb6166525f08bb.png)


### 查看触发日志
1. 登录腾讯云容器服务控制台，选择左侧导航栏中的**镜像仓库**>**[我的镜像](https://console.cloud.tencent.com/tke2/registry/user/self)**。
2. 在“我的镜像”页面中，单击镜像名称进入镜像详情页面。
3. 选择**触发器**页签，即可查看触发日志。如下图所示：
![](https://main.qcloudimg.com/raw/9652c6001d7367e110a12f9a35fbe969.png)
