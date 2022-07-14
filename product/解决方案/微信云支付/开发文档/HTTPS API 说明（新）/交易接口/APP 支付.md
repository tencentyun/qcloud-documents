##  接口描述
**手机 App 支付接口，目前仅支持微信支付。**

|项|	值|
|--|--|
url	|https://pay.qcloud.com/cpay/app_pay

##  输入参数
| 参数名 | 必填 | 类型 |说明
|---------|---------|---------|-------|
request_content|	是	|String	|请求内容，该 string 可以转为 json 结构，json 格式见本节 RequestContent。
authen_info	|是|	AuthenInfo	|认证信息，详见接口调用说明。

### RequestContent 结构
<table class="tg">
  <tr>
    <th class="tg-s268">一级参数名</th>
    <th class="tg-s268">二级参数名</th>
		<th class="tg-s268">三级参数名</th>
    <th class="tg-s268">必填</th>
    <th class="tg-s268">类型</th>
    <th class="tg-s268">说明</th>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="10"><a id="manage_tool">pay_content</a></td>
    <td class="tg-s268">out_trade_no</td>
		<td class="tg-s268">-</td>
    <td class="tg-s268">是</td>
    <td class="tg-s268">String(32)</td>
    <td class="tg-s268">由客户端生成的订单号，前缀必须是云支付订单前缀。</td>
  </tr>
  <tr>
     <td class="tg-s268">total_fee</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">是</td>
    <td class="tg-s268"> Number(32)</td>
		<td class="tg-s268">订单总金额，单位：分。</td>
  </tr>
  <tr> 
      <td class="tg-s268">fee_type</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">是</td>
    <td class="tg-s268">String</td>
		<td class="tg-s268">货币类型（目前只支持人民币，请填 CNY）。 </td>
  </tr>
	<tr> 　  
    <td class="tg-s268">time_expire</td>
		<td class="tg-s268">-</td>
    <td class="tg-s268">否</td>
    <td class="tg-s268"> Number(64) </td>
		<td class="tg-s268">订单过期时间。</td>
  </tr>
	 <tr>　   
      <td class="tg-s268">body 　 </td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">是 </td>
    <td class="tg-s268">String(128) </td>
		<td class="tg-s268">商品或订单简要描述，需传入应用市场上的“APP 名称-实际商品名称”，如“天天爱消除-游戏充值”。</tr>
	<tr>
      <td class="tg-s268">detail</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">否</td>
    <td class="tg-s268">String </td>
		<td class="tg-s268">商品详细列表，由 json 转化而来，json 结构见公共数据结构 Detail。</td>
  </tr>
	<tr>
      <td class="tg-s268">remark</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">否</td>
    <td class="tg-s268">String(127) </td>
		<td class="tg-s268">支付备注信息。</td>
  </tr>
	<tr>
      <td class="tg-s268" rowspan="3">wxpay_pay_content_ext </td>
    <td class="tg-s268">attach</td>
    <td class="tg-s268">否</td>
    <td class="tg-s268">String(127)	</td>
		<td class="tg-s268"> 附加数据，记录子商户自定义数据。</td>
  </tr>
	 <tr> 
      <td class="tg-s268">goods_tag</td>
    <td class="tg-s268">否</td>
    <td class="tg-s268">String(32)	</td>
		<td class="tg-s268">商品标记，代金券或立减优惠功能的参数。</td>
  </tr>
	<tr> 
      <td class="tg-s268">limit_pay</td>
    <td class="tg-s268">否</td>
    <td class="tg-s268">String(32)	</td>
		<td class="tg-s268">定支付方式，目前只能是 no_credit，指定不能使用信用卡支付。</td>
  </tr>
  <tr>
      <td class="tg-s268" rowspan="5">pay_mch_key</td>
    <td class="tg-s268">pay_platform</td>
		<td class="tg-s268">-</td>
    <td class="tg-s268">是</td>
    <td class="tg-s268">Number(32)	</td>
		<td class="tg-s268">第三方支付类型，详见枚举 PayPlatform。</td>
  </tr>
	<tr>
    <td class="tg-s268">out_mch_id</td>
		<td class="tg-s268">-</td>
    <td class="tg-s268">是</td>
    <td class="tg-s268">String(32)	</td>
		<td class="tg-s268">服务商对外帐号。</td>
  </tr>
	<tr>
    <td class="tg-s268">out_sub_mch_id</td>
		<td class="tg-s268">-</td>
    <td class="tg-s268">是</td>
    <td class="tg-s268">String(32)	</td>
		<td class="tg-s268">子商户对外帐号。</td>
  </tr>
	<tr>
    <td class="tg-s268">out_shop_id</td>
		<td class="tg-s268">-</td>
    <td class="tg-s268">是</td>
    <td class="tg-s268">String(32)	</td>
		<td class="tg-s268">门店对外帐号。</td>
  </tr>
	<tr>
      <td class="tg-s268">wxpay_pay_mch_key_ext </td>
    <td class="tg-s268">mob_app_id </td>
    <td class="tg-s268">是</td>
    <td class="tg-s268">String(32)	</td>
		<td class="tg-s268">受理商户的 APPID，在微信开放平台绑定申请。</td>
  </tr>
	<tr>
    <td class="tg-s268">nonce_str</td>
		<td class="tg-s268">-</td>
		<td class="tg-s268">-</td>
    <td class="tg-s268">是</td>
    <td class="tg-s268">String(32)	</td>
		<td class="tg-s268">随机字符串。</td>
  </tr>
</table>

## 输出参数

|参数名 | 	必填 |类型 |	说明
|---------|---------|---------|-----|
response_content|	是|	ResponseContent	|请求内容，详见本节 ResponseContent。
authen_info|	否	|AuthenInfo	|认证信息，详见接口调用说明。

### ResponseContent 结构
|参数名 | 	必填 |类型 |	说明
|---------|---------|---------|-----|
status	|是	|Status	|错误码，详见 Status。0：成功；非0：失败。
description|	否	|String(255)|	错误描述。
log_id|	是	|Number(32)	|消息 ID。
internal_status|	是|	Number(32)	|调试使用，调用者可以不予理会。
app_pay	|否|	AppPayResponse	|authen_info 存在时必填。详见 AppPayResponse。


### AppPayResponse 结构 

|一级参数名|	二级参数名|	必填	|类型|	说明
|---------|---------|---------|-----|-----|
pay_mch_key|	-	|是|	PayMchKey	|支付商户信息，详细见公共结构 PayMchKey。
nonce_str	|-	|是|	String(32)	|随机字符串。
sdk_args|	wxpay	|否|	WxpaySdkArguments	|微信 App 支付 SDK 接口参数，结构见下文。

### WxpaySdkArguments 结构 
|参数名 | 	必填 |类型 |	说明
|---------|---------|---------|-----|
app_id|	是	|String	|子商户在微信开放平台上申请的 APPID。
timestamp	|是	|String	|时间戳。
nonce_str	|是|	String|	随机字符串。
package_value|	是|	String	|暂填写固定值 Sign=WXPay。
partner_id	|是|	String	|子商户的商户号。
sign	|是	|String	|签名。
prepare_id	|是|	String	|微信返回的支付交易会话 ID。

##  示例
**输入参数示例：**

```
{  
    "authen_info": {  
        "a": {  
            "authen_type": 1,  
            "authen_code": "E6E70FF7E330E046239B05E100942B15C469928B044DF6488F3BD88AB385C682"  
        }  
    },  
    "request_content": "{  
		"pay_mch_key": {  
			"out_sub_mch_id": "sz01LG0dvp4O09jjuPbA",  
			"wxpay_pay_mch_key_ext": {  
					"mob_app_id": "wx87dd198b78jucir8"  
			},  
			"out_mch_id": "sz01fdd7icm7JKjkkfc3",  
			"out_shop_id": "sz011Zszd73bocifI9eG",  
			"pay_platform": 1,  
			"out_mch_id": "sz01MaHltuPggtcvcTUM"  
		},  
		"nonce_str": "k8s03nyOPIQxju4lw69CCfeUWL66GDBH",  
		"pay_content": {  
			"body": "body",  
			"fee_type": "CNY",  
			"out_trade_no": "011888520000211567600739877620",  
			"total_fee": 100,  
			"time_expire": 1567601636  
		}  
	}"  
}  
```
**输出参数示例：**

```
{  
    "response_content": "{  
		"status": 0,  
		"description": "\u64CD\u4F5C\u6210\u529F\u3002",  
		"log_id": 3637968353,  
		"internal_status": 0,  
		"app_pay": {  
			"pay_mch_key": {  
				"pay_platform": 1,  
				"out_mch_id": "sz01fdd7icm7JKjkkfc3",  
				"out_sub_mch_id": "sz01LG0dvp4O09jjuPbA",  
				"out_shop_id": "sz011Zszd73bocifI9eG",  
				"sub_pay_platform": 100,  
				"wxpay_pay_mch_key_ext": {  
					"app_id": "wx0b0ebc671d51405b",  
				}  
			},  
			"nonce_str": "zWbxyYBupz2DDIRiO9u9BsmjbAQsmnGv",  
			"sdk_args": {  
				"wxpay": {  
					"app_id": "wx87dd198b78jucir8",  
					"partner_id": "257300488",  
					"package_value": "Sign=WXPay",  
					"nonce_str": "k8s03nyOPIQxju4lw69CCfeUWL66GDBH",  
					"timestamp": "1567600739",  
					"sign": "B3E62ECF398573085397AFCAE1568A8A"  
				}  
			}  
		} 
	}",  
    "authen_info": {  
        "a": {  
            "authen_type": 1,  
            "authen_code": "852F74DA744049B1C629056FE8E8CC7BB59C49A25546ED66C8B75F4E6475AD73"  
        }  
    }  
}  
```
