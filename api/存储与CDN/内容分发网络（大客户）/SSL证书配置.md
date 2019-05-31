## 1. 接口描述
本接口（SetHttpsInfo）用于配置/删除域名的HTTPS配置。

接口请求域名：cdn.api.qcloud.com


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://www.qcloud.com/doc/api/231/4473)页面。其中，此接口的Action字段为 SetHttpsInfo。

| 参数名称        | 是否必选 | 类型     | 描述                                       |
| ----------- | ---- | ------ | ---------------------------------------- |
| host        | 是    | String | 需要配置证书的域名                                |
| httpsType   | 是    | Int    | 配置类型设置，若设置为 0 ，表示清除https配置，此时无需填写证书及私钥参数；若设置为1，表示开启并http回源；若设置为2，表示开启并https回源；开启时需要传递证书及私钥； |
| cert        | 否    | String | PEM格式证书                                  |
| privateKey  | 否    | String | PEM格式私钥                                  |
| forceSwitch | 否    | Int    | 强制跳转开关，若设置为1，则表示http强制跳转，设置-1关闭http强制跳转；若设置为2，则表示https强制跳转，设置-2关闭https强制跳转 |

**注意事项**

+ COS源、FTP源域名暂时无法设置为Https回源
+ 证书&私钥传递：请将证书、私钥内容按照base64编码后传输
+ httpsType与forceSwith不可同时为空

## 3. 输出参数
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Object | 返回结果数据                                   |


## 4. 示例
### 4.1 输入示例
> host: www.test.com
> httpsType: 1
> cert: 9Zs0K3FV+azvYI7eYYVqRd/ZvlyaI3ctzHnqVSuYk5UxELFobd5IQpUo9V5SviFQoBibyZLG4qvmh7VRD7G6yYOKzVzONm++yP5JJb1OvJyB/2bRS/aZLNAEJ4DAWFZpSSdajGSuM5TvV3q0MDYMkuSl3rW+ldTPdeLZopZVjfHQCfXdYetWdLxE1YVzRY+JMWPWztD2v9TSxxUNhKiCe3KvFrusU2mEZNFkReUDiakiCbwBryT4Yg+6zopvwD32eCxwK9zW0WCcBqMKsea5hXvyFJoLyUvhLb8V0ZHySuuneorUeVokszpPJpWIUAtajlIjK5lSPAvYUSUAHZk=
> privateKey: 9Zs0K3FV+azvYI7eYYVqRd/ZvlyaI3ctzHnqVSuYk5UxELFobd5IQpUo9V5SviFQoBibyZLG4qvmh7VRD7G6yYOKzVzONm++yP5JJb1OvJyB/2bRS/aZLNAEJ4DAWFZpSSdajGSuM5TvV3q0MDYMkuSl3rW+ldTPdeLZopZVjfHQCfXdYetWdLxE1YVzRY+JMWPWztD2v9TSxxUNhKiCe3KvFrusU2mEZNFkReUDiakiCbwBryT4Yg+6zopvwD32eCxwK9zW0WCcBqMKsea5hXvyFJoLyUvhLb8V0ZHySuuneorUeVokszpPJpWIUAtajlIjK5lSPAvYUSUAHZk=

### 4.2 GET 请求
GET 请求需要将所有参数都加在 URL 后（key=value形式，value需要进行URL encode）：
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

### 4.2 POST请求
POST请求时，参数填充在HTTP Requestbody中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 formdata等格式，参数数组如下：

```
array (
	'Action' => 'SetHttpsInfo',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'host' => ''www.test.com",
    'httpsType'  => 1,
    'cert' => 'XXXXXXXXXXXXXXXXXXX',
    'privateKey' => 'XXXXXXXXXXXXXXXXX'
)
```

### 4.3 返回示例

注意：示例中IP仅供参考。

```
{
  "retcode":0,
  "errmsg":'ok",
  "data":[],
  "code":0,
  "message":""
}
```
