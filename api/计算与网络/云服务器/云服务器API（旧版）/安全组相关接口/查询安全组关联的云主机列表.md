>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口（DescribeInstancesOfSecurityGroup）用于查询已关联指定的安全组的云服务器。
接口请求域名：<font style="color:red">dfw.api.qcloud.com</font>
1)此接口允许查询云服务器列表中的一部分成员信息，使用offset和limit两个输入字段控制。不输入时，默认查询前20台云服务器。
2)一台云服务器允许关联多个安全组，在不同安全组的查询结果中可能有重复的云服务器实例ID。
3)云服务器列表以列表方式返回，列表成员是云服务器的实例ID。

**特别提示**：为提供更丰富的按安全组查询绑定实例的需求，建议客户使用各类云资源的实例查询接口，在这些接口中使用安全组ID过滤条件。以云服务器为例，
<<a href="https://cloud.tencent.com/document/product/213/9388">DescribeInstances</a>> 接口可以使用安全组ID作过滤条件，查询出更为完整的实例信息。

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的Action字段为DescribeInstancesOfSecurityGroup。
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> sgId <td> 是 <td> String <td> 安全组id
<tr>
<td> offset <td> 否 <td> Int <td> 分页开始位置， 默认值: 0
<tr>
<td> limit <td> 否 <td> Int <td> 数量限制，默认值: 20
</tbody></table>

 

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败 |
| message |   String | 错误信息 |
| totalCount |   Int | 关联云服务器实例总数|
| data |   Array | 返回的数据结构|

Data结构：
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> instanceId <td> Array <td> 云服务器实例Id，例如ins-a1iofc4j
</tbody></table>

 

## 4. 示例
 
输入
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeInstancesOfSecurityGroup
  &sgId=sg-56p1yd1o
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>

</pre>

输出
```

{
    "code": 0,
    "message": "",
   "totalCount":0,
    "data": [
            {
                "instanceId": "ins-tks7a12z"
            }
     ]
}

```

