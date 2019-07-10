>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述


本接口 (BindInstanceKey) 用于将密钥绑定到CVM实例上。
接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>


* 系统将密钥的公钥写入到实例的SSH配置当中，用户就可以通过这个密钥的私钥登录CVM了。
* 如果实例原来绑定过密钥，那么原来的密钥将失效。
* 如果实例原来是通过密码登录，绑定密钥后无法使用密码登录。
* 只有已关机状态的子机才能绑定密钥。
* **<font color="red">注意：Windows无法绑定密钥。</font>**
 

## 2. 输入参数


以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。
 
| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| instanceIds.n  | 是 | String | 实例ID（此接口支持同时传入多个ID。此参数的具体格式可参考API[简介](https://cloud.tencent.com/doc/api/229/568)的`id.n`一节）。|
| keyId  | 是 | String | 密钥ID。|


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|





## 4. 示例

输入
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=BindInstanceKey
  &instanceIds.0=ins-xxxxx
  &instanceIds.1=ins-xxxxx
  &keyId=skey-xxxxx
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```
{
    "code": 0,
    "message": ""
}

```





