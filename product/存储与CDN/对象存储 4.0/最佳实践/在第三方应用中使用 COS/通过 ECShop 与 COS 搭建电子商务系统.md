## 简介


[ECShop](https://www.ecshop.com/) 是一个基于 PHP + MYSQL 构建的开源电子商务平台。本文主要介绍如何使用插件实现远程附件功能，将 ECShop 的商品图、LOGO 图等文件存储在腾讯云 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上。


## 前提条件

1. 已有 COS 存储桶。如无，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 操作指引。
2. 已创建服务器。例如云服务器 CVM。相关指引可参见 [CVM 产品文档](https://cloud.tencent.com/document/product/213)。




## 实践步骤

### 安装 ECShop


您可以在 [ECShop 官方页面](https://www.ecshop.com/download) 下载 ECShop 的最新版并查看安装指南。您也可以通过宝塔面板安装。宝塔面板安装指引请参见 [宝塔官网](https://www.bt.cn/)。下面以宝塔安装 ECShop 为例。

#### 安装宝塔
1. 首先准备一台 CVM 机器，然后安全组的入站规则和出站规则按照如下配置：
 - 入站规则
![](https://qcloudimg.tencent-cloud.cn/raw/e90f6a65388de747676dd894090ce158.png)
 - 出站规则
![](https://qcloudimg.tencent-cloud.cn/raw/0fd12abd0a1a729d7dc78678a8c50b94.png)
2. 执行宝塔官网提供的 Centos 安装脚本：
```
yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh ed8484bec
```
在 CVM 机器上直接执行如下图所示：
![img](https://qcloudimg.tencent-cloud.cn/raw/672aed3217d3d1cf33cd880ed4977aba.png)
3. 执行中会出现如下信息，直接输入 y 回车即可。
![img](https://qcloudimg.tencent-cloud.cn/raw/164affb276edefaad6265e0438c197ad.png)
执行成功后，会生成网站账号（需记录保存），如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2a4a8cb983ba22d6148b3985343df773.png)

#### 通过宝塔安装 ECShop


1. 宝塔安装后，打开桌面上的浏览器，输入在 CVM 生成的宝塔外网链接：`http://43.xxx.xxx.132:16859/c2601bbd`（使用时请替换为自己的 IP）。
2. 单击添加站点，并配置相关参数，输入 CVM 的 IP，其他配置（根目录、FTP 账号、数据库账号等）保持默认。
![](https://qcloudimg.tencent-cloud.cn/raw/d2f1041e87750e292f7d0128f90fd5a7.png)
3. 站点创建完成后，进入站点。
4. 单击**文件**导航栏，在文件页面中单击**上传**，将已下载的 ECShop 安装包上传到宝塔面板的 IP 目录下。
![](https://qcloudimg.tencent-cloud.cn/raw/6272b4a75f041271e8e64a13a5319808.png)
5. 将安装包解压后，得到下面两个文件夹。
![](https://qcloudimg.tencent-cloud.cn/raw/8fe1eeb72310910945698d2a6802bc7f.png)
6. 然后通过浏览器访问链接`http://43.xxx.xxx.132/ecshop/ecshop/install/index.php`（使用时请替换为自己的站点 IP和 ECShop 解压后的文件目录路径）。
7. 根据页面提示，单击下一步，并填写数据库和其他配置，这里的数据库名称和密码一定要跟您宝塔面板的一致。
![](https://qcloudimg.tencent-cloud.cn/raw/089ee9f3a3b0817b43a150b00e1c147a.png)
8. 以上配置完成后，即可完成 ECShop 的安装。浏览器访问`http://43.xxx.xxx.132/ecshop/ecshop/admin`即可进入 ECShop 后台。




### 安装 COS 插件


1. 在宝塔43.xxx.xxx.132目录下单击**远程下载**，填入以下插件链接，然后得到该插件的压缩文件。
```
https://gitee.com/Tencent-Cloud-Plugins/tencentcloud-ecshop-plugin-cos/repository/archive/master.zip
```
2. 对压缩包进行解压后，得到下面的文件夹。
![](https://qcloudimg.tencent-cloud.cn/raw/f15d2eec77fbcba04bccd9228a5d4523.png)
3. 将 tencentcloud-ecshop-plugin-cos-master/tencentcloud_cos/ecshop 这路径下的所有文件合并到 ecshop 源码中对应文件夹中，单击覆盖即可。
4. 刷新 ECShop 的后台，即可在左侧导航栏中看到“腾讯云设置”配置项。
5. 在“腾讯云设置”配置项中单击**对象存储配置**，设置相关参数以便关联到 COS，配置信息如下：
<table>
   <tr>
      <th width="0%" >配置项</td>
      <th width="0%" >配置值</td>
   </tr>
	 
   <tr>
      <td>开启腾讯云存储</td>
      <td>选择是。</td>
   </tr>
   <tr>
      <td>开启自定义配置</td>
      <td>选择是。 </td>
   </tr>
	 
   <tr>
      <td>SecretId</td>
      <td>访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取。</td>
   </tr>
   <tr>
      <td>SecretKey</td>
      <td>访问密钥信息，可前往 <a href="https://console.cloud.tencent.com/capi">云 API 密钥</a> 中创建和获取。</td>
   </tr>
   <tr>
      <td>所属地域</td>
      <td>创建存储桶时所选择的地域。详情请参见 <a href="https://cloud.tencent.com/document/product/436/6224">地域和访问域名</a>。</td>
   </tr>
   <tr>
      <td>空间名称</td>
      <td>创建存储桶时自定义的名称，例如 examplebucket-1250000000。</td>
   </tr>
   <tr>
      <td>访问域名</td>
      <td>存储桶的访问域名，详情请参见 <a href="https://cloud.tencent.com/document/product/436/6224">地域和访问域名</a>。</td>
   </tr>
</table>
<img style="width:700px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/c97e216d2129e9ce07581aed408a0ae2.png" />
6. 完成以上设置后，单击**开始测试**，提示测试成功即完成与 COS 的连通。
![](https://qcloudimg.tencent-cloud.cn/raw/7279783bf9052aa7fb619c8fce24080a.png)




