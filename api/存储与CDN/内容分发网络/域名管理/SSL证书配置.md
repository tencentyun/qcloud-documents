## 接口描述
本接口用于配置/删除域名的 HTTPS 配置。
请求域名：<font style="color:red">cdn.api.qcloud.com</font>
接口名：<font style="color:red">SetHttpsInfo</font>

>!
+ COS 源、FTP 源域名暂时无法将回源方式设置为协议跟随。
+ 证书&私钥传递：选择自上传证书，请将证书、私钥内容按照 Base64 编码后传输。
+ 选择托管证书，使用接口 [查询托管证书列表](https://cloud.tencent.com/document/product/228/12543) 获取对应的证书 ID。
+ httpsType 与 forceSwith 不可同时为空。
+ 接口暂不支持子账号调用。

[查看调用示例](https://cloud.tencent.com/document/product/228/1734)。


## 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 。其中，此接口的 Action 字段为 SetHttpsInfo。

| 参数    | 是否必选 | 类型   | 描述                                                         |
| ----------- | -------- | ------ | ------------------------------------------------------------ |
| host        | 是       | String | 需要配置证书的域名。                                           |
| httpsType   | 否       | Int    | 配置类型设置<br/>"0" ：清除 HTTPS 配置，无需填写证书及私钥参数。<br/>"1"：上传自有证书，并 HTTP 回源。<br/>"2"：上传自有证书，并协议跟随回源。<br/>"3"：使用托管证书，并 HTTP 回源。<br/>"4"：使用托管证书，并 协议跟随回源。<br/>1&2 域名未配置证书或配置的是自有证书，则 必须上传 cert 及 privateKey。<br/>3&4 域名未配置证书或配置的是托管证书，则必须传递 certId。 |
| cert        | 否       | String | PEM 格式证书。                                                  |
| privateKey  | 否       | String | PEM 格式私钥。                                                  |
| forceSwitch | 否       | Int    | 强制跳转开关<br/>"1"：HTTP 强制跳转。<br/>"-1"：关闭 HTTP 强制跳转。<br/>"2"：开启 HTTPS 强制跳转（302）。<br/>"-2"：关闭 HTTPS 强制跳转（302）。<br/>"3"：开启 HTTPS 强制跳转（301）。<br/>"-3"：关闭 HTTPS 强制跳转（301）。 |
| http2       | 否       | String | HTTP2.0 开关<br/>"on"：开启 HTTP2.0。<br/>"off"：关闭 HTTP2.0。  |
| certId      | 否       | String | 证书 ID，可通过接口 [查询托管证书列表](https://cloud.tencent.com/document/product/228/12543) 获取。 |

## 输出参数
| 参数    | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。<br/>详情请参见错误码页面 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                        |
| codeDesc | String | 英文错误信息，或业务侧错误码。<br/>详情请参见错误码页面 [业务错误码](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| data     | Object | 返回结果数据。                                   |


## 代码示例
### 示例参数

>!示例中证书私钥仅供参考。

```
host：www.test.com
httpsType：1
cert：9Zs0K3FV+azvYI7eYYVqRd/ZvlyaI3ctzHnqVSuYk5UxELFobd5IQpUo9V5SviFQoBibyZLG4qvmh7VRD7G6yYOKzVzONm++yP5JJb1OvJyB/2bRS/aZLNAEJ4DAWFZpSSdajGSuM5TvV3q0MDYMkuSl3rW+ldTPdeLZopZVjfHQCfXdYetWdLxE1YVzRY+JMWPWztD2v9TSxxUNhKiCe3KvFrusU2mEZNFkReUDiakiCbwBryT4Yg+6zopvwD32eCxwK9zW0WCcBqMKsea5hXvyFJoLyUvhLb8V0ZHySuuneorUeVokszpPJpWIUAtajlIjK5lSPAvYUSUAHZk=
privateKey：9Zs0K3FV+azvYI7eYYVqRd/ZvlyaI3ctzHnqVSuYk5UxELFobd5IQpUo9V5SviFQoBibyZLG4qvmh7VRD7G6yYOKzVzONm++yP5JJb1OvJyB/2bRS/aZLNAEJ4DAWFZpSSdajGSuM5TvV3q0MDYMkuSl3rW+ldTPdeLZopZVjfHQCfXdYetWdLxE1YVzRY+JMWPWztD2v9TSxxUNhKiCe3KvFrusU2mEZNFkReUDiakiCbwBryT4Yg+6zopvwD32eCxwK9zW0WCcBqMKsea5hXvyFJoLyUvhLb8V0ZHySuuneorUeVokszpPJpWIUAtajlIjK5lSPAvYUSUAHZk=
```

###  GET 请求
GET 请求需要将所有参数都加在 URL 后（key = value形式，value 需要进行 URL encode）：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=SetHttpsInfo
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
&httpsType=1
&cert=XXXXXXXXXXXXXXXXXXXXXXXXXX
&privateKey=XXXXXXXXXXXXXXXXXXXXXXX
```

### POST 请求
POST 请求时，参数填充在 HTTP Request body 中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 form-data 等格式，参数数组如下：

```
array (
	'Action' => 'SetHttpsInfo',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'host' => "www.test.com",
    'httpsType'  => 1,
    'cert' => 'XXXXXXXXXXXXXXXXXXX',
    'privateKey' => 'XXXXXXXXXXXXXXXXX'
)
```

### 返回示例

```
{
	"data": [],
	"code": 0,
	"message": ""
}
```


