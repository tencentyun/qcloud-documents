本文将指导您使用腾讯云提供的数据迁移产品 DTS 将阿里云数据库（RDS）的数据迁移到腾讯云的 TencentDB 中。

## 环境要求
阿里云云服务器 MySQL 5.6 或更低版本。
腾讯云 TencentDB MySQL 5.6实例。
>数据传输过程中，腾讯云数据库的数据复制方式必须为异步复制，如需修改数据复制方式，需要在数据传输完成后升级即可。

## 操作步骤

### 获取源数据库基本信息和 AccessKey 
 1. 登录[ RDS 管理控制台][1]，选择目标实例。
 2. 在目标实例的基础信息页即可获取我们所需的信息，具体如图所示：
![](https://main.qcloudimg.com/raw/e55af45a5c36a99097418808cc542389.png)
>**注意：**
>阿里云提供的外网地址需要将其转化成 IP 格式。此处列举一个[ IP/服务器地址查询 ][2]的网址。
 3. 您将鼠标悬停于右上方头像处，在出现的下拉菜单中选择【 accesskeys 】。进入页面后即可获取所需的 Accesskey。
	![](https://main.qcloudimg.com/raw/2d67bd05558d5762c322d0c33d344332.png)
	
### 创建腾讯云TencentDB的DTS任务
1. 登录控制台，进入数据迁移页面，单击【新建任务】
![](https://mc.qcloudimg.com/static/img/2ad6200dc53556f2c03f45e7a1af8320/image.png)
2. 跳转页面后，填写任务设置、源库设置和目标库设置。信息详情：

![](https://main.qcloudimg.com/raw/27cb0363ec0324605161a4de595c8002.png)
#### 任务设置
* 任务名称： 为任务指定名称
* 定时执行：可为您的迁移任务指定开始时间
![](https://mc.qcloudimg.com/static/img/6d45bf22f31923704b6055f3f94f1781/image.png)
##### 源库信息
根据需要选择接入类型，依次填写对应的源库连接信息。
![](https://main.qcloudimg.com/raw/b099d7a519f80fcdb450e8476a17d314.png)
>**注意：**
>您需要在阿里云开通 TencentDB 对外映射出去的 IP 的白名单。否则在测试连通性时将不通过。
>例如：
>1. 有公网 IP 的 MySQL ”腾讯云的映射，您需要将相对应的地区外网 IP 添加到阿里云的白名单中。
>2. DTS配置时源库类型为“专线”或者“VPN” 会在任务生成后出现对外映射的IP，需将此IP添加到阿里云白名单中。

##### 目标库信息
目标实例类型选择 TencentDB 实例，填写对应的目标库链接信息。
![](https://main.qcloudimg.com/raw/28b1998fd0b7e512be01c281490703bb.png)
### 选择所要迁移的数据库
选择要迁移的数据库,创建并检查迁移任务信息。
![](https://main.qcloudimg.com/raw/ed8274a0b47d81ecf1466adea1fac10c.png)
#### 数据一致性检测
选择数据检测类型(可选择全部检测或不检测) 
![](https://main.qcloudimg.com/raw/efa134922b1097f832f0c1e41fafaef3.png)
>**注意：**
>选择部分检测选项时，需填写检测比例

#### 校验迁移任务信息
 在创建完迁移任务后，您需要对迁移任务信息进行校验，单击【下一步：校验任务】进行校验，只有所有校验项通过后才能启动迁移任务，单击【启动】即可。
![](https://main.qcloudimg.com/raw/f0d5e8a304edd34bebe4d21d9ff4746d.png)
任务校验存在3种状态：

 - 通过：表示校验完全通过
 - 警告：表示校验不通过，迁移过程中或迁移后可能影响数据库正常运行但不影响迁移任务的执行。
 - 失败：表示校验不通过，无法进行迁移。如果校验失败，请根据出错的校验项，检查并修改迁移任务信息，然后重试校验。

### 启动迁移
在校验通过后，您可以单击【启动迁移】立即开始迁移数据。需要注意的是，如果您设定了迁移任务的定时时间，则迁移任务会在设定的时间开始排队并执行，如果没有设置定时任务，则迁移任务会立即执行。
迁移启动后，您可以在迁移任务下看到对应的迁移进度信息。在鼠标指向步骤后的感叹号提示符时，可显示迁移所需流程和当前所处阶段。
 
> **注意：**
> 由于系统设计限制，一次性提交或排队多个迁移任务将按排队时间串行执行。

### 撤销迁移
在迁移过程中，如果您需要撤销迁移，可以单击【撤销】按钮。
![](https://main.qcloudimg.com/raw/d57e495a06627c9d10274c3e3ea9beba.png)

### 完成迁移
当迁移进度达到 100% 时，可单击右侧【完成】按钮，完成迁移任务。
![](https://main.qcloudimg.com/raw/30dbf7018d72cee1daef076323dd5377.png)

>**注意：**
> 当迁移处于【未结束】状态时，迁移任务将一直进行，数据库数据同步。














[1]:    https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Frdsnew.console.aliyun.com%2F%3Fspm%3Da2c4g.11186623.2.5.cdjgiR
[2]:   http://ip.chinaz.com
[3]:   https://console.cloud.tencent.com/dtsnew
