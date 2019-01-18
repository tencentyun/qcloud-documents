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
| code | Int | 公共错误码。0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。|
| message | String | 模块错误信息描述，与接口相关。详见错误码页面的[模块错误码](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。|
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
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>

</pre>

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

