# PPT动画转码服务接入文档

## 1. 功能简介

腾讯云PPT动画转码服务为您提供 `.ppt`、`.pptx` 文件转码为 `HTML5`
页面的能力，转码得到HTML5页面可高度还原PPT动画特效，结合[互动白板接口文档](SDK文档/互动白板接口文档.md)，为您提供和线下教育体验高度一致的在线教育服务。

## 2. 服务开通

若您能还没开通PPT动画转码服务，请按照[购买指南](../购买指南.md)发送邮件申请开通。

## 3. 服务接入

### 3.1 基本流程

PPT动画转码服务接入有两种方式，一种为主动轮询（较适用于客户端发起转码请求），一种为注册CGI接口回调（较适用于服务端发起转码请求）。两种接入方式的基本使用流程如图所示：

#### 主动轮询

![主动轮询](https://main.qcloudimg.com/raw/2aec841a20d1f729bae2040659091dd8/PPT%E8%BD%AC%E7%A0%81%E4%B8%BB%E5%8A%A8.png)

#### 注册CGI接口回调

![注册CGI回调](https://main.qcloudimg.com/raw/35b6b5b8654a0af6ea1834c6789de965/PPT%E8%BD%AC%E7%A0%81CGI.png)

### 3.2 鉴权签名算法

所有转码请求调用都需要带上签名以便服务器鉴权，签名算法如下：

```
sign = md5(TicKey+expire_time)
```

| 参数名      | 描述                             |
|:------------|:---------------------------------|
| TicKey      | 2.1中获取的密钥 TicKey           |
| expire_time | Unix时间戳，单位秒，签名过期时间 |

> 签名举例：
> 1. 当前时间戳是 `1548247717`
> 2. 签名有效时间是 `120` 秒，则过期时间戳是 `expire_time =
>    1548247717+120=1548247837`
> 3. `tic_key = 9016607A382749C69D4F4B00C61DD083`
> 4. 计算签名：`sign =
>    md5(9016607A382749C69D4F4B00C61DD0831548247837)=5400bac77ba6467a8f8ac056f1769f45`
> 5. 在使用的接口的JSON请求参数中，带上`expire_time`字段，值为`1548247837`

GoLang代码示例：

```go

func CalculateSign(ticKey string, expireTime int) string {
    // 获取签名过期时间为当前时间加上签名有效期
    // TicKey为邮件中的回复的32位TicKey，expireTime是当前签名过期时间的Unix时间戳（单位秒）
    
    // 拼接TicKey与过期时间
    hashString := fmt.Sprintf("%v%v", ticKey, expireTime)
    // 计算拼接后字符串的MD5获得签名
    return GetMD5Hash([]byte(hashString))
}

func GetMD5Hash(data []byte) string {
    checksum := md5.Sum(data)
    return fmt.Sprintf("%x", checksum)
}
```

## 4. 接口说明

### 4.1 上传PPT并获取链接

发起转码时需要提供待转码PPT的下载链接，转码服务将在PPT下载完成后开始转码。您可以选择使用腾讯云对象存储上传PPT并获取下载链接，也可以使用您自己的文件服务器，有以下几点需要注意：

1. 目前仅支持`ppt/pptx`文件转换为`HTML5`页面，因此下载URL中需包含`.ppt/.pptx`后缀
2. 目前请支持包含`http://`或`https://`前缀的URL
3. 请检查URL的访问权限，保证PPT转码服务能正常访问并下载该PPT原文件。如果您使用腾讯云对象存储（Cloud Object Storage，COS），请检查存储桶的访问权限为**公有读私有写**。您可以在腾讯云控制台设置存储桶的访问权限，具体操作参考文档
   [设置访问权限](https://cloud.tencent.com/document/product/436/13315)
4. 如果您使用其他的文件存储服务，请注意文件存储服务的上传带宽，PPT转码服务提供**1分钟**的下载时间，如果下载不成功本次的转码请求将以失败终止
5. 目前支持PPT页数最大为500页，如有特殊需求，请发送邮件到`ticsupport@qq.com`单独申请

### 4.2 请求PPT转码

##### 接口说明

发布一个PPT转码任务

| 请求基本信息 | 描述                                            |
|:-----------|:-----------------------------------------------|
| 方法        | POST                                           |
| 请求URL     | https://iclass.api.qcloud.com/ppt2h5/v1/create |
| 请求Header  | Content-Type:application/json                  |

##### 请求参数

URL参数

| 参数名   | 描述                                              |
|:---------|:--------------------------------------------------|
| sdkappid | 客户的sdkappid                                    |
| sign     | 用于鉴权的签名                                    |
| random   | 随机int32正整数，每次请求都需要带上，用于定位问题 |

Body参数（json格式）

| 参数名       | 类型    | 描述                                                                       |
|:------------|:-------|:--------------------------------------------------------------------------|
| expire_time | int    | 签名的过期时间                                                              |
| url         | string | 4.1中获取的PPT下载URL，需要以`.ppt`或`.pptx`为文件名后缀，同时请检查URL的访问权限  |

请求示例：
> 请将参数替换为实际值

```
请求URL：https://iclass.api.qcloud.com/ppt2h5/v1/create?random=526919&sdkappid=1400127115&sign=d33bfea49d7f2795a4829c0d80047a7d
请求Header："Content-Type:application/json"
请求包体：
{
    "expire_time":1557202745,
    "url": "http://e4fb-edu-1400127115-1257240643.cos.ap-shanghai.myqcloud.com/语文课.ppt"
}
```

> 如果转码过程中出现PPT下载失败相关的错误，请检查URL的访问权限，或者联系客服人员并提供task_id方便进行排查

##### 接口返回参数

返回参数（json格式）

| 参数名     | 类型   | 描述                                       |
|:-----------|:-------|:-------------------------------------------|
| error_code | int    | 错误码                                     |
| error_msg  | string | 错误信息                                   |
| task_id    | string | 任务的唯一标识ID，用于查询该转码任务的进度 |

返回示例：

```json
{
    "error_code": 0,
    "error_msg": "ok",
    "task_id": "g68cee8e90jcq4ogg8jb"
}
```

### 4.3 查询转码任务进度

##### 接口说明

| 请求基本信息 | 描述                                          |
|:-------------|:----------------------------------------------|
| 方法         | POST                                          |
| 请求URL      | https://iclass.api.qcloud.com/ppt2h5/v1/query |
| 请求Header   | Content-Type:application/json                 |


##### 请求参数

URL参数

| 参数名   | 描述                                                                    |
|:---------|:------------------------------------------------------------------------|
| sdkappid | 客户的sdkappid                                                          |
| sign     | 用于鉴权的签名                                                          |
| random   | 随机int32正整数，每次请求都需要带上，定位问题时需要提供该次请求的random |

Body参数（json格式）

| 参数名      | 类型   | 描述                  |
|:------------|:-------|:----------------------|
| expire_time | int    | 签名的过期时间        |
| task_id     | string | PPT转码任务的唯一标识 |

请求示例：
> 请将参数替换为实际值

```
请求URL：https://iclass.api.qcloud.com/ppt2h5/v1/query?random=526919&sdkappid=1400127115&sign=d33bfea49d7f2795a4829c0d80047a7d
请求Header："Content-Type:application/json"
请求包体：
{
    "expire_time":1557202745,
    "task_id": "g68cee8e90jcq4ogg8jb"
}
```

##### 接口返回参数

返回参数（json格式）

| 参数名      | 类型    | 描述                    |
|:-----------|:-------|:-----------------------|
| error_code | int    | 错误码                  |
| error_msg  | string | 错误信息                 |
| task_id    | string | 任务的唯一标识ID          |
| status     | string | 任务状态                 |
| progress   | int    | 0-100的整数表示转码当前进度 |
| h5_url     | string | 转码完成后H5的URL         |
| resolution | string | PPT的分辨率              |
| pages      | int    | PPT的总页数              |
| title      | string | PPT的文件名              |

返回示例：

```json
{
    "error_code": 0,
    "error_msg": "ok",
    "task_id": "g68cee8e90jcq4ogg8jb",
    "status": "processing",
    "progress": 62,
    "h5_url": "https://test04-1257240443.cos.ap-shanghai.myqcloud.com/05iftk0sb6b26k5uv7jb/index.html",
    "resolution": "1024x768",
    "pages": 20,
    "title": "test20-pages.pptx"
}
```

1. 转码任务可能的状态有

| status     | 描述             |
|:-----------|:-----------------|
| queued     | 正在排队等待转换 |
| processing | 转换中           |
| finished   | 转换完成         |

1. PPT转码服务需要耗时较长，因此转码任务可能需要短时间排队执行

### 4.4 设置转码服务回调地址

##### 接口说明

| 请求基本信息 | 描述                                             |
|:-------------|:-------------------------------------------------|
| 方法         | POST                                             |
| 请求URL      | https://iclass.api.qcloud.com/ppt2h5/v1/callback |
| 请求Header   | Content-Type:application/json                    |


##### 请求参数

URL参数

| 参数名   | 描述                                                                    |
|:---------|:------------------------------------------------------------------------|
| sdkappid | 客户的sdkappid                                                          |
| sign     | 用于鉴权的签名                                                          |
| random   | 随机int32正整数，每次请求都需要带上，定位问题时需要提供该次请求的random |

Body参数（json格式）

| 参数名       | 类型    | 描述                                                                                                           |
|:------------|:-------|:--------------------------------------------------------------------------------------------------------------|
| expire_time | int    | 签名的过期时间                                                                                                  |
| callback    | string | PPT转码进度回调地址，如果传空字符串会删除原来的回调地址配置，回调地址仅支持http或https协议，即回调地址以`http://`或`https://`开头 |

请求示例：
> 请将参数替换为实际值

```
请求URL：https://iclass.api.qcloud.com/ppt2h5/v1/callback?random=526919&sdkappid=1400127115&sign=d33bfea49d7f2795a4829c0d80047a7d
请求Header："Content-Type:application/json"
请求包体：
{
    "expire_time":1557202745,
    "callback": "https://iclass.api.qcloud.com/task/callback"
}
```

##### 接口返回参数

返回参数（json格式）

| 参数名     | 类型   | 描述     |
|:-----------|:-------|:---------|
| error_code | int    | 错误码   |
| error_msg  | string | 错误信息 |


返回示例：

```json
{
    "error_code": 0,
    "error_msg": "ok"
}
```

### 4.5 转码进度回调格式

##### 接口说明

如果您的业务服务器设置了回调地址，当转码任务进度有更新时，转码服务会主动往回调地址发送任务的转换进度

- 业务服务器需对签名做校验，判断是否为有效请求
- 业务服务器必须回包`{"error_code":
  0}`，否则，转码服务认为回调发送失败后进行重试，每分钟重试1次，最大重试10次


| 请求基本信息 | 描述                          |
|:-------------|:------------------------------|
| 方法         | POST                          |
| 请求Header   | Content-Type:application/json |


##### 回调请求参数

URL参数

| 参数名 | 描述                                                                    |
|:-------|:------------------------------------------------------------------------|
| sign   | 用于鉴权的签名，需对该签名做校验，判断是否为有效请求                    |
| random | 随机int32正整数，每次请求都需要带上，定位问题时需要提供该次请求的random |
| sdkappid | 客户的sdkappid                                                 |

Body参数（json格式）

| 参数名       | 类型    | 描述                             |
|:------------|:-------|:--------------------------------|
| expire_time | int    | 签名的过期时间                    |
| error_code  | int    | 错误码                           |
| error_msg   | string | 错误信息                         |
| timestamp   | int    | 回调发送的时间戳                   |
| task_id     | string | 任务的唯一标识ID                  |
| task_type   | string | PPT动画转码任务类型固定为`"ppt2h5"` |
| status      | string | 任务状态                         |
| progress    | int    | 0-100的整数表示转码当前进度         |
| h5_url      | string | 转码完成后H5的URL                 |
| resolution  | string | PPT的分辨率                      |
| title       | string | PPT的文件名                      |
| pages       | int    | PPT的总页数                      |

回调示例：

```
回调URL：https://业务后台URL?random=526919&sign=d33bfea49d7f2795a4829c0d80047a7d&sdkappid=1400127140
回调Body：
{
    "error_code":0,
    "error_msg":"",
    "expire_time":1554246423,
    "timestamp": 1553245423,
    "task_id": "9m4e2mr0ui3e8a215n4g",
    "task_type": "ppt2h5",
    "status":"processing",
    "progress": 10,
    "h5_url":"http://xxxxx/index.html",
    "resolution": "1024x768",
    "title": "test.ppt",
    "pages": 100
}
```

##### 回调地址返回参数

返回示例：

```json
{"error_code": 0}
```

## 5. 后台错误码

#### PPT转码过程错误码

| 错误码 | 错误描述                              | 解决方法                                                 |
|:-------|:--------------------------------------|:---------------------------------------------------------|
| -1     | ppt 下载的url格式错误                 | 请检查PPT下载URL                                         |
| -2     | ppt 打开过程中发生未知错误            | 请检查PPT格式是否正确                                    |
| -3     | ppt打开超时                           | 请检查PPT格式是否正确                                    |
| -4     | ppt 打开无响应                        | 请检查PPT格式是否正确                                    |
| -5     | ppt 文件被加密                        | 不支持转换已加密的PPT                                    |
| -6     | 未知ppt格式                           | 请检查PPT格式是否正确                                    |
| -7     | ppt 打开时发生异常                    | 请检查PPT格式是否正确                                    |
| -8     | ppt 为只读格式                        | 不支持只读ppt，请检查PPT格式是否正确                     |
| -9     | ppt 转码失败                          | 请检查PPT格式是否正确                                    |
| -10    | pptx 格式解析错误                     | 请检查PPT格式是否正确                                    |
| -11    | ppt 下载失败，未知错误                | 请检查PPT下载URL是否有效                                 |
| -12    | h5 上传失败                           | 请联系客服人员或重试                                     |
| -13    | ppt 转换服务未加载                    | 请联系客服人员                                           |
| -14    | ppt 转码过程中，发生错误              | 某些元素不支持转码，请检查PPT格式是否正确                |
| -15    | ppt 转码文件生成失败                  | 请联系客服人员或重试                                     |
| -16    | ppt 转换模式异常                      | ppt格式不支持或联系客服人员                              |
| -17    | ppt 超过最大的转换页数限制(目前为500) | 不支持转换超过500页的PPT                                 |
| -18    | ppt 转换失败，错误未知                | ppt格式不支持或联系客服人员                              |
| -19    | ppt 被加密                            | 不支持加密的PPT                                          |
| -20    | ppt 未知属性错误                      | 请检查PPT格式是否正确                                    |
| -21    | ppt 检测属性超时                      | 请检查PPT格式是否正确                                    |
| -22    | ppt 转换异常                          | 请检查PPT格式是否正确或重试                              |
| -23    | ppt 下载链接含有非法字符              | 请检查ppt下载链接是否正确                                |
| -24    | ppt 下载链接打开失败                  | 请检查ppt下载地址是否有效                                |
| -25    | ppt 下载链接打开超时                  | 请检查ppt下载链接是否有效 或 下载服务器网络状况          |
| -26    | ppt 下载数据失败                      | 请检查ppt下载服务器网络状况                              |
| -27    | ppt 下载数据超时                      | 请检查ppt下载服务器网络状况 或 是否ppt过大，导致下载超时 |

#### 请求错误码

| 错误码 | 错误描述              | 解决方法                                                       |
|:------|:---------------------|:-------------------------------------------------------------|
| 20000 | 客户未开通服务         | 请参考`2. 服务开通`中流程发送邮件申请开通PPT转码服务                 |
| 20001 | 签名已过期             | 检查请求JSON中的expire_time签名时间，更新过期时间后重新生成签名字符串 |
| 20002 | 签名校验失败           | 检查TicKey与签名算法是否正确                                     |
| 20003 | 参数解析失败           | 根据error_msg查询具体的请求参数异常信息，更正参数缺失/类型错误等      |
| 20004 | 设置回调地址格式错误    | 检查回调地址是否正确                                             |
| 20005 | 数据读取失败           | 请检查请求中的TaskId或联系客服人员                                |
| 20099 | 转码服务内部错误        | 请联系客服人员                                                  |


## 6. ppt演示文稿课件格式建议

1. 建议使用 Microsoft Office 2007或以上版本(wps 和 keynote都有一定的兼容性问题)
2. 请勿使用不支持的四种ppt动效，包括：1:"Bold Flash" 2:"Underline 3:"Grow With Color" 4:"Bold Reveal"
3. 请勿插入flash动画，不支持flash动画播放
4. 如果使用wps，请注意不支持 WPS ppt 中的音视频元素
5. 如果使用keynote，请注意插入的音频播放标签，无法展示
6. 建议使用操作系统默认的中英文字体，请勿使用自己安装的字体，否则可能会出现转码失败 或者 转码h5格式异常 [查看转码服务器支持字体](./SDK文档/PPT转h5支持字体列表.md)
7. ppt页数不要过多，页数越多，转换速度越慢（目前最大支持500页转码）
8. ppt中如果带有音视频，体积尽量小，否则会影响转换速度和转换后的h5加载速度

## 7. 常见问题
1. ppt 转 h5后，出现某些字体错位，或大小不一致，如何处理？  
问题原因：该问题一般是因为 ppt中使用了转码服务器不支持的字体库导致的 [查看转码服务器支持字体](./SDK文档/PPT转h5支持字体列表.md)  
解决方法（两个方法）：  
方法一：
去掉或更改字体为服务器支持的字体库  
操作指引：
打开ppt-->选择不支持字体的文字-->切换到服务器支持的字体  
方法二：
ppt保存时，将字体库一起打包进ppt  
操作指引：
打开ppt-->选择“文件”-->"选项"-->"保存"-->勾选"将字体嵌入文件"-->
选择"仅嵌入演示文稿中使用的字符(适于减小文件大小)"-->点击“确定”
-->保存ppt，看到PowerPoint的底部状态栏，显示“正在嵌入字体”就可以了
![保存字体](https://main.qcloudimg.com/raw/749786466e29a0afb8db26af51aded6e/powerpoint%E4%BF%9D%E5%AD%98%E5%AD%97%E4%BD%93-%E8%8C%83%E4%BE%8B.png)

2. 为什么有些ppt动效，转换为h5后，丢失了呢？  
问题原因：ppt中使用了不支持转换的动效；包括：1:"Bold Flash" 2:"Underline 3:"Grow With Color" 4:"Bold Reveal"  
解决方法：去掉不支持的特效 或者 使用其他特效替换

3. 为什么有些ppt或pptx文件，本地 PowerPoint 预览正常；但是转码时，服务器返回错误“ppt may contain unsupported elements”？  
问题原因：ppt的内容中含有一些不支持转码h5的元素，所以导致转码失败  
解决方法：
如果是 pptx 格式文件，可以用 powerpoint 另存为 ppt 格式，然后重新尝试转码
如果是 ppt 格式文件，可以用 powerpoint 另存为 pptx 格式，然后重新尝试转码
