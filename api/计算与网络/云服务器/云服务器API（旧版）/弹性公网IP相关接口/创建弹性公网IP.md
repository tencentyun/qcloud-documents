>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: CreateEip

* 创建弹性公网IP（EIP），弹性公网 IP是专为动态云计算设计的静态IP地址。借助弹性公网IP，您可以快速将EIP重新映射到您的另一个实例上，从而屏蔽实例故障。
您的弹性公网 IP 与腾讯云账户相关联，而不是与某个实例相关联，而且在您选择显式释放该地址，或欠费超过7天之前，它会一直与您的腾讯云账户保持关联。
* 平台对用户每地域能申请的EIP最大配额有所限制。可参见[EIP产品简介](/doc/product/213/1941)。上述配额可通过 [DescribeEipQuota](/doc/api/229/%E6%9F%A5%E8%AF%A2%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91IP%E9%85%8D%E9%A2%9D) API 获取。


## 2. 输入参数
 


| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
|goodsNum | 否 |Int | 单次申请数量（默认为1, 最大为5）


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
| data |   Array | 返回列表 |

Data结构


| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.eipIds | Array | 创建的EIP实例ID列表

## 4. 示例
 
输入

```
 https://eip.api.qcloud.com/v2/index.php?
 &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
```

输出

```

{
    "code": 0,
    "message": "",
    "data": {
        "eipIds": [
            "eip-m44ku5d2"
        ]
    }
}

```

