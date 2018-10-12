基于 TCB 开发的 AI DEMO，介绍如何通过 TCB 使用腾讯云智能图像服务

![界面展示](https://ask.qcloudimg.com/draft/1011618/3v4vl26ls1.jpg)


## 手动部署
### 下载或 clone 代码仓库
```javascript
git clone https://github.com/TencentCloudBase/tcb-demo-ai.git
```


## 项目结构
```
project
 ├── client               # 客户端代码
 │    ├── lib             # 外部库
 │    ├── pages           # demo 页面
 │    ├── components      # AI 组件代码
 │    └── utils           # 工具
 ├── cloud                # 腾讯云服务相关文件
 │    ├── cos             # 对象存储
 │    ├── database        # 数据库
 │    └── functions       # 云函数
 ├── config               # 配置文件
 ├── server               # 服务端代码
 └── project.config.json  # 项目配置文件
```

## 预览

### 填入小程序 appid

`project.config.json`
```javascript
...
    "libVersion": "2.2.4",
    "appid": "",
    "projectname": "tcb-demo-ai",
...
```

### 填入云小程序环境 id

`client/app.js`
```javascript
App({
    onLaunch: function () {
        wx.cloud.init({
            env: '',
            traceUser: true
        });
    },
});
```

### 为需要云函数填入云服务相关配置

`cloud/functions/*/index.js`
```javascript
...
const AppId = ''; // 腾讯云 AppId
const SecretId = ''; // 腾讯云 SecretId
const SecretKey = ''; // 腾讯云 SecretKey
...
```

如果使用人脸融合功能还需要额外填写人脸融合服务相关字符串
`cloud/functions/faceFuse/index.js`
```javascript
...
    data: {
        uin: '',
        project_id: '',
        model_id: '',
        img_data: imageBase64,
        rsp_img_type: 'url'
    },
...
```

### 上传云函数
在云函数函数目录下安装依赖，并用开发 `IDE` 上传
```javascript
npm install --production
```

完成上以步骤，你便可以用微信开发者 `IDE` 预览该小程序的 `DEMO`


## 使用组件

如果你想使用小程序 AI 自定义组件，你可以按照以下步骤进行。

### 复制并使用自定义 AI 组件
将 `client/components/` 中其中一个组件复制到你的项目中的组件存放位置（lib 目录也需要复制，因为用到了 `weui` 的样式)，在页面的 `json` 文件中进行引用声明。

```json
{
    "usingComponents": {
        "ocr": "path/to/ocr"
    }
}
```

然后在页面 `wxml` 文件中使用组件，具体参数，见下节的 API 文档


```xml

```

### 复制并上传云函数

了解你具体想使用哪个 `AI` 功能，然后把相关的云函数目录，复制到你的项目中的指定云函数目录下。该目录可以在 `project.config.json` 中配置 `cloudfunctionRoot`。复制后，请安装依赖并右键上传云函数。
    
`project.config.json`
```json
{
    "cloudfunctionRoot": "path/to/cloud/functions",
}
``` 

## API 文档

### ocr 组件
### 属性

|属性名|含义|必填|默认值|
|--|--|--|--|
|uploadText|上传按钮的文字|否|上传图片|
|recognizeText|识别按钮的文字|否|进行识别|
|mode|识别模式|是|    -     |
|imgUrl|默认图片 url|否|略|
|type|对象类型(仅在`drivingLicence`模式中有效)|否|0|

#### mode 有效值

|值|含义|
|--|--|
|handWriting|手写体识别|
|idCard|身份证识别|
|bizLicense|营业执照识别|
|drivingLicence|行驶证驾驶证识别|
|plate|车牌号识别|
|general|通用印刷体识别|
|bankCard|银行卡识别|
|bizCard|名片识别（V2)|

### 事件

|事件名|触发条件|
|--|--|
|finish|识别完成|

#### finish 事件对象属性

|属性|类型|说明|
|--|--|--|
|timeStamp|Number|事件触发事件|
|type|String|事件类型|
|detail|Object|识别结果，参考 [腾讯云文字识别 API 文档](https://cloud.tencent.com/document/product/866/17594)|

### img-detect 组件
### 属性

|属性名|含义|必填|默认值|
|--|--|--|--|
|uploadText|上传按钮的文字|否|上传图片|
|recognizeText|识别按钮的文字|否|进行识别|
|mode|识别模式|是|     -          |
|imgUrl|默认图片 url|否|略|

#### mode 有效值
|值|含义|
|--|--|
|pornDetect|图片鉴黄|
|tagDetect|图片标签识别|

### 事件

|事件名|触发条件|
|--|--|
|finish|识别完成|

#### finish 事件对象属性

|属性|类型|说明|
|--|--|--|
|timeStamp|Number|事件触发事件|
|type|String|事件类型|
|detail|Object|识别结果，参考 [腾讯云图片标签 API 文档](https://cloud.tencent.com/document/product/865/17592)以及 [腾讯云智能鉴黄 API 文档](https://cloud.tencent.com/document/product/864/17609)|

### face-fuse 组件
### 属性

|属性名|含义|必填|默认值|
|--|--|--|--|
|uploadText|上传按钮的文字|否|上传图片|
|recognizeText|融合按钮的文字|否|进行融合|
|customImgUrl|默认图片 url|否|略|
|templateImgUrl|模板图片 url|否|略|
|hideTemplate|是否隐藏模板图片|否|false|

>注：templateImgUrl 指定的图片仅供展示，融合中使用的模板图片由云函数的参数指定。

### 事件

|事件名|触发条件|
|--|--|
|finish|识别完成|

#### finish 事件对象属性

|属性|类型|说明|
|--|--|--|
|timeStamp|Number|事件触发事件|
|type|String|事件类型|
|detail|String|融合结果图片 url|
