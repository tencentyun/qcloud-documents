##  1. 简介

+ imageView2是腾讯云·万象优图提供的一种使用简单，但功能强大的图像处理接口。包括裁剪、压缩、格式转换等。
+ 开发者根据业务需求，只需在下载url后面附加相应的参数，就可以生成相应的缩略图。
+ 本文档为万象优图V2加强版，旧版本（V1和V2）请参考


## 2. 接口形式

注意：请忽略下面代码中的回车。

```
download_url?imageView2/<mode>/w/<Width>/h/<Height>
                         /format/<Format>
                         /q/<Quality>
```

## 3. 参数说明

| 参数                                       | 含义                                       |
| ---------------------------------------- | ---------------------------------------- |
| /0/w/&lt;LongEdge&gt;/h/&lt;ShortEdge&gt; | 限定缩略图的长边和短边的最大值分别为LongEdge和ShortEdge，进行等比压缩；如果只指定一边，则另一边自适应 |
| /1/w/&lt;Width&gt;/h/&lt;Height&gt;      | 限定缩略图的宽和高的最小值分别为Width和Height，进行等比压缩，剧中裁剪；如果只指定一边，则表示宽高相等的正方形；缩放后的图片的大小为&lt;Width&gt;x&lt;Height&gt;（其中一边多余的部分会被裁剪掉） |
| /2/w/&lt;Width&gt;/h/&lt;Height&gt;      | 限定缩略图的宽和高的最大值分别为Width和Height，进行等比压缩；如果只指定一边，则另一边自适应 |
| /3/w/&lt;Width&gt;/h/&lt;Height&gt;      | 限定缩略图的宽和高的最小值分别为Width和Height，进行等比压缩；如果只指定一边，代表另外一边为同样的值 |
| /4/w/&lt;LongEdge&gt;/h/&lt;ShortEdge&gt; | 限定缩略图的长边和短边的最小值分别为LongEdge和ShortEdge，进行等比压缩；如果只指定一边，代表另外一边为同样的值 |
| /5/w/&lt;LongEdge&gt;/h/&lt;ShortEdge&gt; | 限定缩略图的长边和短边的最大值分别为LongEdge和ShortEdge，进行等比压缩，居中裁剪；如果只指定一边，则表示宽高相等的正方形；同模式1，缩放后其中一边多余的部分会被裁剪掉 |
| /format/&lt;Format&gt;                   | 目标缩略图的图片格式，Format可为：jpg, bmp, gif, png, webp,yjpeg等，其中yjpeg为万象优图针对jpeg格式进行的优化，本质为jpg格式；缺省为原图格式 |
| /q/&lt;Quality&gt;                              | 图片质量，取值范围0-100，默认值为原图质量；取原图质量和指定质量的最小值；&lt;Quality&gt; 后面加！，表示强制使用指定值 |

## 4. 示例

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageView2/0/w/400/h/300
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageView2/1/w/400/h/600/q/85
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageView2/2/w/400/h/600/q/85!
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageView2/3/w/400/format/png
```

### 