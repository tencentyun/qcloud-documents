本文档以 Windows Server 2012 R2 操作系统为例，介绍 Windows 轻量应用服务器实例因重置密码失败或者不生效的排查方法和解决方案。

## 现象描述
- 重置实例密码后，提示“由于系统繁忙，您的实例重置实例密码失败(7617d94c)”。
- 重置实例密码后，新密码不生效，登录密码仍为原密码。


## 可能原因
导致重置实例密码失败或者不生效的可能原因如下：
- 轻量应用服务器中的 `cloudbase-init` 组件损坏、被修改、禁止或者未启动。
- 轻量应用服务器上安装了例如360安全卫士或火绒等第三方安全软件，则有可能因第三方安全软件拦截了重置密码组件 `cloudbase-init`，导致重置实例密码失效。
- 轻量应用服务器入侵被加密导致密码不生效，建议备份好数据，进行重装系统。

## 处理步骤

- 根据引起密码重置不成功的可能原因，提供以下两种检查方式：

### 检查 cloudbase-init 服务

1. [使用 VNC 方式登录 Windows 实例](https://cloud.tencent.com/document/product/1207/44656)。
2. 在操作系统界面，右键单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin: -3px 0px;"></img>，在弹出的菜单中选择**运行**。
3. 在“运行”窗口中输入 **services.msc**，并按 **Enter** 打开 “服务” 窗口。
4. 在“服务”窗口中，检查是否存在 `cloudbase-init` 服务。如下图所示：
![](https://main.qcloudimg.com/raw/61eb2c9bf42f1da08aae96b44173ac35.png)
 - 是，执行下一步。
 - 否，重新安装 `cloudbase-init` 服务。具体操作请参见 [Windows 操作系统安装 Cloudbase-Init](https://cloud.tencent.com/document/product/213/30000)。
4. 双击打开 `cloudbase-init` 的属性。如下图所示：
![](https://main.qcloudimg.com/raw/1f9292a4e922b662e271ecfb49bf4bef.png)
5. 选择**常规**页签，检查 `cloudbase-init` 的“启动类型”是否设置为**自动**。
 - 是，执行下一步。
 - 否，将 `cloudbase-init` 的“启动类型”设置为**自动**。
6. 选择**登录**页签，检查 `cloudbase-init` 的登录身份是否选择为**本地系统帐户**。
 - 是，执行下一步。
 - 否，将 `cloudbase-init` 的登录身份设置为**本地系统帐户**。
7. 选择**常规**页签，单击服务状态下的**启动**，手动启动 `cloudbase-init` 服务并观察是否报错。
 - 是，[检查轻量应用服务器中安装的安全软件](#CheckSecuritySoftware)。
 - 否，执行下一步。
8. 在操作系统界面，右键单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin: -3px 0px;"></img>，在弹出的菜单中选择**运行**。
9. 在“运行”窗口中输入 **regedit**，并按 **Enter** 打开“注册表编辑器”窗口。
9. 在“注册表编辑器”窗口左侧的注册表导航中，依次展开 **HKEY_LOCAL_MACHINE** > **SOFTWARE** > **Cloudbase Solutions** > **Cloudbase-Init** 目录。
![](https://qcloudimg.tencent-cloud.cn/raw/0e840b213efeac583d803fe1a6f960e2.png)
10. 找到并双击打开 **ins-xxx** 下的全部 “LocalScriptsPlugin” 注册表，并检查 LocalScriptsPlugin 的数值数据是否为2。如下图所示：
![](https://main.qcloudimg.com/raw/2394613b372459707e8209c38e2a4105.png)
 - 是，执行下一步。
 - 否，将 LocalScriptsPlugin 的数值数据设置为2。
11. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin: -3px 0px;"></img>，选择**这台电脑**，检查设备和驱动器中是否加载了 CD-驱动器。如下图所示：
![](https://main.qcloudimg.com/raw/8c6e8c83acfdfaccbdcfc98597662aaa.png)
 - 是，[检查轻量应用服务器中安装的安全软件](#CheckSecuritySoftware)。
 - 否，在设备管理器中启动 CD-ROM 驱动器。


### 检查轻量应用服务器中安装的安全软件[](id:CheckSecuritySoftware)

在已安装的安全软件，选择全盘扫描，检查轻量应用服务器有是否漏洞，以及检查 `cloudbase-init` 的核心组件是否被拦截。
- 如检查出轻量应用服务器有漏洞，请修复。
- 如检查出核心组件被拦截，请取消拦截。

`cloudbase-init` 组件检查及配置步骤如下：
1. [使用 VNC 方式登录 Windows 实例](https://cloud.tencent.com/document/product/1207/44656)。
2. 对应实际安装的第三方安全软件，恢复并设置 `cloudbase-init` 组件。

<dx-tabs>
::: 360安全卫士
360安全卫士安装完成后，会定期扫描系统，如果扫描到 `cloudbase-init` 组件，则会认为其高风险，将其隔离。请参考以下步骤恢复组件，并设置为信任文件：
1. 打开360安全卫士，选择**木马查杀** > **恢复区**。如下图所示：
![](https://main.qcloudimg.com/raw/cfc16c35c1eafbf4938f5ef4711cf0ee.png)
2. 在弹出的“安全操作中心”窗口中，勾选文件并单击**恢复所选**。
3. 在弹出的确定窗口中，勾选“恢复后信任此文件，不再查杀”，并单击**恢复**即可。如下图所示：
![](https://main.qcloudimg.com/raw/4e7dee481a05243cec89ba5c6b1a5eb0.png)
:::
::: 火绒安全软件
火绒安全软件安装完成后，不会主动将 `cloudbase-init` 组件隔离，而是会拦截 `cloudbase-init` 修改密码的行为。请参考以下步骤设置组件为信任文件：
1. 打开火绒安全软件，选择右上角的 <img src="https://main.qcloudimg.com/raw/66dcf0fca93bab386180ab4337ebda92.png" style="margin:-3px 0px">，并在弹出菜单中单击**信任区**。如下图所示：
![](https://main.qcloudimg.com/raw/93e25735ff17294bb36d224b074ec67a.png)
2. 在弹出的“信任区”窗口中，依次添加下列文件及文件夹即可。如下图所示：
![](https://main.qcloudimg.com/raw/a8b0bd702407e5100238237fb6a5821a.png)
文件及文件夹路径如下：
 - `C:\Program Files\Cloudbase Solutions`
 - `C:\Program Files\Cloudbase Solutions\Cloudbase-Init\Python\Scripts`
 - `C:\Program Files\QCloud`
 - `C:\Windows\System32\cmd.exe`
 - `C:\Windows\System32\WindowsPowerShell`
 - `C:\Windows\SysWOW64\cmd.exe`
:::
</dx-tabs>


