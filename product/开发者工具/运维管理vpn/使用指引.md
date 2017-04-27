# 功能说明
## 1.	创建VPN域
每个用户都会拥有一个唯一的域，用于VPN账号的管理，在使用运维管理VPN前设置域的名称，该名称设置成功后不能修改
	
## 2.	创建VPN
在“VPN列表”里点击“新建”，设置VPN基本信息，支付成功后即可完成VPN创建。  
VPN名称：用于识别不同的运维管理VPN  
所属网络：设置此VPN连接后可直接访问的服务器所在的私有网络  
带宽：根据使用量，设置合适的带宽（一般5个终端连接情况下，5M带宽可满足需求）  

限制说明：  
1）一个私有网络（VPC）里，只允许创建一个VPN  
2）当前仅支持最大5个终端同时连接VPN  

![](https://mc.qcloudimg.com/static/img/99033ed16343c77ffa129e1b8e646d94/11.png)

## 3.	查看VPN列表
![](https://mc.qcloudimg.com/static/img/ead9ecdbab48dc4a6887ec177e171885/22.png)

## 4.	查看VPN配置详情
在列表页点击“VPN名称”，可查看VPN配置详情。
![](https://mc.qcloudimg.com/static/img/04c8bdad26b04a4d4aca0bd8d0823850/33.png)

## 5.	配置VPN端口
在配置详情里点击“编辑”，配置VPN端口  
端口可设置为443 或者 1025 ~ 65534 范围内，一个VPN只能对应一个端口  
![](https://mc.qcloudimg.com/static/img/0cadd38561be7d27069a07e73a1f160b/44.png)

## 6.	配置ACL安全策略
用于设置VPN网关的网络访问策略，系统默认为禁止访问所属网络所有服务器，可根据需要配置  
源IP：允许访问VPN网关的客户端IP/IP段，默认为VPN终端IP段  
目的IP：允许VPN网关访问的服务器端IP/IP段，设置范围需在VPN所在私有网络的网段内  
协议：访问协议，支持tcp/udp/icmp/all（所有协议）  
目的端口：目的IP的端口  
策略：允许/拒绝 所设网络路由  

### 6.1.	增加ACL安全策略
![](https://mc.qcloudimg.com/static/img/08c1db45d0215cf3821444ce9dd028e6/55.png)

### 6.2.	删除ACL安全策略
![](https://mc.qcloudimg.com/static/img/47885eb8400964945deb7a02f868726b/66.png)

### 6.3.	修改ACL安全策略
进入“编辑“状态后，
1）调整策略顺序：鼠标靠近移动图标，可调整安全策略顺序；  
![](https://mc.qcloudimg.com/static/img/44ff402adb2ab5f71fc9f7c1d7d5bb61/77.png)

### 6.4.	查看ACL安全策略列表
![](https://mc.qcloudimg.com/static/img/b0d74abfe522ac241e54dfc78731b577/88.png)

## 7.	查看登录日志
用于查看一段时间内VPN的帐号登录信息，主要用于事后安全审计
## 8.	查看VPN帐号
![](https://mc.qcloudimg.com/static/img/5711b5cf4d3b0fdabec02e71e8077a04/99.png)

## 9.	新建VPN帐号
![](https://mc.qcloudimg.com/static/img/03f8c1a390d4e86dbf0b46a3075f5cb0/10.png)

## 10.	删除VPN帐号
![](https://mc.qcloudimg.com/static/img/c7aadad0f8a69c720e344c3ec2c5530b/101.png)

## 11.	修改PIN码
为帐号设置新的PIN码，需要输入原PIN码、新PIN码和云令牌的token码
注：如果忘记原PIN码，请提工单联系客服修改（提交工单地址：http://console.qcloud.com/ticket）
![](https://mc.qcloudimg.com/static/img/35a513c3522de1cc88b92288ce55a6d1/102.png)

## 12.	更换云令牌
更换帐号所绑定的云令牌，需要输入PIN码、新的云令牌的SN码和token码
![](https://mc.qcloudimg.com/static/img/fadd3734c2b6bffd14b6fbb6a8e0c159/103.png)

## 13.	下载VPN客户端
目前已支持多个版本的windows操作系统：
![](https://mc.qcloudimg.com/static/img/8a8d9cc2c245e6de5d5a8f6f545c0758/104.png)

## 14.	通过客户端连接VPN
详见《腾讯SSL VPN智能客户端使用指导》

## 16.	申请使用运维管理VPN
### 16.1申请使用运维管理VPN
请联系大客户经理申请使用运维管理VPN  

### 16.2购买云令牌
购买云令牌请提交工单申请：http://console.qcloud.com/ticket  
发货前会从云账户里扣除对应的费用，请确保账户余额充足。  
单价：20元/个  
工单输入说明：  
1、产品模版：两项均选择“其他”  
2、问题描述：填入购买需求，示例如下：  
	因业务需要申请购买运维管理VPN的云令牌  
	1、购买数量：10个  
	2、邮寄地址  
		收件人：张三  
		收件人联系电话：18612345678  
地址：广东省深圳市南山区腾讯大厦3楼  
![](https://mc.qcloudimg.com/static/img/43afb94bfbca3405e803228409bf7263/105.png)







