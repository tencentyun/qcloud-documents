## 操作场景
Moodle 是一个开源的在线教育系统，也被称为在线学习系统（LMS）。Moodle 采用 PHP 语言和 MySQL 开发，您可使用 Moodle 为学习者建立开放式课程系统。本文档介绍在腾讯云云服务器（CVM）上通过镜像搭建 Moodle 在线学习系统。


## 注意事项
- 如果您**未购买**云服务器，您可以在购买云服务器时，通过选择镜像市场中的 Moodle 镜像直接搭建在线学习系统。详情可参考 [创建云服务器时搭建系统](#create)。
- 如果您**已购买**云服务器，但该云服务器的操作系统并未搭建环境，您可以参考 [更换系统镜像](#change) 完成 Moodle 在线学习系统的搭建。

## 操作步骤
### 搭建 Moodle 在线学习系统
 
### 创建云服务器时搭建系统<span id="create"></span>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的【新建】。
2. 据页面提示选择机型，并在“镜像”中选择【镜像市场】>【从镜像市场选择】。如下图所示：
 弹出“选择镜像”窗口。
 ![](https://main.qcloudimg.com/raw/bd6bbe11ae49f5a398612d495422086f.png)
3. 在“选择镜像”窗口的左侧搜索框中，输入 moodle 并单击<img src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0px;"/>。如下图所示：
>?单击镜像名可查看镜像详情，本文使用 [Moodle LMS在线学习系统](https://market.cloud.tencent.com/products/708?productId=708&_ga=1.158416825.2093467297.1571788865)。
>
![](https://main.qcloudimg.com/raw/e419e15c40090105770b4b1a75fd771a.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的创建。

#### 更换系统镜像<span id="change"></span>
>!
>- 此步骤通过重装云服务器操作系统来搭建 Moodle 在线学习系统，请参考 [重装系统](https://cloud.tencent.com/document/product/213/4933) 了解注意事项。
>- 如果您的云服务器之前使用 Windows 操作系统并挂载了数据盘，请参考 [Windows 重装为 Linux 后读写原 NTFS 类型数据盘](https://cloud.tencent.com/document/product/213/3857) 进行数据盘格式更换，防止重要数据损坏。
>
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，找到需搭建 Moodle 在线学习系统的云服务器。
2. 选择右侧的【更多】>【重装系统】。如下图所示：
![](https://main.qcloudimg.com/raw/110bf0bd6ec70bc4e22e8be3510a451d.png)
3. 在弹出的“重装系统”窗口中，选择【服务市场】>【应用镜像】，并选择 Moodle LMS在线学习系统镜像。如下图所示：
![](https://main.qcloudimg.com/raw/6f154e82ba7968eda22833326f0486a7.png)
4. 根据您的实际需求，选择 LNMP 环境的镜像，并可调整磁盘大小，确认配置信息后，单击【开始重装】。

### 修改数据库密码
1. 在实例的管理页面，找到已创建的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/392ce24430ac82c418ebad7a28874645.png)
2. 在浏览器中访问以下地址，进入 phpMyAdmin 管理平台。
```
http://云服务器实例的公网 IP/phpmyadmin
```
3. 输入数据库账户名及密码，并单击【执行】。如下图所示：
帐户名为 `root`，默认密码为 `123456`。
![](https://main.qcloudimg.com/raw/91ecc1ddfabf11ffe54ba1bc515ec6dc.png)
4. 进入 phpMyAdmin 管理页面，单击【修改密码】。如下图所示：
![](https://main.qcloudimg.com/raw/9fbee5fc98af3e0e021c43195071d1de.png)
5. <span id="sercet"></span>在弹出的“修改密码”窗口中，选择自行设置或自动生成密码，并单击【执行】。如下图所示：
>?本文使用自动生成密码，请记录您的数据库帐号及密码。
>
![](https://main.qcloudimg.com/raw/c1bcf4b3698cc5da369c57317a524479.png)


### 安装 Moodle
1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/392ce24430ac82c418ebad7a28874645.png)
2. 在浏览器中访问该云服务器公网 IP，进入 Moodle 安装页面。
3. 在“语言”选择简体中文（zh_cn），并单击【向后】。如下图所示：
![](https://main.qcloudimg.com/raw/3bc2300625e68caecf2842260a2ca9a4.png)
4. 在“确认路径”页面，保持所有默认设置不变，并单击【向后】。如下图所示：
![](https://main.qcloudimg.com/raw/d9be77619d0deb6e0f1e5857c9760215.png)
5. 在“选择数据库驱动”页面，保持所有默认设置不变。并单击【向后】。如下图所示：
![](https://main.qcloudimg.com/raw/9a0f1b84e5b2db1542439d2595b1d8f2.png)
6. 在“数据库设置”页面根据以下提示填写相关信息，并单击【向后】。如下图所示：
![](https://main.qcloudimg.com/raw/ff263cf3461fb374e75250e990fff820.png)
 - **数据库用户名**：请输入 `root`。
 - **数据库密码**：请输出在步骤 [修改密码](#sercet) 中设置的数据库密码。
 - **数据库服务端口**：请输入3306。
7. 阅读并理解版权说明，并单击【继续】。
8. 在检查安装组件页面看到提示确认部署完毕后，单击【继续】。如下图所示：
![](https://main.qcloudimg.com/raw/1667923a5b420579ed9b5627ce8218e5.png)
9. 等待组件安装完成后，单击页面底部的【继续】。如下图所示：
![](https://main.qcloudimg.com/raw/40acbb9864c44a9391c0d2d7153562bb.png)
10. 按照页面提示填写系统管理员信息，并单击【更新个人资料】。如下图所示：
![](https://main.qcloudimg.com/raw/0a2ae5ed11e4bf6d541bdc3bfe26bef7.png)
11. 根据页面提示进行网站名称及其他相关设置，并单击【保存更改】。
12. 安装成功后，自动登录后台管理页面。如下图所示：
![](https://main.qcloudimg.com/raw/9756654e9f9d2b76857138b4a5aef00e.png)
您已成功搭建 Moodle 在线学习系统，可根据您的实际需求进行网站管理及个性化设置。



