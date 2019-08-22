>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口（DeleteSecurityGroupPolicy）用于删除安全组规则。
接口请求域名：<font style="color:red">dfw.api.qcloud.com</font>


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段为 DeleteSecurityGroupPolicy。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| sgId | 是 | String | 安全组 ID。 |
| version | 否 | Int | 用于指定要操作的安全组的版本。版本，即用户每次更新安全规则版本会自动加 1。入参此 version 若不是最新的，将帮您使操作失败以防止您想要更新的路由规则已过期（如规则位置已变动）；若不传 version 则需要您自己注意确认好此次删除的规则在您传入的 indexes 位置。建议用户使用本参数，防止待删除的规则的 indexes 在调用本规则之前发生变化。 |
| direction | 是 | String | 规则方向(ingress/egress)。 |
| indexes | 是 | Array | 规则所在位置，支持删除多条。 |

 

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码, 0 表示成功，其他值表示失败。详见错误码页面的 <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|
 
 ## 4. 错误码表
 
| 错误码 | 描述 |
|---------|---------|
| 7000 | 安全组后台异常 |


## 5. 示例
 
输入
<pre>

  https://vpc.api.qcloud.com/v2/index.php?Action=DeleteSecurityGroupPolicy
	&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
 &sgId=sg-8pmkv2xx&version=2&direction=ingress&indexes.0=0
</pre>

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}

```

