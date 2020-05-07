
本文档介绍云服务器因安全组设置问题导致无法远程连接的排查方法和解决方案。

## 步骤一：连接测试

 1. 在本地计算机，同时按住【 Windows 】和【 R 】，在弹出窗口中输入【 cmd 】，回车。打开命令提示符。

 2. 输入【 telnet + IP + 端口号 】连接云服务器。例如：输入 `telnet 192.XXX.XXX.XXX 3389`
 
	> - Linux 系统云服务器使用 22 端口测试。
> - Windows 系统云服务器使用 3389 端口测试。
> - 如果已修改过远程连接端口，使用修改后的端口测试。

	测试通过，则仅显示黑屏与光标，请排查其它登录问题。
	测试不通过，则如下图。请继续执行步骤二，检查安全组设置。
	![](//mc.qcloudimg.com/static/img/1fe17b76d99905024d0e5e048000d9f4/image.png)

## 步骤二：检查安全组设置

 1. 登录云服务器 [控制台](https://console.cloud.tencent.com/cvm) 。

 2. 单击需要检查的服务器 ID/主机名。

 3. 单击【安全组】（非左侧导航栏），检查入站规则。以下图为例，检查发现安全组没有开放 3389 端口（系统则检查），只开了 ICMP 协议，所以云服务器是可以 Ping 通，但 Telnet 测试失败。
	![](//mc.qcloudimg.com/static/img/2fdcf758994c7194f12d2fb627bac4e6/image.png)

## 步骤三：修改安全组设置

 - 若账号中未设置安全组或云服务器未绑定过安全组，请先完成创建安全组、向安全组中添加规则、配置 CVM 实例关联安全组。在安全组初始配置时设置端口即可。详见 [安全组](https://cloud.tencent.com/document/product/416/7596) 。

 - 若云服务器绑定过安全组，但未设置端口，请完成以下步骤。

1. 单击 “已绑定安全组”模块中安全组 ID /名称 。

2. 单击【添加规则】。
	![](//mc.qcloudimg.com/static/img/f6e3be97451d3a1aa777696e56acf4cc/image.png)

3. 输入：
  - 来源(本例输入: 0.0.0.0/0 )。
  - 协议端口( Linux 系统云服务器为 TCP:22 ，Windows 系统云服务器为 TCP:3389 )。
  - 选择策略：允许。
  - 单击【完成】。
	![](//mc.qcloudimg.com/static/img/deb951ec299d221e0895656e04b40cbf/image.png)
