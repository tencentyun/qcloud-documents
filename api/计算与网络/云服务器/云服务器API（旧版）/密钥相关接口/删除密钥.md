>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 

本接口 (DeleteKeyPair) 用于删除已在腾讯云托管的密钥。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 可以同时删除多个密钥。
* 不能删除已被实例或镜像引用的密钥；由于这个原因，可能不是全部密钥都会成功删除，需要独立判断。
 
## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|keyIds.n | 是 | String | 密钥ID（此接口支持同时传入多个ID。此参数的具体格式可参考API[简介](https://cloud.tencent.com/doc/api/229/568)的`id.n`一节）。|

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
| deleteKeySet |  Array | 密钥删除结果。因为某个密钥已被绑定等原因，可能不是全部密钥都会成功删除，需要独立判断。 |

其中deleteKeySet包含多个已删除密钥的信息，每个信息的详细数据结构如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| keyId |   String | 密钥ID。 |
| message |  String | 删除后返回的信息。 |
| code |   Int | 结果代码。0为成功。 |

## 4. 示例
 
输入

```
  https://cvm.api.qcloud.com/v2/index.php?Action=DeleteKeyPair
  &keyIds.0=skey-mv9yzyjj
  &<公共请求参数>
```

输出

```
{
    "codeDesc": "Success",
    "message": "",
    "code": 0,
    "detail": {
        "deleteKeySet": [
            {
                "code": 0,
                "message": "success",
                "keyId": "skey-mv9yzyjj"
            }
        ]
    }
}
```





