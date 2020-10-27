## SDK 接口说明    

小程序端文字识别 SDK 主要涉及的有 start 方法，下面对该方法做出详细说明。

## 调用示例

```javascript
ocrSdk.start({
  getAuthorization: function() {
    return new Promise((resolve, reject) => {
      wx.request({
        url: '您服务器端获取临时密钥的接口地址', // 填写您服务器端的接口地址，获取临时密钥
        method: "POST",
        data: {
          option // 您自定义的参数
        },
        success(res) {
          let credentials = res.Credentials;
          resolve({
            secretId: credentials.TmpSecretId,
            secretKey: credentials.TmpSecretKey,
            token: credentials.Token,
          })
        },
        fail(err) {
          resolve(err)
          wx.navigateTo({
            url: '您的小程序页面',
          });
        }
      })
    })
  },
  secretId: '**************', // 不推荐在生产环境中使用固定密钥
  secretKey: '**************', // 不推荐在生产环境中使用固定密钥
  ocrType: ocrSdk.OcrType.ID_CARD,
  ocrOption: {
    Config: {
      "CropIdCard": true,
      "CropPortrait": true,
    }
  },
  resultPageConfig: {
    modifiable: true,
    themeColor: 'red',
  },
  resultPage: true,
  success: (res) => {
    console.log('ocr result is:', res)
    wx.navigateTo({
      url: '您的小程序页面',
    })
  },
  fail: (error)=> {
    console.log('ocr failed:', error)
  }
});
```

## 参数简介

| 参数名称                                | 参数简介       |    参数类型  |  默认值     |  是否必选   |
| ------------------------------------- | ------------- | ----------- | ------     | -------- |
| [getAuthorization](#getAuthorization:) | 获取临时密钥的方法 |   function  |  无    |  否（注：生产环境中强烈推荐使用该方法）  |
| [secretId](#secretId:)                 | SecretId 密钥  |    string   |  无  |  否（注：仅推荐在本地开发时使用）   |
| [secretKey](#secretKey:)               | SecretKey 密钥  |   string    |  无    |  否（注：仅推荐在本地开发时使用）   |
| [ocrType](#ocrType:)                   | OCR 识别类型    |   ocrType  |  无  |  是   |
| [ocrOption](#ocrOption:)             | OCR 识别可选项             |    Object    |  无  |  否   |
| [resultPage](#resultPage:)             | 识别完成后是否需要展示结果页  |     boolean     |  false  |  否   |
| [resultPageConfig](#resultPageConfig:) | 结果页相应配置  |     Object     |  无 |  否   |
| [resultPageConfig.modifiable](#resultPageConfig.modifiable:)             | 识别结果是否可修改  |     boolean     |  false  |  否   |
| [resultPageConfig.themeColor](#resultPageConfig.themeColor:)             | 结果页主题色  |     string     |  #006EFF  |  否   |
| [success](#success:)             | 单击完成后执行的回调函数            |   function(res)   |   无   |  是   |
| [fail](#fail:)             | 识别失败时执行的回调函数             |    function(error)   |   无   |  否   |

<br/>

<span id="getAuthorization:"></span>
### getAuthorization:
获取临时密钥的方法。

小程序 SDK 将在每次调用 OCR 请求时调用该方法，获取最新的临时密钥并做认证签名计算。您只需要在该方法中返回一个 promise，通过 wx.request 方法向后端请求临时密钥。 您在与服务器端完成临时密钥兑换之后，在 wx.request 的 success 回调中将临时密钥 resolve 出来。如果获取密钥失败，只需要将错误 resolve 出来即可，您可以在该方法内定义任意您想要的错误处理方式。SDK 默认弹出获取密钥失败信息。

**OCR SDK 支持使用临时密钥接口，使用临时密钥的好处主要有以下两点，第一将固定密钥与小程序分离可以增加安全性；第二因为兑换临时密钥是您完全可控的行为，因此您可以根据自定义规则来控制最终用户的接口访问权限。因此建议您使用临时密钥的方式，具体可以参考文档 [临时密钥文档与流程链接](https://github.com/TencentCloud/tc-ocr-sdk/tree/master/%E4%B8%B4%E6%97%B6%E5%AF%86%E9%92%A5%E5%85%91%E6%8D%A2)。**

**当同时传入 getAuthorization 与 （secretId，secretKey）时，SDK 会使用 getAuthorization 方法，忽略secretId 和 secretKey**

代码示例：
```javascript
ocrSdk.start({
  getAuthorization: function() {
    return new Promise((resolve, reject) => {
      wx.request({
        url: '您服务器端的接口地址', // 填写您服务器端的接口地址，获取临时密钥
        method: "POST",
        data: {
          option
        },
        success(res) {
          let credentials = res.Credentials;
          resolve({
            secretId: credentials.TmpSecretId,
            secretKey: credentials.TmpSecretKey,
            token: credentials.Token,
          })
        },
        fail(err) {
          resolve(err);
          wx.navigateTo({
            url: '您的小程序页面',
          });
        }
      })
    })
  },
  ...
});
```

<br/>

<span id="secretId:"></span>
### secretId:
SecretId 密钥。将 secretId、secretKey 直接配置到小程序中的方式，会使用固定密钥计算签名，一旦您的密钥泄密，攻击者可以使用您的 secretId、secretKey 信息进行 OCR 识别请求，给您造成损失。因此该方法**仅适用于本地跑通 Demo 和功能调试**

**当同时传入 getAuthorization 与 （secretId，secretKey）时，SDK 会使用 getAuthorization 方法，忽略secretId 和 secretKey**

<br/>

<span id="secretKey:"></span>
### secretKey:
SecretKey 密钥。将 secretId、secretKey 直接配置到小程序中的方式，会使用固定密钥计算签名，一旦您的密钥泄密，攻击者可以使用您的 secretId、secretKey 信息进行 OCR 识别请求，给您造成损失。因此该方法**仅适用于本地跑通 Demo 和功能调试**

**当同时传入 getAuthorization 与 （secretId，secretKey）时，SDK 会使用 getAuthorization 方法，忽略secretId 和 secretKey**

<br/>

<span id="ocrType:"></span>
### ocrType:
ocrType 是一个枚举类型，列举了当前文字识别 OCR 的 SDK 所支持业务类型的种类，大致如下：

| ocrType 类型             | 代表含义             |
| ----------------------- | ------------------- |
| ocrType.ID_Card         | 身份证识别模式        |
| ocrType.Bank_Card       | 银行卡识别模式     |
| ocrType.Business_Card   | 名片识别模式     |

配置了 ocrType 之后，当调用 ocrSdk.start（）方法之后，小程序会前往配置模式对应的页面。

<br/>

<span id="ocrOption:"></span>
### ocrOption:
OCR 识别可选项。
对于不同的识别模式，SDK 提供一些更精细化的可选配置。您可以在 ocrOption 字段中配置这些可选项。
完整的可配置项请参考 [可配置选项](#可配置选项)


代码示例：
```javascript
ocrSdk.start({
  ...
  ocrType: ocrSdk.OcrType.ID_CARD,
  ocrOption: {
    Config: {
      "CropIdCard": true, // 身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）
      "CropPortrait": true // CropPortrait，人像照片裁剪（自动抠取身份证头像区域）
    }
  },
  ...
});
```

<br/>

<span id="resultPage:"></span>
### resultPage:
识别完成后是否展示结果页面。默认不展示。

当该字段配置为 true 时，小程序 SDK 在识别完成之后会进入到结果页，您可以在结果页查看识别结果。
当该字段配置为 false（默认）时，小程序 SDK 在识别完成之后会直接执行您传入的回调函数。

<br/>

<span id="resultPageConfig:"></span>
### resultPageConfig:
结果页配置。本配置项只提供基础配置，如需深度定制，推荐您将 resultPage 配置为 false， 这样您能更灵活的开发您所需的页面。

该字段仅在 resultPage 配置为 true 时才生效。具体配置见下文：


<br/>

<span id="resultPageConfig.modifiable:"></span>
### resultPageConfig.modifiable:
是否允许对 OCR 识别的结果进行修改。默认不允许修改。

该字段仅在 resultPage 配置为 true 时才生效。

当该字段配置为 true 时，小程序在 OCR 识别的结果页中将允许用户对识别结果进行修改。
用户点击“完成”按钮时，SDK 会将修改后的结果作为参数注入到您配置的 success 回调函数中，并执行回调函数。

<br/>

<span id="resultPageConfig.themeColor:"></span>
### resultPageConfig.themeColor:
结果页主题配色，默认为 #006EFF。

<br/>


<span id="success:"></span>
### success:
OCR 识别成功后的回调函数。

当 resultPage 参数配置为 true 时，该回调函数会在结果页单击“完成”时执行。
当 resultPage 参数配置为 false（默认）时，该回调函数会在识别成功时执行。


代码示例：
```javascript
// 用户点击完成后会打印出识别结果，并返回您的小程序页面
ocrSdk.start({
  ...
  success: (res) => {
    console.log('ocr result is:', res)
    wx.navigateTo({
      url: '您的小程序页面',
    })
  },
  ...
});
```

<br/>

<span id="fail:"></span>
### fail:
OCR 识别失败时执行的回调函数。
SDK 在执行该回调函数时会将 OCR 识别结果中的 error 作为参数注入。

代码示例：
```javascript
// 打印出对应的识别错误，并返回您的小程序页面
ocrSdk.start({
  ...
  fail: (error)=> {
    console.log('ocr failed:', error)
    wx.navigateTo({
      url: '您的小程序页面',
    })
  }
  ...
});
```

<br/>

<span id="可配置选项"></span>
## 可配置选项

对于不同的识别模式，SDK 提供一些更精细化的可选配置。您可以在 ocrSdk.start() 方法的 ocrOption 字段中配置这些可选项。

代码示例：
```javascript
ocrSdk.start({
  ...
  ocrType: ocrSdk.OcrType.ID_CARD,
  ...
  ocrOption: {
    Config: {
      "CropIdCard": true, // 身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）
      "CropPortrait": true // CropPortrait，人像照片裁剪（自动抠取身份证头像区域）
    }
  },
  ...
});
```
<br/>

### 身份证识别模式：
| 配置项名称             | 类型             | 描述       |
| ----------------------- | ------------------- |   --------      |
| Config         | Object        |     以下可选字段均为 bool 类型，默认 false：<br/>CropIdCard，身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）<br/>CropPortrait，人像照片裁剪（自动抠取身份证头像区域）<br/>CopyWarn，复印件告警<br/>BorderCheckWarn，边框和框内遮挡告警<br/>ReshootWarn，翻拍告警<br/>DetectPsWarn，PS 检测告警<br/>TempIdWarn，临时身份证告警<br/>InvalidDateWarn，身份证有效日期不合法告警<br/>Quality，图片质量分数（评价图片的模糊程度）<br/>MultiCardDetect，是否开启多卡证检测<br/>ReflectWarn，是否开启反光检测<br/>  |

<br/>

### 名片识别模式：
| 配置项名称             | 类型             | 描述       |
| ----- | ------------------- |   --------      |
| Config   | Object        |    可选字段，根据需要选择是否请求对应字段。<br/>目前支持的字段为：<br/>RetImageType-“PROPROCESS” 图像预处理，string 类型。<br/>图像预处理功能为，检测图片倾斜的角度，将原本倾斜的图片围绕中心点转正，最终输出一张正的名片抠图。   |

<br/>

## 识别结果

当用户点击结果页中“完成”按钮时，小程序 OCR SDK 会调用您在 ocrSdk.start() 方法中定义的 success 回调函数，并将识别结果作为参数传入。

### 身份证输出结果：

| 参数名称             | 类型             |    描述    |
| ----------------------- | ------------------- | --------- |
| Name         | string        | 姓名（人像面）|
| Sex       | string      | 性别（人像面）|
| Nation   | string      | 民族（人像面）|
| Birth         | string        | 出生日期（人像面）|
| Address      | string      | 地址（人像面）|
| IdNum  | string      | 身份证号（人像面）|
| Authority         | string        | 发证机关（国徽面））|
| ValidDate       | string      | 证件有效期（国徽面））|
| AdvancedInfo.FRONT  | string      | 身份证人像面扩展信息，不请求则不返回。<br/>IdCard，裁剪后身份证照片的 base64 编码，请求 Config.CropIdCard 时返回；<br/>Portrait，身份证头像照片的 base64 编码，请求 Config.CropPortrait 时返回；<br/>Quality，图片质量分数，请求 Config.Quality 时返回（取值范围：0 ~ 100，分数越低越模糊，建议阈值≥50）；<br/>BorderCodeValue，身份证边框不完整告警阈值分数，请求 Config.BorderCheckWarn时返回（取值范围：0 ~ 100，分数越低边框遮挡可能性越低，建议阈值≥50）；<br/>WarnInfos，告警信息，Code 告警码列表和释义：<br/>-9100 身份证有效日期不合法告警，<br/>-9101 身份证边框不完整告警，<br/>-9102 身份证复印件告警，<br/>-9103 身份证翻拍告警，<br/>-9105 身份证框内遮挡告警，<br/>-9104 临时身份证告警，<br/>-9106 身份证 PS 告警，<br/>-9107 身份证反光告警。 |
| AdvancedInfo.BACK  | string      | 身份证国徽面扩展信息，不请求则不返回。<br/>具体内容同上 |
| RequestId.FRONT  | string      | 人像面唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |
| RequestId.BACK  | string      | 国徽面唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |

<br/>

### 身份证输出结果示例：

```json
{
  "Name": "李明",
  "Sex": "男",
  "Nation": "汉",
  "Birth": "1987/1/1",
  "Address": "北京市石景山区高新技术园腾讯大楼",
  "IdNum": "440524198701010014",
  "Authority": "",
  "ValidDate": "",
  "AdvancedInfo": {
    "FRONT": "{\"IdCard\":\"/9j/4AAA.........\",\"Portrait\":\"/9j/4AAQSkZJRBA=...........\"}",
    "BACK": "{\"IdCard\":\"/9j/FWSAA.........\",\"Portrait\":\"/9j/FWFWRGKKLAJRBA=...........\"}"
  },
  "RequestId": {
    "FRONT": "97c323da-5fd3-4fe6-b0b3-1cf10b04422c",
    "BACK": "45dddb87-f8f2-4c21-8849-810d57d13e33"
  }
}
```

### 银行卡输出结果：

| 参数名称             | 类型             |    描述    |
| ----------------------- | ------------------- | --------- |
| CardNo         | string        | 卡号 |
| BankInfo       | string      | 银行信息 |
| ValidDate   | string      | 有效期 |
| RequestId         | string        | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |

### 银行卡输出结果示例：

```json
{
  "CardNo": "6225760088888888",
  "BankInfo": "招商银行(03080000)",
  "ValidDate": "08/2022",
  "RequestId": "46ab2e62-11e3-4d04-9fab-0abe18e7c927"
 }
```

### 名片输出结果：

| 参数名称             | 类型             |    描述    |
| ----------------------- | ------------------- | --------- |
| BusinessCardInfos         | Array of [BusinessCardInfo](https://cloud.tencent.com/document/api/866/33527#BusinessCardInfo)       | 名片识别结果，具体内容请单击左侧链接。 |
| RetImageBase64       | string      | 返回图像预处理后的图片，图像预处理未开启时返回内容为空。 |
| Angle   | number      | 图片旋转角度（角度制），文本的水平方向为0°；顺时针为正，逆时针为负。单击查看 [如何纠正倾斜文本](https://cloud.tencent.com/document/product/866/45139) 。 |
| RequestId         | string        | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 |

### 名片输出结果示例：

```json
{
  "BusinessCardInfos": [
    {
      "Name": "姓名",
      "Value": "艾米"
    },
    {
      "Name": "职位",
      "Value": "视觉设计师"
    },
    {
      "Name": "部门",
      "Value": "社交平台部"
    },
    {
      "Name": "公司",
      "Value": "Tencent腾讯"
    },
    {
      "Name": "地址",
      "Value": "深圳市南山区高新技术园科技中一路腾讯大厦"
    },
    {
      "Name": "邮箱",
      "Value": "ab***fg@tencent.com"
    },
    {
      "Name": "手机",
      "Value": "+86-133****5678"
    },
    {
      "Name": "QQ",
      "Value": "1234567"
    },
    {
      "Name": "微信",
      "Value": "amy001"
    }
  ],
  "RetImageBase64": "",
  "Angle": 0,
  "RequestId": "98f8fcbf-933a-4e95-ac48-6f1a9308fs6h"
}
```

## 错误码以及错误信息

当 OCR 识别失败时，小程序 OCR SDK 会调用您在 ocrSdk.start() 方法中定义的 fail 回调函数，并将错误码以及错误信息作为参数传入。

以下仅列出了接口业务逻辑相关的错误码，其他错误码详见 [公共错误码](https://cloud.tencent.com/document/api/866/33521#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) 

### 身份证识别错误码：

| 错误码            | 描述             |
| ----------------------- | ------------------- |
| FailedOperation.DownLoadError        | 文件下载失败。      |
| FailedOperation.EmptyImageError       | 图片内容为空。     |
| FailedOperation.IdCardInfoIllegal   | 身份证信息不合法（身份证号、姓名字段校验非法等）。     |
| FailedOperation.ImageBlur        | 图片模糊。      |
| FailedOperation.ImageDecodeFailed       | 图片解码失败。     |
| FailedOperation.ImageNoIdCard   | 图片中未检测到身份证。     |
| FailedOperation.ImageSizeTooLarge        | 图片尺寸过大，请参考输出参数中关于图片大小限制的说明。      |
| FailedOperation.MultiCardError       | 照片中存在多张卡。     |
| FailedOperation.OcrFailed   | OCR识别失败。     |
| FailedOperation.UnKnowError        | 未知错误。      |
| FailedOperation.UnOpenError       | 服务未开通。     |
| InvalidParameter.ConfigFormatError   | Config 不是有效的 JSON 格式。     |
| InvalidParameterValue.InvalidParameterValueLimit        | 参数值错误。      |
| LimitExceeded.TooLargeFileError      | 文件内容太大。     |
| ResourcesSoldOut.ChargeStatusException  | 计费状态异常。     |

### 银行卡识别错误码：

| 错误码            | 描述             |
| ----------------------- | ------------------- |
| FailedOperation.DownLoadError        | 文件下载失败。      |
| FailedOperation.ImageDecodeFailed       | 图片解码失败。     |
| FailedOperation.OcrFailed   | OCR识别失败。     |
| FailedOperation.UnKnowError        | 未知错误。      |
| FailedOperation.UnOpenError      | 服务未开通。     |
| InvalidParameter.EngineImageDecodeFailed   | 图片解码失败。     |
| InvalidParameterValue.InvalidParameterValueLimit        | 参数值错误。      |
| LimitExceeded.TooLargeFileError       | 文件内容太大。     |
| ResourcesSoldOut.ChargeStatusException   | 计费状态异常。     |

### 名片识别错误码：

| 错误码            | 描述             |
| ----------------------- | ------------------- |
| FailedOperation.DownLoadError        | 文件下载失败。      |
| FailedOperation.ImageDecodeFailed       | 图片解码失败。     |
| FailedOperation.ImageNoBusinessCard       | 照片未检测到名片。     |
| FailedOperation.OcrFailed   | OCR识别失败。     |
| FailedOperation.UnKnowError        | 未知错误。      |
| FailedOperation.UnOpenError      | 服务未开通。     |
| InvalidParameter.ConfigFormatError  | Config 不是有效的 JSON 格式。     |
| InvalidParameterValue.InvalidParameterValueLimit        | 参数值错误。      |
| LimitExceeded.TooLargeFileError       | 文件内容太大。     |
| ResourcesSoldOut.ChargeStatusException   | 计费状态异常。     |