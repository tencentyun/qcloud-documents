## 操作场景
本文介绍如何激活 Windows 云服务器的操作系统。



<dx-alert infotype="explain" title="">
此文档只针对腾讯云提供的 Windows Server 公共镜像，自定义镜像或外部导入镜像不能采用本文的激活方式。
</dx-alert>




## 操作步骤
1. 登录 Windows 云服务器，详情请参见 [使用标准方式登录 Windows 实例](https://cloud.tencent.com/document/product/213/57778)。
2. 在操作系统桌面左下角右键单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/0cfefcbe7474bf6b532a589c53314d5b.png" style="margin:-3px 0px">，在弹出菜单中选择 **Windows PowerShell (管理员)**。
3. 在 powershell 窗口中，依次执行以下命令，激活操作系统。
```
slmgr /upk
```
```
slmgr /ipk <ProductKey>
```
```
slmgr /skms kms.tencentyun.com
```
```
slmgr /ato
```
[](id:ProductKey)`slmgr /ipk <ProductKey>` 命令中的 `<ProductKey>` 请对应操作系统版本进行替换：
   - Windows Server 2008 R2 企业版：`489J6-VHDMP-X63PK-3K798-CPX3Y`
   - Windows Server 2012 R2 数据中心版：`W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9`
   - Windows Server 2016：`CB7KF-BWN84-R7R2Y-793K2-8XDDG`
   - Windows Server 2019：`WMDGN-G9PQG-XVVXX-R3X43-63DFG`
4. 重启云服务器，使配置生效。详情请参见 [重启实例](https://cloud.tencent.com/document/product/213/4928)。


## 相关问题
在某些 Windows 操作系统未被激活的场景下，高配机器的系统内存将被限制只能用至2GB，其余内存会以“为硬件保留的内存”的形式被限制使用。该原因为 `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ProductOptions` 注册表被损坏，您可执行以下命令，判断是否需重新激活系统。
```
(Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\ProductOptions\).ProductPolicy.count
```
 - 若返回结果为例如56184等万级别数值，则无需再次激活系统。
 - 若返回结果为 “未激活值：1960”，则请参考以下方法进行解决。
<dx-tabs>
::: 方法1
1. 执行以下命令，激活系统。
```
slmgr.vbs /ipk <ProductKey>
```
<dx-alert infotype="explain" title="">
`<ProductKey>` 请根据实际使用的操作系统版本进行替换，详情请参见 [ProductKey](#ProductKey)。
</dx-alert>
2. 命令执行完毕后，可重复执行 `(Get-ItemProperty...` 命令进行验证，返回值已变为56184。
3. 重启云服务器，使配置生效。详情请参见 [重启实例](https://cloud.tencent.com/document/product/213/4928)。
4. 执行以下命令，激活系统。
```
slmgr.vbs /ato
```

:::
::: 方法2
1. 执行以下命令，进行修复。
```
slmgr.vbs /rilc 
```
2. 命令执行完毕后，可重复执行 `(Get-ItemProperty...` 命令进行验证，返回值仍为1960。
3. 执行以下命令，激活系统。
```
slmgr.vbs /ato
```

:::
::: 方法3
1. 卸载任意 msi 程序。
2. 重复执行 `(Get-ItemProperty...` 命令进行验证，返回值可能产生变化。但重启系统后，内存限制仍为2GB。
2. 执行以下命令，激活系统。
```
slmgr.vbs /ato
``` 
:::
</dx-tabs>


