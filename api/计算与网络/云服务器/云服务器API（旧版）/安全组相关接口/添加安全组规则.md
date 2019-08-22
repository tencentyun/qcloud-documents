>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口（CreateSecurityGroupPolicy）用于添加安全组规则。
接口请求域名：<font style="color:red">dfw.api.qcloud.com</font>

1)规则[描述](https://cloud.tencent.com/doc/product/213/500#3.-.E5.AE.89.E5.85.A8.E7.BB.84.E8.A7.84.E5.88.99)
2)安全组的每条规则最多可包含四个有效字段：ipProtocol、cidrIp或sgId（两者是排他关系，不允许同时输入）、portRange和action。action字段是必需的，其他字段如果不出现，代表这条规则处理网络报文时，不考虑这个字段而全部匹配。
3)ipProtocol字段支持输入tcp、udp和icmp，不区分大小写。
4)cidrIp字段允许输入符合cidr格式标准的任意字符串。(展开)在基础网络中，如果cidrIp包含您的账户内的云服务器之外的设备在腾讯云的内网IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。
5)sgId字段允许输入与待修改的安全组位于相同项目中的安全组ID，包括这个安全组ID本身，代表安全组下所有云服务器的内网IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个ID所关联的云服务器变化而变化，不需要重新修改。
6)portRange字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当ipProtocol字段是tcp或udp时，portRange字段才被接受。
7)action字段允许输入ACCEPT或DROP字符串，不区分大小写。
8)desc字段允许输入单条规则的描述语，不超过50个UTF-8字符。

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的Action字段为CreateSecurityGroupPolicy。
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> sgId <td> 是 <td> String <td> 安全组id
<tr>
<td> version <td> 否 <td> Int <td> 版本，用户更新安全规则，每次更新安全规则版本会自动加1，防止您更新的路由规则已过期，不填不考虑冲突
<tr>
<td> direction <td> 是 <td> String <td> 方向(ingress/egress)
<tr>
<td> index <td> 是 <td> Int <td> 添加位置，从哪个位置开始添加，当前规则为空时，index需要设置为-1
<tr>
<td> policys <td> 是 <td> Array <td> 安全组规则
</tbody></table>

policys规则成员结构
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> ipProtocol <td> String <td> 网络协议，支持udp、tcp、icmp等，无则表示全协议
<tr>
<td> cidrIp <td> String <td> ip网段地址，不传为全地址，和sgId互斥，一条规则中两参数都存在会报错
<tr>
<td> sgId <td> String <td> 安全组ID，和cidrIp互斥，一条规则中两参数都存在会报错
<tr>
<td> addressModule <td> String <td> IP地址ID或者IP地址组ID，和cidrIp、sgId互斥
<tr>
<td> portRange<td> String <td> 端口，不传为不限端口
<tr>
<td> serviceModule<td> String <td> 协议端口ID或者协议端口组ID，和ipProtocol+portRange互斥
<tr>
<td> desc <td> String <td> 规则描述
<tr>
<td> action <td> String <td> 动作，accept或者drop
</tbody></table> 

## 3. 输出参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code <td> Int <td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message <td> String <td> 错误信息
</tbody></table>

 ## 4. 错误码表
 <table class="t"><tbody><tr>
<th><b>错误码数值</b></th>
<th><b>原因</b></th>
<tr>

<td> 7000 <td> 安全组后台异常
<tr>
<td> 7001 <td> 安全组不属于当前用户
<tr>
<td> 7002 <td> 规则数量超过配额
<tr>
<td> 7006 <td> 系统默认安全组禁止修改
<tr>
<td> 9003 <td> 规则数据格式错误
</tbody></table>

## 5. 示例
 
输入
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=CreateSecurityGroupPolicy
  &sgId=sg-33ocnj9n
  &version=2
  &direction=ingress
  &index=0
  &policys.0.ipProtocol=tcp
  &policys.0.cidrIp=10.0.0.0/8
  &policys.0.action=ACCEPT
  &policys.0.portRange=22
  &policys.0.desc=内网入流量tcp协议22端口禁止访问
  &policys.0.action=ACCEPT
  &policys.0.ipProtocol=tcp
  &policys.0.desc=内网tcp出流量放通
  &policys.0.cidrIp=10.0.0.0/8
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>

</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

