# uploadFile

- 功能描述

将本地资源上传到服务器。客户端发起一个 HTTPS POST 请求，其中 `content-type` 为 `multipart/form-data`。使用前请注意阅读[相关说明](/develop/frame/basic_ability/basic_network.md)。

- 参数

**Object object**

| 属性     | 类型     | 默认值 | 必填 | 说明                                                         | 最低版本                                                     |
| :------- | :------- | :----- | :--- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| url      | string   |        | 是   | 开发者服务器地址                                             |                                                              |
| filePath | string   |        | 是   | 要上传文件资源的路径 (本地路径)                              |                                                              |
| name     | string   |        | 是   | 文件对应的 key，开发者在服务端可以通过这个 key 获取文件的二进制内容 |                                                              |
| header   | Object   |        | 否   | HTTP 请求 Header，Header 中不能设置 Referer                  |                                                              |
| formData | Object   |        | 否   | HTTP 请求中其他额外的 form data                              |                                                              |
| success  | function |        | 否   | 接口调用成功的回调函数                                       |                                                              |
| fail     | function |        | 否   | 接口调用失败的回调函数                                       |                                                              |
| complete | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）             |                                                              |

**object.success 回调函数**

参数

**Object res**

| 属性       | 类型   | 说明                           |
| :--------- | :----- | :----------------------------- |
| data       | string | 开发者服务器返回的数据         |
| statusCode | number | 开发者服务器返回的 HTTP 状态码 |

返回值

[UploadTask](./UploadTask.md)

一个可以监听上传进度进度变化的事件和取消上传的对象

- 示例代码

```js
wx.chooseImage({
  success (res) {
    const tempFilePaths = res.tempFilePaths
    wx.uploadFile({
      url: 'https://example.weixin.qq.com/upload', //仅为示例，非真实的接口地址
      filePath: tempFilePaths[0],
      name: 'file',
      formData: {
        'user': 'test'
      },
      success (res){
        const data = res.data
        //do something
      }
    })
  }
})
```