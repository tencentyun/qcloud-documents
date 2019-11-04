## 操作场景
Magento 是使用 PHP 语言开发的开源电子商务平台，是国际电子商务解决方案之一。本文介绍通过在腾讯云云服务器（CVM）上通过 Magento 镜像来搭建个人电子商务网站。

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
3. 在“选择镜像”窗口的左侧搜索框中，输入 Magento 并单击<image src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0px"/>。如下图所示：
>?单击镜像名可查看镜像详情。
>
![](https://main.qcloudimg.com/raw/7adadb8a4f4f2d99a5803535b3e4dbbd.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。

### 修改数据库密码
1. 在实例的管理页面，找到已创建的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/aeff0a3a2401527d488fb582cb121e2b.png)
2. 在浏览器中访问以下地址，进入 phpMyAdmin 管理平台。
```
http://云服务器实例的公网 IP/phpmyadmin
```
3. 输入数据库账户名及密码，并单击【执行】。如下图所示： 
账户名为 `root`，默认密码为 `123456`。
![](https://main.qcloudimg.com/raw/09d8594288adefc1514f8bc906473b20.png)
4. 进入 phpMyAdmin 管理页面，单击【修改密码】。如下图所示：
![](https://main.qcloudimg.com/raw/9fbee5fc98af3e0e021c43195071d1de.png)
5. <span id="password"></span>在弹出的“修改密码”窗口中，选择自行设置或自动生成密码，并单击【执行】。如下图所示：
>?本文使用自动生成密码，请记录您的数据库密码。
>
![](https://main.qcloudimg.com/raw/72a31bdc7b9ec873f21921cd5bd6232c.png)

### 安装 Magento 客户端
1. 在浏览器访问以下地址，进入 Magento 配置页面。
```
http://云服务器实例的公网 IP
```
2. 在 Magento 配置页面，单击【Agree and Setup Magento】。如下图所示：
![](https://main.qcloudimg.com/raw/c809d222f149ee26dcbb816ce6f61afe.png)
3. 单击【Start Readiness Check】，进行环境检测。如下图所示：
![](https://main.qcloudimg.com/raw/b3d8041e70e3e2599f2ed8fa20f553c9.png)
4. 环境检测通过后，单击【Next】进入下一步。如下图所示：
![](https://main.qcloudimg.com/raw/f54c130dbb2ea32a8aa2ff1526188ea0.png)
5. 添加数据库信息，请输入从 [修改密码](#password) 步骤中获取的数据库密码，并单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/82794a1e1495da4d8ce48e1805e4bb5d.png)
6. <span id="admin"></span>将 Magento 管理员登录地址修改为 `admin` ，并单击【Next】。如下图所示：
>?请记录您的商务网站地址及管理员登录地址。
>
![](https://main.qcloudimg.com/raw/b7b0c3e65c324f58c65e9d3b735b8275.png)
7. 根据您的实际情况设置语言、时区等信息，并单击【Next】。本文设置如下图所示：
![](https://main.qcloudimg.com/raw/a65892572c33952981643a9a8fb8b90e.png)
8. 根据您的实际情况设置管理员登录账号及密码，并单击【Next】。如下图所示：
![](https://main.qcloudimg.com/raw/5168fcdacaac4b3f2162f68fcb34c328.png)
9. 单击【Install Now】进行安装。
10. 成功安装后请记录页面上的信息，并单击【Launch Magento Admin】。如下图所示：
![](https://main.qcloudimg.com/raw/6c74ce4e8f31a388c53fd9931499678e.png)
11. 进入管理员登录页面，输入 [步骤6](#admin) 设置的管理员账号及密码，并单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/43b1ccc91aa2029d5e4b6a1a8f4b4f82.png)
12. 登录成功后，即可进入管理员页面配置个人商务网站。如下图所示：
![](https://main.qcloudimg.com/raw/70c7c47306de2cc796b8593493ab35af.png)


### 验证配置
使用浏览器访问下列地址，查看 Magento 客户端是否安装成功。
```
http://云服务器实例的公网 IP
```
显示结果为 Magento 默认主页，则说明安装成功。如下图所示：
![](https://main.qcloudimg.com/raw/e3e69a9113e21119da267b808415acf5.png)





