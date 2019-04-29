## 接口描述
本接口（InstallAgent）用于安装 agent。

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见公共请求参数。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---|---|---|---|
| Cluster | 是 | String | 集群名称。| 
| TiaVersion | 否 | String | TI-A Agent 版本。|

## 输出参数
| 参数名称 | 类型 | 描述 |
|---|---|---|
| TiaVersion | String | TI-A Agent 版本。 |
| RequestId | String | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。|

## 错误码
| 错误码 | 描述 |
|---|---|
| FailedOperation.AlreadyExists | 资源已存在。|
| InternalError | 内部错误。|
| InvalidParameter | 参数错误。|
| UnauthorizedOperation | 未授权操作。|
| UnsupportedOperation.UnsupportedVersion | 集群版本过低。|

## 示例
>**注意：**
>只有未安装过 agent 或者 kubeflow 相关组件的集群需要安装。

#### 输入：
```
 https://tia.tencentcloudapi.com/?Action=InstallAgent
&Cluster=cls-xxxxxxxx
&TiaVersion=xxxx-xx-xx
&<公共请求参数>

```
#### 输出：
```
 {
  "Response": {
    "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  }
}
```
