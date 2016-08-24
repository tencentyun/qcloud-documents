## 1. 接口描述

本接口（DescribeCdnEntites）只适用于托管源且使用SVN去管理CDN源文件的场景，不适用于自有源或者FTP托管源这样的场景。该接口用于获取SVN下的CDN下某个目录文件实例列表。
可输入基础路径来获取文件实例列表返指定数量的文件实例列表。

接口请求域名：<font style="color:red">cdn.api.qcloud.com</font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://www.qcloud.com/doc/api/231/4473)页面。其中，此接口的Action字段为DescribeCdnEntites。

| 参数名称   | 是否必选   | 类型     | 描述              |
| ------ | ---- | ------ | --------------- |
| entityBaseDir | 否    | String | 查询的基础路径，默认“/” |
| offset | 否 | Int | 偏移量，默认为0 |
| limit | 否 | Int | 返回的文件实例数量，默认20，最大值200 |

## 3. 输出参数
| 参数名称      | 类型     | 描述             |
| ------- | ------ | -------------- |
| code    | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message | String | 模块错误信息描述，与接口相关。          |
| totalCount | Int | 符合查询条件的文件实例总数 |
| entitySet | Array | CDN实例文件信息列表，详细说明见下文 | 

#### entitySet结构说明
| 参数名称   | 类型     | 描述              |
| ------ | ---- |  --------------- |
| fileName | String | 文件名称 |
| fileSize | Int | 文件大小，单位byte |
| fileType | Int | 文件类型，1：普通文件，2：目录|
| lastUpdateTime | String | 最后修改时间，格式如2014-11-24 16:41:07 | 


## 4. 示例
 
### 4.1 输入示例
```
https://cdn.api.qcloud.com/v2/index.php?
Action=DescribeCdnEntites
&SecretId=XXXXXXXXXXXXXXXXX
&Timestamp=1462430812
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&entityBaseDir=/image
```

### 4.2 输出示例
```
{
  'code': 0,
  'message': '',
  'totalCount': 2,
  'entitySet': [
    {
      'fileName': '/xxx/111.jpg',
      'fileSize ': 1040,
      'fileType': 1,
      'lastUpdateTime': '2014-11-24 16:41:07'
    },
    {
      'fileName': '/xxx/222.jpg',
      'fileSize ': 1129,
      'fileType': 1,
      'lastUpdateTime': '2014-11-24 16:42:07'
    }
  ]
}

```

### PHP&Python示例下载
**[示例代码 PHP&Python 新版](https://github.com/zz-mars/CDN_API_DEMO/tree/master/Qcloud_CDN_API)**