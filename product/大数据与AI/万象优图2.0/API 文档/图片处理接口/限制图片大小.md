## 功能概述

腾讯云数据万象通过 **imageMogr2/size-limit** 接口可限制图片处理（例如缩放、压缩等）后的文件大小。

## 接口形式

```
download_url?imageMogr2/size-limit
```

## 参数说明

操作名称：size-limit。

| 参数            | 含义                                                         |
| :-------------- | :----------------------------------------------------------- |
| download_url    | 文件的访问链接，具体构成为`<BucketName-APPID>.cos.<Region>.myqcloud.com/<picture name>`， 例如`examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/picture.jpeg` |
| size-limit      | 限制图片转换后的大小，支持以兆字节和千字节为单位的图片<br>1. 仅支持 JPG 格式的图片，可以用于限制处理后图片的大小<br>2. 若在尾部加上`!`，表示用处理后的图片大小与原图大小做比较，如果处理后的图片比原图小，则返回处理后的图片，否则返回原图。例如：examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/picture.jpg?imageMogr2/size-limit/15k!<br>3. 建议搭配`strip`参数使用，去除图片的一些冗余信息，会有更好的效果。例如：examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/picture.jpg?imageMogr2/strip/format/png/size-limit/15k! |
| /ignore-error/1 | 当处理参数中携带此参数时，针对文件过大导致处理失败的场景，会直接返回原图而不报错 |

## 示例

将 JPG 图片转换为 PNG 格式，并限制图片大小为15KB，实际案例如下：

```plaintext
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpg?imageMogr2/strip/format/png/size-limit/15k!
```
