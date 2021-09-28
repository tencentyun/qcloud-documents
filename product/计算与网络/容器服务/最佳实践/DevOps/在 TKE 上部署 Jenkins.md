## 操作场景

许多 DevOps 的需求需要借助 Jenkins 来实现，本文将介绍如何在容器服务 TKE 上部署 Jenkins。

## 前提条件

已创建 [TKE 集群](https://cloud.tencent.com/document/product/457/32189)。

## 操作步骤

### 安装 Jenkins

1. 登录容器服务控制台，选择左侧导航栏中的 **[应用市场](https://console.cloud.tencent.com/tke2/market)**。
2. 在“应用市场”页面搜索 Jenkins，并进入 Jenkins 应用页面。
3. 单击**创建应用**，创建应用窗口中的“参数” values.yaml 部分，可以根据自身需求进行微调。
![](https://main.qcloudimg.com/raw/566dfe260dddce05ba60b5b7c92e7de7.jpg)
4. 单击**创建**既可安装 Jenkins。

### 暴露 Jenkins UI

默认情况下，在集群外无法访问 Jenkins UI。如需访问 Jenkins UI，通常使用 Ingress 来暴露访问。TKE 提供 [CLB 类型 Ingress](https://cloud.tencent.com/document/product/457/45685) 与 [Nginx 类型 Ingress](https://cloud.tencent.com/document/product/457/50502) 两种 Ingress，您可参考文档自行选择。


### 登录 Jenkins

进入 Jenkins UI 界面，输入初始用户名和密码登录 Jenkins 后台，用户名为 admin，初始密码需通过以下命令获取。

```bash
kubectl -n devops get secret jenkins -o jsonpath='{.data.jenkins-admin-password}' | base64 -d
```

>!执行上述命令时，需替换为实际环境所安装的命名空间。

### 创建用户



建议通过普通用户管理 Jenkins，创建普通用户之前，需配置认证与授权策略。

1. 登录 Jenkins 后台，选择**Dashboard** > **Manage Jenkins** > **Security** > **Configure Global Security**，进入认证与授权策略页面。如下图所示：
![](https://main.qcloudimg.com/raw/98801d650feb5e2a9623dff3057a1c1a.png)
 - **Security Realm**：选择**Jenkins‘ own user database**。
 - **Authorization**：选择**Logged-in users can do anything**。
2. 选择**Dashboard** > **Manage Jenkins** > **Security** > **Manage Users** > **Create User**，进入创建用户界面，根据以下提示创建用户。如下图所示：
![](https://main.qcloudimg.com/raw/b0e04f93312ee575d42d074979f4797f.png)
	- **Username**：输入用户名。
	- **Password**：输入用户密码。
	- **Confirm password**：确认用户密码。
	- **Full name**：输入用户名全称。
3. 单击**Create User**即可创建用户。




### 安装插件

登录 Jenkins 后台，选择**Dashboard** > **Manage Jenkins** > **System Configuration** > **Manage Plugins**，进入插件管理页面。
![](https://main.qcloudimg.com/raw/3f0c59f227e66ff388a41c2bfbb07fe3.png)
您可以安装以下常用插件：
- kubernetes
- pipeline
- git
- gitlab
- github
