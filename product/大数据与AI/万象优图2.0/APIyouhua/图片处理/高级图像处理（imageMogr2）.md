## 1.  简介

+ imageMogr2是腾讯云·万象优图为开发者提供的简单而功能强大的高级图像处理接口，包括旋转、智能裁剪、获取exif信息、格式转换等功能。
+ 裁剪为缩放裁剪，即先将图片进行等比缩放，在进行裁剪。例如：原图为1500x1200，裁剪成600x600，会先将图片缩放为750x600，然后再裁剪成600x600,目前支持 20M 以内文件处理。
+ 本文档为万象优图V2加强版

## 2.  接口形式

注意：请忽略一下接口中的回车。

```
  download_url?imageMogr2/auto-orient
                         /thumbnail/<imageSizeGeometry>
                         /strip
                         /gravity/<gravityType>
                         /crop/<imageSizeAndOffsetGeometry>
                         /scrop/<imageSizeAndOffsetGeometry>
                         /rotate/<rotateDegree>
                         /format/<Format>
                         /quality/<Quality>
                         /cgif/<FrameNumber>
                         /interlace/<Mode>
```

## 3. 参数说明

| 参数                                      | 含义                                       |
| --------------------------------------- | ---------------------------------------- |
| /auto-orient                            | 根据原图的exif信息自动把图片旋转回正。                    |
| /strip                                  | 去除不安全代码包括exif信息。                         |
| /gravity/&lt;gravityType&gt;                 | 图片处理位置，影响其后的裁剪偏移参数，参见下面九宫格方位，默认值为中间：Center。 |
| /thumbnail/&lt;imageSizeAndOffsetGeometry&gt; | 参考下面的缩放操作参数表。                            |
| /crop/&lt;imageSizeAndOffsetGeometry&gt;      | 请参考下面的裁剪参数表，缺省不裁剪。                       |
| /scrop/&lt;imageSizeAndOffsetGeometry&gt;     | 基于人脸识别执行智能裁剪功能。裁剪区域根据人的头像位置自动确定。 输出的裁剪后图片大小需要结合宽高参数指定。参考下面的智能裁剪参数表。 |
| /rotate/&lt;rotateDegree&gt;                  | 图片旋转角度，取值范围0-360，默认不旋转。                  |
| /format/&lt;Format&gt;                        | 目标缩略图的图片格式，Format可为：jpg, bmp, gif, png, webp,yjpeg等，其中yjpeg为万象优图针对jpeg格式进行的优化，本质为jpg格式；缺省为原图格式。 |
| /quality/&lt;Quality&gt;                      | 图片质量，取值范围0-100，默认值为原图质量；取原图质量和指定质量的最小值；&lt;Quality&gt;后面加！，表示强制使用指定值，如：90！。 |
| /cgif/&lt;FrameNumber&gt;                     | 只针对原图为gif格式，对gif图片格式进行的优化，降帧降颜色。分为以下两种情况：FrameNumber=1，则按照默认帧数30处理，如果图片帧数大于该帧数则截取；FrameNumber取值(1,100]，则将图片压缩到指定帧数FrameNumber。 |
| /interlace/&lt;Mode&gt;                       | 输出为渐进式jpg格式。Mode可为0或1,0表示不开启渐进式；1表示开启渐进式。该参数仅在输出图片格式为jpg格式时有效。如果输出非jpg图片格式，会忽略该参数，默认值0。 |

### 3.1 缩放操作表格

| 参数                                  | 含义                                       |
| ----------------------------------- | ---------------------------------------- |
| /thumbnail/!&lt;Scale&gt;p                | 指定图片的宽高为原图的Scale%                        |
| /thumbnail/!&lt;Scale&gt;px               | 指定图片的宽为原图的Scale%，高度不变                    |
| /thumbnail/!x&lt;Scale&gt;p               | 指定图片的高为原图的Scale%，宽度不变                    |
| /thumbnail/&lt;Width&gt;x                 | 指定目标图片宽度为Width，高度等比压缩                    |
| /thumbnail/x&lt;Height&gt;                | 指定目标图片高度为Height，宽度等比压缩                   |
| /thumbnail/&lt;LongEdge&gt;x&lt;ShortEdge&gt;   | 限定缩略图的长边和短边的最大值分别为LongEdge和ShortEdge，进行等比缩放 |
| /thumbnail/!&lt;LongEdge&gt;x&lt;ShortEdge&gt;r | 限定缩略图的长边和短边的最小值分别为LongEdge和ShortEdge，进行等比缩放 |
| /thumbnail/&lt;Width&gt;x&lt;Height&gt;!        | 忽略原图宽高比例，指定图片宽度为Width，高度为Height，强行缩放图片，可能导致目标图片变形 |
| /thumbnail/&lt;Area&gt;@                  | 等比缩放图片，缩放后的图像，总像素数量不超过Area                   |



```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/!50p
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/!50px
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/!x50p
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/200x
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/200x400!
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/thumbnail/35000@
```

### 3.2 九宫格方位图

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/apicankao-3.jpg)

### 3.3 裁剪操作

**普通裁剪操作表格（cropSize）**

| 参数                     | 含义                                       |
| ---------------------- | ---------------------------------------- |
| /crop/&lt;Width&gt;x         | 指定目标图片宽度为Width，高度不变。Width取值范围为10-16383   |
| /crop/x&lt;Height&gt;       | 指定目标图片高度为Height，宽度不变。Height取值范围为10-16383 |
| /crop/&lt;Width&gt;x&lt;Height&gt; | 指定目标图片宽度为Width，高度为Height。Width和Height取值范围都为10-16383 |

**智能裁剪操作表格（scropSize）**

基于人脸识别执行智能裁剪功能。裁剪区域根据人的头像位置自动确定。 输出的裁剪后图片大小需要结合宽高参数指定。

| 参数                      | 含义                                       |
| ----------------------- | ---------------------------------------- |
| /scrop/&lt;Width&gt;x         | 指定目标图片宽度为Width，高度不变。Width取值范围为10-16383   |
| /scrop/x&lt;Height&gt;        | 指定目标图片高度为Height，宽度不变。Height取值范围为10-16383 |
| /scrop/&lt;Width&gt;x&lt;Height&gt; | 指定目标图片宽度为Width，高度为Height。Width和Height取值范围都为10-16383 |

开发者可以指定裁剪的具体偏移位置，如下表所示：

| 参数                          | 含义                                       |
| --------------------------- | ---------------------------------------- |
| /crop/!{cropSize}a&lt;dx&gt;a&lt;dy&gt; | 相对于偏移位置，水平向右偏移dx，同时垂直向下偏移dy。取值范围小于原图宽高即可 |
| /crop/!{cropSize}-&lt;dx&gt;a&lt;dy&gt; | 相对于偏移位置，从指定宽度中减去dx，同时垂直向下偏移dy。取值范围小于原图宽高即可 |
| /crop/!{cropSize}a&lt;dx&gt;-&lt;dy&gt; | 相对于偏移位置，水平向右偏移dx，同时从指定高度中减去dy。取值范围小于原图宽高即可 |
| /crop/!{cropSize}-&lt;dx&gt;-&lt;dy&gt; | 相对于偏移位置，从指定宽度中减去dx个像素，同时从指定高度中减去dy个像素。取值范围小于原图宽高即可 |

例如：
/crop/!600x600a20a20: 表示从原图的坐标（x,y）为（20,20）的位置裁剪600x600的缩略图。
/crop/!600x600-20a20: 表示从原图的坐标（x,y）为（0,20）的位置裁剪580x600的缩略图。
注意：scrop 参数与 crop 参数同时使用，当智能裁剪没有识别到人脸时，会执行普通的裁剪。 要求使用的宽高参数一致，否则输出图片宽高是两个宽高参数中的一个。
http://v2enhance-10000812.image.myqcloud.com/tencentyunRestfulAPITest?imageMogr2/scrop/300x400/crop/300x400

## 4. 示例：

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/crop/!600x600a20a20/quality/85
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/crop/!600x600-20a20/quality/85!
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/format/jpg/interlace/1
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?imageMogr2/scrop/300x400
```
