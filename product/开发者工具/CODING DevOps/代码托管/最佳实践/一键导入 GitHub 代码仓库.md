本文为您详细介绍在 CODING 中如何一键导入 GitHub 代码仓库。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 选择左侧菜单**代码仓库**。

目前 CODING 支持一键导入 GitHub 仓库至项目内代码仓库啦！一键同步，让您的代码紧跟潮流。

>!静默同步：定时自动同步外部仓库。双向同步：外部仓库也能导入 CODING 代码仓库；功能仍在紧张开发中，敬请期待。

## 快速上手

您可以 [通过链接导入](#link) 或 [创建仓库时导入](#create) 两种方式完成代码同步。

<span ID = "link"></span>
### 通过链接导入

单击此处访问 [功能入口](https://e.coding.net/login?mmsg=vcs-import&redirect=/import)，按照指引登录团队。输入 GitHub 用户名后，选择拟导入的仓库；您也可以直接输入 GitHub 仓库地址完成导入，目前单次最多支持导入十个仓库。
![](https://main.qcloudimg.com/raw/a0b50cc036efcc9f2a1b5eeb15a0a814.png)
单击**完成**开始导入。完成后将会于右上角铃铛处更新或企业微信 [小程序](https://help.coding.net/docs/admin/service-integration/applets.html#pageTitle) 内推送通知，欢迎绑定使用。

>! 下图所示页面不会自动更新为完成状态，请以通知为准。

![](https://main.qcloudimg.com/raw/d1c3b0991f1771e6d7f8f3acbc82e311.png)
导入完成后的代码仓库位于新建的项目中。
![](https://main.qcloudimg.com/raw/a2ddf286192924e60c540596c8622a55.png)

<span ID = "create"></span>
### 创建仓库时导入

在项目内的代码仓库中单击**新建代码仓库**，勾选导入外部仓库并输入 GitHub 代码仓库地址，单击**确认**后完成导入。
![](https://main.qcloudimg.com/raw/759a3dde9dd3f92978cc2b17e0797750.png)

## 同步代码仓库

导入完成后，可以在代码仓库中进行查看。单击右侧**强制同步远端仓库**按钮，可以手动同步远程仓库中作的所有改动至当前的 CODING 仓库。**同步会强制覆盖当前仓库中作出的所有改动**，同步完成后仓库内容会自动刷新。
![](https://main.qcloudimg.com/raw/9ce991821abfbbd55643ef8f12b2ece9.png)
您还可以在代码仓库的**设置**中查看历次同步信息。
![](https://main.qcloudimg.com/raw/52d08f6797f0fe8ff7548a960f64d898.png)


