>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口 (ResizeInstanceHour) 用于调整指定实例的配置，包括CPU、内存、数据盘。

接口请求域名：<font style="color:red">cvm.api.qcloud.com</font>

* 只能对预付费用户的按量计费实例进行调整，如需调整包年包月实例可以使用 [ResizeInstance](https://cloud.tencent.com/doc/api/229/1306) API。
* 只能对已关机的实例进行配置升级操作。
* 只支持拥有云硬盘系统的实例升级。
* 不支持正在挂载弹性云硬盘的实例。
* 暂不支持降级。



## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](/document/api/213/6976)页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| instanceId | 是 | String | 待操作的实例ID。可通过 [DescribeInstances](/doc/api/229/831) API返回值中的 unInstanceId 获取。
| cpu| 否| Int| 升级后的实例核数。CPU与内存具体的配比限制参见[CVM实例配置](/document/product/213/2177)。|
| mem| 否| Int| 升级后的实例内存大小(GB)。CPU与内存具体的配比限制参见[CVM实例配置](/document/product/213/2177)。|
| storageSize| 是| Int| 数据盘大小（GB）。最小调整步长为10G，此参数默认值为0，表示不购买数据盘。其所分配数据盘的类型与创建实例时 `storageType` 所指定的一致，无法更改。关于不同类型数据盘的特性与容量限制请参考[硬盘产品简介](/doc/product/213/498)。|


## 3. 输出参数
 
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
 
 

## 4. 示例
 
输入

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=ResizeInstanceHour
  &instanceId=qcvm8e7bf56c115c53ce2d2a1ac2ea6e657a
  &mem=2
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出

```
{
    "code": 0,
    "message": "ok"
}
```





