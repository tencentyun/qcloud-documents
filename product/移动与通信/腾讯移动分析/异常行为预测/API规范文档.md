异常行为预测问询API，通过API接口调用的形式，方便用户进行签名认证与接口集成，并根据不同行业，方便用户完成不同类型的数据反馈。
## 公共参数与API
### API公共请求参数
**通用必填项**

| &emsp;	参数名&emsp;		| &emsp;	类型&emsp;		|  &emsp;	说明 &emsp;	| 
| :---: | :-----: | :----: |
| appkey	| String	| 业务侧身份标识| 
| timestamp	| String	| 业务侧发请求的 UNIX 使劲按戳| 
| random	| String	| 当前请求的标识随机数| 
| userid	|String	| 业务的的用户身份标识| 
| mobile	| Ulong	| 手机号| 
| signature	|String	| 请求签名，验证当前请求合法性| 

签名步骤：
1.由腾讯侧提供加密算法，并分配业务侧动态加密码；
2.业务侧组装通用项数据，采取动态加密码和加密算法生成密文，以密文生成 md5 值作为 signature 请求签名；
### 异常评分问询API
**接口描述**
接口：http://fbi.qq.com/api/ask/score
调用：POST
说明：业务侧提交申请用户的相关信息，获取风险评分以及风险原因点。

**输入参数**
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数。

**基础信息，必填项**

| 参数名	     | 类型	       |  说明                                     | 
| :---:          | :-----:      | :----                                       | 
| os	| String	| 数据渠道 :&nbsp;0 : 未知 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 : iOS<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 : Android<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 : H5| 
| device| String	| 业务侧发请求的 UNIX 使劲按戳| 
| random	| String	| 当前请求的标识随机数| 
| userid	|String	| 业务的的用户身份标识| 
| mobile	| Ulong	| 手机号| 
| signature	|String	| 请求签名，验证当前请求合法性| 
**扩展信息**

|参数名	| &emsp;	&emsp;	&emsp;	类型	&emsp;	&emsp;	&emsp;	|  &emsp;	&emsp;	说明 &emsp;	&emsp;	 | 
| :---: | :-----: | :----:|
| industry	| String | 行业	| 
| company	| String	| 公司名| 
| job	| String	| 职业| 
| address_company	|String	| 公司地址| 
| emailAddress	| String	| 邮箱地址| 
| QQ	|String	| QQ号| 
| WX	|String	| 微信号|
**输出信息**

|参数名	| &emsp;	&emsp;	&emsp;	类型	&emsp;	&emsp;	&emsp;	|  &emsp;	&emsp;	说明 &emsp;	&emsp;	 | 
| :---: | :-----: | :----:|
| code	| Uint | 接口返回码，0 即为成功；其他为错误码	| 
| desc	| String	|返回码描述，当 code 为 0 时为 succses，其他时为具体出错描述| 
| flowid	| String	| 服务器反馈的当次申请标识，当期仅当 code = 0 时有效| 
| score	|Uint	| 异常预测评分，万分制| 
| scoreDesc	| String	| 异常因子详情，存在多个因子情况下则用分号 " ; " 分隔 |
**风险建议**

|  风险等级	| &emsp;	&emsp;	&emsp;	分数段	&emsp;	&emsp;	&emsp;	|  &emsp;	&emsp;	建议 &emsp;	&emsp;	 | 
| :---: | :-----: | :----:|
| 高风险	| [8000,10000] | 异常系数高，建议拒绝	| 
| 中风险	| [4000,8000)	|结合业务指标调控| 
| 低风险	| [1,4000)]	| 结合业务指标调控| 
**示例**
1. 请求示例
```
http://fbi.qq.com/api/ask/score?appkey=22b608f45b291a5d2decc5fdbdf80d37180620f8bef122ee880bfce93e1db9e3&
timestamp=13252352352&random=2352352&signature=4a9c5689036bdfc304613f528dc6aba9&mobile=1321852512&userid
=23532523&idcard=532131987558651425&banknos=621412414141141;621412414141142&contacts=13221877657;17133655920
```
2. 返回示例
```
{"scoreDesc":"201","score":2614,"flowid":"de8eefd5b88b43fc877f4b1fa201bdf1","code":0,"desc":"success"}
```
## 金融网贷
### 授权数据同步
**接口描述**
接口：http://fbi.qq.com/api/data/synch
调用：POST
说明：针对用户已授权，并客户已采集的数据，进行同步至 FBI 平台侧。
时效：基于关联异常分析可显著提高准确度，建议业务端授权拉取后，即时同步。

**输入参数**
存在相应数据，则请同步

| 参数名 | 类型 | 说明 | 属性值 |
| :----:    | :----: | :----: | :---- |
| processTime | Ulong | 授权拉取时间戳，单位秒 | |
| phoneList |String | 手机通讯录列表 | 昵称(n),手机号(m) |
| callLIst | String | 通话清单列表 | 昵称(n),手机号(m)，时间( t, 格式 yyyyMMddHHmmSS)|
| msgReceList | String | 短信接收列表 | 昵称(n),手机号(m)，时间( t, 格式 yyyyMMddHHmmSS)，内容 (c)|
| msgSendList | String | 短信发送列表 | 昵称(n),手机号(m)，时间( t, 格式 yyyyMMddHHmmSS)，内容 (c)|
| socialSecurityList | String | 社保记录列表 | 缴纳时间( t, 格式 yyyyMMdd); 社保缴纳总金额( j, 单位元)|
| publicFundList | String | 公积金记录列表 | 缴纳时间( t, 格式 yyyyMMdd); 公积金缴纳总金额( j, 单位元)|
|creditBillList | String | 信用卡账单列表 | 账单还款日( t1, 格式 yyyyMMdd)；实际还款时间( t2, 格式 yyyyMMddHHmmSS； 未还款则不填)；账单金额( j,单位元)|

**输出参数**

| 参数名 | 类型 | &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;说明&emsp;&emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|
| :----: | :----: | :-----: |
| code | Uint | 接口返回码，0 即为成功；其他为错误码|
| desc | String | 返回描述， 当 code 为 0 时为 success ,其他时为具体出错描述| 

**示例**
1. 请求示例
```
fbi.qq.com/api/data/synch?appkey=84c8292358be3614afc35525a09f4b55180620f8bef122ee880bfce93e1db9e3&timestamp=1513688850127&random=111&signature=4dd558d888aa5f2d056e5ada4e697496&mobile=13580211212&userid=1530728&phoneList=[{"n":"张三","m":"15611111111"},{"n":"李四","m":"15611111112"}]&creditBillList=[{"t1":"20171123","j":"2602.50","t2":"20171120"},{"t1":"20171223","j":"3000.21"}]
```
2. 返回示例
```
{"code":0,"desc":"success"}
```

### 放款流程反馈
**接口描述**
接口：http://fbi.qq.com/api/feedback/process
调用：POST
说明：当业务调用 3.2 风险问询 API 后，结合自身风控策略对申请用户进行流程处置，如放贷、拒绝， 需调用此接口反馈流程结果，作为业务反馈和后续贷中监控源。
时效：建议实时同步，延迟同步不超过t+1(最迟每日凌晨5点同步前一天)。
>注意：<br>若 t+1 未收到问询评分对应用户的相关放款反馈，官方将停止问询评分 API 的开放；

**输入参数**
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数。

| 参数名 | 类型 | 说明 |
| :----:    | :----: | :--|
| flowid | String | 申请用户在业务侧的当次申请标识，由 “ 异常评分问询 API ”返回 |
| resultType | Unit | 业务处置状态: &nbsp;1. 拒绝放贷<br> &nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;2. 通过放贷 <br> &nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&ensp;&nbsp;&nbsp;3. 拒绝首次授信<br> &nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. 通过首次授信<br> &nbsp;&nbsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;5. 拒绝提额度<br> &nbsp;&nbsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;&emsp;&nbsp;6. 通过提额<br> &nbsp;&nbsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&emsp;&emsp;&emsp;&nbsp;7. 系统降频<br> &nbsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8. 用户取消借贷<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;(含“用户收不到借款”情况)|
| processTime | Ulong | 业务处置时间戳，单位秒 | 
| money | Uint | 金额，单位元(人名币)；即放贷金额、或首次授信额度、提额、降频后金额 | 
| stages | Uint | 分期数，非分期产品则为 1；非 “ 通过放贷 ”状态下不填 | 
| repaymentTimes | String | 还款计划（数组格式），若非分期则仅 1 元素；非“ 通过放贷 ”状态下不填 | 
| reason | String | 审核不通过情况下的原因、人工备注等； “ 通过放贷 ”状态下不填 | 

**输出参数**

| 参数名 | 类型 | 说明 | 属性值 |
| :----:    | :----: | :----: | :---- |
| processTime | Ulong | 授权拉取时间戳，单位秒 | |
| phoneList |String | 手机通讯录列表 | 昵称(n),手机号(m) |
| callLIst | String | 通话清单列表 | 昵称(n),手机号(m)，时间( t, 格式 yyyyMMddHHmmSS)|
| msgReceList | String | 短信接收列表 | 昵称(n),手机号(m)，时间( t, 格式 yyyyMMddHHmmSS)，内容 (c)|

**输出参数**

| 参数名 | 类型 | 说明 |
| :----:    | :----: | :----: | 
| code | Uint | 接口返回码: 0 ,成功；其他为错误码 | 
| desc |String | 返回描述，code 为 0 时为 success，其他时为具体出错描述 |
**示例**
1. 请求示例：
```
http://fbi.qq.com/api/feedback/process?appkey=22b608f45b291a5d2decc5fdbdf80d37180620f8bef122ee880bfce93e1
db9e3&timestamp=13252352352&random=2352352&signature=4a9c5689036bdfc304613f528dc6aba9&flowid=096daf24ba75
44b8b738059367678cf4&userid=23532523&resultType=2&processTime=13252352362&money=700&stages=3&repaymentTim
es=[20171101;20171201;20180101]
```

2. 返回示例：
```
{"code":0,"desc":"success"}
```

### 还款效果反馈
**接口描述**
接口：http://fbi.qq.com/api/feedback/effect
调用：POST
说明：针对放款用户，在还款时间点或后续判定环节，进行效果反馈。
时效：建议实时同步，延迟同步不超过t+1(最迟每日凌晨5点同步前一天)。

>注意：<br>若t+1未收到问询评分对应用户的相关还款效果反馈，官方将停止问询评分API的开放；

**输入参数**
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数。

|参数名 | 类型 | 说明 |
| :----:    | :----: | :--:|
| flowid | String | 申请用户在业务侧的当次申请标识，由 “ 风险问询  ”提供 |
| stageId | Uint | 分期数：非分期则为 1|
| resultType | Uint | 业务处置状态，1. 正常还款、2. 判定为 M1 逾期 （> 30 天还未还款）、3. 判定为 M3 欺诈（ >  90天未还款）、4. 逾期还款、5. 到期但未还款 | 
| processTime | Ulong | 业务处置时间，单位秒 | 
>备注：
>1. 分期指的是需要同步每一分期期数的还款情况，若用户多分期未还款，则调用多次； 
>2. 逾期指的是若用户账单到期且未还款，则每日需要同步其 "5. 到期但未还款 ",直到2、3、4三种情况产生；
>3. 欺诈指的是若用户M1逾期，且>90天未还款，则于时间点"账单到期91天"时进行反馈；

**输出参数**

| 参数名 | 类型 | 说明 |
| :----:    | :----: | :----: | 
| code | Uint | 接口返回码: 0 ,成功；其他为错误码 | 
| desc |String | 返回描述，code 为 0 时为 success，其他时为具体出错描述 |
**示例**
1. 请求示例：
```
http://fbi.qq.com/api/feedback/effect?appkey=22b608f45b291a5d2decc5fdbdf80d37180620f8bef122ee880bfce93e1db9e3
&timestamp=13252352352&random=2352352&signature=4a9c5689036bdfc304613f528dc6aba9&flowid=096daf24ba7544b8b7380
59367678cf4&userid=23532523&resultType=1&processTime=13252352372&stageId=1
```

2. 返回示例：
```
{"code":0,"desc":"success"}
```

