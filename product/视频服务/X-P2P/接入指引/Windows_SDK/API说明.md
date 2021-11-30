
SDK 接口除初始化接口，其余接口均由 HTTP 实现，请求格式为：
```
http:://${host}:${port}/${func}?${param}
```
其中 `http://${host}:${port}` 为本地代理服务器（即 `XP2PService::host()`）。

## 统计
### 接口描述
- 描述：请求对应频道的统计数据
- 方法：GET
- 路径：`/stat?xresid=${yourUrl}`

### 请求参数

| 参数名称 | 必选 | 类型   | 说明   |
| -------- | -------- | -------- | -------- |
| xresid   | 是   | string | 默认为 URL 中的 resource，如果有 xresid，则用 xresid，否则为频道的 encode url |

### 返回参数
| 返回码 | 说明                 |
| ------ | -------------------- |
| [200](#code_200)    | 查询成功             |
| 404    | 查询失败，频道不存在 |

其中，返回码 200 返回的 JSON 内容，格式详细说明如下：[](id:code_200) 

| 参数名称     | 类型 | 说明            |
| ------------- | ---- | --------------- |
| flow.p2pBytes | num  | 对应频道 P2P 流量 |
| flow.cdnBytes | num  | 对应频道 CDN 流量 |

### 示例
- **请求示例：**
```
http://127.0.0.1:16080/live.p2p.com/stat?xresid=${yourURL}
```
>? xresid 即 `http://127.0.0.1:16080/live.p2p.com/resoruce.ext` 中的 resource。
- **返回示例：**
``` json
    "{"flow":{"p2pBytes":0,"cdnBytes":0}}"
```

## 设置上下行
### 接口描述
- 描述：请求设置 P2P 上行与下行，0为开启，1为关闭
- 方法：GET
- 路径：`/feature?download=${0or1}&upload=${0or1}`

### 请求参数

| 参数名称 | 必选 | 类型 | 说明                     |
| -------- | ---- | ---- | ------------------------ |
| download | 是   | num  | 0为关闭；1为开启（默认值） |
| upload   | 是   | num  | 0为关闭；1为开启（默认值 |

### 返回参数
返回的 JSON 内容，格式说明如下：

| 参数名称 | 必选 | 类型   | 说明                        |
| -------- | ---- | ------ | --------------------------- |
| ret      | 是   | num    | 0为正常                   |
| msg      | 是   | string | 相关信息, 调试使用          |
| upload   | 是   | bool   | true 为开启，false 为关闭 |
| download | 是   | bool   | true 为开启，false 为关闭 |
  
### 示例
- **请求示例：**
```
http://127.0.0.1:16080/live.p2p.com/feature?download=1&upload=0
```
>?  一般情况下移动网络可以关闭上传。
- **返回示例：**
```json
    "{"ret":0, "msg":"ok", "download":0,"upload":0}}"
```


