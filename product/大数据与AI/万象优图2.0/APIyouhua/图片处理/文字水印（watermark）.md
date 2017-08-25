### 接口描述

腾讯云·万象优图支持实时文字水印功能，即通过在图片URL后面附加参数为图片实时打文字水印。

接口形式：请忽略一下接口中的回车。

```
  download_url?watermark/2
                        /text/<encodedText>
                        /font/<encodedFontName>
                        /fontsize/<fontSize>
                        /fill/<encodedTextColor>
                        /dissolve/<dissolve>
                        /gravity/<gravity>
                        /dx/<distanceX>
                        /dy/<distanceY>
```

## 参数说明

| 参数                       | 含义                                       |
| ------------------------ | ---------------------------------------- |
| /text/<encodedText>      | 水印内容，需要经过URL安全的Base64编码                  |
| /font/<encodedFontName>  | 水印字体，需要经过URL安全的Base64编码，默认值tahoma.ttf。水印字体列表参考[支持字体列表](/doc/product/275/万象优图支持字体列表) |
| /fontsize/<fontSize>     | 水印文字字体大小，单位是: 磅，缺省值13                    |
| /fill/<encodedTextColor> | 字体颜色，缺省为白色，RGB格式，可以是颜色名称（如blue）或者十六进制（如#FF0000），参考[RGB编码表](http://www.rapidtables.com/web/color/RGB_Color.htm)，需经过URL安全的Base64编码，默认值#3D3D3D |
| /dissolve/<dissolve>     | 文字透明度，取值1-100，默认100（完全不透明）               |
| /gravity/<gravity>       | 文字水印位置，九宫格位置，参见8.2.2节的九宫格方位图，默认值SouthEast |
| /dx/<distanceX>          | 水平（横轴）边距，单位为像素，缺省值为0                     |
| /dy/<distanceY>          | 垂直（纵轴）边距，单位像素，默认值为0                      |

## 示例

```
http://v2test-10000812.image.myqcloud.com/tencentyunRestfulAPITest?watermark/2
       /text/6IW-6K6v5LqRwrfkuIfosaHkvJjlm74=/fill/d2hpdGU=/fontsize/100/dissolve/50/gravity/northeast/dx/20/dy/20
```

