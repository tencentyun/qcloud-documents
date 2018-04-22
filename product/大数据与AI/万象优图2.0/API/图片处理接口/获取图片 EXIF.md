## 简介
EXIF（Exchangeable Image File）是“可交换图像文件”的缩写，可记录数码照片的拍摄参数、缩略图及其他属性信息。
## 接口形式
download_url?imageInfo
## 参数说明
| 参数                                      | 含义                                       |
| --------------------------------------- | ---------------------------------------- |
|download_url                            |文件的访问链接，具体构成为&lt;bucket id&gt;-&lt;appid&gt;.&lt;picture region&gt;.&lt;domain&gt;.com/&lt;picture name&gt;，如examples-1251000004.picsh.myqcloud.com/sample.jpeg|
## 示例
```
http://examples-1251000004.picsh.myqcloud.com/sample.jpeg?exif
```
