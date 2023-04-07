# wx.previewImage

### wx.previewImage(Object object)

在新页面中全屏预览图片。预览的过程中用户可以进行保存图片、发送给朋友等操作。

#### 参数

##### Object object

| 属性     | 类型             | 默认值        | 必填 | 说明                                             |
| -------- | ---------------- | ------------- | ---- | ------------------------------------------------ |
| urls     | Array.\<string\> |               | 是   | 需要预览的图片链接列表。 支持云文件 ID。         |
| current  | string           | urls 的第一张 | 否   | 当前显示图片的链接                               |
| success  | function         |               | 否   | 接口调用成功的回调函数                           |
| fail     | function         |               | 否   | 接口调用失败的回调函数                           |
| complete | function         |               | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### 示例代码

```js
wx.previewImage({
  current: '', // 当前显示图片的http链接
  urls: [], // 需要预览的图片http链接列表
})
```