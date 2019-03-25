## 接口名称
SmallFileUpload

## 功能说明
1. 当前仅支持小1M的封面文件上传

## 请求方式

### 请求域名
vod2.qcloud.com

> 注意：
> - 服务端视频上传的域名与其他服务端API不同，*不是* vod.api.qcloud.com；
> - 该接口POST方法。

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| Action | 是 | String | 命令字，填SmallFileUpload |
| fileName | 是 | String | 文件本地名称，如果包含中文空格，则需要使用rawurlencode编码，长度在40个字符以内，不得包含\ / : * ? “ < > \| 等字符 |
| fileSha | 是 | String | 文件的sha，采用SHA-1计算文件内容 |
| fileSize | 是 | Int64 | 文件的总大小，单位字节Byte，注意本接口仅支持1M以内的文件上传 |
| dataSize | 是 | Int | 上传的分片大小，协议对齐用，等于fileSize |
| fileType | 是 | String | 视频文件的类型，根据后缀区分 |
| extra.usage | 是 | Int | 标识该文件用途，填1，表示上传指定视频的封面 |
| extra.fileId | 否 | String | extra.usage=1时填，上传封面对应的视频文件id|

### 请求示例
如下为请求URL，真正的视频数据需要在POST请求的body中提交。
```
https://vod2.qcloud.com/v2/index.php?Action=SmallFileUpload
&fileName=test
&fileSha=b4a5c70c76e79e01ab3a5c306de3d9eedeadeca9
&fileSize=1048576
&dataSize=1048576
&fileType=jpg
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Int | 小于0：失败；0：成功 |
| message | String | 返回信息说明 |
| url | String | 文件url | 
| fileId | String | 文件id，code=2 时返回 |
| canRetry | Int | code<0 时，是否可重试，canRetry=1时可重试 |

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| -10001 | 检查公共参数出错 |
| -10002 | 检查签名出错 |
| -10003 | 检查协议参数出错 |
| -10004 | 写缓存信息失败 |
| -10005 | 获取缓存信息失败|
| -10006 | 包体非法 |
其他错误码可能为网络原因导致的偶发失败。所有小于0的错误码，当canRetry=1时，均可重试解决。
### 应答示例
```
{
    "canRetry": 0,
    "code": 0,
    "codeDesc": "",
    "fileId": "11868222811305801",
    "message": "",
    "url": "http://1251132154.vod2.myqcloud.com/vod1251132154/9031868222807461771/11868222811305801.jpg"
}
```
