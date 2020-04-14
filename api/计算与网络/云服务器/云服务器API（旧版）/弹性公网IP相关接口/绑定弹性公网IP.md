>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: EipBindInstance

弹性公网IP和服务器或弹性网卡绑定

>注意：
如待操作服务器带有普通公网IP，绑定过程会把其普通公网IP自动解绑并释放，服务器将绑定所指定的弹性公网IP。

 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> eipId <td> 是 <td> String <td> EIP的实例ID，可通过<a href="https://cloud.tencent.com/document/api/213/1379" title="DescribeEip">DescribeEip</a>接口返回字段中的eipId获取
<tr>
<td> unInstanceId <td> 否 <td> String <td> 待操作服务器的实例ID，可通过<a href="https://cloud.tencent.com/document/api/213/831" title="DescribeInstances">DescribeInstances</a>接口返回字段中的unInstanceId获取，传入参数unInstanceId表示绑定服务器的主网卡主IP
<tr>
<td> networkInterfaceId <td> 否 <td> String <td> 弹性网卡唯一ID，可通过<a href="/doc/api/245/4814" title="DescribeNetworkInterfaces">DescribeNetworkInterfaces</a>接口返回字段中的networkInterfaceId获取
<tr>
<td> privateIpAddress <td> 否 <td> String <td> 服务器内网IP，绑定时或者传入参数unInstanceId，或者传入参数networkInterfaceId和privateIpAddress。当networkInterfaceId和privateIpAddress没有绑定在服务器上时，绑定操作会保持其与EIP的关系。
</tbody></table>

 

## 3. 输出参数
 

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码。0表示成功，其他值表示失败。|
| message | String | 模块错误信息描述，与接口相关。|


 

## 4. 示例
 
输入
<pre>

  https://eip.api.qcloud.com/v2/index.php?
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &eipId=eip-mksy14ay
  &unInstanceId=ins-hyvbipjg

</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

