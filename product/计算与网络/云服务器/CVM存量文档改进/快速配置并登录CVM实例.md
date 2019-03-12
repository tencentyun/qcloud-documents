
如果您是首次购买和使用云服务器CVM的个人用户，腾讯云推荐您按照本文介绍的流程快速配置、购买和连接CVM实例。

![](https://main.qcloudimg.com/raw/bcdbc0a8d6360f7846c40e90a5b1bbdb.png)


## 1. 注册账号与选型

### 注册腾讯云账号

新用户需在腾讯云官网进行 [注册](https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F)。注册指引可参考 [如何注册腾讯云](https://cloud.tencent.com/doc/product/378/9603) 。

### 确定云服务器所在地域及可用区

地域选择原则：

- 靠近用户原则。
  请根据您的用户所在地理位置选择云服务器地域。云服务器越靠近访问客户，越能获得较小的访问时延和较高的访问速度。

- 内网通信同地域原则。

  - 相同地域下的云服务器可以通过内网相互通信（内网通信，免费）。

  - 不同地域之间的云服务器不能通过内网互相通信（通信需经过公网，收费）。

    需要多个云服务器**内网通信的用户须选择相同云服务器地域**。

### 确定云服务器配置方案

对于个人用户，腾讯云推荐您使用**入门配置**。

- **入门配置**：适用于起步阶段的个人网站。例如个人博客等小型网站。

或者根据需求您可以选择：

- **基础配置**：适合有一定访问量的网站或应用。例如较大型企业官网、小型电商网站。
- **普及配置**：适合常使用云计算等一定计算量的需求。例如门户网站、SaaS 软件、小型 App 。
- **专业配置**：适用于并发要求较高的应用及适合对云服务器网络及计算性能有一定要求的应用场景。例如大型门户、电商网站、游戏 App 。

若推荐的配置不能满足您的需求，您可以在[更多机型](https://buy.cloud.tencent.com/cvm?tabIndex=1)中根据实际需要比较各配置方案。当然您也可以在购买云服务器之后，根据您的需求随时进行 [配置升级](https://cloud.tencent.com/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#1.-%E9%85%8D%E7%BD%AE%E5%8D%87%E7%BA%A7) 或  [配置降级](https://cloud.tencent.com/doc/product/213/%E8%B0%83%E6%95%B4CVM%E5%AE%9E%E4%BE%8B%E9%85%8D%E7%BD%AE#2.-%E9%85%8D%E7%BD%AE%E9%99%8D%E7%BA%A7) 。

### 确定付费方式

腾讯云提供**包年包月**和**按量付费**两种付费模式。具体详情可参见 [计费模式说明](https://cloud.tencent.com/doc/product/213/2180) 。
若您选择按量付费，则需先完成 [实名认证](https://console.cloud.tencent.com/developer/infomation) 。



## 2. 快速配置及购买CVM实例

腾讯云提供**快速配置**和**自定义配置**两种方式。本部分以快速配置为例说明，若快速配置不能满足您的需求，您可参考 [自定义配置 Linux 云服务器](https://cloud.tencent.com/doc/product/213/10517) 文档进行配置。

![](https://main.qcloudimg.com/raw/1070f6c81fa7ae94e70dd6df9387ad9c.png)

完成云服务器的购买和创建后，云服务器的实例名称、公网 IP 地址、内网 IP 地址、登录名、初始登录密码等信息都将以 [站内信](https://console.cloud.tencent.com/message) 的方式发送到账户上。
![](https://main.qcloudimg.com/raw/3e9630ea483d4154d58187091d51cecf.png)



## 3. 登录及连接CVM实例

配置及购买CVM实例后，您购买的实例会显示在控制台的实例列表中，选择您需要登录的实例，单击右侧【登录】。

![](https://main.qcloudimg.com/raw/876fcf96c4d24635906bd311f223a8a2.png)

根据您实例的类型，可以参考以下连接中的方式远程登录CVM实例。

- [连接及登录Linux实例](https://cloud.tencent.com/document/product/213/5436)。
- [连接及登录Windows实例](https://cloud.tencent.com/document/product/213/5435)。



## 4. 格式化与数据盘分区

### 前提条件
- 此步骤针对已购买数据盘的用户，需要格式化数据盘。**未购买数据盘的用户可以跳过此步骤。**
- 登录并连接了CVM实例。

### Linux系统格式化及数据盘分区

#### 分区数据盘

 1. 登录Linux云服务器。
	>! 仅支持对数据盘进行分区，不支持对系统盘进行分区。若您强行对系统盘分区可能导致系统崩溃等严重问题，针对此种情况腾讯云不承担赔偿责任。
 2. 输入命令`fdisk -l`查看您的数据盘信息。
	本示例中，有一个54GB的数据盘`(/vdb)`需要挂载。
	>! `fdisk -l` 与 `df -h` 都为查看数据盘信息命令，但在没有分区和格式化数据盘之前，使用 `df -h` 命令无法看到数据盘。

	![](//mc.qcloudimg.com/static/img/f26b5a092e1521556410afdc75a95474/image.png)
 3. 对数据盘进行分区。按照界面的提示，依次操作：
 	1. 输入`fdisk /dev/vdb`（对数据盘进行分区），回车。
 	2. 输入`n`（新建分区），回车。
 	3. 输入`p`（新建扩展分区），回车。
 	4. 输入`1`（使用第1个主分区），回车。
 	5. 输入回车（使用默认配置）。
 	6. 再次输入回车（使用默认配置）。
 	7. 输入`wq`（保存分区表），回车开始分区。

 这里以创建1个分区为例，开发者也可以根据自己的需求创建多个分区。
	![](//mc.qcloudimg.com/static/img/8a9c8ff4db5a7e4622bf2968d0309129/image.png)
 4. 使用`fdisk -l`命令，即可查看到，新的分区 vdb1 已经创建完成。
	![](//mc.qcloudimg.com/static/img/304ccd9491f2a25b8d3b33b5213faa0e/image.png)

#### 格式化数据盘

  1. 新分区格式化
  分区后需要对分好的区进行格式化，您可自行决定文件系统的格式，如 ext2、ext3 等。本例以 ext3 为例。
  使用下面的命令对新分区进行格式化： 
  ```
  mkfs.ext3 /dev/vdb1
  ```
  ![](//mc.qcloudimg.com/static/img/fce59c4aba93c688c429fe4760452264/image.png)
  2. 挂载分区
  使用以下命令创建 mydata 目录并将分区挂载在该目录下：
  ```
  mkdir /mydata
  mount /dev/vdb1 /mydata
  ```
  使用命令查看挂载：
  ```
  df -h
  ```
  出现如图框选的 vdb1 信息则说明挂载成功，即可以查看到数据盘了。
  ![](//mc.qcloudimg.com/static/img/d6bc35b30b823c567812affd032bfedf/image.png)
  3. 设置启动自动挂载
  如果希望云服务器在重启或开机时能自动挂载数据盘，必须将分区信息添加到 `/etc/fstab `中。
  使用以下命令添加分区信息：
  ```
  echo '/dev/vdb1 /mydata ext3 defaults 0 0' >> /etc/fstab
  ```
  使用以下命令查看：
  ```
  cat /etc/fstab
  ```
  出现如图最下方框选的 vdb1 信息则说明添加分区信息成功。
  ![](//mc.qcloudimg.com/static/img/39025e909cd849d5a34378a7d0078d13/image.png)
  
  ### Windows系统格式化及数据盘分区
  
  #### 格式化数据盘

 1. 登录Windows云服务器。

 2. 单击【开始】-【服务器管理器】-【工具】-【计算机管理】-【存储】-【磁盘管理】。

 3. 在磁盘1上右键单击，选择【联机】：
 ![](//mc.qcloudimg.com/static/img/1217193557509925a622dcdb81aa2e35/image.png)

 4. 右键单击，选择【初始化磁盘】：
 ![](//mc.qcloudimg.com/static/img/94ab92867d77ea69bc803a0b20f2b941/image.png)

 5. 根据分区方式的不同，选择【GPT】或【MBR】，单击【确定】按钮：
 > **注意：**
 > 磁盘大于 2TB 时仅支持 GPT 分区形式。若您不确定磁盘后续扩容是否会超过该值，则建议您选择 GPT 分区；若您确定磁盘大小不会超过该值，则建议您选择 MBR 分区以获得更好的兼容性。
 ![](//mc.qcloudimg.com/static/img/1f7b0f72767193cfa662e188c86cf31b/image.png)

### 磁盘分区（可选）

 1. 在未分配的空间处右击，选择【新建简单卷】：
	![](//mc.qcloudimg.com/static/img/a6ca720af2082d7a470ece17a8e13f5d/image.png)

 2. 在弹出的“新建简单卷向导”窗口中，单击【下一步】：
	![](//mc.qcloudimg.com/static/img/10fdcd70b510a57919c6a40cf43452a7/image.png)

 3. 输入分区所需磁盘大小，单击【下一步】：
	![](//mc.qcloudimg.com/static/img/05c8d1425a0208597b1d2c75a9c811b6/image.png)

 4. 输入驱动器号，单击【下一步】：
	![](//mc.qcloudimg.com/static/img/737ed569049ad617715efb06fe44e7b2/image.png)

 5. 选择文件系统，格式化分区，单击【下一步】：
	![](//mc.qcloudimg.com/static/img/896cb3f2705fb9fcd04c236b8fb9ec59/image.png)

 6. 完成新建简单卷，单击【完成】：
	![](//mc.qcloudimg.com/static/img/1e257b9c76d80f30b34f612496b8007b/image.png)

 7. 在【开始】中打开【这台电脑】，查看新分区：
	![](//mc.qcloudimg.com/static/img/1cbb4ad1c3c01852a00a1415526a3e12/image.png)


