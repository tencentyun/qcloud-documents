>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: DescribeEipQuota

查询指定地域弹性公网IP配额。


## 2. 输入参数
 
无。
 
## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。|
| message | String | 模块错误信息描述，与接口相关。|
| data |   Array | 返回的数据结构。|

Data结构

<table class="t"><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
</tr><tr>
<td> data.eipNumQuota </td><td> Int </td><td> 能申请EIP个数的总配额</td>
</tr><tr>
<td> data.currentEipNum </td><td> Int </td><td> 当前EIP个数</td>
</tr><tr>
<td> data.dailyApplyQuota </td><td> Int </td><td> 日申请EIP的次数限制</td>
</tr><tr>
<td> data.dailyApplyCount </td><td> Int </td><td> 当天申请EIP次数</td>
</tr><tr>
<td> data.dailyAllocWanIpQuota </td><td> Int </td><td> 日解绑EIP时重新分配普通公网IP的次数限制</td>
</tr><tr>
<td> data.dailyAllocWanIpCount </td><td> Int </td><td> 当天解绑EIP并重新分配普通公网IP次数</td>
</tr></table>

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

