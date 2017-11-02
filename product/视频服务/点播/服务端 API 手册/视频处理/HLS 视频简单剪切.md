## 接口名称
SimpleClipHls

## 功能说明
1. 将源视频文件按指定偏移时间进行掐头去尾剪切，新生成的视频文件（目标文件）将拥有新的FileID；
2. 源文件目前只支持腾讯云直播录制生成的原始HLS格式，其它来源文件均不支持剪切；
3. 目标文件与源文件使用相同的ts分片,源文件删除会导致目标文件不可播放。

## 事件通知
无。

## 请求方式
### 请求域名
vod.api.qcloud.com

### 最高调用频率
100次/分钟

### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------------|----------|---------|---------|
| srcFileId | 是 | String | 源文件的唯一标识ID |
| newFileName| 是 | String    | 目标文件名称|
| startTimeOffset | 是 | Integer| 目标文件开始相对源文件的时间偏移，单位为秒，大于0表示从头部开始计算，小于0表示从尾部开始计算 |
| endTimeOffset | 是 | Integer| 目标文件结束相对源文件的时间偏移，单位为秒，大于0表示从头部开始计算，小于0表示从尾部开始计算 |
| COMMON_PARAMS | 是 |  | 参见[公共参数](/document/product/266/7782#.E5.85.AC.E5.85.B1.E5.8F.82.E6.95.B0) |

### 请求示例一：时间偏移都为正数
期望生成的目标文件为源文件的第2秒到第10秒的视频内容，请求示例如下：
```
https://vod.api.qcloud.com/v2/index.php?Action=SimpleClipHls
&srcFileId=16092504232103571364
&newFileName=cutFileName
&startTimeOffset=2
&endTimeOffset=10
&COMMON_PARAMS
```

### 请求示例二：时间偏移有负数
期望生成的目标文件不包含源文件开始2秒和结束5秒的内容
```
https://vod.api.qcloud.com/v2/index.php?Action=SimpleClipHls
&srcFileId=16092504232103571364
&newFileName=cutFileName
&startTimeOffset=2
&endTimeOffset=-5
&COMMON_PARAMS
```

## 接口应答

### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码, 0: 成功, 其他值: 失败 |
| message | String | 错误信息 |
| newFileId | String | 目标文件的唯一标识ID|
|newFileUrl|String|目标文件播放的地址|

### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000-7000 | 参见[公共错误码](/document/product/266/7783)  |
| 1000 | 无效参数  |
| 1001 | 用户信息错误  |
| 10009 | 文件状态异常  |

### 应答示例

```javascript
{
    "code": 0,
    "message": "",
    "newFileId": "16092504232103571365",
    "newFileUrl": "http://vcloud1200.tc.qq.com/1200_0a78cf44c4285026a4c.playlist.m3u8"
}
```
