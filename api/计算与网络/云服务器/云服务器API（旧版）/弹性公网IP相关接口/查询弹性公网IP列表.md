>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: DescribeEip

查询弹性公网 IP。

 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> eipIds.n  <td> 否 <td> String <td> EIP 实例 ID 列表，列表下标从0开始
<tr>
<td> eips.n  <td> 否 <td> String <td> EIP 列表，列表下标从0开始
<tr>
<td> unInstanceIds.n  <td> 否 <td> String <td> 服务器实例 ID 列表，列表下标从0开始，可通过<a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeInstances">DescribeInstances</a>接口返回字段中的 unInstanceId 获取
<tr>
<td> networkInterfaceIds.n <td> 否 <td> String <td> 弹性网卡唯一 ID 列表，列表下标从0开始，可通过 <a href="/doc/api/245/4814" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a> 接口返回字段中的 networkInterfaceId 获取
<tr>
<td> privateIpAddress  <td> 否 <td> String <td> 服务器内网 IP
<tr>
<td> searchKey <td> 否 <td> String <td> EIP 实例名称，模糊匹配
<tr>
<td> status.n  <td> 否 <td> Int <td> 状态列表，列表下标从0开始<br>0：创建中； 1：绑定中； 2：已绑定； 3：解绑中； 4：未绑定； 6：下线中； 9：创建失败
<tr>
<td> type  <td> 否 <td> Int <td> 0：CVM；1：NAT 网关
<tr>
<td> limit <td> 否 <td> Int <td> 返回 EIP 数量，默认20, 最大值100
<tr>
<td> offset <td> 否 <td> Int <td> 偏移量，默认为0
<tr>
<td> orderBy <td> 否 <td> String <td> 排序字段，支持： eipId, eip, ispId, status, unInstanceId, arrears, createdAt
<tr>
<td> orderType <td> 否 <td> Int <td> 1倒序，0顺序，默认倒序
</tbody></table>

 > 查询接口中单次查询一般都有一个默认最大返回记录数，要遍历所有资源，需要使用 limit，offset 进行分页查询；例如我想查询第110~149 这40条记录，则可以设置 offset=110，limit=40。

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
|  totalCount  |  Int |  返回符合过滤条件的 EIP 数量；假如指定 limit，offset，该值有可能大于 data 列表中的数量 |
| data |   Array | 返回列表 |

Data结构


<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> data.eipSet <td> Array <td> 返回 EIP 信息列表
<tr>
<td> data.eipSet.eipId <td> String <td> EIP 实例 ID
<tr>
<td> data.eipSet.eipName <td> String <td> EIP 名称
<tr>
<td> data.eipSet.eip <td> String <td> EIP 地址
<tr>
<td> data.eipSet.ispId <td> Int <td> 运营商 ID<br> 0：电信； 1：联通； 2：移动； 3：教育网； 4：盈科； 5：BGP； 6：中国香港
<tr>
<td> data.eipSet.status <td> Int <td> 状态<br> 0：创建中； 1：绑定中； 2：已绑定； 3：解绑中； 4：未绑定； 6：下线中； 9：创建失败
<tr>
<td> data.eipSet.type <td> Int <td> 类型<br> 0：CVM； 1：NAT网关
<tr>
<td> data.eipSet.arrears <td> Int <td> 是否欠费隔离<br> 1： 欠费隔离； 0： 正常。处在欠费隔离情况下的 EIP 不能进行任何管理操作。
<tr>
<td> data.eipSet.unInstanceId <td> String <td> EIP所绑定的服务器实例 ID，未绑定则为空
<tr>
<td> data.eipSet.networkInterfaceId <td> String <td> 弹性网卡唯一 ID
<tr>
<td> data.eipSet.privateIpAddress <td> String <td> 服务器内网 IP
<tr>
<td> data.eipSet.createdAt <td> String <td> 创建时间
<tr>
<td> data.eipSet.updatedAt <td> String <td> 更新时间
<tr>
<td> data.eipSet.freeSecond <td> Int <td> EIP 未绑定服务器时长（单位：秒）
</tbody></table>

 

## 4. 示例
 
输入
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
</pre>

输出
```

{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "eipSet": [
            {
                "eipId": "eip-co9m2t7k",
                "eipName": "",
                "eip": "119.29.239.140",
                "ispId": 5,
                "status": 2,
                "arrears": 0,
                "unInstanceId": "ins-pjrzryru",
                "createdAt": "2016-07-11 21:23:35",
                "updatedAt": "2016-07-11 21:23:35",
                "freeSecond": 0,
                "type": 0,
                "privateIpAddress": "10.104.211.58",
                "networkInterfaceId": ""
            }
        ]
    },
    "totalCount": 1
}

```

