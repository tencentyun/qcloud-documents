

## 简介


[ECShop](https://www.ecshop.com/) 是一个基于 PHP + MYSQL 构建的开源电商平台。本文主要介绍如何使用插件实现远程附件功能，将 ECShop 电商平台上的商品图、商品品牌 LOGO 等资源附件存储在腾讯云 [对象存储（Cloud Object Storage，COS）](https://cloud.tencent.com/product/cos) 上。


## 前提条件

1. 已有 COS 存储桶。如无，可参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 操作指引。
2. 已创建服务器。例如云服务器 CVM。相关指引可参见 [CVM 产品文档](https://cloud.tencent.com/document/product/213)。


## 实践步骤


### 下载并安装 ECShop

您可以在 [ECShop 官方页面](https://www.ecshop.com/)，找到源码下载入口，选择 ECShop 商城源码进行下载即可。

下载 ECShop 商城源码后，您可在 ECShop 平台的帮助中心查看 ECShop 官方安装指南并进行安装，或者通过宝塔面板进行安装。宝塔面板安装指引请参见 [宝塔官网](https://www.bt.cn/)。下面以宝塔安装 ECShop V4.1 版本为例。


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
   ![img](https://qcloudimg.tencent-cloud.cn/raw/6b12cfe7b0b28497a272ea6027cf40b3.png)



#### 通过宝塔安装 ECShop



1. 宝塔安装完成后，打开桌面上的浏览器，输入在 CVM 生成的宝塔外网链接：`http://43.xxx.xxx.132:16859/c2601bbd`（使用时请替换为自己的 IP），然后通过生成的宝塔账号密码进行登录。
2. 登录宝塔后，按照弹窗提示，选择安装以下依赖环境：

 - Apache 2.4
 - MySQL 5.7
 - PHP 7.4
   ![](https://qcloudimg.tencent-cloud.cn/raw/4fd0e9941b8a799f0b199e6a6bcfa554.png)

3. 单击添加站点，并配置相关参数，输入 CVM 的 IP，其他配置（根目录、FTP 账号、数据库账号等）保持默认。
   ![](https://qcloudimg.tencent-cloud.cn/raw/d2f1041e87750e292f7d0128f90fd5a7.png)
4. 站点创建完成后，进入站点。
5. 单击**文件**导航栏，进入网站根目录，例如 `/www/wwwroot/43.xxx.xxx.132`（使用时请替换为自己的站点 IP），将 ECShop 商城源码解压后，将 source 目录下的 ecshop 目录拷贝到网站根目录下。
6. 通过浏览器访问链接 `http://43.xxx.xxx.132/ecshop/install/index.php`（使用时请替换为自己的站点 IP），此时将进入 ECShop 安装流程。
7. 根据页面提示，输入在安装宝塔面板时所生成的用户账号和密码：
   ![](https://qcloudimg.tencent-cloud.cn/raw/157b2a1854cb1f77af23ad69c9ed1f5d.png)

>?
>数据库账号可在宝塔界面中获取。
>![](https://qcloudimg.tencent-cloud.cn/raw/0b93553c5219c6945a266bce16c4b3ff.png)

8. 输入无误后，单击立即安装，稍等片刻即可完成 ECShop 系统的安装。
9. 登录 ECShop 系统管理后台 `http://43.xxx.xxx.132/ecshop/admin`（使用时请替换为自己的站点 IP），并输入安装 ECShop 时所输入的管理员账号和密码，即可登录 ECShop 管理后台。




### 安装 COS 插件

1. 进入宝塔面板，在宝塔 43.xxx.xxx.132 目录下单击**远程下载**，填入以下插件链接，然后得到该插件的压缩文件。

```plaintext
https://github.com/Tencent-Cloud-Plugins/tencentcloud-ecshop-plugin-cos/archive/refs/heads/master.zip
```

2. 对压缩包进行解压后，将 tencentcloud_cos/ecshop 目录下的所有文件复制粘贴到网站根目录下的 ecshop 目录中，如下图所示：
   ![](https://qcloudimg.tencent-cloud.cn/raw/5456b15e1481388d922ed4da41022285.png)

>!该 ecshop 目录是 ecshop 安装包目录，请谨慎操作。



### 配置 COS 插件

1. 进入 ECShop 系统管理后台 `http://43.xxx.xxx.132/ecshop/admin`（使用时请替换为自己的站点 IP）。
2. 单击**腾讯云设置 > 对象存储配置**，即可配置 COS 插件。配置项说明如下：

<table>
   <tr>
      <th width="0%" >配置项</td>
      <th width="0%" >配置值</td>
   </tr>
   <tr>
      <td>开启腾讯云存储</td>
      <td>选择是</td>
   </tr>
   <tr>
      <td>开启自定义配置</td>
      <td>选择是。SecretId、SecretKey 为访问密钥信息，建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参考 <a href="https://cloud.tencent.com/document/product/598/37140">子账号访问密钥管理</a>。</td>
   </tr>


   <tr>
      <td>所属地域</td>
      <td>创建存储桶时所选择的地域，详情请参见  <a href="https://cloud.tencent.com/document/product/436/6224">地域和访问域名</a>。 </td>
   </tr>
   <tr>
      <td>空间名称</td>
      <td>创建存储桶时自定义的名称，例如 examplebucket-1250000000，详情请参见  <a href="https://cloud.tencent.com/document/product/436/13312">存储桶概述</a>。</td>
   </tr>
   <tr>
      <td>访问域名</td>
      <td>输入存储桶的访问域名，详情请参见 <a href="https://cloud.tencent.com/document/product/436/6224">地域和访问域名</a>。</td>
   </tr>
</table>
<img style="max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/65a0dc6cdaa7522209ab6bef65e6dabf.png" />

3. 配置完成后，单击开始测试，提示测试成功后，即表示插件已成功配置到 ECShop 系统。


## 验证 ECShop 商品图存储到 COS


1. 登录 ECShop 系统管理后台 `http://43.xxx.xxx.132/ecshop/admin`（使用时请替换为自己的站点 IP）。
2. 单击商品管理，在商品列表中添加新商品并上传商品图。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4bbb0723ccd44c509b65c38eeef7554e.png)
3. 添加商品完成后，登录 COS 控制台，进入您所配置的存储桶，在存储桶的 images 文件夹下可看到系统所生成的图片分类，在商品类别中可找到已上传的商品图。

>?
>
>- 上传的商品图以上传日期归类，请根据上传日期进行查找。
>- 在 ECShop 平台中选择删除商品图也将同步删除 COS 存储桶中对应的商品图。



## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击 [此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406) 一键启动，立即使用！

