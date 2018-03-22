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
