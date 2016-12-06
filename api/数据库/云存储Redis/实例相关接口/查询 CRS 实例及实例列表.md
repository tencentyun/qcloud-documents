## 1. 接口描述
 
本接口(DescribeRedis)用于查询CRS实例列表。
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='/doc/api/260/1753' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的 Action 字段为 DescribeRedis。

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>是否必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> limit <td> 是 <td> Uint <td> 返回实例列表数量，默认 20, 最大值 100
<tr>
<td> offset <td> 是 <td> Uint <td> 偏移量，默认为0。 查询接口中单次查询一般都有一个默认最大返回记录数，要遍历所有资源，需要使用 limit，offset进行分页查询；例如查询第110~149 这40条记录，则可以设置 offset=110 limit=40。
<tr>
<td> redisId <td> 否 <td> String <td> 实例Id
<tr>
<td> redisName <td> 否 <td> String <td> 实例名称
<tr>
<td> orderBy <td> 否 <td> String <td> 枚举范围：redisId，projectId，createtime
<tr>
<td> orderType <td> 否 <td> Uint <td> 排序方式： 1 - 倒序，0 - 顺序，默认1倒序
<tr>
<td> projectIds <td> 否 <td> String <td> 项目ID数组
</tbody></table>

 

## 3. 输出参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code <td> Int <td>  公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>。
<tr>
<td> message <td> String <td> 错误信息
<tr>
<td> codeDesc <td> String <td> 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因。
<tr>
<td> totalCount <td> UInt <td> 记录总数
<tr>
<td> data <td> Array <td> 返回数组
<tr>
<td> data.redisSet <td> Array <td> 实例集合
<tr>
<td> data.redisSet.redisName <td> String <td> 实例名称
<tr>
<td> data.redisSet.redisId <td> String <td> 实例ID
<tr>
<td> data.redisSet.appid <td> UInt <td> 用户ID
<tr>
<td> data.redisSet.projectId <td> UInt <td>项目ID
<tr>
<td> data.redisSet.regionId <td> UInt <td> 地域ID
<tr>
<td> data.redisSet.zoneId <td> UInt <td> 可用区ID
<tr>
<td> data.redisSet.vpcId <td> UInt <td> 网络ID
<tr>
<td> data.redisSet.subnetId <td> UInt <td> 子网ID
<tr>
<td> data.redisSet.status <td> Int <td> 状态, 0 - 待初始化； 1 - 流程中； 2  - 运行中；  -2 - 已隔离
<tr>
<td> data.redisSet.statusDesc <td> String <td> 状态描述
<tr>
<td> data.redisSet.wanIp <td> String <td> 服务IP，内网ip，redis不能同外网访问
<tr>
<td> data.redisSet.port <td> UInt <td> 服务端口
<tr>
<td> data.redisSet.createtime <td> String <td> 创建时间
<tr>
<td> data.redisSet.size <td> UInt <td> 实例容量，单位： MB
<tr>
<td> data.redisSet.sizeUsed <td> UInt <td> 实例使用量， 单位： MB
<tr>
<td> data.redisSet.deadlineTime <td> String <td> 到期时间
</tbody></table>

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|

## 5. 示例
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=DescribeRedis
&<<a href="https://www.qcloud.com/doc/api/229/6976">公共请求参数</a>>
&limit=10
&offset=0
</pre>
返回示例如下：
```
{
    "code": 0,
	"message": ""，
	"codeDesc": "Success",
    "totalCount": 1,
    "data": {
        "redisSet": [
            {
                "redisName": "腾讯云测试实例",
                "redisId": "crs-ifmymj41",
                "appid": 125100000,
                "projectId": 0,
                "regionId": 1,
                "zoneId": 100002,
                "vpcId": 0,
                "subnetId": 0,
                "status": 2,
                "statusDesc": "实例运行中",
                "wanIp": "10.66.114.214",
                "port": 6379,
                "createtime": "2015-09-11 11:16:00",
                "size": 1024,
                "sizeUsed": 0,
                "deadlineTime": "2016-09-19 00:00:00"
            }
        ]
    }
}
```