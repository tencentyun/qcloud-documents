## 现象描述
当您使用本地计算机远程连接 Windows 轻量应用服务器实例时，出现如下图所示报错信息：
![](https://main.qcloudimg.com/raw/fc8eb4050af9a2b5d808b6bf5f40cbe7.png)

远程桌面由于以下原因之一无法连接到远程计算机：
1）未启用对服务器的远程访问
2）远程计算机已关闭
3）在网络上远程计算机不可用

确保打开远程计算机、连接到网络并且启用远程访问。


## 可能原因

导致出现以上提示的原因包括（不限于以下情况，请根据实际情况进行分析）：
- 实例处于非正常运行状态
- 实例的防火墙未放通远程登录端口（默认为3389）
- 远程桌面服务未启动
- 远程桌面设置问题
- Windows 防火墙设置问题


## 解决思路
按照 [处理步骤](#ProcessingSteps) 依次排查并解决问题。


## 处理步骤[](id:ProcessingSteps)


### 检查实例是否处于运行状态
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 在“服务器”页面，查看实例是否处于“运行中”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/faee7a4ea28561aac4612b0c1741883d.png)
 - 是，请进行下一步。
 - 否，请启动该 Windows 实例。


### 检查实例远程登录端口（3389）是否放通
1. 在实例详情页面中，选择**防火墙**页签。
2. 检查实例的防火墙是否放通远程登录接口（默认远程桌面端口：3389）。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c5e3626c744eff84c824236598dec6e8.png)
 - 是，请进行下一步。
 - 否，请编辑对应的防火墙规则，进行放通。操作方法请参考 [添加防火墙规则](https://cloud.tencent.com/document/product/1207/44577#.E6.B7.BB.E5.8A.A0.E9.98.B2.E7.81.AB.E5.A2.99.E8.A7.84.E5.88.99)。

### 检查远程桌面服务
1. [使用 VNC 方式登录 Windows 实例](https://cloud.tencent.com/document/product/1207/44656)，检查 Windows 实例远程桌面服务是否开启。
<dx-alert infotype="explain" title="">
 以下操作以 Windows Server 2016 操作系统的实例为例。
</dx-alert>
2. 右键单击 <img src="https://main.qcloudimg.com/raw/6191c3ad8f212e7f8f6dddbbabd43f12.png" style="margin: -5px 0px;">，在弹出的菜单中选择**系统**。
3. 在打开的“系统”窗口中，选择**高级系统设置**。
4. 在打开的“系统属性”窗口中，选择**远程**页签，检查是否勾选“允许远程连接到此计算机”。如下图所示：
![](https://main.qcloudimg.com/raw/cfe9604b72b95f3250d146d27f5d2f3b.png)
 - 是，请执行 [步骤5](#step04_5)。
 - 否，请勾选并单击**确定**。
5. [](id:step04_5) 右键单击 <img src="https://main.qcloudimg.com/raw/6191c3ad8f212e7f8f6dddbbabd43f12.png" style="margin: -5px 0px;">，在弹出的菜单中选择**计算机管理**。
6. 在打开的“计算机管理”窗口左侧菜单栏中，选择**服务和应用程序** > **服务**。
7. 在右侧的服务列表中，检查 **Remote Desktop Services** 是否启动。如下图所示：
![](https://main.qcloudimg.com/raw/0ce9909d728725f832722a7ef1afa4e1.png)
 - 是，请执行 [步骤8](#step04_8)。
 - 否，请启动服务。
8. [](id:step04_8) 右键单击 <img src="https://main.qcloudimg.com/raw/6191c3ad8f212e7f8f6dddbbabd43f12.png" style="margin: -5px 0px;">，在弹出的菜单中选择**运行**。
9. 在弹出的“运行”窗口中，输入 **msconfig** 并单击**确定**。
10. 在打开的“系统配置”窗口中，检查是否勾选**正常启动**。如下图所示：
![](https://main.qcloudimg.com/raw/599835372c8b577025f9023ce8758c8a.png)
 - 是，请进行下一步。
 - 否，请勾选并单击**确定**。


### 检查 Windows 实例的系统设置
1. [使用 VNC 登录实例](https://cloud.tencent.com/document/product/213/35704)，排查 Windows 实例的系统设置。
<dx-alert infotype="explain" title="">
 以下操作以 Windows Server 2016 操作系统的实例为例。
</dx-alert>
2. 右键单击 <img src="https://main.qcloudimg.com/raw/6191c3ad8f212e7f8f6dddbbabd43f12.png" style="margin: -5px 0px;">，在弹出的菜单中选择**运行**。
3. 在弹出的“运行”中输入 **services.msc**，并按 **Enter**，打开“服务”窗口。
4. 双击打开 **Remote Desktop Services** 的属性，检查远程桌面服务是否已启动。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/291fe25b6822f2631dd67a938f53ed53.png)
 - 是，请执行 [步骤5](#step05_5)。
 - 否，请将“启动类型”设置为“自动”，“服务状态”设置为“正在运行”（即单击**启动**，启动服务）。
5. [](id:step05_5)右键单击 <img src="https://main.qcloudimg.com/raw/6191c3ad8f212e7f8f6dddbbabd43f12.png" style="margin: -5px 0px;">，在弹出的菜单中选择**控制面板**，打开控制面板。
6. 在“控制面板”中，选择**系统与安全** > **Windows 防火墙**，打开 “Windows 防火墙”。
7. 在 “Windows 防火墙”中，检查 Windows 防火墙状态。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a3f57eebe53dba84b575ac01c1babab6.png)
 - 为“启用”状态，请执行 [步骤8](#step8)。
 - 为“关闭”状态，请开启。若无法开启，则请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_1207) 反馈。
8. [](id:step8)在 “Windows 防火墙”中，单击**允许应用或能通过 Windows 防火墙**，打开“允许的应用”窗口。
9. 在“允许的应用”窗口中，检查“允许的应用和功能(A)”是否勾选“远程桌面”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/40c065daf7f98cc6d12c4b0a608f523e.png)
 - 是，请执行 [步骤10](#step10)。
 - 否，请勾选 “远程桌面”，放通“远程桌面”。
10. [](id:step10)在 “Windows 防火墙” 中，单击**启用或关闭 Windows 防火墙**，打开“自定义设置”窗口。
11. 在“自定义设置”窗口中，将“专用网络设置”和“公用网络设置”设置为“关闭 Windows 防火墙(不推荐)”。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5560c0aa60bdee371f5e100b0c346865.png)

若执行以上操作后仍无法通过远程桌面连接到 Windows 实例，请通过 [在线支持](https://cloud.tencent.com/online-service?from=doc_1207) 反馈。




