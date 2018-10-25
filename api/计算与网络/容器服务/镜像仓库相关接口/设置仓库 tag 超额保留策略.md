## 1. 接口描述
本接口 ( SetAutoDelStrategy ) 用于设置仓库 tag 超额保留策略，当 tag 配额达到限制时自动清理 tag。
接口请求域名：`ccr.api.qcloud.com`。

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/doc/api/457/9463)。

| 参数名称 | 描述 |类型 | 必选  | 
|---------|---------|---------|---------
| reponame   | 仓库名字 | String |是 |
| type   | 策略类型<br>keep\_last\_days：保留最近几天的数据<br>keep\_last\_nums：保留最近多少个数据 | String |是 |
| val   | 策略值 | Int |是 |


## 3. 输出参数
 
| 参数名称 | 描述 |类型 | 
|---------|---------|---------|
| code | 公共错误码。0 表示成功，其他值表示失败|Int | 
| codeDesc | 业务侧错误码。成功时返回 Success，错误时返回具体业务错误原因|String |
| message |  模块错误信息描述，与接口相关|String |

## 4. 示例
输入

```
  https://domain/v2/index.php?Action=SetAutoDelStrategy
  &reponame=test/kube_test
  &type=keep_last_nums
  &val=10 
  &其它公共参数
```
输出

```
{
    "code": 0,
    "message": "", 
    "codeDesc": "Success"
}

```
