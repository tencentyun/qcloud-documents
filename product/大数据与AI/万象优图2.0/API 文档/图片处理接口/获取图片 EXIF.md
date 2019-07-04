## 简介
EXIF（Exchangeable Image File）是“可交换图像文件”的缩写，可记录数码照片的拍摄参数、缩略图及其他属性信息。目前支持大小在 20M 以内、长宽小于 9999 像素的图片处理。
## 接口形式
download_url?exif
## 参数说明
| 参数                                      | 含义                                       |
| --------------------------------------- | ---------------------------------------- |
|download_url                            |文件的访问链接，具体构成为<bucket id>-<appid>.<picture region>.<domain>.com/<picture name>，如examples-1251000004.picsh.myqcloud.com/sample.jpeg|

## 示例

```
http://examples-1251000004.picsh.myqcloud.com/sample.jpeg?exif

```
