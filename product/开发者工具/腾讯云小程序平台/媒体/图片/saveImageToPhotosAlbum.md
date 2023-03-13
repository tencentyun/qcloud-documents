# wx.saveImageToPhotosAlbum

### wx.saveImageToPhotosAlbum(Object object)

> 调用前需要 '用户授权' scope.writePhotosAlbum

保存图片到系统相册。

#### 参数

##### Object object

| 属性     | 类型     | 默认值 | 必填 | 说明                                                               |
| -------- | -------- | ------ | ---- | ------------------------------------------------------------------ |
| filePath | string   |        | 是   | 图片文件路径，可以是临时文件路径或永久文件路径，不支持网络图片路径 |
| success  | function |        | 否   | 接口调用成功的回调函数                                             |
| fail     | function |        | 否   | 接口调用失败的回调函数                                             |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）                   |

#### 示例代码

```js
wx.saveImageToPhotosAlbum({
  success(res) {},
})
```