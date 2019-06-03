## 简介

提供获取对象 URL、获取请求预签名 URL 接口。

## 获取对象带签名 URL

### 使用示例

示例一：获取不带签名 Object Url。

```js
var url = cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg',
    Sign: false
});
```

示例二：获取带签名 Object Url。

```js
var url = cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg'
});
```

示例三：如果签名过程是异步获取，需要通过 callback 获取带签名 Url。

```js
cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg',
    Sign: false
}, function (err, data) {
    console.log(err || data.Url);
});
```

示例四：指定链接有效时间

```js
cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg',
    Sign: true,
    Expires: 3600, // 单位秒
}, function (err, data) {
    console.log(err || data.Url);
});
```

示例五：获取预签名 Put Object 上传 Url。

```js
cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Method: 'PUT',
    Key: '1.jpg',
    Sign: true
}, function (err, data) {
    console.log(err || data.Url);
});
```

示例六：获取文件 Url 并下载文件。

```js
cos.getObjectUrl({
    Bucket: 'examplebucket-1250000000',
    Region: 'ap-beijing',
    Key: '1.jpg',
    Sign: true
}, function (err, data) {
    if (!err) {
        var downloadUrl = data.Url + (data.Url.indexOf('?') > -1 ? '&' : '?') + 'response-content-disposition=attachment'; // 补充强制下载的参数
        window.open(downloadUrl); // 这里是新窗口打开 url，如果需要在当前窗口打开，可以使用隐藏的 iframe 下载，或使用 a 标签 download 属性协助下载
    }
});
```

### 参数说明

| 参数名  | 参数描述                                                     | 类型    | 必填 |
| ------- | ------------------------------------------------------------ | ------- | ---- |
| Bucket  | Bucket 的名称。命名规则为 BucketName-APPID，此处填写的存储桶名称必须为此格式 | String  | 是   |
| Region  | Bucket 所在地域。枚举值请见：[Bucket 地域信息](https://cloud.tencent.com/document/product/436/6224) | String  | 是   |
| Key     | 对象键（Object 的名称），对象在存储桶中的唯一标识，**如果请求操作是对文件的，则为文件名，且为必须参数**。如果操作是对于 Bucket，则为空 | String  | 是   |
| Sign    | 是否返回带有签名的 Url                                       | Boolean | 否   |
| Method  | 操作方法，如 get，post，delete， head 等 HTTP 方法，默认 get | String  | 否   |
| Query   | 参与签名计算的 query 参数对象                                | Object  | 否   |
| Headers | 参与签名计算的 header 参数对象                               | Object  | 否   |
| Expires | 签名几秒后失效，默认900                                      | Number  | 否   |

### 返回值说明

返回值是一个字符串，两种情况：

1. 如果签名计算可以同步计算（如：实例化传入了 SecretId 和 SecretKey），则默认返回带签名的 url。
2. 否则返回不带签名的 url。

### 回调函数说明

```
function(err, data) { ... }
```

| 参数名 | 参数描述                                                     | 类型   |
| ------ | ------------------------------------------------------------ | ------ |
| err    | 请求发生错误时返回的对象，包括网络错误和业务错误。如果请求成功则为空，更多详情请参阅 [错误码文档](https://cloud.tencent.com/document/product/436/7730) | Object |
| data   | 请求成功时返回的对象，如果请求发生错误，则为空               | Object |
| - Url  | 计算得到的 Url                                               | String |

### 浏览器下载文件

浏览器下载文件需要先通过 cos.getObjectUrl 获取 url 之后再自行调用下载，以下几个下载例子可供参考。

浏览器下载过程实际上是浏览器直接发起的 Get Object 请求，具体参数可以参考 cos.getObject 方法。

### 使用示例

示例一：获取文件 url 并下载文件。

```js
cos.getObjectUrl({
    Key: '1.jpg',
    Sign: true
}, function (err, data) {
    if (!err) {
        var downloadUrl = data.Url + (data.Url.indexOf('?') > -1 ? '&' : '?') + 'response-content-disposition=attachment'; // 补充强制下载的参数
        window.open(downloadUrl); // 这里是新窗口打开 url，如果需要在当前窗口打开，可以使用隐藏的 iframe 下载，或使用 a 标签 download 属性协助下载
    }
});
```

示例二：通过隐藏 iframe 下载。

```html
<iframe id="downloadTarget" style="width:0;height:0;" frameborder="0"></iframe>
<a id="downloadLink" href="javascript:void(0)">下载</a>
<script>
document.getElementById('downloadLink').onclick = function () {
    document.getElementById('downloadTarget').src = downloadUrl; // 示例一里获取的下载 url
};
</script>
```

示例三：通过隐藏 a 标签的 download 属性。

> !download 属性不兼容低版本浏览器。

```html
<iframe id="downloadTarget" style="width:0;height:0;" frameborder="0"></iframe>
<!-- 把示例一里的 downloadUrl 放在以下 a 标签的 href 参数里 -->
<a id="downloadLink" href="{downloadUrl}" download="1.jpg">下载</a>
```
