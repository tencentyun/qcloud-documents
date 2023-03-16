# chooseImage

- 功能描述

从本地相册选择图片或使用相机拍照。

- 参数

**Object object**

| 属性       | 类型           | 合法值及说明                          | 默认值                     | 必填 | 说明                                             |
| :--------- | :------------- | ------------------------------------- | :------------------------- | :--- | :----------------------------------------------- |
| count      | number         |                                       | 9                          | 否   | 最多可以选择的图片张数                           |
| sizeType   | Array.<string> | original：原图<br>compressed：压缩图  | ['original', 'compressed'] | 否   | 所选的图片的尺寸                                 |
| sourceType | Array.<string> | album：从相册选图<br>camera：使用相机 | ['album', 'camera']        | 否   | 选择图片的来源                                   |
| success    | function       |                                       |                            | 否   | 接口调用成功的回调函数                           |
| fail       | function       |                                       |                            | 否   | 接口调用失败的回调函数                           |
| complete   | function       |                                       |                            | 否   | 接口调用结束的回调函数（调用成功、失败都会执行） |

**object.success 回调函数**

- 参数

**Object res**

| 属性          | 类型           | 说明                                  | 最低版本                                                     |
| :------------ | :------------- | :------------------------------------ | :----------------------------------------------------------- |
| tempFilePaths | Array.<string> | 图片的本地临时文件路径列表 (本地路径) |                                                              |
| tempFiles     | Array.<Object> | 图片的本地临时文件列表                |  |

**res.tempFiles 的结构**

| 属性 | 类型   | 说明                     |
| ---- | ------ | ------------------------ |
| path | string | 本地临时文件路径         |
| size | number | 本地临时文件大小，单位 B |

- 示例代码

```js
wx.chooseImage({
  count: 1,
  sizeType: ['original', 'compressed'],
  sourceType: ['album', 'camera'],
  success (res) {
    // tempFilePath可以作为 img 标签的 src 属性显示图片
    const tempFilePaths = res.tempFilePaths
  }
})
```