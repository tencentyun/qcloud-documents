>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
域名: eip.api.qcloud.com
接口名: TransformWanIpToEip

普通公网IP转弹性公网IP，将服务器当前绑定的普通公网IP转换成弹性公网IP，转换后随着服务器的释放，该弹性公网IP将会保留。

 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> unInstanceId <td> 是 <td> String <td> 待操作有普通公网IP的服务器实例ID，可通过<a href="https://cloud.tencent.com/document/api/213/831" title="DescribeInstances">DescribeInstances</a>接口返回字段中的unInstanceId获取。
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
  &unInstanceId=ins-hyvbipjg

</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

