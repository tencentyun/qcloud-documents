当您的自定义域名接入云点播后，系统会为您自动分配一个 CNAME 域名（以 .cdn.dnsv1.com 为后缀)，您可在云点播控制台 [域名管理](https://console.cloud.tencent.com/vod/distribute-play/domain) 进行查看。自动分配的CNAME 域名不能直接访问，您需要在域名服务提供商处完成 CNAME 配置，配置生效后，即可正常访问。

![](https://main.qcloudimg.com/raw/3666cc48cac239f76d7238c0b1df0994.png)
## 腾讯云设置方法
若您的 DNS 服务商为腾讯云，您可通过如下步骤添加 CNAME 记录。
1. 登录 [域名管理](https://console.cloud.tencent.com/domain) 控制台，在“我的域名”列表中，找到需要添加 CNAME 记录的域名，单击操作类中的**解析**。
![](https://main.qcloudimg.com/raw/5f1db6e690ab50c9498dd563a1a4e11d.png)
2. 跳转到指定域名的 **记录管理** 页面，单击**添加记录**。
![](https://main.qcloudimg.com/raw/b2da788dd6230b1404325fd703a8925e.png)
3. 在弹出框中，将 **记录类型** 设置为 CNAME，在 **主机记录** 处填写域名前缀（如：www），在 **记录值** 处填写 CNAME 域名，单击**确定**，即可添加 CNAME 记录。
![](https://main.qcloudimg.com/raw/7c3dd58437b49145c8954fceebe8d2f6.png)
	1. 主机记录处填子域名（例如需要添加`www.123.com`的解析，只需要在主机记录处填写`www`即可。如果只是想添加`123.com`的解析，主机记录直接留空，系统会自动填一个“@”到输入框内，@的 CNAME 会影响到 MX 记录的正常解析，添加时慎重考虑）。
	2. 记录类型为 CNAME。
	3. 线路类型（默认为必填项，否则会导致部分用户无法解析。在上图中，默认的作用为：除了联通用户之外的所有用户，都会指向 1.com）。
	4. 记录值为 CNAME 指向的域名，只可以填写域名，记录生成后会自动在域名后面补一个“.”，这是正常现象。
	5. MX 优先级不需要填写。
	6. TTL 不需要填写，添加时系统会自动生成，默认为600秒（TTL 为缓存时间，数值越小，修改记录各地生效时间越快）。


## 万网设置方法
若您的 DNS 服务商为万网，您可通过如下步骤添加 CNAME 记录。
1. 登录万网会员中心。
2. 单击会员中心左侧导航栏中的**产品管理**> **我的云解析**进入万维网云解析列表页。
3. 单击要解析的域名，进入解析记录页。
4. 进入解析记录页后，单击新增解析按钮，开始设置解析记录。
![](https://main.qcloudimg.com/raw/b122299f088cee9c9f1a0a044f34a232.png)
5. 若要设置 CNAME 解析记录，将记录类型选择为 CNAME。主机记录即域名前缀，可任意填写（如：`www`）。记录值填写为当前域名指向的另一个域名。解析线路，TTL 默认即可。
![](https://main.qcloudimg.com/raw/bff5be116fd6e0cd73ec26ce91ecfb1e.png)
6. 填写完成后，单击**保存**，完成解析设置。

## 新网设置方法
若您的 DNS 服务商为新网，您可通过如下步骤添加 CNAME 记录。
**设置别名（CNAME 记录）**
即：别名记录。这种记录允许您将多个名字映射到同一台计算机。通常用于同时提供 WWW 和 MAIL 服务的计算机。例如，有一台计算机名为`host.mydomain.com`（A记录）。它同时提供 WWW 和 MAIL 服务，为了便于用户访问服务。可以为该计算机设置两个别名（CNAME）：WWW 和 MAIL 。如下图：
![](https://main.qcloudimg.com/raw/2e93d51c7fe8502670475d71bbfb20cb.png)

## 验证 CNAME 是否生效
不同的 DNS 服务商，CNAME 生效的时间略有不同，一般会在半个小时之内生效。您可以通过以下方式查询 CNAME 是否配置生效。
- 方法一：**开始**→**运行**→输入 cmd 并回车，输入 PING 命令来查询 CNAME 是否生效，如果返回的解析结果与该域名的 CNAME 值一致，则 CNAME 已配置生效。
![](https://main.qcloudimg.com/raw/3ecec823ae0159bc114754a8a3875ff9.png)
- 方法二：**开始**→**运行**→输入 cmd 并回车，输入 nslookup 命令来查询 CNAME 是否生效，如果返回的解析结果与该域名的 CNAME 值一致，则 CNAME 已配置生效。
![](https://main.qcloudimg.com/raw/3b29de73c80e9d651df6bb38aed83d2a.png)
