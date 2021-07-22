## 现象描述
Windows 云服务器实例在安装了第三方安全软件后，重置实例密码不生效。

## 可能原因
若您在 Windows 实例上安装了例如360安全卫士或火绒等第三方安全软件，则有可能因第三方安全软件拦截了重置密码组件 `cloudbase-init`，导致重置实例密码失效。

## 解决思路
参考 [处理步骤](#ProcessingSteps) 检查并设置信任 `cloudbase-init` 组件。

## 处理步骤[](id:ProcessingSteps)
>?以下操作步骤以 Windows server 2012 R2 为例。
>
1. 参考 [使用标准方式登录 Windows 实例（推荐）](https://cloud.tencent.com/document/product/213/57778)，登录目标 Windows 实例。
2. 对应实际安装的第三方安全软件，恢复并设置 `cloudbase-init` 组件。

<dx-tabs>
::: 360安全卫士
360安全卫士安装完成后，会定期扫描系统，如果扫描到 `cloudbase-init` 组件，则会认为其高风险，将其隔离。请参考以下步骤恢复组件，并设置为信任文件：
1. 打开360安全卫士，选择【木马查杀】>【恢复区】。如下图所示：
![](https://main.qcloudimg.com/raw/cfc16c35c1eafbf4938f5ef4711cf0ee.png)
2. 在弹出的“安全操作中心”窗口中，勾选文件并单击【恢复所选】。
3. 在弹出的确定窗口中，勾选“恢复后信任此文件，不再查杀”，并单击【恢复】即可。如下图所示：
![](https://main.qcloudimg.com/raw/4e7dee481a05243cec89ba5c6b1a5eb0.png)
:::
::: 火绒安全软件
火绒安全软件安装完成后，不会主动将 `cloudbase-init` 组件隔离，而是会拦截 `cloudbase-init` 修改密码的行为。请参考以下步骤设置组件为信任文件：
1. 打开火绒安全软件，选择右上角的 <img src="https://main.qcloudimg.com/raw/66dcf0fca93bab386180ab4337ebda92.png" style="margin:-3px 0px">，并在弹出菜单中单击【信任区】。如下图所示：
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
