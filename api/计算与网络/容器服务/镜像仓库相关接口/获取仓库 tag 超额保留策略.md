>?当前页面接口为旧版 API，未来可能停止维护。容器服务 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [容器服务 API 3.0](https://cloud.tencent.com/document/api/457/31853)。
>
## 1. 接口描述
本接口 ( GetAutoDelStrategy ) 获取仓库 tag 超额保留策略。
接口请求域名：`ccr.api.qcloud.com`。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)。

| 参数名称 | 描述 |类型 | 必选  | 
|---------|---------|---------|---------
| reponame   | 仓库名字 | String |是 |


## 3. 输出参数
 
| 参数名称 | 描述 |类型 | 
|---------|---------|---------|
| code | 公共错误码。0 表示成功，其他值表示失败|Int | 
| codeDesc | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因|String |
| message |  模块错误信息描述，与接口相关|String |
| totalCount |  策略数目|Int |
| strategyInfo |  策略详情列表|Object Array|

策略信息字段：

| 参数名称 | 描述 |类型 
|---------|---------|------
| username   | 镜像仓库用户名 | String |
| reponame   | 仓库名字 | String |
| type   | 策略类型<br>keep\_last\_days：保留最近几天的数据<br>keep\_last\_nums：保留最近多少个数据 | String |
| value   | 策略值 | Int |
| valid   | 策略是否有效。1：有效，0：无效 | Int |
| creation_time   | 策略创建时间 | String |

## 4. 示例
输入

```
  https://domain/v2/index.php?Action=GetAutoDelStrategy
  &reponame=test/kube_test 
  &其它公共参数
```
输出

```
{
    "code": 0,
    "message": "", 
    "codeDesc": "Success",
    "data": {
        "strategyInfo": [
            {
                "username": "100001066666",
                "repo_name": "test/kube_test",
                "type": "keep_last_nums",
                "value": 10,
                "valid": 1,
                "creation_time": "2018-03-07T16:53:23+08:00"
            }
        ],
        "totalCount": 1
    }
}

```
