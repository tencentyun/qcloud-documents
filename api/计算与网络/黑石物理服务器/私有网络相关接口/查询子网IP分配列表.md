>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述 
 
本接口（DescribeBmSubnetIps）用于查询黑石VPC子网IP分配列表。

接口访问域名: bmvpc.api.qcloud.com


## 请求

### 请求示例

```
GET https://bmvpc.api.qcloud.com/v2/index.php?
  &Action=DescribeBmSubnetIps
  &<公共请求参数>
  &unVpcId=<VPC实例ID>&unSubnetId=<子网ID>

```

### 请求参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="/doc/api/229/6976" title="公共请求参数">公共请求参数</a>页面。其中，此接口的Action字段为DescribeBmSubnetIps。

| 参数名称 | 描述 | 类型 | 必选 |
|---------|---------|---------|---------|
| unVpcId | 子网所属的私有网络ID值，例如：vpc-kd7d06of。可通过DescribeBmVpcEx接口查询。 | String | 是 |
| unSubnetId | 要删除的子网ID值，例如：subnet-k20jbhp0。可通过DescribeBmSubnetEx接口查询。 | String | 是 |
 
## 响应

### 响应示例

```

{
 "code": 0,
 "message": "",
 "codeDesc": "Success",
 "data": {
  "cpmSet": ["< 物理机IP >"],
  "vmSet": ["<云服务器IP >"],
  "tgSet": ["<托管机器IP >"]
 }
}

```

### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href="/document/product/386/6725" title="公共错误码">公共错误码</a>。| Int |
| message | 模块错误信息描述，与接口相关。| String |
| data.cpmSet | 物理机类型IP信息。| Array |
| data.vmSet | 云服务器类型IP信息。| Array |
| data.tgSet | 托管机器类型IP信息。| Array |

## 错误码
 
| 错误代码 |英文提示| 描述 |
|--------|---------|---------|
| -3047  | InvalidBmVpc.NotFound | 无效的VPC。VPC资源不存在，请再次核实您输入的资源信息是否正确，可通过DescribeBmVpcEx接口查询VPC。 |
| -3001  | InvalidInputParams | 输入参数不符合指定格式。 |
| -3051  | BmVpc.SubnetNotExist | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过DescribeBmSubnetEx接口查询子网。 |

## 实际案例

### 输入

```

GET https://bmvpc.api.qcloud.com/v2/index.php?Action=DescribeBmSubnetIps
    &SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
    &Nonce=6791
    &Timestamp=1507777243
    &Region=bj
    &Signature=RLfmJ0mnkm2Fla4zbTGABkRA%2Ft4%3D
    &unVpcId=vpc-34cxlz7z
    &unSubnetId=subnet-jv24ivq0
```

### 输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "cpmSet": [
            "10.10.0.2",
            "10.10.0.3",
            "10.10.0.4",
            "10.10.0.5",
            "10.10.0.6",
            "10.10.0.9",
            "10.10.0.10"
        ],
        "vmSet": [],
        "tgSet": []
    }
}

```

