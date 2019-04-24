## 问题描述

Windows 使用远程桌面连接 Windows 实例时，出现如下图所示的提示：
![无法连接到远程计算机](https://main.qcloudimg.com/raw/fc8eb4050af9a2b5d808b6bf5f40cbe7.png)
远程桌面由于以下原因之一无法连接到远程计算机：
1）未启用对服务器的远程访问
2）远程计算机已关闭
3）在网络上远程计算机不可用
确保打开远程计算机、连接到网络并且启用远程访问。


## 问题分析

导致该提示的原因包括但不限于以下情况，请根据实际情况进行分析。
- 实例处于非正常运行状态
- 无公网 IP 或公网带宽为0
- 实例绑定的安全组未放通远程登录端口（默认为3389）
- 远程桌面服务未启动
- 远程桌面设置问题
- Windows 防火墙设置问题

## 排查步骤

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在 “云主机” 页面的实例列表中，查看实例是否处于【运行中】。如下图所示：
![CVM列表页](https://main.qcloudimg.com/raw/4e7ac5b5c386b8619418e2a9adf3bbc3.png)
 - 是，请执行下一步。
 - 否，请启动该 Windows 实例。
3. 检查服务器是否设置公网 IP。如下图所示：
![无公网IP](https://main.qcloudimg.com/raw/762719d42601ce99448df7dc94acfe32.png)
 - 是，请执行下一步。
 - 否，请 [申请弹性公网IP并进行绑定](https://cloud.tencent.com/document/product/213/16586)。
4. 检查公网带宽是否为0Mb。
 - 是，请执行下一步。
 - 否，请通过 [调整网络](https://cloud.tencent.com/document/product/213/15517) 将带宽调整到1Mb或以上。
5. 单击实例名称，进入实例信息页面。
6. 在 “安全组” 页签下，检查实例的安全组是否放通远程登录接口（默认远程桌面端口：3389）。如下图所示：
![安全组](https://main.qcloudimg.com/raw/8591cea100c0e39b7d2f6cde250b4b16.png)
 - 是，请执行下一步。
 - 否，请编辑对应的安全组规则，进行放通。操作方法请参考 [安全组操作指南](https://cloud.tencent.com/document/product/213/18197)。
7. 使用 VNC 登录实例，排查 Windows 实例的系统设置。
>? VNC 登录详细请参考 [登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435) 中的 “使用 VNC 登录” 。
8. 单击【开始】，在【运行】中输入 **services.msc**，并按 **Enter**，打开 “服务” 窗口。
9. 双击打开 “Remote Desktop Services” 的属性，检查远程桌面服务是否已启动。如下图所示：
![Remote Desktop Service](https://main.qcloudimg.com/raw/ad9fc18310fc823ea11883f9c31b7838.png)
 - 是，请执行下一步。
 - 否，请将 “启动类型” 设置为 “自动”，“服务状态” 设置为 “正在运行”（即单击【启动】，启动服务）。
10. 单击【开始】，在【运行】中输入 **sysdm.cpl**，按 **Enter**，打开 “系统属性” 窗口。
11. 在 “远程” 页签中，检查远程桌面是否设置为 “允许远程连接到此计算机(L)”。如下图所示：
![远程设置](https://main.qcloudimg.com/raw/7cadb6d62af77f7035d973283b104ac8.png)
 - 是，请执行下一步。
 - 否，请将远程桌面设置为 “允许远程连接到此计算机(L)”。
12. 单击【开始】，选择【控制面板】，打开控制面板。
13. 在 “控制面板” 中，选择【系统与安全】>【Windows 防火墙】，打开 “Windows 防火墙”。
14. 在 “Windows 防火墙” 中，检查 Windows 防火墙状态。如下图所示：
![Windows 防火墙状态](https://main.qcloudimg.com/raw/5a18e345dd8fcb6aaa5b9f95c4bc4d63.png)
 - 为 “启用” 状态，请执行下一步。
 - 为 “关闭” 状态，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=7&source=0&data_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8CVM&level3_id=142&radio_title=%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%99%BB%E5%BD%95%E4%B8%8D%E4%B8%8A&queue=15&scene_code=12686&step=2) 反馈。
15. 在 “Windows 防火墙” 中，单击【允许应用或能通过 Windows 防火墙】，打开 “允许的应用” 窗口。
16. 在 “允许的应用” 窗口中，检查 “允许的应用和功能(A)” 是否勾选 “远程桌面”。如下图所示：
![勾选远程桌面](https://main.qcloudimg.com/raw/4a0d3906b5be714610fa8e21e4ed3624.png)
 - 是，请执行下一步。
 - 否，请勾选 “远程桌面”，放通“远程桌面”。
17. 在 “Windows 防火墙” 中，单击【启用或关闭 Windows 防火墙】，打开 “自定义设置” 窗口。
18. 在 “自定义设置” 窗口中，将 “专用网络设置” 和 “公用网络设置” 设置为 “关闭 Windwos 防火墙(不推荐)”。如下图所示：
![关闭](https://main.qcloudimg.com/raw/4a09dea7a9695599b02a2facc1be02ec.png)


