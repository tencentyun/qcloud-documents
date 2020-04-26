## 前言

数据无价，相信很多人都深有体会。数码照片、电子文档、工作产出、游戏存档，哪一样都丢不起。除了硬盘故障导致的文件丢失，人为的误操作、计算机宕机或软件崩溃导致的单一文件丢失，以及被要求“回滚版本”却发现没有保存历史版本的尴尬，都是工作和生活中令人头疼不已的问题。因此，备份的重要性，毋庸置疑。

说起备份，很多人想到的就是使用移动硬盘或者在局域网内搭建 NAS 存储，然后将文件往里面上传就行了。

真的这么简单吗？

备份，其实是一个系统工程。除了将文件复制到备份媒介上，还需要验证备份内容的准确性。而复制与验证这两项工作，还需要定期去执行，这样在发生文件丢失时，才能最大限度挽回损失。此外，备份媒介也是需要去维护的，需要及时将损坏的硬盘进行替换。

那么，有没有简单的办法可以保证文件的安全呢？

答案是肯定的。随着云服务的发展，我们有可靠的企业级云存储服务，腾讯云 COS 对象存储就是这样一类服务；随着国家提速降费的号召，宽带越来越快，而且越来越便宜，让我们将文件备份上云成为现实。接下来，我们就需要一款软件，打通计算机中的文件和云存储，将我们的文件定期自动备份到云上，并定期验证备份文件的准确性。

## 软件介绍

[Arq® Backup](https://www.arqbackup.com/) 是一款支持 Windows 和 macOS 系统的商业备份软件，该软件在系统后台运行，根据配置每隔一段时间自动备份指定的目录，同时软件会保留每个时间点备份的文件，因此可以轻松的找到某个文件的历史版本。此外，每个时间点的备份只会备份有差异的文件，对于不同路径的重复文件也只备份一次，使备份体积尽可能小，备份速度尽可能快。在将备份文件传输到网络之前，软件会基于用户输入的密码对备份文件进行加密，保证其在网络传输过程中或在云端存储中都不会被盗用，保证用户敏感数据的安全性。

Arq® Backup 商业授权为49.99美元每个用户，用户购买后可在自己的任意多台桌面计算机上使用，同时软件提供30天免费使用，可以试用后再购买。

> ?Arq® Backup 软件目前暂时没有简体中文版，软件的下载、购买和相关说明均可在该软件 [官方网站](https://www.arqbackup.com/) 内查看。

## 准备腾讯云对象存储

1. [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 登录 [对象存储 COS 控制台](https://console.cloud.tencent.com/cos5)，按照提示开通 COS。
>?若您目前已经在使用 COS，可忽略1 - 2步骤。
3. 在对象存储 COS 控制台中，[创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
 - 名称：存储桶名称，例如 “backups”。
 - 所属地域：可以根据您所在地就近选择，但是请不要选择有“金融”字样的金融专区，目前我们对于西南地区有价格上的优惠，因此也可以选择“成都”或“重庆”享受更优惠的价格。
  ![](https://main.qcloudimg.com/raw/c2acd4b17d722b3f63cdb50833bdf713.png)
其他配置项保持默认，将【请求域名】地址复制保存，然后单击【确定】完成创建。
4. 登录 [ API 密钥管理控制台](https://console.cloud.tencent.com/cam/capi) ，记录保存密钥信息。
  ![](https://main.qcloudimg.com/raw/6ab82302ad45f9dfe92cd406a4ce15bc.png)

## 安装并配置 Arq® Backup

> ?本文以 Windows 版作为示例。

1. 从 [Arq® Backup 官网](https://www.arqbackup.com/) 下载软件。
2. 按提示完成软件安装，安装完成后软件会自动启动，首次启动时会提示登录，先单击【Cancel】跳过，随后软件会弹出窗口要求选择备份媒介类型。
   ![](https://main.qcloudimg.com/raw/a094270a7f9c23fc68b136c92c18b26b.png)
3. 选择 Other S3-Compatible Service，单击【Continue】。
4. 按照以下说明进行配置：
	- S3-Compatible Server URL：上文记录的请求域名中从 cos 开始的部分，并在前面加上 `https://`，例如 `https://cos.ap-chengdu.myqcloud.com`，请注意这里不包含存储桶名称。
	- Access Key ID：上文记录的密钥信息中的SecretId。
	- Secret Access Key：上文记录的密钥信息中的SecretKey。
	- Request Signature Version：Signature Version 2。
		![](https://main.qcloudimg.com/raw/2f148ce6ad147b286dbad49c5991bf03.png)
5. 单击【Add Destination】确定备份媒介。
6. 等待软件完成网络请求，在随后的界面中选择【Use existing bucket】，并选择上文创建的存储桶，如【backups-1250000000】。
	 ![](https://main.qcloudimg.com/raw/ac47c16ceb1d9726de4a019bcc8f5f96.png)
7. 单击【Add】完成添加，随后会提示要做什么，单击【Set Up Backups】。
   ![](https://main.qcloudimg.com/raw/b4fbec94ea2fa1bf65fd59ecd79aa8f4.png)
8. 在开始备份前，软件会要求输入用于加密备份文件的密码。输入两次用于加密备份文件的密码，并单击【Continue】。**注意请牢记备份密码，否则将无法从备份恢复文件！**在随后的弹框中单击【确定】。
   ![](https://main.qcloudimg.com/raw/a275c88371abf0de9a6ec1d1a43b0457.png)
9. 等待软件完成扫描后，会提示自动每小时备份 C 盘，单击【确定】关闭，在主界面左侧列表中，展开 CONFIGURE BACKUPS，选择 To cos.xxx.myqcloud.com（其中xxx根据存储桶所在地域有所不同）。
   ![](https://main.qcloudimg.com/raw/6b5ec789cb7fc5f6f8d77229c5e56e97.png)
10. 单击右侧【Add a Folder to Backups ...】，在弹出的界面中选择其他要备份的目录，如 D:\Pictures，单击【OK】确认。
    ![](https://main.qcloudimg.com/raw/d81843dcb0bc477a187508b93bfb14e9.png)
11. 至此您已经完成备份的基本配置，软件默认将在下一个整点小时开始执行备份作业，您也可以单击 Backups 菜单中的【Back Up Now】立即开始首次备份。
    ![](https://main.qcloudimg.com/raw/2de7d08435cdfc101c5d037b88129358.png)

## 从备份中恢复文件

1. 在主界面左侧列表中，展开 RESTORE FILES，选择 From cos.xxx.myqcloud.com（其中 xxx 根据存储桶所在地域有所不同），等待软件完成扫描。由于 Arq® Backup 支持将多台计算机中的文件备份至同一存储桶，因此在随后的子项目中会列出所有备份至该存储桶的计算机名，继续展开要恢复的文件所在的计算机、待恢复的目录。Arq® Backup 根据设置的备份频率周期自动执行备份，而旧的备份并不会被新的备份所覆盖，因此您可以恢复文件的历史版本。在最后单击要恢复的文件对应的时间点，此时在右侧将列出该备份时间点所包含的文件。
   ![](https://main.qcloudimg.com/raw/ff29abab8c7163da17675792d7a31d88.png)
2. 在右侧文件列表选择要恢复的文件或目录，单击右下角【Restore】，在弹出的界面中指定一个目录用于存放恢复出来的文件。等待下方界面提示恢复完成即可到刚刚指定的目录中查看恢复的文件。
   ![](https://main.qcloudimg.com/raw/bd4bb13dc4c220e8164d05ff70ed6974.png)

## 补充说明

Arq® Backup 默认每个整点小时备份一次，备份采用增量备份，即只备份距离上次备份时有变化的文件，每60天验证一次最新备份数据的完整性，您可以在【File】-【Preferences】-【Destinations】中，选择之前配置的备份存放位置，单击【Edit ...】修改相关的设置。
