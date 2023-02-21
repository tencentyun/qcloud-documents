## 操作场景
用于您获取某个主机名在当前解析的轻量应用服务器 设置HTTPS 的历史记录及其状态。
### 说明
设置 HTTPS 需要通过关联实例中的自动化助手执行命令完成操作。每次执行设置 HTTPS 操作后，关联实例的自动化助手执行命令历史中将会增加相应的任务记录。
<dx-alert infotype="notice" title="">
- 您在轻量应用服务器控制台删除域名解析，已经设置的 HTTPS 不会发生变化，但已不能通过该主机名访问轻量应用服务器实例中部署的网站。
-  如果您对轻量应用服务器实例进行重装系统，则已经设置的 HTTPS 将会失效，但轻量应用服务器控制台仍然会显示该次设置记录的状态。
</dx-alert>

## 操作步骤
登录腾讯云轻量应用服务器控制台，选择任意一种方式查看 HTTPS 设置历史记录：
<dx-tabs>
::: 方式一：在域名解析列表查看 HTTPS 设置历史记录
1. 从域名页面进入域名解析列表。
2. 将鼠标悬停在对应域名解析的 **HTTPS 设置历史记录** 一列，即可查看该域名解析对应 HTTPS 设置历史的记录。

 ![](https://qcloudimg.tencent-cloud.cn/raw/c701efbe3a1db456fa45802df980cb1d.png)

3. 如该解析记录对应的 HTTPS 设置历史的记录超过 5 条，可以在悬停气泡最下方点击查看全部历史记录。
 <img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/4f68585493fee8f6e7cd104a4a53aa67.png" />
:::
::: 方式二：在实例详情页查看 HTTPS 设置历史记录
1.  登录轻量应用服务器控制台，选择左侧导航栏中的服务器。
2. 在实例列表中，选择目标实例并进入实例详情页。
3. 选择域名页签，将鼠标悬停在对应域名解析的 **HTTPS 设置历史记录** 一列，即可查看该域名解析对应 HTTPS 设置历史的记录。

 ![](https://qcloudimg.tencent-cloud.cn/raw/c701efbe3a1db456fa45802df980cb1d.png)
4. 如该解析记录对应的 HTTPS 设置历史的记录超过 5 条，可以在悬停气泡最下方点击查看全部历史记录。
 <img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/4f68585493fee8f6e7cd104a4a53aa67.png" />

:::
</dx-tabs>






