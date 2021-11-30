## 前言

数据无价，相信很多人都深有体会。数码照片、电子文档、工作产出、游戏存档，哪一样丢失都很头疼。除了硬盘故障导致的文件丢失，人为的误操作、计算机宕机或软件崩溃导致的单一文件丢失，以及被要求“回滚版本”却发现没有保存历史版本的尴尬，都是工作和生活中令人头疼不已的问题。因此，备份的重要性，毋庸置疑。

说起备份，很多人想到的就是使用移动硬盘或者在局域网内搭建 NAS 存储，然后将文件往里面上传就行了。但实际上真的这么简单吗？

备份，其实是一个系统工程。除了将文件复制到备份媒介上，还需要验证备份内容的准确性。而复制与验证这两项工作，还需要定期去执行，这样在发生文件丢失时，才能最大限度挽回损失。此外，备份媒介也是需要去维护的，需要及时将损坏的硬盘进行替换。

综上所述，那么有没有简单的办法可以保证文件的安全呢？答案是肯定的。

随着云服务的发展，我们有可靠的企业级云存储服务，腾讯云 COS 对象存储就是这样一类服务；随着国家提速降费的号召，宽带越来越快，而且越来越便宜，让我们将文件备份上云成为现实。接下来，我们就需要一款软件，打通计算机中的文件和云存储，将我们的文件定期自动备份到云上，并定期验证备份文件的准确性。

## 软件介绍

[Arq® Backup](https://www.arqbackup.com/) 是一款支持 Windows 和 macOS 系统的商业备份软件，该软件在系统后台运行，根据配置每隔一段时间自动备份指定的目录，同时软件会保留每个时间点备份的文件，因此可以轻松的找到某个文件的历史版本。此外，每个时间点的备份只会备份有差异的文件，对于不同路径的重复文件也只备份一次，使备份体积尽可能小，备份速度尽可能快。在将备份文件传输到网络之前，软件会基于用户输入的密码对备份文件进行加密，保证其在网络传输过程中或在云端存储中都不会被盗用，保证用户敏感数据的安全性。

Arq® Backup 商业授权为49.99美元每个用户，用户购买后可以在单台计算机上使用，同时软件提供30天免费使用，可以试用后再购买。

> ?Arq® Backup 软件目前暂时没有简体中文版，软件的下载、购买和相关说明均可在该软件 [官方网站](https://www.arqbackup.com/) 内查看。

## 准备腾讯云对象存储

> ?若您目前已经在使用 COS，请忽略1 - 2步骤。

1. [注册腾讯云账号](https://cloud.tencent.com/document/product/378/17985) 并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。
2. 登录 [对象存储 COS 控制台](https://console.cloud.tencent.com/cos5)，按照提示开通 COS。
3. 在对象存储 COS 控制台中，单击左侧导航栏的【存储桶列表】，然后单击【创建存储桶】，开始创建存储桶：
	- 名称：存储桶名称，例如 “backups”。
	- 所属地域：可以根据您所在地就近选择，但是请不要选择金融地域，目前我们对于西南地区有价格上的优惠，因此也可以选择“成都”或“重庆”享受更优惠的价格。
  ![](https://main.qcloudimg.com/raw/c2acd4b17d722b3f63cdb50833bdf713.png)
  其他配置项保持默认，将【请求域名】地址复制保存，然后单击【确定】完成创建。
> ?创建存储桶的详细步骤，请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309)。
4. 登录 [ API 密钥管理控制台](https://console.cloud.tencent.com/cam/capi) ，创建并记录密钥信息 SecretId 和 SecretKey。
   ![](https://main.qcloudimg.com/raw/6ab82302ad45f9dfe92cd406a4ce15bc.png)

## 安装并配置 Arq® Backup

>? 本文以 Windows 的 Arq® Backup 6.2.11版本为例。
>

1. 从 [Arq® Backup 官网](https://www.arqbackup.com/) 下载软件。
2. 按提示完成软件安装，安装完成后软件会自动启动，首次启动时会提示登录，此时输入邮箱地址并单击【Start Trial】。
   ![](https://main.qcloudimg.com/raw/b9ea1e5cebb30c96fe5894bb5adb7214.png)
3. 在【Backup】界面中单击【Create a new backup plan】，添加备份计划。
   ![](https://main.qcloudimg.com/raw/397c1b77f1a3871644ef9eec63ebda7e.png)
4. 在跳转界面，选择需要备份的目录，可以选择所有硬盘或指定目录。
   ![](https://main.qcloudimg.com/raw/410a0f1728cda892f375c89103b46531.png)
5. 单击【Add storage location】，添加备份存储位置，如下图所示。
   ![](https://main.qcloudimg.com/raw/a8d33f582c5600eec6c67893f2ee3c46.png)
6. 此处我们选择【S3-Compatible Server】。
   ![](https://main.qcloudimg.com/raw/9d515b8ef332dc00a4f7a9277b70eef1.png)
7. 在跳转界面中按照以下说明进行配置。配置完毕后，单击【Continue】。
   - Server URL：输入上文记录的请求域名中，从`cos`开始的部分，并在前面加上`https://`，例如 `https://cos.ap-chengdu.myqcloud.com`，请注意这里不包含存储桶名称。
   - Access Key ID：上文记录的密钥信息中的 SecretId。
   - Secret Access Key：上文记录的密钥信息中的 SecretKey。
     ![](https://main.qcloudimg.com/raw/bfe1454b37d756068a61050d4585e451.png)
8. 在随后的界面中选择【Use an existing bucket】，并选择上文创建的存储桶，例如【backups-1250000000】，然后单击【Save】。
   ![](https://main.qcloudimg.com/raw/bcb5223dad1ac34ce642c0ecdff184b1.png)
9. （可选）选择是否加密备份数据，此处我们选择**开启**按钮。
   ![](https://main.qcloudimg.com/raw/8744311c148e6ebbc2a35c230de76002.png)
10. 在弹窗中设置用于加密的密码。输入两次用于加密备份文件的密码，并单击【OK】。**注意请牢记备份密码，否则将无法从备份恢复文件！**
    ![](https://main.qcloudimg.com/raw/43213532f56da02450b1ea52321457c6.png)
11. （可选）设置备份周期。
    ![](https://main.qcloudimg.com/raw/70bf92401110bce7b3b49af3017c189b.png)
12. 单击【Save】保存设置，然后单击【Back Up Now】开始备份。
    ![](https://main.qcloudimg.com/raw/65093effc29b66385f8ee20f293cde01.png)

## 从备份中恢复文件

1. 在主界面左侧【Backup】列表中，单击【Restore】。
   ![](https://main.qcloudimg.com/raw/844349292e7fd2d89441fe37c789349e.png)
2. 如果按照上面第9步设置了加密备份数据，则需要输入密码。
   ![](https://main.qcloudimg.com/raw/41360bd0dbaa4b131a42d56d43d1eae5.png)
3. 选择要恢复的目录或文件，以及保存恢复目录或文件的位置，单击【Restore】开始恢复。
   ![](https://main.qcloudimg.com/raw/513d4c1f317834a55d7ad1f1f93a3d80.png)
4. 恢复操作默认是从最新的备份中恢复，如果有需要，可以从快照中找到历史版本的备份，并从历史版本的备份中恢复。单击【Snapshots】查看历史快照。
   ![](https://main.qcloudimg.com/raw/6c37ee6a7450dbf8ad1a7198b43ec247.png)
5. 选择历史快照。
   ![](https://main.qcloudimg.com/raw/b1e02efe3b3e018a8cadd1a1203a6efa.png)
6. 选择要恢复的历史目录或文件，以及保存恢复目录或文件的位置，单击【Restore】开始恢复。 
7. 等待界面提示恢复完成，即可到刚才指定的目录中查看恢复的文件。

