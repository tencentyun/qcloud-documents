## 接口描述
**StartCdnService**  用于开通 CDN （国内）加速服务。

接口请求域名：<font style="color:red">cdn.api.qcloud.com</font>

**注意事项**

+ 开通 CDN 服务的账号需要先进行实名认证，[前往认证](https://console.cloud.tencent.com/developer)
+ 此接口仅支持国内 CDN 加速服务开通
+ 使用此接口开通 CDN 服务，默认同意 [腾讯云CDN产品服务保障协议](https://cloud.tencent.com/document/product/228/2946)


[查看调用示例](https://cloud.tencent.com/document/product/228/1734)

## 入参说明
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://cloud.tencent.com/doc/api/231/4473)页面。其中，此接口的Action字段为 StartCdnService。

| 参数名称    | 类型   | 是否必填 | 描述                                                         |
| ----------- | ------ | -------- | ------------------------------------------------------------ |
| payType     | String | 是       | 计费方式选择<br/> "flux"：日结流量计费<br/>"bandwidth"：日结带宽计费 |
| serviceType | String | 是       | 服务类型选择<br/>详情如下                                    |

#### 详细说明

##### serviceType

根据相关部门要求，开通 CDN 服务时，需备注对应的服务内容，可填充服务内容如下：

```
0：即时通信
1：搜索引擎
2：综合门户
3：网上邮局
4：网络新闻
5：博客/个人空间
6：网络广告/信息
7：单位门户网站
8：网络购物
9：网上支付
10：网上银行
11：网络炒股/股票基金
12：网络游戏
13：网络音乐
14：网络影视
15：网络图片
16：网络软件/下载
17：网上求职
18：网上交友/婚介
19：网上房产
20：网络教育
21：网站建设
22：WAP
23：其他
```

### 实名信息补充

根据相关部门要求，CDN 服务需要备注更多的个人实名信息，开通时若反馈您的实名认证信息不全，请按以下参数进行补齐：

| 参数名称   | 类型   | 是否必填 | 描述                                                         |
| ---------- | ------ | -------- | ------------------------------------------------------------ |
| idCardType | Int    | 否       | 实名认证方式<br/>"1"：个人认证，需补充身份证信息<br/>"2"：企业认证，需补充企业联系人实名信息 |
| idCard     | String | 否       | idCardType 为 1 时，需补充身份证信息<br/>idCardType 为 2 时，需补充企业联系人身份证信息 |
| contact    | String | 否       | idCardType 为 2 时，需补充企业联系人姓名                     |
| telephone  | String | 否       | idCardType 为 2 时，需补充企业联系人联系方式                 |

## 出参说明

| 参数名称 | 类型   | 描述                                                         |
| -------- | ------ | ------------------------------------------------------------ |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败<br/>详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                               |
| codeDesc | String | 英文错误信息，或业务侧错误码。                               |

## 调用案例

### 示例参数

```
serviceType：0
payType：flux
```

### GET 请求

GET 请求需要将所有参数都加在 URL 后（逗号进行转码）：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=StartCdnService
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1522399440
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&payType=flux
&serviceType=0
```

### POST请求
POST请求时，参数填充在HTTP Requestbody中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 formdata、xwwwformurlencoded 等格式，参数数组如下：

```
array (
	'Action' => 'StartCdnService',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1522399440,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'serviceType'=>'0',
	'payType'=>'flux'
)
```

### 返回示例
```json
{
    "code": 4000,
    "message": "(9123)EC_CDN_USER_EXIST cdn user exist",
    "codeDesc": "InvalidParameter"
}
```

