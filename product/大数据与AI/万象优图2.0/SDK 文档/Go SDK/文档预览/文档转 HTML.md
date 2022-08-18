## 简介

本文档提供关于文档预览同步请求的 API 概览以及 SDK 示例代码。

| API  |	说明  |
|----|-----|
| [文档转 HTML](https://cloud.tencent.com/document/product/436/54059)  | 文档转 HTML 功能支持对多种文档类型的文件生成 HTML 格式预览，满足 PC、App 等多个用户端的文档在线浏览需求，适用于在线教育、企业 OA、在线知识库、网盘文档预览等业务场景。 | 


## 文档转 HTML

#### 功能说明

支持对多种文档类型的文件生成 HTML 格式预览。

#### 方法原型

```go
func (s *CIService) DocPreviewHTML(ctx context.Context, name string, opt *DocPreviewHTMLOptions) (*Response, error)
```

#### 请求示例

```go
opt := &cos.DocPreviewHTMLOptions{
    DstType:  "html",
    SrcType:  "ppt",
    Copyable: "1",
    HtmlParams: &cos.HtmlParams{
        CommonOptions: &cos.HtmlCommonParams{
            IsShowTopArea: false,
        },
        PptOptions: &cos.HtmlPptParams{
            IsShowBottomStatusBar: true,
        },
    },
    Htmlwaterword:  "5pWw5o2u5LiH6LGhLeaWh+aho+mihOiniA==",
    Htmlfillstyle:  "cmdiYSgxMDIsMjA0LDI1NSwwLjMp", // rgba(102,204,255,0.3)
    Htmlfront:      "Ym9sZCAyNXB4IFNlcmlm",         // bold 25px Serif
    Htmlrotate:     "315",
    Htmlhorizontal: "50",
    Htmlvertical:   "100",
}
resp, err := c.CI.DocPreviewHTML(context.Background(), "form.pdf", opt)
```

#### 参数说明

```go
type DocPreviewHTMLOptions struct {
	DstType        string      `url:"dstType,omitempty"`
	SrcType        string      `url:"srcType,omitempty"`
	Sign           string      `url:"sign,omitempty"`
	Copyable       string      `url:"copyable,omitempty"`
	HtmlParams     *HtmlParams `url:"htmlParams,omitempty"`
	Htmlwaterword  string      `url:"htmlwaterword,omitempty"`
	Htmlfillstyle  string      `url:"htmlfillstyle,omitempty"`
	Htmlfront      string      `url:"htmlfront,omitempty"`
	Htmlrotate     string      `url:"htmlrotate,omitempty"`
	Htmlhorizontal string      `url:"htmlhorizontal,omitempty"`
	Htmlvertical   string      `url:"htmlvertical,omitempty"`
}

type HtmlParams struct {
	CommonOptions *HtmlCommonParams `json:"commonOptions,omitempty"`
	WordOptions   *HtmlWordParams   `json:"wordOptions,omitempty"`
	PdfOptions    *HtmlPdfParams    `json:"pdfOptions,omitempty"`
	PptOptions    *HtmlPptParams    `json:"pptOptions,omitempty"`
}

type HtmlCommonParams struct {
	IsShowTopArea           bool `json:"isShowTopArea"`
	IsShowHeader            bool `json:"isShowHeader"`
	IsBrowserViewFullscreen bool `json:"isBrowserViewFullscreen"`
	IsIframeViewFullscreen  bool `json:"isIframeViewFullscreen"`
}

type HtmlWordParams struct {
	IsShowDocMap          bool `json:"isShowDocMap"`
	IsBestScale           bool `json:"isBestScale"`
	IsShowBottomStatusBar bool `json:"isShowBottomStatusBar"`
}

type HtmlPdfParams struct {
	IsShowComment         bool `json:"isShowComment"`
	IsInSafeMode          bool `json:"isInSafeMode"`
	IsShowBottomStatusBar bool `json:"isShowBottomStatusBar"`
}

type HtmlPptParams struct {
	IsShowBottomStatusBar bool `json:"isShowBottomStatusBar"`
}

```


| 名称        | 参数说明                                                         | 类型   | 是否必选 |
| ----------- | ------------------------------------------------------------ | ------ | -------- |
| DstType   | 转换输出目标文件类型，文档 HTML 预览固定为 html（需为小写字母）  | String  | 是       |  
| SrcType | 指定目标文件类型，支持的文件类型请见 [文档转 HTML](https://cloud.tencent.com/document/product/436/54059) 文档   | String | 否 |
| Sign          | 对象下载签名，如果预览的对象为私有读时，需要传入签名，详情请参见 [请求签名](https://cloud.tencent.com/document/product/460/6968) 文档</br>注意：需要进行 urlencode  | String | 否      | 
| Copyable          | 是否可复制。默认为可复制，填入值为1；不可复制，填入值为0     | String   | 否      | 
| HtmlParams          | 自定义配置参数，json结构，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认配置为：{ commonOptions: { isShowTopArea: true, isShowHeader: true } }，支持的配置参考 [自定义配置项说明](https://cloud.tencent.com/document/product/436/59408#.E8.87.AA.E5.AE.9A.E4.B9.89.E9.85.8D.E7.BD.AE.E9.80.89.E9.A1.B9)    | String   | 否   |
| Htmlwaterword          | 水印文字，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为空     | String  | 否      | 
| Htmlfillstyle          | 水印 RGBA（颜色和透明度），需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为：rgba(192,192,192,0.6)  | String   | 否      | 
| Htmlfront          | 水印文字样式，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为：bold 20px Serif    | String   | 否      | 
| Htmlrotate          | 水印文字旋转角度，0 - 360，默认315度  | String   | 否      | 
| Htmlhorizontal          | 水印文字水平间距，单位 px，默认为50  | String | 否      | 
| Htmlvertical          | 水印文字垂直间距，单位 px，默认为100  | String | 否      | 

