在域名的记录管理页有如下提示，说明DNS服务器不正确，需将域名DNS修改为提示的DNS地址，解析方可生效。

![](https://mc.qcloudimg.com/static/img/a75cc4cebd9655a2021e30b93658aecb/1.png)

__注意：不同解析套餐对应的DNS地址不同，请根据提示来修改。__

### 1. 腾讯云注册域名修改DNS
如果域名在腾讯云注册，或者已转入腾讯云，可以通过以下步骤修改DNS服务器

1.1 进入【域名管理】控制台
![](https://mc.qcloudimg.com/static/img/a2984f9928955ed3ae49d82cfd18f55d/2.png)

1.2 选择相应域名【管理】
![](https://mc.qcloudimg.com/static/img/d0425544b447491fbb7164617976f351/3.png)

1.3 【修改】DNS服务器
![](https://mc.qcloudimg.com/static/img/167d5e318df0d4de62f2a4cb1801c838/4.png)

1.4 填写指定的DNS服务器地址
![](https://mc.qcloudimg.com/static/img/0b866d917b994eb84eab2a58b6cd16e3/5.png)


如果域名在其他注册商处管理，您需要前往域名注册商提供的域名管理页面，修改为指定的域名DNS。
下面以阿里云（万网）、GoDaddy为例说明修改方法：

### 2. 阿里云（万网）注册商域名修改DNS

2.1 选择需要在腾讯云进行解析的域名，进入域名管理页的【DNS修改/创建】，点击【修改域名DNS】；

![](https://mccdn.qcloud.com/static/img/2ade9bc496f296f14186df348835ed8e/image.png)

2.2 分别填写f1g1ns1.dnspod.net，f1g1ns2.dnspod.net，保存后最长等待72小时可以全球生效。

![](https://mccdn.qcloud.com/static/img/bca1fc5a448568567c3498b3d2c0da4d/image.png)


### 3. GoDaddy注册商域名修改DNS

登录 [http://www.godaddy.com](http://www.godaddy.com)

3.1 登录后单击【DOMAINS】的【Manage】

![1](https://mccdn.qcloud.com/static/img/857a65f25a4c950dab04f36c6773bf20/GD-1.png)

3.2 在域名列表中找到要修改要修改DNS的域名，然后点击该域名后的下拉图标，点击下拉列表中的 【Set NameServers】

![2](https://mccdn.qcloud.com/static/img/d692fab785a928ebbfc183637bdd9c31/GD-2.png)

3.3 选择【Custom】，然后点击右下角的【Add Nameserver】

![3](https://mccdn.qcloud.com/static/img/2b5194f50b656d4d75666d2357f784b6/GD-3.png)

3.4 输入腾讯云的2个DNS短地址，然后点击【Add】，再点击【Save】即可。

f1g1ns1.dnspod.net
f1g1ns2.dnspod.net

![4](https://mccdn.qcloud.com/static/img/bed919b5d4fe0b33b6bc9f537dce1a8d/GD-4.png)

![5](https://mccdn.qcloud.com/static/img/8c4f15a5fa913037a06f752ac62ac22b/GD-5.png)

3.5 最后，点击保存，等待全球递归DNS服务器刷新（最多72小时）。
