腾讯云的CMQ消息服务，通过CAM能力，实现权限的管理与控制。具体操作如下：


#一、创建用户（user）



### 1、访问入口
请访问[用户与权限控制台](https://console.cloud.tencent.com/cam)
![](//mccdn.qcloud.com/static/img/bc95b9e687ddb4c8eba5481f04af3e7a/image.png)

### 2、用户管理的作用
你可以将需要管理账户内云资源的员工(以QQ帐号为登录凭证)添加为你账户的子用户，可以为子用户关联适当的策略，以分配不同权限。

![](//mccdn.qcloud.com/static/img/10728645b9bf6e48b3c1f61e6d3caa28/image.png)
> 类比于公司组织架构，子用户即公司员工。

![](//mccdn.qcloud.com/static/img/104e9ca6e0e22db0efe4795adbae9f5b/image.png)
> 【用户管理】即是对组织架构中员工管理的抽象。

### 3、如何新建子用户
step1:访问[用户与权限控制台](https://console.cloud.tencent.com/cam)，并点击【新建用户】

step2:如果该用户需要登录腾讯云控制台或者调用云API，则需要选择【允许该用户登录腾讯云】、并填写【QQ帐号】作为登录凭证
![](//mccdn.qcloud.com/static/img/717db35eae2332917a152eb69e8b4339/image.png)

step3:请为该用户关联策略(策略描述了权限，关联策略后用户即获得策略描述的权限）
![](//mccdn.qcloud.com/static/img/6554d84d46a16ea7f708402600bfe08b/image.png)

step4: 在【用户管理】列表中，即可查看刚刚添加的子用户。
![](//mccdn.qcloud.com/static/img/f25458bc47e905348883376d3d645244/image.png)


### 4、子账户的秘钥

秘钥：使用子账户的登录账户、密码，可以在控制台的“云产品”--“云API秘钥”找到该子用户的秘钥。秘钥用于生成签名，认证通过后可访问相关腾讯云资源。

签名的作用：

- 1、验证请求用户身份。通过用户密钥来确认。
 
  2、防止内容被篡改。通过对请求内容使用hash算法进行签名，通过签名的一致性来判定内容是否备篡改。
 
  3、防止重放攻击。签名内容中包括请求时间、签名时间及有效期，可避免过期请求重放。同时云服务也可以通过请求时间来拒绝过期请求。



-



#二、新建自定义策略（控制台）



###1、指定具体api接口（开启权限）

我们可以创建某自定义策略，如指定CMQ Queue的写权限（消费消息、批量消费消息）

![](//mc.qcloudimg.com/static/img/ebe81c0f3661863f9961db0c5716081d/image.png)

指定具体api接口


![](//mc.qcloudimg.com/static/img/6237ef0c57ef39db790e19638f4e1bc5/image.png)




###3、指定资源对象

示例中，我们指定该策略，将该子账户下（包括该子账户创建）的所有Queue。作为关联对象


![](//mc.qcloudimg.com/static/img/ee8053f051805493d53d6f4f67f2d531/image.png)



###4、关联子用户

再关联到子用户。完成后，该子用户，对该子用户内的所有Queue资源，拥有消费消息、批量消费消息的权限。


![](//mc.qcloudimg.com/static/img/0bfdf9df7ad29dbae8e51c28904be972/image.png)


-



#三、API调用简单示例

###1、接口协议

```
编码类型：utf8
编码格式：json
传输方式：post
请求协议：http
调用规范示例如下：
{
	"version"	: 1,
"componentName"	:"MC",
	"eventId"	:123456,
	"interface":{
"interfaceName" : "接口名"
"para" : {
                          接口对应参数
                    }
}
}
返回结果，各返回结果如果出错则returnCode不为0, returnMessage 内容为出错信息
{
"version" : 1,
"eventId" :   123456,
"componentName" :  "CONSOLE_LOGICAL_SERVER",
"returnValue" :   0,
"returnCode" :   0,
"returnMessage" :  "OK",
"data" : {
"ownerUin":123,
"uin":124,
"ownerAppid":323
}
}
后续对输入参数中的interfaceName 、para和输出参数中的data 进行说明

```


### 2、接口说明



https://mc.qcloudimg.com/static/pdf/0d1b37b99bb74fd6a796d6ca7fd0353c/docfile.pdf




###3、调用示例

```
1. 新增策略：CreateCamStrategy
{
"strategyName":"strategy1",
"strategyInfo":'{"version":"2.0","principal":{"qcs":["qcs::cam::uin/1238423:uin/3232","qcs::cam::uin/1238423:groupid/13"]},"statement":[{"effect":"allow","action":"name/cmqqueue:ListQueue","resource":"*"},{"effect":"allow","action":["name/cmqqueue:ReceiveMessage","name/cmqqueue:BatchDeleteMessage"],"resource":["qcs::cmqqueue:bj:uin/1238423:queueName/3232/horacetest1","qcs::cmqqueue:bj:uin/1238423:queueName/3232/horacetest1"]}]}',
"remark":"horace test"
}
子用户Uin:3232
strategyName：策略名称。
strategyInfo：策略描述的内容。(！注意，这里要传一个json字符串)
remark：策略的备注
resource设置*：如果操作是需要关联资源的，它表示所有对象。如果操作是不需要关联资源的（比如list操作），它表示空对象
策略含义：指定了某个子用户3232，有list账户下所有queue的权限，且对北京region的horacetest1有消费消息、批量删除消息的权限

```

```
2. 子账户关联/移除策略API：OperateCamStrategy
{
	"groupId":-1,
	"relateUin":123456,
	"strategyId":666,
	"actionType":1
}
字段解析：
groupId：如果是关联用户，则groupId传-1；如果是关联用户组，则groupId传具体组id。
relateUin：如果是关联用户，则relateUin传具体用户uin；如果是关联用户组，则relateUin传-1。
strategyId：需要关联的策略id。
actionType：值为“1”表示关联策略；值为“2”表示移除策略。
（此接口可给用户或者用户组联/移除策略）
```



##4、调用说明：

```
说明：
	1）principal可以不填，后续通过关联策略接口去关联用户
	2）principal、action、resource，当只有一个元素时，可以不加[]。
	3）资源(resource)描述格式通常采用六段式,格式为"qcs: project :serviceType:region:account:resource",
		a.project可以用id/0, "*"或者"id/*"表示所有项目。授权时project为空表示id/0,鉴权时project为空表示可在任意项目中出现。默认为空。
		b.serviceType为cos、cdn、vpc等，"*"表示所有业务。不可以为空。
		c.region为地域，值为空，表示所有地域，其他地域分别是"gz", "st", "tj", "sh", "hk", "ca", "shjr", "bj"。默认为空。
		d.account，表示为"uin/${uin}"或者"uid/${uid}"。为空时，对于cdn业务和VPC业务等的资源，填充为"uin/${uin}"，对于COS业务的资源，填充化为"uid/${uid}“， "${uin}"或"${uid}"表示访问者的uin或者uid。默认为空。（还有一种特殊情况，“uin/-1”,一般是预设策略才出现，扩展表展开后会把-1变成开发商的uin，后续也可以考虑cos的uid/-1的形式，现阶段比较麻烦，因为db里没存uin和uid的对应关系。另外预设策略只允许子账户或角色的授权，所以可以直接用子账户或角色所属的根账户uin来替换-1）
		e.resource由name/value构成。name表示业务对资源的定义。如cos是用prefix描述，cdn用host描述等。"*"表示所有资源，归一化为"*/*"的形式。不可以为空。
		f.用户、策略也是一种资源。CAM根账户描述为qcs::cam::uin/1238423: uin/1238423，CAM子账户描述为qcs::cam::uin/1238423: uin/3236671，匿名用户描述为qcs::cam::anonymous:anonymous。
	    g.resource为空时表示操作不需要关联对象。在系统中归一化为*。
        h.对资源描述中uin或uid是否真的是该资源的拥有者，需要由业务来校验。强制要求业务在鉴权通过后必须校验，建议在授权时也进行校验。 
        
```