## 1. 接口描述
 
域名: vod.api.qcloud.com
接口名: DescribeVodCover

为视频设置显示封面，仅支持将视频截图的 URL 设置为封面，不支持上传图片。如需上传图片，可以使用以下方式：

* 【控制台】-【视频管理】-选择文件-【基本信息】
* [UGC 上传 SDK](/document/product/266/9219)
 

## 2. 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> fileId <td> 是 <td> Int <td> 视频文件的id
<tr>
<td> type <td> 是 <td> Int <td> 封面设置方法（当前填1，表示使用截图地址）
<tr>
<td> para <td> 是 <td> String <td> 截图url
<tr>
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

 

## 4. 示例
 
输入
<pre>
  https://domain/v2/index.php?Action=DescribeVodCover
  &fileId=8782277315343726561
  &amp;para=https://125111232654.vod2.myqcloud.com/vodtransgzp1251132654/9031868221236647/shotup/f0.100_2.jpg
  &type=1
  &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```


