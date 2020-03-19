## 问题描述

Windows 使用远程桌面连接 Windows 实例时，出现如下图所示的提示：
![错误提示](https://main.qcloudimg.com/raw/52a79c81015d7e6b2f5299f98474348d.png)
要远程登录，你需要具有通过远程桌面服务进行登录的权限。默认情况下，远程桌面用户组的成员有这项权限。如果你所属的组没有这项权限，或者远程桌面用户组中已经删除了这项权限，那么需要手动为你授予这一权限。

## 解决方案

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在 “云主机” 页面中，选择连接异常的 CVM 实例，单击【登录】。如下图所示：
![云服务器列表页](https://main.qcloudimg.com/raw/56596196a93181ac4c9467abe19c383a.png)
3. 在弹出的 “登录Windows云服务器” 窗口中，选择 “浏览器 VNC 方式登录”，单击【立即登录】。如下图所示：
![VNC登录入口](https://main.qcloudimg.com/raw/80b613a90328bb34a006d5988dcff18b.png)
4. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 **Ctrl-Alt-Delete** 进入系统登录界面。如下图所示：
![Ctrl-Alt-Delete](https://main.qcloudimg.com/raw/27daf8cc33746b195c74dfb5066addee.png)
5. 在操作系统界面，选择【开始】>【运行】，输入 **gpedit.msc**。
6. 按 **Enter**，打开本地组策略略编辑器。
7. 在左侧导航树中，选择【计算机配置】>【Windows 设置】>【安全设置】>【本地策略】>【用户权限分配】。如下图所示：
![拒绝通过远程桌面服务登录](	https://main.qcloudimg.com/raw/55937ed371582903a7235b56aa0a38f1.png)
5. 在右侧的策略列表中，双击打开【拒绝通过远程桌面服务登录】策略的属性。
6. 在 “拒绝通过远程桌面服务登录 属性” 窗口中，检查拒绝通过远程桌面服务登录的用户列表是否存在需要登录的帐户。
 - 是，请将需要登录的帐户从列表中删除。
 - 否，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=7&source=0&data_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8CVM&level3_id=142&radio_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%99%BB%E5%BD%95%E4%B8%8D%E4%B8%8A&queue=15&scene_code=12686&step=2) 反馈。

