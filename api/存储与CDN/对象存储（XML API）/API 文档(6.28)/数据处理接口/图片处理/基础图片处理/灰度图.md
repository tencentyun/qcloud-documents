## 功能概述
对象存储通过数据万象 **imageMogr2/grayscale** 接口将图片设置为灰度图。

## 接口示例

```plaintext
download_url?imageMogr2/grayscale/<value>
```

## 处理参数说明

操作名称：grayscale。

| 参数                  | 含义                                                         |
| --------------------- | ------------------------------------------------------------ |
| download_url          | 文件的访问链接，具体构成为&lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com/&lt;picture name>，<br>例如 `examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/picture.jpeg`。 |
| /grayscale/&lt;value> | 将图片设置为灰度图。<br>value 取值为0表示不改变图片。<br>value 取值为1表示将图片变为灰度图。 |
| /ignore-error/1       | 当处理参数中携带此参数时，针对文件过大导致处理失败的场景，会直接返回原图而不报错。 |

## 实际案例

将图片变为灰度图，示例如下：

```plaintext
http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?imageMogr2/grayscale/1
```

最终效果如下：

![img](http://examples-1251000004.cos.ap-shanghai.myqcloud.com/sample.jpeg?imageMogr2/grayscale/1)
