## 前提：子用户的密钥

使用子账户的账户及密码登录，在控制台的【云产品】- 【[云API密钥](https://console.cloud.tencent.com/capi)】，找到子用户的密钥。密钥用于生成签名，认证通过后可访问相关腾讯云资源。

签名的作用：
- **验证请求用户身份：**通过用户密钥来确认。
- **防止内容被篡改：**通过对请求内容使用 hash 算法进行签名，通过签名的一致性来判定内容是否备篡改。
- **防止重放攻击：**签名内容中包括请求时间、签名时间及有效期，可避免过期请求重放。同时云服务也可以通过请求时间来拒绝过期请求。


## API调用简单示例

### 1. 接口协议

编码类型：utf8
编码格式：json
传输方式：post
请求协议：http

调用规范示例如下：
```
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
```
返回结果：各返回结果如果出错则 returnCode 不为0，returnMessage 内容为出错信息。

```
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
```

>注：后续对输入参数中的 interfaceName 、para 和输出参数中的 data 进行说明。

### 2. 接口说明

有关用户与权限 CAM 的详细 API 接口介绍，可 [点击此处查阅 >>](https://mc.qcloudimg.com/static/pdf/0d1b37b99bb74fd6a796d6ca7fd0353c/docfile.pdf) 

### 3. 调用示例

#### 新增策略：CreateCamStrategy

**策略示例：**

设置某个子用户（Uin 为 3232）具有 list 账户下所有 queue 的权限，且对北京 region 的 horacetest1 有消费消息、批量删除消息的权限。

**字段解析：**

| 参数 | 描述 | 示例取值 |
|---------|---------|---------|
| strategyName | 策略名称。 | strategy1 |
| strategyInfo | 策略描述的内容。（注意，这里要传一个json字符串) | 见示例代码 |
| remark | 策略的备注。 | horace test |
| resource设置* | 如果操作是需要关联资源的，它表示所有对象。如果操作是不需要关联资源的（比如 list 操作），它表示空对象。 |* |

**示例代码：**

```
{
"strategyName":"strategy1",
"strategyInfo":'{"version":"2.0","principal":{"qcs":["qcs::cam::uin/1238423:uin/3232","qcs::cam::uin/1238423:groupid/13"]},"statement":[{"effect":"allow","action":"name/cmqqueue:ListQueue","resource":"*"},{"effect":"allow","action":["name/cmqqueue:ReceiveMessage","name/cmqqueue:BatchDeleteMessage"],"resource":["qcs::cmqqueue:bj:uin/1238423:queueName/3232/horacetest1","qcs::cmqqueue:bj:uin/1238423:queueName/3232/horacetest1"]}]}',
"remark":"horace test"
}
```


#### 子账户关联/移除策略：OperateCamStrategy

此接口可给用户或者用户组联/移除策略。

**策略示例：**将 UIN 为 123456 的用户关联到策略 ID 为 666 的策略。

**字段解析：**

| 参数 | 描述 | 示例取值 |
|---------|---------|---------|
| groupId | 如果是关联用户，则groupId传-1；<br>如果是关联用户组，则groupId传具体组id。 |  -1 |
| relateUin | 如果是关联用户，则relateUin传具体用户uin；如果是关联用户组，则relateUin传-1。 | 123456 |
| strategyId | 需要关联的策略id。 | 666 |
| actionType | 值为“1”表示关联策略；值为“2”表示移除策略。 | 1 |

**示例代码：**

```
{
	"groupId":-1,
	"relateUin":123456,
	"strategyId":666,
	"actionType":1
}
```


## 调用说明
> 注：该小节内容适用于各种业务的用户与权限管理，在设置 CMQ 业务时，请根据以下说明判断 CMQ 的相关取值。

1. principal 可以不填，后续通过关联策略接口去关联用户；
2. principal、action、resource，当只有一个元素时，可以不加[]。
3. 资源(resource)描述格式通常采用六段式，格式为"qcs:project:serviceType:region:account:resource",
	- project可以用id/0, "*"或者"id/*"表示所有项目。授权时 project 为空表示 id/0，鉴权时project 为空表示可在任意项目中出现。默认为空。
	- serviceType为cos、cdn、vpc等，"*"表示所有业务。不可以为空。
	- region为地域，值为空，表示所有地域，其他地域分别是"gz", "st", "tj", "sh", "hk", "ca", "shjr", "bj"。默认为空。
	- account，表示为"uin/${uin}"或者"uid/${uid}"。为空时，对于CDN业务和VPC业务等的资源，填充为"uin/${uin}"，对于COS业务的资源，填充化为"uid/${uid}“， "${uin}"或"${uid}"表示访问者的uin或者uid。默认为空。（还有一种特殊情况，“uin/-1”,一般是预设策略才出现，扩展表展开后会把-1变成开发商的uin，另外预设策略只允许子账户或角色的授权，所以可以直接用子账户或角色所属的根账户uin来替换-1。）
	- resource由name/value构成。name表示业务对资源的定义。如cmq的为queueName和topicName。cos是用prefix描述，cdn用host描述等。"*"表示所有资源，归一化为"*/*"的形式。不可以为空。
	- 用户、策略也是一种资源。CAM 根账户描述为 qcs::cam::uin/1238423: uin/1238423，CAM子账户描述为qcs::cam::uin/1238423: uin/3236671，匿名用户描述为qcs::cam::anonymous:anonymous。
	- resource 为空时表示操作不需要关联对象。在系统中归一化为*。
  - 对资源描述中uin或uid是否真的是该资源的拥有者，需要由业务来校验。强制要求业务在鉴权通过后必须校验，建议在授权时也进行校验。 
        