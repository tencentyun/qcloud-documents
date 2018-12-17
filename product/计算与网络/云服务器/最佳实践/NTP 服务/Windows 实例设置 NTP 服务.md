## 操作场景

本文介绍 Windows Server 如何开启 NTP 服务和修改时钟源服务器地址。

Windows 时间服务（Windows Time service， W32Time）用于本地系统与时钟源服务器之前的时间同步。其使用网络时间协议（NTP）来同步网络上的计算机时钟。 下面以 Windows Server 2016 为例，说明如何用客户端和命令行的方式开启 NTP 服务和修改时钟源服务器地址。

## 操作步骤

1. [远程登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)。
2. 单击 “管理工具 > 服务 > Windows Time”。
![Windows Time](https://main.qcloudimg.com/raw/0791d5ed9387f4f876e87e41d368f837.png)
3. 启动类型设置为 “自动”，如果服务未启动，则单击 “启动”。
![w32time](https://main.qcloudimg.com/raw/5c1bb71c0e459a3b1e6504179751a727.png)
4. 任务栏的通知区域，单击时间，单击 “更改日期和时间设置”。
![时间设置](https://main.qcloudimg.com/raw/977f0739c7cccdb5ef10a563d60220d2.png)	
5. 切换到 “Internet时间” 标签，单击更改设置。
![Internet时间](	https://main.qcloudimg.com/raw/ed410b96b0f38e6be2837a13e9237b33.png)
6. 在 Internet 时间设置弹窗中，输入目标时钟源服务器域名或者 IP 地址，单击 “确定”。
![Internet时间设置](https://main.qcloudimg.com/raw/f34302c371c011d3b6e4046036910baa.png)
7. 设置完成后，重新打开 “日期与时间” 即可看到时钟源服务器已经更换。
![确认](	https://main.qcloudimg.com/raw/ed410b96b0f38e6be2837a13e9237b33.png)


