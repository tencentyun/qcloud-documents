您可通过拖拽组合多功能 IVR 模块完成较复杂呼入流程的搭建。

## 转外线模块
该模块用于将来电转接到外部电话。

| 关键参数      | 说明                                 | 示例           |
| --------- | ---------------------------------- | ------------ |
| 标签        | 可自定义该模块的名称                         | 转外线          |
| 转接外线过程中放音 | 转接外线过程中的等待音乐。                      | 可选择系统预置的等待音  |
| 转外线主叫号码   | 转外线时外呼使用的号码，下拉菜单中展示的为系统所有的可外呼号码列表。 | 020-6624XXXX |
| 转外线被叫号码   | 转外线时需要转接的外部号码                      | 010-7654XXXX |

![](https://qcloudimg.tencent-cloud.cn/raw/577f6f6beb513453c36c7f862026ab98.png)

## 收号模块
收号模块通过语音播报引导用户输入按键信息（DTMF)，用户输入信息将被存储在设定的变量名中。
![](https://qcloudimg.tencent-cloud.cn/raw/f4ad950403933b06ccd2c8727e808936.png)
收号节点一般后面需要连接一个接口调用模块，将收号变量通过入参形式给到第三方系统接口，做业务处理，再将结果通过出参形式注入到 IVR 后续的流程中，实现定制化的 IVR 需求。示例如下：
![](https://qcloudimg.tencent-cloud.cn/raw/4d1fe581f29ff9083900825d3cf69013.png)

## 接口调用模块
接口调用模块支持第三方系统通过配置 HTTP API 接口调用的模式，注入自定义业务参数到 IVR 流程中，IVR 流程中的其他模块节点可以使用这些业务参数。
![](https://qcloudimg.tencent-cloud.cn/raw/46b32c62176fcd68af8cf9174cd3e1f2.png)
- **最大错误数**：接口调用失败后将重试，此配置调用接口允许失败的次数
- **超时时间**：每次调用接口的超时时间
- **默认值**：在接口调用失败时，变量会被赋予默认值
>?调用接口均失败的情况，系统会自动保底走到下一跳节点。
>
- **接口请求地址**：任意支持公网访问的客户URL
- **METHOD**: POST
- **Content-Type**: `application/json;charset=utf-8`

request：

| 参数    | 类型  | 说明            |
| ----- | --- | ------------- |
| 请求参数1 | 字符串 | ivr配置中指定的请求参数 |
| ...   |     |               |

可支持的系统参数：

| 参数                    | 类型  | 说明   |
| --------------------- | --- | ---- |
| ${SystemCallerNumber} | 字符串 | 主叫号码 |
| ${SystemCalleeNumber} | 字符串 | 被叫号码 |
| ${SystemSessionId}    | 字符串 | 会话ID |

response：

| 参数    | 类型  | 说明            |
| ----- | --- | ------------- |
| 返回参数1 | 字符串 | ivr配置中指定的返回参数 |
| ...   |     |               |

示例：
``` 
https://www.customurl.com/fetchVariables
请求
{
    "Callee":"008618621500000"
}

返回
{
    "Score":"95"
}
```


## 条件判断模块
该模块通过配置添加各个条件分支，可以结合系统参数以及传参模块中注入的业务参数进行逻辑路由。条件分支支持的运算语法包括判断：等于、不等于、大于、小于、大于等于、小于等于、与。
**默认分支**：是一种特殊的分支，提供保底的功能，在所有分支逻辑判断都失败的情况下，系统将走到默认分支。
 1. 通过传参模块，调用第三方接口传入主叫号码，获取分数参数值。
 2. 条件判断模块，将分数分为4个不同等级，分别走4个不同分支。

示例如下：
![](https://qcloudimg.tencent-cloud.cn/raw/a57a4c38e83df73a7280b28a8c37bc2e.png)
![](https://qcloudimg.tencent-cloud.cn/raw/a108f259210bb1d3065d8e62cf6b4231.png)
![](https://qcloudimg.tencent-cloud.cn/raw/3031990a2dc862cd3142375c53ce46d2.png)

## 放音模块（动态播报）
放音模块可以通过 ${variable} 的形式，使系统播报动态传入的第三放参数。
>?如果文本中涉及阿拉伯数字播报，建议通过汉字形式，如：“按一转咨询，按二转销售”。
>
![](https://qcloudimg.tencent-cloud.cn/raw/4bc4c58862d9aad10af9111393919086.png)

## 转人工模块（获取指定坐席列表）
URL：`https://{custom_url}?action=specifiedSeat&version=1`
METHOD: POST
Content-Type: `application/json;charset=utf8`
REQUEST：

| 参数          | 类型  | 说明              |
| ----------- | --- | --------------- |
| RequestId   | 字符串 | 请求序号            |
| Timestamp   | 数值  | Unix 秒级时间戳      |
| SdkAppId    | 数值  | 呼叫中心实例ID        |
| SessionType | 字符串 | 会话类型，目前只有 "tel" |
| User        | 字符串 | 用户号码（带0086前缀）   |

RESPONSE：

| 参数         | 类型    | 说明       |
| ---------- | ----- | -------- |
| RequestId  | 字符串   | 请求序号     |
| ErrMsg     | 字符串   | 错误说明     |
| ErrCode    | 数值    | 错误码      |
| SeatEmails | 字符串数组 | 指定坐席列表   |
| SkillGroup | 数值    | 指定技能组 ID |

## 分支模块（启用动态分支）
IVR 中分支节点支持动态分支功能，业务方可以通过第三方传参的形式自行构建动态分支结构。将动态分支选项设为启用，动态分支参数选择为 IVR 流程之前传参模块传入的第三方业务参数。动态分支参数的格式见下。
>!传参模块中对应传入的 json 数组格式的参数需要转为 string 字符串。
>
动态分支参数：

| 参数     | 类型  | 说明                         |
| ------ | --- | -------------------------- |
| digits | 字符串 | 分支对应的按键信息，取值：0-9、#、\*      |
| name   | 字符串 | 分支唯一ID，建议用GUID唯一标识一个分支     |
| lable  | 字符串 | 分支的中文描述（会和按键信息一起体现在话单中）    |
| next   | 字符串 | 下一跳节点名称（可点击需跳转的节点，标题栏上可获取） |

![](https://qcloudimg.tencent-cloud.cn/raw/c778347c92f2506ccd7e98642884b374.png)

示例：
![](https://qcloudimg.tencent-cloud.cn/raw/064a901343baf8eb99ccebd4c2367952.png)

```
https://www.customurl.com/fetchVariables
请求
{
    "Callee":"008618621500000"
}

返回
{
    "tts":"按一转咨询，按二转购买",
    "dynamicEntries":"[{
        	\"digits\": \"1\",
        	\"next\": \"01FN8J6WZ984WR9PP4ZZTC8YXS\",
        	\"label\": \"咨询\",
        	\"name\": \"120b5ad2-6b6e-49e8-ade7-d952e7de6f32\"
        },
        {
        	\"digits\": \"2\",
        	\"next\": \"01FN8J92EH5HP4SBS5W4MXZD0J\",
        	\"label\": \"购买\",
        	\"name\": \"4ac833b5-9019-4ba9-8c5a-a11fb893dca2\"
        }]"
}
```
## 转分机
前提条件：完成 [SIP 话机注册](https://cloud.tencent.com/document/product/679/79223)。
该模块中，输入目标座席的 SIP 话机分机号即可转接。
![](https://qcloudimg.tencent-cloud.cn/raw/7aa6bc1d8b4dc48cb8987dc2eca7ab44.png)
同一个转分机模块仅支持转**同一长度**的分机号，您需要在此进行设置：
![](https://qcloudimg.tencent-cloud.cn/raw/4e2ebdd12e21ce3441d1dda3c6c60c00.png)
