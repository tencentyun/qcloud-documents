## 接口说明
**请求方式**：POST。
**调用频率限制**：200次/小时。
 
```plaintext
服务地址v3/toolbox/getPushListByToken
```
接口服务地址与服务接入点一一对应，请选择与您的应用服务接入点对应的 [服务地址](https://cloud.tencent.com/document/product/548/49157)。

**接口功能**：查询应用某个 Token 一天的推送数据。

## 参数说明
#### 请求参数

| 参数名称  | 必选 | 类型   | 描述                                                         |
| --------- | ---- | ------ | ------------------------------------------------------------ |
| token | 是   | String | 设备 Token |

#### 应答参数

| 参数名称                  | 类型      | 描述                                                |
| ------------------------- | --------- | --------------------------------------------------- |
| retCode                   | Integer       | 返回状态码                                         |
| errMsg                    | String    | 错误信息                                            |
| pushTaskList | pushTask  | 推送参数 |

#### pushTask

| 参数名称 | 类型   | 说明           |
| -------- | ------ | -------------- |
| pushId     | Integer |  推送任务 id       |
| pushTime   | Integer    | 推送时间戳     |
| pushTargetType    | Array    | 推送类型   |


## 示例说明
#### 请求示例
    
```json
{
   "token":"05a305f6b71abb3a6b8c759fd1bc56b4bb44"
}
```
#### 应答示例
```json
{
   "retCode": 0,
    "errMsg": "NO_ERROR",
    "pushTaskList": [
        {
            "pushId": 589840563,
            "pushTime": 1651662600,
            "pushTargetType": "TAG_PUSH"
        },
        {
            "pushId": 590166744,
            "pushTime": 1651741604,
            "pushTargetType": "TAG_PUSH"
        },
        {
            "pushId": 590178525,
            "pushTime": 1651742807,
            "pushTargetType": "TAG_PUSH"
        },
        {
            "pushId": 590179538,
            "pushTime": 1651742914,
            "pushTargetType": "TAG_PUSH"
        },
        {
            "pushId": 590179672,
            "pushTime": 1651742928,
            "pushTargetType": "TAG_PUSH"
        },
        {
            "pushId": 590235722,
            "pushTime": 1651750200,
            "pushTargetType": "TAG_PUSH"
        }
        ]
}
```
