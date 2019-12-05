## 接口描述

腾讯云•万象优图支持实时图片水印处理功能，目前，水印图片必须指定为已存储于万象优图中的图片。

接口形式：请忽略一下接口中的回车。

```
  download_url?watermark/1
                        /image/<encodedImageURL>
                        /gravity/<gravity>
                        /dx/<distanceX>
                        /dy/<distanceY>
```

## 参数说明

| 参数                       | 含义                                       |
| ------------------------ | ---------------------------------------- |
| /image/<encodedImageURL> | 水印源图片地址，需要经过URL安全的Base64编码。指定的水印图片必须存在于万象优图中。 |
| /gravity/<gravity>       | 文字水印位置，九宫格位置，参见8.2.2节的九宫格方位图，默认值SouthEast |
| /dx/<distanceX>          | 水平（横轴）边距，单位为像素，缺省值为0                     |
| /dy/<distanceY>          | 垂直（纵轴）边距，单位像素，默认值为0                      |

## 示例

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestAPITest?watermark/1
       /image/aHR0cDovL3Rlbmd4dW55dW4tMTAwMDQ0ODYuaW1hZ2UubXlxY2xvdWQuY29tL3NodWl5aW5fMi5wbmc=/gravity/southwest
```

### 