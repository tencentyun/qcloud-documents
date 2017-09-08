通过本教程，您将了解到如何通过 CDN 快速地分发内容。腾讯云在全国各省份部署 800+ 加速节点，您的服务内容将缓存至距离用户最近的节点，再通过全网监控与智能调度，将用户请求精准调度到最优接入节点，降低访问延迟，帮助用户快速获取所需内容。要实现 CDN 加速，您需要准备一个原始服务器（又称：源站），当节点中没有缓存用户请求的内容时，CDN 会向源站请求内容，返回给用户并缓存到 CDN 节点。本次教程将使用腾讯云 [对象存储](https://www.qcloud.com/product/cos) 存储桶作为源站，按照下列步骤进行操作，最终您将可以通过浏览器访问存储桶中的内容。

**开始前请将您的 CDN 计费方式设为流量计费。CDN 及对象存储服务的免费额度足以完成本次教程，无需任何花费。**

## 一、配置源站
开始使用 CDN 服务前，您需要准备好 **对象存储（Cloud Object Storage，简称：COS）** 存储桶作为源站，并将您的内容上传。内容可以是音视频、图片、HTML页面、css样式文件等静态内容。具体操作步骤如下。
1. 本教程中我们将使用下图作为测试图片。您可以单击 [Tencent_CDN.png](http://cdntest-1253833564.cosgz.myqcloud.com/Tencent_CDN.png) 下载原图，也可以使用您计算机上的图片。
![](https://mc.qcloudimg.com/static/img/975e127f832bf943b5b0575d96c9d160/Tencent_CDN.png)
2. 创建 COS 存储桶。若您已有 COS 存储桶，请跳到步骤 3。
	2-1. 登录 [COS 控制台](https://console.qcloud.com/cos4) ，单击概览页上的【创建 Bucket】，弹出创建 Bucket 对话框。
	![](https://mc.qcloudimg.com/static/img/94a92b09d6dd58e9de2e9a3c8a3c3586/image.png)
	2-2. 填写存储桶名称（如：cdntest），选定存储桶所属地域，单击【确定】即可快速创建一个存储桶。
	![](https://mc.qcloudimg.com/static/img/2da55897ed9666300bb2a0eeacdb0ea6/create_bucket.png)
3. 将测试图片 **Tencent_CDN.png** 上传至 COS 存储桶。
	3-1. 登录 [COS 控制台](https://console.qcloud.com/cos4) ，单击【Bucket 列表】，进入存储桶列表。单击您想存储对象的存储桶，进入存储桶的文件列表页面。
	![](https://mc.qcloudimg.com/static/img/ddbbd04cea224839ec026ca11c2ea56c/bucket_list.png)
	3-2. 在文件列表中，单击【上传文件】，出现上传文件对话框。
	![](https://mc.qcloudimg.com/static/img/78b365fd883bfd6231a65c3f9d935166/upload_file.png)
	3-3. 单击【上传文件】，选择 **Tencent_CDN.png**，单击【确定上传】，上传成功后会弹出提示框。
	![](https://mc.qcloudimg.com/static/img/ca01c8ea5c1032e067ba572e5360953a/select_file.png)

## 二、接入域名
配置源站完成后，将您的域名接入 CDN。
1. 登录 [CDN 控制台](https://console.qcloud.com/cdn)，单击左侧菜单中【域名管理】进入 **域名管理** 页面，单击【添加域名】。
![](https://mc.qcloudimg.com/static/img/e68a96fa42843fa13f58afc7ba15e2fe/add_host.png)
2. 填写域名相关配置及加速服务相关配置。
	2-1. 在 **域名** 处填入您的域名，域名必须已经在工信部备案。
	2-2. 在 **源站类型** 下拉菜单中选中【对象存储（COS）】。在 **源站** 下拉菜单中选中您创建的存储桶作为源站。 
	2-3. 在 **业务类型** 下拉菜单中选中静态加速，静态加速适用于图片、静态网站等内容的加速场景。
	2-4. 单击 【提交】 完成域名接入。
	![](https://mc.qcloudimg.com/static/img/7662acc676fa17f306712da17f75b7de/add_domain.png)

## 三、CNAME 配置
接入域名完成后，CDN 会自动为您分配一个以 ```.cdn.dnsv1.com``` 为后缀的 CNAME 域名。您需要在您的域名 DNS 服务商为您的域名添加一条 CNAME 记录。
1. 登录 [CDN 控制台](https://console.qcloud.com/cdn)，单击左侧菜单中【域名管理】进入 **域名管理** 页面，查看您的 CNAME 域名。
![](https://mc.qcloudimg.com/static/img/39bf233c5145c1f1c64bfa2c628c6019/check_cname.png)
2. 到您的域名 DNS 服务商处添加 CNAME 解析记录。本教程所使用域名 DNS 服务商为腾讯云，其他服务商请参阅 [CNAME 配置](https://www.qcloud.com/document/product/228/3121)。
	2-1. 登录 [域名管理](https://console.qcloud.com/domain) 控制台，单击您的域名右侧的【解析】跳转到 **记录管理** 页面。
	![](https://mc.qcloudimg.com/static/img/d736722a9a2f0788f55c3ea10320baab/mydomain.png)
	2-2. 单击【添加记录】，添加 CNAME 记录。
	![](https://mc.qcloudimg.com/static/img/280a9f09e37eeb5938a8b10b7e671b9c/add_record.png)
	2-3. 在弹出的窗口中，将 **记录类型** 设置为 CNAME，在 **主机记录** 处填写域名前缀（如：www），在 **记录值** 处填写 CNAME 域名，单击【确定】，即可添加 CNAME 记录。
	![](https://mc.qcloudimg.com/static/img/398f272e255e7645c7a170c483a29f68/record_info.png)
	2-4. 在命令行中 PING 您的域名，PING 到后缀为 ```.sp.spcdntip.com``` 的域名表示域名 CNAME 已生效。
	![](https://mc.qcloudimg.com/static/img/6935d942002b83117157028b6dbad46c/ping.png)


## 四、结果测试
完成上述操作后，通过浏览器访问您的内容测试是否配置成功。
1. 登录 [CDN 控制台](https://console.qcloud.com/cdn)，选择左侧菜单栏的【域名管理】，单击您的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/064a6808d098beea397e55b6e776194d/domain_manage.png)
2. 在【基本配置】页面中，查看 **源站信息** 中的 **源站地址**。
![](https://mc.qcloudimg.com/static/img/72392441874862aa65307d4214af1ec8/host_info.png)
3. 打开文本编辑器，将下列代码复制到编辑器中，将倒数第二行 img 标签中 src 属性的“xxxxxx”替换成您在步骤 2 中查看的 **源站地址**。替换后将文件另存为“cdntest.html”。
``` HTML
<!DOCTYPE HTML>
<head>
<title>CDN Test</title>
<meta charset="UTF-8">
</head>
<body>
<h1>THIS IS MY CDN TEST HTML！</h1>
<!-- 请将 src 中的 “xxxxxx” 替换成您的源站地址 -->
<img src="http://xxxxxx/Tencent_CDN.png">
</body>
```
4. 将 ```cdntest.html``` 上传到您的 COS 存储桶。
![](https://mc.qcloudimg.com/static/img/0ead26411755696e3b61a5f4eb8feb18/upload_html.png)
5. 在您的 COS 存储桶页面中，单击【基础配置】，找到静态网站设置，单击【编辑】按钮，进入可编辑状态。
![](https://mc.qcloudimg.com/static/img/682188854dabd038d34a452569feefa3/image.png)
6. 开启静态网站功能，单击【保存】。
![](https://mc.qcloudimg.com/static/img/cc3a70001267a80581c162ecb83f2d96/static_site.png)
7. 通过浏览器访问您的内容，在浏览器地址栏输入 ```xxxxxx/cdntest.html``` 进行访问，请将“xxxxxx”替换成您的 **域名**。浏览器将显示下图展示的页面。如果访问失败，请确认您是否完成了前面的所有操作。
![](https://mc.qcloudimg.com/static/img/3b1dc8791ca7540f1f3e119f0f31e741/test_ok.png)

## 五、关闭 CDN
您可以在 CDN 控制台中关闭域名加速服务。若您决定不再使用某些内容，最好关闭他们对应的 CDN 服务，以免产生不必要的消耗。关闭本教程中对应的 CDN 服务后，用户将不能再通过您的域名访问您 COS 源中的内容。
1. 登录 [CDN 控制台](https://console.qcloud.com/cdn)，单击【域名管理】进入 **域名管理** 页面，右键单击要关闭加速服务的域名，选择【关闭 CDN】。
![](https://mc.qcloudimg.com/static/img/367e6359e85fb7eebb2a9867506948a8/shutdown_cdn.png)
2. 单击【确定关闭】即可关闭 CDN。
![](https://mc.qcloudimg.com/static/img/6f16a16eb5999c72ad9b3b39139eccd7/shutdown_confirm.png)

至此，您已成功完成本教程的所有步骤。你可以参照上述步骤配置您自己的 CDN 服务，通过设置更多自定义选项优化您的 CDN 加速效果。