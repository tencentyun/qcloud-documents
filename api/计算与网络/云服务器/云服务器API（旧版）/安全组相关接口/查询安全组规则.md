>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口（DescribeSecurityGroupPolicys）用于查询已经存在的安全组的规则。
接口请求域名：<font style="color:red">dfw.api.qcloud.com</font>
1)返回数据包含 ingress（入站）和 egress（出站）两个列表
2)安全组的每条规则最多可包含四个有效字段：ipProtocol、cidrIp 或 sgId（两者是排他关系，不会同时出现）、portRange 和 action。action 字段是必然存在的，其他字段如果不出现，代表这条规则处理网络报文时，不考虑这个字段而全部匹配。
 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的 Action 字段为 DescribeSecurityGroupPolicys。
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> sgId <td> 是 <td> String <td> 安全组 Id
</tbody></table>

 

## 3. 输出参数
 
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码，0：成功，其他值：失败 |
| message |   String | 错误信息 |
| data |   Array | 返回的数据结构|

Data 结构：
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> data.ingress <td> Array <td> 入方向规则列表
<tr>
<td> data.egress <td> Array <td> 出方向规则列表
</tbody></table>

ingress/egress规则成员结构
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> index <td> Int <td> 规则位置，从 0 开始
<tr>
<td> addressModule <td> String <td> IP 地址 ID 或者 IP 地址组ID；与 cidrIp sgId 互斥。
<tr>
<td> ipProtocol <td> String <td> 网络协议，支持 udp、tcp、icmp 等，无则表示全协议
<tr>
<td> cidrIp <td> String <td> IP 或 IP 段，无则表示全 IP。与 sgId 不会同时出现
<tr>
<td> sgId <td> String <td> 安全组 ID。与 cidrIp 不会同时出现
<tr>
<td> portRange<td> String <td> 端口或端口段，无则表示全端口
<tr>
<td> serviceModule<td> String <td> 协议端口 ID 或者协议端口组 ID；与 ipProtocol+portRange 互斥
<tr>
<td> desc <td> String <td> 规则描述
<tr>
<td> action <td> String <td> 动作，accept 或者 drop
<tr>
<td> version <td> Int <td> 版本，用户更新安全规则，每次更新安全规则版本会自动加1，防止您更新的路由规则已过期
</tbody></table>

 ## 4. 错误码表
 <table class="t"><tbody><tr>
<th><b>错误码数值</b></th>
<th><b>原因</b></th>
<tr>

<td> 7000 <td> 安全组后台异常
<tr>
<td> 7001 <td> 安全组不属于当前用户
</tbody></table>


## 5. 示例
 
输入
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeSecurityGroupPolicys
  &sgId=sg-33ocnj9n
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>

</pre>

输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "ingress": [
            {
                "index": 0,
                "action": "ACCEPT",
                "serviceModule": "ppm-i083665x",
                "addressModule": "ipmg-poo8128q"
            },
            {
                "index": 1,
                "action": "ACCEPT",
                "portRange": "22",
                "sgId": "sg-ghm9l8ve",
                "ipProtocol": "tcp"
            },
            {
                "index": 2,
                "action": "ACCEPT",
                "cidrIp": "10.1.1.10",
                "ipProtocol": "tcp"
            }
        ]
    }
}

```

