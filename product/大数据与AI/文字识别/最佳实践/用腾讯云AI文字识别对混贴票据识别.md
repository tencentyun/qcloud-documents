
在企业经营活动中，一直伴随着种类繁多的票据，包括增值税发票、定额发票、通用机打发票、差旅报销发票等等。在财务做归档整理过程中，使用手工方式对多张混贴票据信息进行统计和整理也一直是一项非常繁重的工作，而且非常容易出错；特别是存在大量多张混贴票据进行识别的场景下，环境的复杂性也影响着票据识别和分类的准确度。




那么，有没有这么一款产品：可以对多张不同类型的混贴票据进行智能识别和分类呢？



经过对国内外票据识别的产品进行调研和试用，发现腾讯云AI文字识别的混贴票据识别就非常契合，且具有高易用性、高性价比。



一番深入了解后，发现腾讯云AI文字识别混贴票据识别支持单张、多张、多类型票据的混合识别；同时支持自选需要识别的票据类型，已支持票种包括：增值税发票（专票、普票、卷票）、全电发票、非税发票、定额发票、通用机打发票、购车发票、火车票、出租车发票、机票行程单、汽车票、轮船票、过路过桥费发票共14种标准报销发票，实现了全自动的模式。也支持对混贴票据进行分类返回分类后的发票图片，方便发票整理、统计、审核，极大地减轻了财税人员的工作量。



接下来，我将详细讲述是如何使用腾讯云AI文字识别的混贴票据识别能力。

## 一、准备工作
为了使用腾讯云 AI 文字识别的混贴票据识别能力，需要先进行一些准备工作。

### 1.1 使用官网的体验服务
腾讯云 AI 文字识别提供了体验服务（[功能演示页面](https://cloud.tencent.com/act/event/ocrdemo)），我们先对混贴票据的识别能力进行了体验，识别的效果很不错可以对多种类型的票据进行识别和内容提取，给了我一个非常好的体验。


#### 1.1.1 发票信息识别
![](https://qcloudimg.tencent-cloud.cn/raw/6528f03a65b7ec98a8fd89fa7b0bb6df.png)
这次体验了同时对三张不同类型的票据进行识别，识别结果中包含三张票据的详细信息。

增值税发票涵盖了票据类型、旋转角度、位置信息、内容、发票代码、发票号码、打印发票代码、打印发票号码、开票日期、购买方名称、密码区、购买方地址、电话、销售方开户行及账号、地址等信息。

过路过桥费发票涵盖了旋转角度位置信息、内容、发票名称、发票代码、发票号码、入口、出口、金额、时间、发票消费类型、日期、高速标志等信息。

火车票涵盖了旋转角度、位置信息、内容、编号、出发站、车次、到达站、出发时间、座位号、票价、席别、身份证号、姓名、序列号、售票站、仅供报销使用、发票消费类型、发票类型等信息。

识别结果相当详细，票据上的信息也全部识别返回。

#### 1.1.2 发票类别识别
![](https://qcloudimg.tencent-cloud.cn/raw/5dc1ffc0bdf731b93e82ccc23748631e.png)
这次体验了同时对三张不同类型的票据进行识别，可以通过设置 "ReturnImage" 参数为 true 将发票按照分类截切后以 base64 返回。将 base64 编码的图片转换后如下：
![](https://qcloudimg.tencent-cloud.cn/raw/2abaaa63e1f3efb44e6e3ebbd7338fb7.png)
![](https://qcloudimg.tencent-cloud.cn/raw/0cd49b2edcbdb82eef4eebf31a328094.png)![](https://qcloudimg.tencent-cloud.cn/raw/3c4ae8ef3d8343b2910ff7dd069f1582.png)

### 1.2 开通文字识别服务
在使用腾讯云 AI 文字识别之前，通过腾讯云 OCR [控制台页面](https://console.cloud.tencent.com/ocr/v2/overview) 开通文字识别服务。
![](https://qcloudimg.tencent-cloud.cn/raw/1d2e1fd8d5e4e3d5463bde03bbbc164a.png)
服务开通成功后，腾讯云AI文字识别赠送了免费的资源包，其中通用票据识别有1000次的免费额度，可以在资源包管理页面查看资源包使用情况。
![](https://qcloudimg.tencent-cloud.cn/raw/d1aa473922019890d4c5919b393d7954.png)
另外，还可以在 [设置页面](https://console.cloud.tencent.com/ocr/settings) 开通后付费服务，这样就不用担心资源包耗尽导致调用接口失败了，但是后付费设置每月只能变更一次。
![](https://qcloudimg.tencent-cloud.cn/raw/f69b21e202934e7666e63831e72d73a5.png)

### 1.3 控制台监控信息

经过使用了解到所有文字识别服务的使用情况都可以在 [控制台](https://console.cloud.tencent.com/ocr/overview) 中查看使用信息，可以从下图看到统计出当前月份的调用情况、计费情况、成功数、成功率等。
![](https://qcloudimg.tencent-cloud.cn/raw/e37fac04d5b37881d50742a5d341b108.png)

## 二、操作流程
接下来，通过下面几个步骤就可以使用腾讯云 AI 文字识别的混贴票据识别功能。
- 获取个人密钥
- 查看混贴票据 API 文档
- 财务混贴票据识别和分类产品实现
- 查询调用量

### 2.1 获取个人密钥
在腾讯云访问管理的 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，我们新建一个个人密钥。
![](https://qcloudimg.tencent-cloud.cn/raw/b68fad0fd116bf1a2b5dee0d5ba8ae1c.png)
复制生成的密钥，可以 [单击此处](https://console.cloud.tencent.com/cam/capi) 可直达。
![](https://qcloudimg.tencent-cloud.cn/raw/2d37ff80703e6d664b7b81fb3b10248c.png)

### 2.2 查看混贴票据 API 文档
可以在 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=MixedInvoiceOCR&SignVersion=) 中选择文字识别服务—混贴票据识别—输入参数—选择需要的语言—即可生成对应语言的 API 调用代码。
![](https://qcloudimg.tencent-cloud.cn/raw/9993acb95a8f2d9a543fd469bd1655f1.png)

#### 2.2.1 API 参数说明
**1.  请求 API 参数**
请求 API 参数需要指定服务的接口，产品的版本号，地域等参数，如果使用 base64 格式的图片就需要设置 ImageBase64，如果使用 PNG、JPG、JPEG、PDF 这类图片可以使用 ImageUrl，也可以指定发票类型，如果不指定默认为识别所有发票。
**2.  响应 API 参数**
我在测试过程中了解到当 Code 响应为 ok 表示识别成功，在 Type 中存放的是发票的类型，还会返回图片在发票中的位置，以及识别的内容和分类后的图片。 

### 2.3 财务混贴票据识别和分类产品实现
在财务混贴票据识别和分类产品实现过程中主要分为一下几个步骤：
- 安装环境依赖的 SDK。
- 使用 gin 框架来提供服务的支持。
- 调用混贴票据识别和分类接口。
- 将识别后的结果和图片写入 Excel。

#### 2.3.1 环境搭建
1. 安装 SDK
```
#	安装公共基础包
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common
#	安装对应的产品包（如 CVM）
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm
#	一次性下载腾讯云所有产品的包
go get -v -u github.com/tencentcloud/tencentcloud-sdk-go
```
2. 服务启动程序
这里是启动整个产品的服务。
```
//初始化配置
func initInfo() (*ocr.Client,error){
	// 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
	// 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
	credential := common.NewCredential( 
		"SecretId",
		"SecretKey",
	)
	// 实例化一个client选项，可选的，没有特殊需求可以跳过
	cpf := profile.NewClientProfile()
	cpf.HttpProfile.Endpoint = "ocr.tencentcloudapi.com"
	// 实例化要请求产品的client对象,clientProfile是可选的
	client, err := ocr.NewClient(credential, "ap-beijing", cpf) //这里注入了API密钥，区域，
	return client,err
}
//上传发票图片实现识别发票类别信息识别和分类
func UploadImageToMixedInvoiceOCR(c *gin.Context,) {
	//接受上传的图片
	file, image, err := c.Request.FormFile("image")
	if err != nil {
		code = e.ERROR
		c.JSON(http.StatusOK, gin.H{
			"code": code,
			"msg":  e.GetMsg(code),
			"data": data,
		})
	}
	//调用混合识别接口
	invoiceData := MixedInvoiceOCR(client)
	
	//调用分类识别接口
	invoiceImages := MixedInvoiceDetect(client)
	
	//将识别的结果和图片写入excel
	InvoiceToExcel(invoiceData,invoiceImages)
	
	// 如果写入成功返回响应消息
	c.JSON(200, gin.H{
		"message": code.SUCCESS,
	})
}

func main() {
	//创建默认服务
	r := gin.Default()

	//初始化配置
	client, err = initInfo()

	//注册路由
	r.GET("/uploadImageToMixedInvoiceOCR",UploadImageToMixedInvoiceOCR)

	// 启动HTTP服务
	err = r.Run()
	if err != nil {
		return
	}
}
```
3. 混合发票信息识别实现
通过混合发票的信息识别的接口可以获得发票识别后的响应结果。
``` 
func MixedInvoiceOCR(client *ocr.Client) string{
	// 实例化要请求产品的client对象,clientProfile是可选的
	client, _ := ocr.NewClient(credential, "ap-beijing", cpf) //这里注入了API密钥，区域，

	// 实例化一个请求对象,每个接口都会对应一个request对象
	request := ocr.NewMixedInvoiceOCRRequest()

  //设置需要识别混贴票据的信息
	request.ImageUrl = common.StringPtr("图片地址url")

	// 返回的resp是一个MixedInvoiceOCRResponse的实例，与请求对象对应
	response, err := client.MixedInvoiceOCR(request)
	if _, ok := err.(*errors.TencentCloudSDKError); ok {
		fmt.Printf("An API error has returned: %s", err)
		return
	}
	if err != nil {
		log.Fatal(err)
	}
	// 输出json格式的字符串回包
	fmt.Printf("%s", response.ToJsonString())
}
4）混合发票分类实现
通过混合发票分类接口可以返回混合发票分类后的图片。

func MixedInvoiceDetect(client *ocr.Client) *ocr.MixedInvoiceDetectResponse{
  
  // 实例化一个请求对象,每个接口都会对应一个request对象
  request := ocr.NewMixedInvoiceDetectRequest()

  request.ImageUrl = common.StringPtr("https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/invoice/MixedInvoiceDetect/MixedInvoiceDetect1.jpg")
  request.ReturnImage = common.BoolPtr(true)
  // 返回的resp是一个MixedInvoiceOCRResponse的实例，与请求对象对应
  response, err := client.MixedInvoiceDetect(request)
  if _, ok := err.(*errors.TencentCloudSDKError); ok {
    fmt.Printf("An API error has returned: %s", err)
    return
  }

  // 输出json格式的字符串回包
  //fmt.Printf("%s", response.ToJsonString())
  for i, info := range response.Response.InvoiceDetectInfos {
    fmt.Printf("第%v张发票，base64是%v\v",i,info)
    err = InvoiceToExcel(i, *info.Image)
  }

  if err != nil {
    log.Fatal(err)
  }
}

func writeFile(i int,s string) error{
  //解析base64字符串
  dist, _ := base64.StdEncoding.DecodeString(s)
  //写入新文件
  f, _ := os.OpenFile("data"+strconv.Itoa(i)+".png", os.O_RDWR|os.O_CREATE, os.ModePerm)
  defer f.Close()
  _, err := f.Write(dist)
  return err
}
```
5. 数据导出实现
将混合发票识别接口返回的发票信息和混合发票接口分类后的发票图片写入 Excel。
```
func InvoiceToExcel(invoiceInfo invoiceData,fileImage string) {
  excel := xlsx.newfile()

  // 新建一个sheet
  sheet, err := excel.addsheet("sheet1")
  if err != nil {
    t.fatal(err)
  }
  // 创建首行
  headerrow := sheet.addrow()

  // 设置行高
  headerrow.setheightcm(0.5)

  // 填充行中的单元格
  for _, line := range invoiceInfo {
    row := sheet.addrow()
    row.setheightcm(0.5)
    ...
    for _, v := range line {
      row.addcell().value = v
      ...
    }
  }
  // 持久化到磁盘
  if err := excel.save(fileName+".xlsx"); err != nil {
    t.fatal(err)
  }
}
```

#### 2.3.2 产品结果展示
下面是使用腾讯云 AI 文字识别混贴票据识别功能，做出的一款方便财务对发票进行统计和整理、审核的一个产品，这个产品可以将输入的混贴发票图片进行分类和识别，最终输出到 Excel 中，其中 Excel 中包含了混贴发票的所有信息和分类后的图片，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/36272ed2fa6dc5a40846608c775b9f94.png)
我们通过混合发票接口响应回来的 json 数据，Type 类型可以获取到发票类型，Image 可以获取分类后的图片。

### 2.4 查询调用量
接口调用成功后，我们可以在 [腾讯云文字识别控制台](https://console.cloud.tencent.com/ocr/stats) 查看接口的调用明细，包括调用量、成功量、失败量、错误码等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/5e7040983f4ec18b3fcac0d2e8b35918.png)
使用过程中发现主账号登录后可以查看所有账号的调用量明细，子账号只能查询自己的调用量明细。

如果想要让子账号也有权限查看所有账号的调用明细，就在 [用量查询权限管理页面](https://console.cloud.tencent.com/ocr/permission) 给子账号赋权，这样子账号也可以查询到所有账号的调用量了。
![](https://qcloudimg.tencent-cloud.cn/raw/f4c28bf75b79d4d03ea81e67e1f1ca31.png)

单击了解更多 [腾讯云 AI 票据单据识别能力](https://cloud.tencent.com/product/invoiceocr)。
