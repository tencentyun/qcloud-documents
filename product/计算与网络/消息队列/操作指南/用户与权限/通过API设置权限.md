## 子用户密钥
使用子账号登录访问管理控制台的【[云 API 密钥](https://console.cloud.tencent.com/capi)】，找到**子用户的密钥**。密钥用于生成签名，认证通过后可访问相关腾讯云资源。

**签名的作用**：
- 验证请求用户身份：通过用户密钥来确认。
- 防止内容被篡改：通过对请求内容使用 hash 算法进行签名，通过签名的一致性来判定内容是否被篡改。
- 防止重放攻击：签名内容中包括请求时间、签名时间及有效期，可避免过期请求重放。同时云服务也可以通过请求时间来拒绝过期请求。


## API 调用示例
### 接口协议
- 编码类型：UTF8
- 编码格式：JSON
- 传输方式：POST
- 请求协议：HTTP

调用规范示例：
<dx-codeblock>
::: json
{
	"version": 1,
	"componentName": "MC",
	"eventId": 123456,
	"interface": {
		"interfaceName": "接口名",
		"para": {
			接口对应参数
		}
	}
}
:::
</dx-codeblock>


返回结果：
<dx-codeblock>
::: json
{
	"version": 1,
	"eventId": 123456,
	"componentName": "CONSOLE_LOGICAL_SERVER",
	"returnValue": 0,
	"returnCode": 0,
	"returnMessage": "OK",
	"data": {
		"ownerUin": 123,
		"uin": 124,
		"ownerAppid": 323
	}
}
:::
</dx-codeblock>

当返回结果出错时，则 returnCode 不为0，returnMessage 内容为出错信息。
输入参数中的 interfaceName 、para 和输出参数中的 data 说明详见 [调用说明](#调用说明)。

### 接口说明
有关 CAM 用户与权限的详细 API 接口介绍，可查看 [ CAM API 文档](https://cloud.tencent.com/document/product/598/33155)。

### 调用示例
#### 新增策略（CreateCamStrategy）
策略示例：设置某个子用户（Uin 为“3232”）具有 list 账户下所有 queue 的权限，且对北京 region 的 horacetest1 有消费消息、批量删除消息的权限。

- 字段解析

| 参数 | 描述 | 示例取值 |
|---------|---------|---------|
| strategyName | 策略名称。 | strategy1 |
| strategyInfo | 策略描述的内容（这里要传一个 **JSON 字符串**）。 | 见 [示例代码](#示例代码1) |
| remark | 策略的备注。 | hello test |
| resource | CMQ 的资源六段式描述，例如`qcs::cmqqueue:bj:uin/1238423:queueName/uin/3232/myqueue`<br>第一段为固定格式 qcs；<br>第二段为空；<br>第三段表示消息队列的类型，队列模型为 cmqqueue，主题模型为 cmqtopic；<br>第四段为地域信息，例如 gz、bj、sh 若为全地域，则设置为空；<br>第五段为主账号 `uin/{主账号uin}`；<br>第六段为资源的描述，当为队列模式时，则 `queueName/uin/{创建者Uin}/{队列名字}` ，当为主题模式时该值取 `topicName/uin/{创建者Uin}/{主题名字}`。创建者的 Uin 可以通过控制台详情页获取，或者通过 yunapi 接口 GetQueueAttributes 或者GetTopicAttributes 的返回值 createUin 获取。|* |

- 示例代码：<span id="示例代码1"></span>
```
{
"strategyName":"strategy1",
"strategyInfo":{"version":"2.0","principal":{"qcs":["qcs::cam::uin/1238423:uin/3232/myqueue","qcs::cam::uin/1238423:groupid/13"]},"statement":[{"effect":"allow","action":"name/cmqqueue:ListQueue","resource":"*"},{"effect":"allow","action":["name/cmqqueue:ReceiveMessage","name/cmqqueue:BatchDeleteMessage"],"resource":["qcs::cmqqueue:bj:uin/1238423:queueName/uin/3232/myqueue","qcs::cmqqueue:bj:uin/1238423:queueName/uin/3232/*"]}]},
"remark":"horace test"
}
```
>?在第六段的资源的描述中，`uin/`后的创建者 ID 可以在创建策略时查看。

 ![](https://main.qcloudimg.com/raw/c6d7be9b98c8021d1ffc2fac6e4d2522.png)

#### 子账户关联/移除策略（OperateCamStrategy）
此接口可给用户或者用户组联/移除策略。

- 策略示例：将 UIN 为“123456”的用户关联到策略 ID 为“666”的策略。

- 字段解析：

| 参数 | 描述 | 示例取值 |
|---------|---------|---------|
| groupId | 如果是关联用户，则 groupId 传-1；<br>如果是关联用户组，则 groupId 传具体组 ID。 |  -1 |
| relateUin | 如果是关联用户，则 relateUin 传具体用户 uin；如果是关联用户组，则 relateUin 传-1。 | 123456 |
| strategyId | 需要关联的策略 ID。 | 666 |
| actionType | 值为“1”表示关联策略；值为“2”表示移除策略。 | 1 |

- 示例代码：
```
{
	"groupId":-1,
	"relateUin":123456,
	"strategyId":666,
	"actionType":1
}
```


## 调用说明<span id="调用说明"></span>
该说明适用于各种业务的用户与权限管理，在设置 CMQ 业务时，请根据以下说明判断 CMQ 的相关取值。
1. principal 可以不填，后续通过关联策略接口关联用户。
2. principal、action、resource，当只有一个元素时，可以不加`[]`。
3. 资源（resource）描述格式通常采用六段式，格式为`qcs:project:serviceType:region:account:resource`。
	- project：可以用`id/0`、`*`或者`id/*`表示所有项目。授权时 project 为空表示`id/0`，鉴权时 project 为空表示可在任意项目中出现。默认为空。
	- serviceType：为 cos、cdn、vpc 等，`*`表示所有业务。不可以为空。
	- region：为地域，值为空，表示所有地域，其他地域分别是"gz"、"st"、"tj"、"sh"、"hk"、"ca"、"shjr"、"bj"。默认为空。
	- account：表示为`uin/${uin}`或者`uid/${uid}`。为空时，对于 CDN 业务和 VPC 等业务的资源，填充为`uin/${uin}`，对于 COS 业务的资源，填充化为`uid/${uid}`，`${uin}`或`${uid}`表示访问者的 uin 或者 uid。默认为空。
	还有一种特殊情况，`uin/-1`一般是预设策略才出现，扩展表展开后会把-1变成开发商的uin，另外预设策略只允许子账户或角色的授权，所以可以直接用子账户或角色所属的根账户 uin 来替换-1。
	- resource 由 name/value 构成。name 表示业务对资源的定义。如 cmq 的为 queueName 和 topicName。cos 是用 prefix 描述，cdn 用 host 描述等。`*`表示所有资源，归一化为`*/*`的形式。不可以为空。
	- 用户、策略也是一种资源。CAM 根账户描述为`qcs::cam::uin/1238423: uin/1238423`，CAM 子账户描述为`qcs::cam::uin/1238423: uin/3236671`，匿名用户描述为`qcs::cam::anonymous:anonymous`。
	- resource 为空时表示操作不需要关联对象。在系统中归一化为`*`。
	- 对资源描述中 uin 或 uid 是否真的是该资源的拥有者，需要由业务来校验。强制要求业务在鉴权通过后必须校验，建议在授权时也进行校验。 
        
