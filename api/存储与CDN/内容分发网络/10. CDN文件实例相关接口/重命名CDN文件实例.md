## 1. 接口描述

本接口（RenameCdnEntity）只适用于托管源且使用SVN去管理CDN源文件的场景，不适用于自有源或者FTP托管源这样的场景。该接口用于对SVN下CDN文件实例重命名。

接口请求域名：<font style="color:red">cdn.api.qcloud.com</font>
 

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://www.qcloud.com/doc/api/231/4473)页面。其中，此接口的Action字段为RenameCdnEntity。

| 参数名称   | 是否必选   | 类型     | 描述              |
| ------ | ---- | ------ | --------------- |
| entityFileName | 是 | String | 文件实例完整路径 |
| entityNewFileName | 是 | String | 新的实例名|


## 3. 输出参数

| 参数名称      | 类型     | 描述             |
| ------- | ------ | -------------- |
| code    | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message | String | 模块错误信息描述，与接口相关。          |


## 4. 示例
 
### 4.1 输入示例
```
https://cdn.api.qcloud.com/v2/index.php?
Action=RenameCdnEntity
&SecretId=XXXXXXXXXXXXXXXXX
&Timestamp=1462430812
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&entityFileName=/image/111.jpg
&entityNewFileName=/image/222.jpg
```

### 4.2 输出示例
```
{
  'code': 0,
  'message': '',
}

```

### PHP&Python示例下载
**[示例代码 PHP&Python 新版](https://github.com/zz-mars/CDN_API_DEMO/tree/master/Qcloud_CDN_API)**