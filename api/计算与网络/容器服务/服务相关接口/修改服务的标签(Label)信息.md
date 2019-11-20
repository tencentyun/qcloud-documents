>?当前页面接口为旧版 API，未来可能停止维护。容器服务 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [容器服务 API 3.0](https://cloud.tencent.com/document/api/457/31853)。
>
## 接口描述
本接口（ModifyServiceLabels）用于修改服务的标签（Label）信息。

接口请求域名：
```
ccs.api.qcloud.com
```


## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)。

| 参数名称   | 描述                               | 类型     | 必选 |
|------------|------------------------------------|----------|------|
| clusterId   | 集群 ID，请填写 [查询集群列表](/doc/api/457/9448) 接口中返回的 clusterId 字段   | String   | 是   |
| serviceName | 服务名，服务名称由小写字母、数字和`-`组成，由小写字母开头，小写字母或数字结尾， 且长度不超过 63 个字符 | String   | 是   |
| namespace   | 命名空间，请填写 查询集群命名空间 接口中返回的 namespaces 字段，默认为 default   | String   | 否   |
| labels    | 服务标签（Label）信息，仅支持 k-v 模式，详情见示例（label 中 key 字段暂时不支持"."和"_"） | Array | 否 |

## 输出参数

| 参数名称 | 描述 |类型 |
|----------|------|-----|
| code |公共错误码。0 表示成功，其他值表示失败| Int |
| codeDesc | 业务错误码。成功时返回 Success，错误时返回具体业务错误原因|String |
| message | 模块错误信息描述，与接口相关|String |
| data | 修改标签服务信息的返回数据部分 |Object |

data 字段的结构如下

| 参数名称 | 描述 |类型 |
|---------|---------|---------|
| labels | 服务的标签信息 | Object |
| sysLabels | 系统自带的 Lables，例如 qcloud-app，无法修改 | Object |
| userLabels | 用户自定义 Lables，可修改 | Object |

## 示例
### 输入
```
  https://ccs.api.qcloud.com/v2/index.php?
  Action=ModifyServiceLabels
  &clusterId=cls-xxxxx
  &serviceName=d2048
  &namespace=default
  &labels.app=d2048
  &labels.application-label=d2048
  &labels.aaa=bbb
  &其他公共参数
```
### 输出
```
{
    "data": {
        "code": 0,
        "message": "",
        "codeDesc": "Success",
        "data": {
            "labels": {
                "aaa": "bbb",
                "qcloud-app": "d2048",
                "qcloud-application-label": "d2048"
            },
            "sysLabels": {
                "qcloud-app": "d2048",
                "qcloud-application-label": "d2048"
            },
            "userLabels": {
                "aaa": "bbb"
            }
        }
    },
    "message": "",
    "code": 0
}
```
