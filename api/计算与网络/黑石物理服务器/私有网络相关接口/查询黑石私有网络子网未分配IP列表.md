>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述 
本接口（DescribeBmSubnetAvailableIp）用于查询黑石 VPC 子网未分配 IP 列表。

接口访问域名：
```
bmvpc.api.qcloud.com
```

## 请求
### 请求示例
```
GET https://bmvpc.api.qcloud.com/v2/index.php?
  &Action=DescribeBmSubnetAvailableIp
  &<公共请求参数>
  &unSubnetId=<子网ID>

```

### 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上 <a href="/doc/api/229/6976" title="公共请求参数">公共请求参数</a>。其中，此接口的 Action 字段为 DescribeBmSubnetAvailableIp。

| 参数名称 | 描述 | 类型 | 必选 |
|---------|---------|---------|---------|
| unSubnetId | 子网唯一ID，例如：subnet-k20jbhp0。可通过 DescribeBmSubnetEx 接口查询。 | String | 是 |
 
## 响应
### 响应示例
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        "<不连续的单个可分配IP>",
        "<连续的可分配IP开始>-<连续的可分配IP结束>"
    ]
}

```

### 响应参数

| 参数名称 | 描述 | 类型 |
|---------|---------|---------|
| code | 公共错误码，0 表示成功，其他值表示失败。详见错误码页面的 <a href="/document/product/386/6725" title="公共错误码">公共错误码</a>。| Int |
| message | 模块错误信息描述，与接口相关。| String |
| data | 子网未分配 IP 数组。对于不连续的 IP，单独一个 IP 作为数组的一个值，对于连续的 IP 段使用`-`字符进行连接作为数组的一个值。| Array |

## 错误码
 
| 错误代码 |英文提示| 描述 |
|--------|---------|---------|
| -3001  | InvalidInputParams | 输入参数不符合指定格式。 |
| -3051  | BmVpc.SubnetNotExist | 无效的子网。子网资源不存在，请再次核实您输入的资源信息是否正确，可通过 DescribeBmSubnetEx 接口查询子网。 |

## 实际案例

### 请求

```

GET https://bmvpc.api.qcloud.com/v2/index.php?Action=DescribeBmSubnetAvailableIp
    &SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
    &Nonce=6791
    &Timestamp=1507777243
    &Region=bj
    &Signature=RLfmJ0mnkm2Fla4zbTGABkRA%2Ft4%3D
    &unSubnetId=subnet-jv24ivq0
```

### 响应
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        "10.0.0.5",
        "10.0.0.17",
        "10.0.0.41-10.0.0.133",
        "10.0.0.135-10.0.0.254"
    ]
}

```
