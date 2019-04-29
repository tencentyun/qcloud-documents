
## 1. 接口描述

本接口(CreateSnapshot)用于对指定云硬盘创建快照，此接口会返回新创建快照的ID，用户可使用此ID调用[DescribeSnapshots(查询快照列表)](https://cloud.tencent.com/doc/api/364/2530)接口来查询快照创建进度(percent)。快照说明详见[快照作用](https://cloud.tencent.com/doc/product/213/502)。

接口请求域名：<font style="color:red">snapshot.api.qcloud.com</font>


使用限制：
1. 只有具有快照能力的云硬盘才能创建快照。详见[DescribeCbsStorages(查询云硬盘信息)](https://cloud.tencent.com/doc/api/364/2519)接口回包中snapshotAbility字段 |
2. 可创建快照数量限制见[产品使用限制](https://cloud.tencent.com/doc/product/362/5145)。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见[公共请求参数](https://cloud.tencent.com/document/product/240/8320)页面。


| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| storageId | 是 | String | 需要创建快照的云硬盘ID，可通过[DescribeCbsStorages(查询云硬盘信息)](https://cloud.tencent.com/doc/api/364/2519)接口查询 |
| snapshotName | 否 | String | 快照名称,如不传则新快照名称为未命名 |


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0：成功，其他值：失败|
| message | String | 错误信息|
| snapshotId | String | 新创建的快照ID |


## 4. 示例

输入：
```
https://snapshot.api.qcloud.com/v2/index.php?
<公共请求参数>
&Action=CreateSnapshot
&storageId=disk-g73hhs4o
&snapshotName=mySnap
```

返回示例如下。从中可以看出，成功创建一个快照，快照ID为snap-o7zxxxr3

```
{
    "code":"0",
    "message":"",
    "snapshotId":"snap-o7zxxxr3"
}
```

