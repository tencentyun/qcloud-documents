## 前言
文件备份是文件管理中始终无法绕过的一环，文件备份工作做得是否到位很大程度上地影响了数据的安全性。

无论是个人文件（文档、照片、视频等）还是项目数据（项目代码、数据库文件、配置文件等），都需要一个可靠的备份过程来保证其数据安全。

对于其中特别重要的文件，我们还应该遵守数据备份中的3-2-1黄金法则（即数据应该要有3份拷贝，保存在2种不同的介质上，其中至少有1份存放在异地），以保证数据的可靠性。  

随着云存储服务的飞速发展，其所能提供的容量越来越大、传输速率越来越高、价格也越来越便宜。作为云存储服务的代表，COS 除了能带来上述的优势，还能为用户提供数据处理、内容审核、应用集成等高级特性，无论是面向个人或是企业用户，其都能提供一套完整的云存储解决方案。  

本文从零开始，一步一步地指引您使用 GoodSync 将您的重要文件备份到 COS，完成3-2-1黄金法则中的一环（1份拷贝、1种介质、1份存放于异地的拷贝），享受由云存储服务飞速发展所带来的成果。  

## 软件介绍
GoodSync 是一个备份和文件同步程序。它用于在两个目录之间同步文件，无论是在一台计算机上，还是在计算机与另一个存储设备（例如，另一台计算机、可移动磁盘、闪存驱动器或智能手机）之间，或者在计算机与远程计算机或服务器之间。GoodSync 允许在多个计算设备上维护相同版本的文件。

换言之，当两台设备同步时，用户可以确保文件的最新版本在两台设备上都可用，而不管最后修改的位置如何。  

## 操作步骤 
### 步骤1：创建存储桶
1. 进入 [对象存储控制台](https://console.cloud.tencent.com/cos5)，单击侧边栏的**存储桶列表**，再单击页面中的**创建存储桶**，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/d4ffa6ff099c6303205528680ca60aa6.png)
2. 在**所属地域**中选择合适的存储地域（建议选择距离您较近的地域以提高传输效率），输入一个合适的名称，本文填写了**goodsync-backup**，**访问权限**选择**私有读写**，然后单击**下一步**，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/b4d3a5ce7a9d697c7d0e82b124062a74.png)
3. 在下一步界面中根据自身需求选择存储桶所需的高级特性，这里为了简便，暂不开启任何特性，直接单击**下一步**，如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/f561db3bb9da146b5d644083256989d1.png)
4. 在**确认配置**页面审阅存储桶配置信息，确认无误后单击**创建**即可完成存储桶的创建，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/5ecf186545003338f5e301e764d9507c.png)

### 步骤2：创建专用子用户
为了存储桶的数据安全，我们应该遵循 [最小权限原则](https://baike.baidu.com/item/%E6%9C%80%E5%B0%8F%E6%9D%83%E9%99%90%E5%8E%9F%E5%88%99)，使用子用户进行访问，而不是直接使用根用户进行访问。  

1. 单击 [控制台](https://console.cloud.tencent.com/cos5) 右上角的头像，在菜单中单击 **[访问管理](https://cloud.tencent.com/product/cam?from=10680)**，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/09cc1ca7d0eb39519a985f94506b9bf6.png)
2. 单击侧边栏的**用户**>**用户列表**，单击页面中的**新建用户**，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7d0c876ec389be783bd72debffbfacf0.png)
3. 页面中的**自定义创建**，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/1a2cc6e9789256707fcb21b4f669957f.png)
4. 用户类型选择**可访问资源并接收消息**，并单击**下一步**，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/3de21b83968466d405e95d3609758f1f.png)
5. 输入子用户的用户名，本文输入了**goodsync-backup**，您可自由地选择名称，然后勾选**编程访问**并单击**下一步**，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/d2993fc0cb72257d1aff911ec40591ce.png)
6. 此时可根据需要配置子用户的权限策略，本文不涉及子用户的权限策略配置，因此无需勾选任何一个策略，直接单击**下一步**即可，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/1bf3ff0f7730332df9d2d1410795ad7e.png)
7. 根据需求设置用户标签，本文不设置用户标签，直接单击**下一步**即可，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/4f00bf119a95da279a451596891c01d9.png)
8. 审阅用户信息，确认无误后单击**完成**即可创建子用户，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/1e26193791f824bba210a59dc451ca18.png)
9. 接下来会显示该子用户的 **SecretId** 和 **SecretKey**，我们先将它们复制出来，后续的步骤会用到它们，如下图所示。 
![](https://qcloudimg.tencent-cloud.cn/raw/729cd67a0fe04624dacb92ffcfd6e0b0.png)

### 步骤3： 为子用户添加存储桶的访问权限
1. 目前我们创建的子用户是没有任何访问权限的，我们需要为子用户添加存储桶的访问权限。  
回到 [对象存储控制台](https://console.cloud.tencent.com/cos)，单击侧边栏的**存储桶列表**，在页面的列表中单击之前创建的存储桶。  
2. 单击左侧的**权限管理**-**存储桶访问权限**，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/cba659269d325ad26794691fd9a848d7.png)
3. 单击**添加用户**，**用户类型**选择**子账号**，**账号ID**填写之前创建的子用户，**权限**勾选**完全控制**，最后单击**保存**即可。如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/d5229363ae463a2f3972f735f687b8ca.png)

### 步骤4：GoodSync 配置
1. 本文以 macOS 为例，其他操作系统的用户可参照本文进行设置。假设我们需要备份的目录为 /Users/Shared/my-data，其目录结构如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/6b92778a13a370a53c44d72182ed7576.png)
2. 打开 GoodSync，单击左上角的**新建任务**，输入任务名称，本文输入**个人数据备份**，任务类型选择**备份**，然后单击**确定**。如下图所示。 
![](https://qcloudimg.tencent-cloud.cn/raw/85df1781f7f41d3d085320766229db78.png)
3. 单击软件上方偏左的文件夹图标，将鼠标移动到下方列表中的 **My Mac**上，单击选择需同步的目录，如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/720a877d3b5b5b51d837afd9760bc0d9.png)
4. 单击软件上方偏右的文件夹图标，将鼠标移动到下方列表中的 **Amazon S3**上，单击其右侧的添加，如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/59296360768a0043f9d31fbbff88cdd6.png)
5. 在 **Server Address** 中输入 cos.<存储桶所属地域>.myqcloud.com  

>?存储桶所属地域可在 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224?from=10680) 中获取。

- 本文存储桶所属地域为广州，因此输入 **cos.ap-guangzhou.myqcloud.com**。

- 在 **Initial path** 中输入/<存储桶名称>，本文输入**/goodsync-backup-**。（注意前面的**"/"**）  

- 在 **AWS Access Key ID** 中输入之前保存的子用户的 SecretId。

- 在 **AWS Secret Access Key** 中输入之前保存的子用户的 SecretKey。

上述配置如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/6573aef43eed858afdd1f177c4aadd5e.png)
单击 **Test** 即可测试存储桶连通性，此时软件提示连接成功，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/82ad9011595debbbfd27daab6f3ee6c6.png)
最后单击**保存**即可，在右侧列表中选择刚刚创建的存储桶，并单击左上角的**应用**。


### 步骤5：备份文件
1. 配置好 GoodSync 后，便可以开始备份文件了，单击左上角的**分析**，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/24c1681c496a3ccbbefeecadbaaf89e5.png)
2. 分析过程结束后，单击**同步**即可开始备份文件，如下图所示。  
![](https://qcloudimg.tencent-cloud.cn/raw/41fab7a7111cebb67bf266e3122e76ce.png)
3. 由于数据量不大，同步过程很快就结束了，此时回到存储桶文件列表页面，我们可以看到数据已如预期完整的备份到了存储桶中，如下图所示。其中_gsdata_目录保存了 GoodSync 的任务数据，忽略即可。  
![](https://qcloudimg.tencent-cloud.cn/raw/8893f5715dd157f6ec62ef5c04c336b1.png)
