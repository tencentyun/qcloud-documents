如果域名在腾讯云以外平台注册，需将域名DNS修改为腾讯云解析DNS地址，解析方可生效，修改域名DNS步骤如下：
1. 首先前往域名注册商提供的域名管理页面
2. 修改域名DNS为：
f1g1ns1.dnspod.net
f1g1ns2.dnspod.net

下面以阿里云（万网）、GoDaddy为例说明修改方法


### 1. 阿里云（万网）注册商域名修改DNS

1.1 选择需要在腾讯云进行解析的域名，进入域名管理页的【DNS修改/创建】，点击【修改域名DNS】；

![](https://mccdn.qcloud.com/static/img/2ade9bc496f296f14186df348835ed8e/image.png)

1.2 分别填写f1g1ns1.dnspod.net，f1g1ns2.dnspod.net，保存后最长等待72小时可以全球生效。

![](https://mccdn.qcloud.com/static/img/bca1fc5a448568567c3498b3d2c0da4d/image.png)


### 2. GoDaddy注册商域名修改DNS

登录 [http://www.godaddy.com](http://www.godaddy.com) 

2.1 登录后单击【DOMAINS】的【Manage】

![1](https://mccdn.qcloud.com/static/img/857a65f25a4c950dab04f36c6773bf20/GD-1.png)
 
2.2 在域名列表中找到要修改要修改DNS的域名，然后点击该域名后的下拉图标，点击下拉列表中的 【Set NameServers】

![2](https://mccdn.qcloud.com/static/img/d692fab785a928ebbfc183637bdd9c31/GD-2.png)
 
2.3 选择【Custom】，然后点击右下角的【Add Nameserver】

![3](https://mccdn.qcloud.com/static/img/2b5194f50b656d4d75666d2357f784b6/GD-3.png)

2.4 输入腾讯云的2个DNS短地址，然后点击【Add】，再点击【Save】即可。

f1g1ns1.dnspod.net
f1g1ns2.dnspod.net

![4](https://mccdn.qcloud.com/static/img/bed919b5d4fe0b33b6bc9f537dce1a8d/GD-4.png)

![5](https://mccdn.qcloud.com/static/img/8c4f15a5fa913037a06f752ac62ac22b/GD-5.png)

2.5 最后，点击保存，等待全球递归DNS服务器刷新（最多72小时）。 
