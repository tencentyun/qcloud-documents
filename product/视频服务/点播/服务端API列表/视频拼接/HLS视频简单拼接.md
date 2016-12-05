## 接口名称
SimpleConcatHls

## 功能说明
1. 拼接文件；
2. 源文件需要是hls的；
3. 目标文件生成后一定是hls的。

## 请求方式
Get

### 请求域名
vod.api.qcloud.com

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------------|----------|---------|---------|
| srcFileList | 是 | Array | 文件id列表 |
| name          | 是 | String    | 拼接出来的文件名称|

### 请求示例
```
https://vod.api.qcloud.com/v2/index.php?Action=SimpleConcatHls
&srcFileList.0.fileId=16092504232103571364
&srcFileList.1.fileId=16092504232103571365
&name=testfile
&COMMON_PARAMS
```
## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| fileId | String | 拼接出的文件id |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见公共错误码。  |
| 1000 | 无效参数  |
| 1001 | 数据库获取用户信息失败  |
| 10009 | 文件状态异常  |

### 应答示例
```
{
    "code": 0,
    "message": "",
    "fileId": "123121321234"
}
```
