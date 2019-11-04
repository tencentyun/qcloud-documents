## 操作场景
Joomla 是使用 PHP 语言及 MySQL 数据库开发的开源内容管理系统，您可通过 Joomla 建立个人网站或功能强大的在线应用。本文介绍通过在腾讯云云服务器（CVM）上通过镜像来搭建 Joomla 基础管理平台。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤
### 创建云服务器
>!此步骤针对全新购买云服务器。如果您已购买云服务器实例，可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933) 选择对应的操作系统。
>
1. 在实例的管理页面，单击【新建】。
2. 根据页面提示选择机型，并选择【镜像市场】>【从镜像市场选择】。如下图所示：
弹出“选择镜像”窗口。
![](https://main.qcloudimg.com/raw/bd6bbe11ae49f5a398612d495422086f.png)
3. 在“选择镜像”窗口的左侧搜索框中，输入 Joomla 并单击<img src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0px">。如下图所示：
>?本文使用镜像为 [LNMP环境（CentOS7.6 Nginx PHP7.2 内置Joomla）](https://market.cloud.tencent.com/products/16472?productId=16472&_ga=1.121836424.2093467297.1571788865)。
>
![](https://main.qcloudimg.com/raw/2ccf94a1fb9ab33816b260820b8d257f.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。

### 修改数据库密码
1. 在实例的管理页面，找到已创建的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/a87c24c75bdbcc568a1ab0f1fd62c357.png)、
2. 在浏览器中访问以下地址，进入 phpMyAdmin 管理平台。
```
http://云服务器实例的公网 IP/tools/phpMyAdmin
```
3. 输入数据库帐户名及密码，并单击【执行】。如下图所示：
帐户名为 `root`，默认密码为 `joomla@2019`。
![](https://main.qcloudimg.com/raw/5e28e56c05b2ee861478eec14aa5a1af.png)
4. 进入 phpMyAdmin 管理页面，单击【修改密码】。如下图所示：
![](https://main.qcloudimg.com/raw/4dbfb941a21eb8caff5380d8388af7c5.png)
5. <span id="step5"></span>在弹出的“修改密码”窗口中，选择自行设置或自动生成密码，并单击【执行】。如下图所示：
>?本文使用自动生成密码，请记录您的数据库密码。
>
![](https://main.qcloudimg.com/raw/1e0ef4e89766f8c796b254a4cf71a956.png)

### 安装配置 Joomla
1. 在浏览器中访问以下地址，即可进入 Joomla 安装页面。
```
http://云服务器实例的公网 IP
```
2. 根据页面上的提示信息进行网站配置，填写完成后单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/6fd98398cb1fab152c40ac32cdb118f4.png)
3. 在“数据库配置”页面根据以下提示，填写相关信息后单击【下一步】。如下图所示：
![](https://main.qcloudimg.com/raw/bce0baec553bda4db6442d83fd0d41b2.png)
 - **数据库类型**：选择 MySQL(PDO)。
 - **数据库主机名**：输入127.0.0.1。
 - **数据库用户名**：输入 root。
 - **数据库密码**：输入在 [步骤5](#step5) 中已设置的 root 帐户密码。
 - **数据库名称**：自定义，本文以 Joomla 为例。
 其余设置保持默认值。
4. 在“配置概览”页面确认配置，并单击【安装】。如下图所示：
![](https://main.qcloudimg.com/raw/c1e8761097117a838975458276a07b5e.png)
5. 安装成功后，单击【删除 “installation” 目录】。如下图所示：
![](https://main.qcloudimg.com/raw/c0c55419c83e2b11196bbb29f81f5bac.png)
Joomla 基础管理平台已搭建完成，请通过以下方式进行网站访问及管理：
 - 网站前台地址：`http://云服务器实例的公网 IP`
 - 网站后台管理地址：`http://云服务器实例的公网 IP/administrator`

## 相关操作
### Joomla 汉化
您可参考以下步骤对已安装的 Joomla 基础管理平台进行汉化。 
1. 将 Joomla 中文语言包下载至本地。
2. 访问网站后台管理地址，并使用管理员帐户登录。如下图所示：
![](https://main.qcloudimg.com/raw/b6a45856bfa04750c3457c7d7197c210.png)
3. 选择左侧导航栏中的【install Extensions】进入扩展安装页面。
4. 单击【Or browse for file】，在弹出页面中选择本地已下载的语言包。如下图所示：
![](https://main.qcloudimg.com/raw/63e61f8434e3aee0e7b54a07b438ae46.png)
上传成功后，界面如下图所示：
![](https://main.qcloudimg.com/raw/12b891d757104980fce61a01af2c9fa6.png)
5. 选择界面上方【Extensions】>【Languages(s)】>【installed】，进入语言安装界面。如下图所示：
![](https://main.qcloudimg.com/raw/3eaa1ce9899aa2f863d6e3ffc63c5e8a.png)
6. 单击<img src="https://main.qcloudimg.com/raw/7b76d0bf4a03cdc8faa0775a4bf76972.png" style="margin:-3px 0px">，将简体中文设置为默认使用语言。如下图所示：
![](https://main.qcloudimg.com/raw/8ed58b22a1a1746adba7aec5ed0926a1.png)
7. 单击页面右上角<img src="https://main.qcloudimg.com/raw/48da0f5df951306d1616ba6b3bea9705.png" style="margin:-3px 0px">，并选择【Logout】退出后台管理。
8. 再次访问后台管理地址，选择使用语言为【简体中文】并重新登录。如下图所示：
![](https://main.qcloudimg.com/raw/755698a043eec20b7ee015a7980e09ed.png)
成功登录后即可开始配置 Joomla 管理平台。如下图所示：
![](https://main.qcloudimg.com/raw/3d607051d7a143cf9b781af48eb4394a.png)

