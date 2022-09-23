## 简介

本文档提供关于通用文字识别的 API 概览以及 SDK 示例代码。

| API                                                          | 说明       |
| :----------------------------------------------------------- | :--------- |
| [通用文字识别](https://cloud.tencent.com/document/product/436/64324) | 通用文字识别功能（Optical Character Recognition，OCR）基于行业前沿的深度学习技术，将图片上的文字内容，智能识别为可编辑的文本，可应用于随手拍扫描、纸质文档电子化、电商广告审核等多种场景，大幅提升信息处理效率。|


## 通用文字识别

#### 功能说明

通用文字识别。

#### 方法原型

```go
func (s *CIService) OcrRecognition(ctx context.Context, key string, opt *OcrRecognitionOptions) (*OcrRecognitionResult, *Response, error)
```

#### 请求示例

```go
obj := "pic/ocr.png"
opt := &cos.OcrRecognitionOptions{
    Type:              "general",
    LanguageType:      "zh",
    Isword:            true,
    EnableWordPolygon: true,
}
res, _, err := c.CI.OcrRecognition(context.Background(), obj, opt)
```

#### 参数说明

| 参数名称  | 参数描述                                                     |
| --------- | ------------------------------------------------------------ |
| key       | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名`examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/pic/pic.jpg`中，对象键为 pic/pic.jpg |
| opt       | 通用文字识别的参数 |

#### 结果说明

```go
type OcrRecognitionResult struct {
	XMLName        xml.Name         `xml:"Response"`
	TextDetections []TextDetections `xml:"TextDetections,omitempty"`
	Language       string           `xml:"Language,omitempty"`
	Angel          float64          `xml:"Angel,omitempty"`
	PdfPageSize    int              `xml:"PdfPageSize,omitempty"`
	RequestId      string           `xml:"RequestId,omitempty"`
}

type TextDetections struct {
	DetectedText string        `xml:"DetectedText,omitempty"`
	Confidence   int           `xml:"Confidence,omitempty"`
	Polygon      []Polygon     `xml:"Polygon,omitempty"`
	ItemPolygon  []ItemPolygon `xml:"ItemPolygon,omitempty"`
	Words        []Words       `xml:"Words,omitempty"`
	WordPolygon  []WordPolygon `xml:"WordPolygon,omitempty"`
}

type Polygon struct {
	X int `xml:"X,omitempty"`
	Y int `xml:"Y,omitempty"`
}

type ItemPolygon struct {
	X      int `xml:"X,omitempty"`
	Y      int `xml:"Y,omitempty"`
	Width  int `xml:"Width,omitempty"`
	Height int `xml:"Height,omitempty"`
}

type Words struct {
	Confidence     int             `xml:"Confidence,omitempty"`
	Character      string          `xml:"Character,omitempty"`
	WordCoordPoint *WordCoordPoint `xml:"WordCoordPoint,omitempty"`
}

type WordCoordPoint struct {
	WordCoordinate []Polygon `xml:"WordCoordinate,omitempty"`
}

type WordPolygon struct {
	LeftTop     *Polygon `xml:"LeftTop,omitempty"`
	RightTop    *Polygon `xml:"RightTop,omitempty"`
	RightBottom *Polygon `xml:"RightBottom,omitempty"`
	LeftBottom  *Polygon `xml:"LeftBottom,omitempty"`
}
```
