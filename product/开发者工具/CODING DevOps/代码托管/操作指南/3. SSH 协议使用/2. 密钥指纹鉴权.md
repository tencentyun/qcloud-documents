本文为您详细介绍如何使用密钥指纹进行代码仓库鉴权，用以确认所连接的远程仓库是否为真正的 CODING 仓库。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 选择左侧菜单**代码仓库**，进入代码仓库首页。
4. 若左侧未显示代码仓库，需项目管理员前往**项目设置** > **项目与成员** > **功能开关**打开功能开关。

## 功能介绍[](id:intro)

代码安全是永不过时的议题，为了保证您所连接的远端仓库是真正的 CODING 代码仓库，现提供 SSH 密钥指纹用于鉴权。您只需要在本地运行命令后，验证返回的结果就可以知晓远端代码仓库的真实性。

## 验证 SHA256 算法指纹[](id:sha256)

查看本地 `.ssh/know_hosts` 文件中关于 `e.coding.net` 的 SHA256 算法的指纹，如果返回值为 `jok3FH7q5LJ6qvE7iPNehBgXRw51ErE77S0Dn+Vg/Ik`，则证明您连接到了正确的 CODING 服务器。可在终端中运行命令查看结果。
<dx-codeblock>
:::  bash
ssh-keygen -lf ~/.ssh/known_hosts
:::
</dx-codeblock>

![](https://qcloudimg.tencent-cloud.cn/raw/13301b96bbccb08ebc1d78f23858ea96.png)

## 验证 MD5 算法指纹[](id:md5)

查看本地 `.ssh/know_hosts` 文件中关于 `e.coding.net` 的 MD5 算法的指纹，如果返回值是 `98:ab:2b:30:60:00:82:86:bb:85:db:87:22:c4:4f:b1`，则证明您连接到了正确的 CODING 服务器。可在终端中运行命令查看结果。
<dx-codeblock>
:::  bash
ssh-keygen -E md5 -lf ~/.ssh/known_hosts
:::
</dx-codeblock>

![](https://qcloudimg.tencent-cloud.cn/raw/409314f22ce3b4d3f0cb423ffc1527a8.png)
