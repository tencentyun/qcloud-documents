## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: DescribeEipQuota

查询指定地域弹性公网IP配额。

 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th>参数名称</th>
<th>必选</th>
<th>类型</th>
<th>描述</th>
<tr>
<th>空</th>
<th>-</th>
<th>-</th>
<th>-</th>
</tbody></table>

 

## 3. 输出参数
 | 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考<a href="/document/product/213/6982" title="错误码">错误码</a>。 |
| message |   String | 错误信息 |
| data |   Array | 返回的数据结构|

Data结构

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> data.eipNumQuota <td> Int <td> 能申请EIP个数的总配额
<tr>
<td> data.currentEipNum <td> Int <td> 当前EIP个数
<tr>
<td> data.dailyApplyQuota <td> Int <td> 日申请EIP的次数限制
<tr>
<td> data.dailyApplyCount <td> Int <td> 当天申请EIP次数
<tr>
<td> data.dailyAllocWanIpQuota <td> Int <td> 日解绑EIP时重新分配普通公网IP的次数限制
<tr>
<td> data.dailyAllocWanIpCount <td> Int <td> 当天解绑EIP并重新分配普通公网IP次数
</tbody></table>

 

## 4. 示例
 
输入
```

  https://eip.api.qcloud.com/v2/index.php?
  &<公共请求参数>

```

输出
```

{
    "code": 0,
    "message": "",
    "data": {
        "eipNumQuota": 20,
        "currentEipNum": 2,
        "dailyApplyQuota": 10,
        "dailyApplyCount": 7,
        "dailyAllocWanIpQuota": 10,
        "dailyAllocWanIpCount": 2    
    }
}

```

