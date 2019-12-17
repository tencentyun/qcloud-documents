>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: TransformMode

弹性公网IP模式切换。

 

## 2. 输入参数 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> eipId <td> 是 <td> String <td> EIP实例ID，可通过<a href="https://cloud.tencent.com/document/api/213/1379" title="DescribeEipQuota">DescribeEip</a>接口返回字段中的 eipId获取
<tr>
<td> mode <td> 是 <td> Int <td> 要切换到的模式<br>0：NAT模式，1：直通模式。
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
  &mode=0

</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

