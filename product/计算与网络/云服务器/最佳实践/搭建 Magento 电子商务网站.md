## 操作场景
Magento 是使用 PHP 语言开发的开源电子商务平台，是国际电子商务解决方案之一。本文介绍通过在腾讯云云服务器（CVM）上通过 Magento 镜像来搭建个人电子商务网站。

## 注意事项
- 如果您**未购买**云服务器，您可以在购买云服务器时，通过选择镜像市场中的 Magento 镜像直接搭建网站。详情可参考 [创建云服务器时使用 Magento 镜像](#create) 。
- 如果您**已购买**云服务器，但该云服务器的操作系统并不具备 Magento，您可以参考 [更换系统镜像](#change) 使用 Magento 镜像。

## 操作步骤
### 步骤一：使用 Magento 镜像
#### 创建云服务器时使用 Magento 镜像<span id="create"></span>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 根据页面提示选择机型，并在“镜像”中选择【镜像市场】>【从镜像市场选择】。如下图所示：
弹出“选择镜像”窗口。
![](https://main.qcloudimg.com/raw/079615fcf41610885b6462a478cab823.png)
3. 在“选择镜像”窗口的左侧搜索框中，输入 Magento 并单击<image src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0px"/>。如下图所示：
>?
>- 本文以下图所示的 Magento开源电子商务系统为例，您可根据实际需求进行选择。
>- 单击镜像名可查看镜像详情。
>
![](https://main.qcloudimg.com/raw/7adadb8a4f4f2d99a5803535b3e4dbbd.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。

#### 更换系统镜像<span id="change"></span>
>!
>- 此步骤通过重装云服务器操作系统来使用 Magento 镜像，请参考 [重装系统](https://cloud.tencent.com/document/product/213/4933) 了解注意事项。
>- 如果您的云服务器之前使用 Windows 操作系统并挂载了数据盘，请参考 [Windows 重装为 Linux 后读写原 NTFS 类型数据盘](https://cloud.tencent.com/document/product/213/3857) 进行数据盘格式更换，防止重要数据损坏。.
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，找到需使用 Magento 镜像的云服务器。
2. 选择右侧的【更多】>【重装系统】。如下图所示：
![](https://main.qcloudimg.com/raw/caf6b8c826f1ddd79148164ae70825b2.png)
3. 在弹出的“重装系统”窗口中，选择【服务市场】>【建站系统】，并搜索 Magento 镜像。如下图所示：
![](https://main.qcloudimg.com/raw/0e867d31f56b90392d8edba970525718.png)
4. 根据您的实际需求，选择 Magento 镜像，并可调整磁盘大小，确认配置信息后，单击【开始重装】。

### 步骤二：修改数据库密码
>!为提高数据库安全性，请执行此步骤修改默认密码。
>
1. 在实例的管理页面，找到已创建的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/a5eab449a37929844c7f3af268b76e0d.png)
2. 在浏览器中访问以下地址，进入 phpMyAdmin 管理平台。
```
http://云服务器实例的公网 IP/phpmyadmin
```
3. 输入数据库账户名及密码，并单击【执行】。如下图所示： 
帐户名为 `root`，默认密码为 `123456`。
![](https://main.qcloudimg.com/raw/30bc260727a56b8779236e8fdb502478.png)
4. 进入 phpMyAdmin 管理页面，单击【修改密码】。如下图所示：
![](https://main.qcloudimg.com/raw/c7ea866691b61167dcac1cf467a35896.png)
5. <span id="password"></span>在弹出的“修改密码”窗口中，选择自行设置或自动生成密码，并单击【执行】。如下图所示：
>?本文使用自动生成密码，请记录您的数据库密码。
>
![](https://main.qcloudimg.com/raw/287a33f4b12b74a4c12d655096addc09.png)

### 步骤三：安装 Magento 客户端
1. 在浏览器访问以下地址，进入 Magento 配置页面。
```
http://云服务器实例的公网 IP
```
2. 在 Magento 配置页面，单击【Agree and Setup Magento】。如下图所示：
![](https://main.qcloudimg.com/raw/f32243c018ed86b0dfafcdb2e1082311.png)
3. 单击【Start Readiness Check】，进行环境检测。如下图所示：
![](https://main.qcloudimg.com/raw/8e883ec4322f3f0d26fa181d62cebb82.png)
4. 环境检测通过后，单击【Next】进入下一步。如下图所示：
![](https://main.qcloudimg.com/raw/778703a93dc61a3450e77a5cf8e3909e.png)
5. 添加数据库信息，请输入从 [修改密码](#password) 步骤中获取的数据库密码，并单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/277d201ee1422c4db4e96ff6133c993f.png)
6. <span id="admin"></span>将 Magento 管理员登录地址修改为 `admin` ，并单击【Next】。如下图所示：
>?请记录您的商务网站地址及管理员登录地址。
>
![](https://main.qcloudimg.com/raw/70b58f8f5e756623ba6fe729f342d0bc.png)
7. 根据您的实际情况设置语言、时区等信息，并单击【Next】。本文设置如下图所示：
![](https://main.qcloudimg.com/raw/04680a23990f5e9602461ec88804a79a.png)
8. 根据您的实际情况设置管理员登录账号及密码，并单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/6829620bc690ed45e567950d8e21d822.png)
9. 单击【Install Now】进行安装。
10. 成功安装后请记录页面上的信息，并单击【Launch Magento Admin】。如下图所示：
![](https://main.qcloudimg.com/raw/cec0f027b3100ddcc31c73dfd4890b78.png)
11. 进入管理员登录页面，输入 [步骤8](#admin) 设置的管理员账号及密码，并单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/d196f04eec071c0ab27895698c75c88b.png)
12. 登录成功后，即可进入管理员页面配置个人商务网站。如下图所示：
![](https://main.qcloudimg.com/raw/ceb05283332f12e84358e3bd47ce8a25.png)


### 步骤四：验证配置
使用浏览器访问下列地址，查看 Magento 客户端是否安装成功。
```
http://云服务器实例的公网 IP
```
显示结果为 Magento 默认主页，则说明安装成功。如下图所示：
![](https://main.qcloudimg.com/raw/bc9c493afe48623eb0ea3a22bf02a5b4.png)

## 常见问题
如果您在使用云服务器的过程中遇到问题，可参考以下文档并结合实际情况分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。
- 云服务器硬盘问题，可参考 [系统盘和数据盘](https://cloud.tencent.com/document/product/213/17351)。





