>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 

本接口 (ModifyKeyPair) 用于修改密钥名称。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 可以根据密钥ID修改密钥名称；密钥ID属于密钥的唯一标识，不可修改。

## 2. 输入参数


以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| keyId  | 是 | String | 用于指定密钥ID。
| keyName  | 是 | String | 修改后的密钥名称。只能包含数字，字母和下划线。

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|




 

## 4. 示例
 
输入

```
  https://cvm.api.qcloud.com/v2/index.php?Action=ModifyKeyPair
  &keyId=skey-mv9yzyjj
  &keyName=Tencent
  &<公共请求参数>

```

输出

```
{
    "codeDesc": "Success",
    "message": "",
    "code": 0,
    "data": []
}

```





