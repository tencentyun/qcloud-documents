## 操作场景
对于需要入域且使用域账号登录 Windows 云服务器的用户，可在创建自定义镜像前，执行 Sysprep 操作以确保在实例入域后 SID 唯一。否则，通过自定义镜像创建的云服务器会因为包含了和原实例相关的信息（如具有相同的 SID 信息），导致入域失败。如果您的 Windows 云服务器不需要入域等操作，可以跳过此操作。

本文以 Windows Server 2012 R2 64位操作系统为例，指导您在 Windows 操作系统上执行 Sysprep，使得 Windows 云服务器入域后 SID 唯一。

更多 Sysprep 信息可参考：`https://technet.microsoft.com/zh-cn/library/cc721940(v=ws.10).aspx`


## 注意事项

- Windows 云服务器必须为正版 Windows 操作系统，且已激活。
- 如您的 Windows 云服务器通过非公共镜像方式创建，该云服务器仅支持使用原镜像自带的 Sysprep 版本，且 Sysprep 必须始终从 `%WINDIR%\system32\sysprep` 目录运行。
-  必须保证剩余 Windows 重置计数 ≥ 1，否则不能执行 Sysprep 封装。
您可以通过执行 `slmgr.vbs /dlv` 命令，查看剩余 Windows 重置计数。
-  Windows 云服务器中的 Cloudbase-Init 帐户为 Cloudbase-Init 代理程序的内置帐户，用于云服务器启动时获取元数据并执行相关配置。如果您修改、删除此帐户或者卸载 Cloudbase-Init 代理程序，会导致由此云服务器创建的自定义镜像生成的云服务器在初始化时，自定义信息注入失败。不建议修改或删除 Cloudbase-init 帐户。  

## 前提条件

- 已使用 Administrator 帐号 [登录 Windows 云服务器](https://cloud.tencent.com/document/product/213/5435)。
- 已 [在 Windows 云服务器中安装 Cloudbase-Init](https://cloud.tencent.com/document/product/213/30000)。

## 操作步骤

1. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png"></img>，打开 Windows PowerShell 窗口。
2. 在 Windows PowerShell 窗口中，执行以下命令，进入 Cloudbase-init 工具的安装路径。
<dx-alert infotype="explain" title="">
以 Cloudbase-init 工具安装在 `C:\Program Files\Cloudbase Solutions\` 目录下为例。
</dx-alert>
```
cd 'C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf'
```
3. 执行以下命令，对 Windows 系统进行封装。
<dx-alert infotype="notice" title="">
 - 执行以下命令时，命令必须包含`/unattend:Unattend.xml`，否则会重置您当前云服务器的用户名、密码等重要配置信息。后续使用此镜像创建云服务器时，若登录方式选择了“保留镜像设置”，启动云服务器后需要手动重置该云服务器的用户名和密码。
- 执行以下命令后，云服务器会自动关机。为了保证后续通过此镜像创建的云服务器 SID 唯一，在创建自定义镜像之前，请不要重新启动该台云服务器，否则此操作将仅对当前云服务器生效。  
- 针对 Windows Server 2012 以及 Windows Server 2012 R2 的操作系统，执行以下命令后，该云服务器的帐户（Administrator）和密码会被清除。待重新启动云服务器后，请重置您的帐户和密码，并妥善保管新设置的密码。具体操作请参见 [重置实例密码](https://cloud.tencent.com/document/product/213/16566)。
</dx-alert>
```
C:\Windows\System32\sysprep\sysprep.exe /generalize /oobe /unattend:Unattend.xml
```
4. 参考 [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942)，将执行了 Sysprep 操作的云服务器实例制作成镜像，并使用该镜像创建云服务器实例。
即可实现所有新建的云服务器实例入域后具有唯一的 SID。
<dx-alert infotype="explain" title="">
您可以通过执行 `whoami /user` 命令，查看云服务器的 SID。
</dx-alert>






