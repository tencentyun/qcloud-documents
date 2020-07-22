## 问题描述
Windows 使用远程桌面连接 Windows 实例时，提示 “连接被拒绝，因为没有授权此用户帐户进行远程登录。”。如下图所示：
![连接被拒绝](https://main.qcloudimg.com/raw/9ce749a2481cabf30cccdefeb00ae770.png)

## 问题原因

该用户未被允许通过远程桌面连接方式登录 Windows 实例。

## 解决方案

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在 “云主机” 页面的实例列表中，选择待登录的 CVM 实例，单击【登录】。如下图所示：
![云服务器列表页](https://main.qcloudimg.com/raw/56596196a93181ac4c9467abe19c383a.png)
3. 在弹出的 “登录Windows云服务器” 窗口中，选择 “浏览器 VNC 方式登录”，单击【立即登录】。如下图所示：
![VNC登录入口](https://main.qcloudimg.com/raw/80b613a90328bb34a006d5988dcff18b.png)
4. 在弹出的登录窗口中，选择左上角的 “发送远程命令”，单击 **Ctrl-Alt-Delete** 进入系统登录界面。如下图所示：
![Ctrl-Alt-Delete](https://main.qcloudimg.com/raw/27daf8cc33746b195c74dfb5066addee.png)
5. 在操作系统界面，选择【开始】>【运行】，输入 **gpedit.msc**。
6. 按 **Enter**，打开本地组策略略编辑器。
7. 在左侧导航树中，选择【计算机配置】>【Windows 设置】>【安全设置】>【本地策略】>【用户权限分配】。如下图所示：
![本地组策略编辑器](https://main.qcloudimg.com/raw/60b534aab8567e20a8f39c883c7f522b.png)
8. 在右侧的策略列表中，双击打开【允许通过远程桌面服务登录】策略的属性。
9. 在 “允许通过远程桌面服务登录 属性” 窗口中，检查允许通过远程桌面服务登录的用户列表是否存在需要登录的帐户。如下图所示：
![允许通过远程桌面服务登录](https://main.qcloudimg.com/raw/9d7d4d42a9cc3765580e7fba88e87ddd.png)
 - 是，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=7&source=0&data_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8CVM&level3_id=142&radio_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%99%BB%E5%BD%95%E4%B8%8D%E4%B8%8A&queue=15&scene_code=12686&step=2) 反馈。
 - 否，请执行下一步。
10. 单击【添加用户或组(U)】，打开 “选择用户或组”。
11. 在 “选择用户或组” 的窗口中，输入需要进行远程登录的帐户，单击【确定】。如下图所示：
![添加](https://main.qcloudimg.com/raw/e335878ede2c8af8b59330155430ee80.png)
