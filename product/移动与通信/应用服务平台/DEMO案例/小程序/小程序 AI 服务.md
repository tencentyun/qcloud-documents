基于小程序云开发的 AI DEMO，使用腾讯云智能图像服务

![界面展示](https://ask.qcloudimg.com/draft/1011618/3v4vl26ls1.jpg)

## 预览

### 下载或clone代码包
```javascript
git clone https://github.com/TencentCloudBase/tcb-demo-ai.git
```

### 填入小程序 appid
用 [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/devtools.html)，打开上一步下载下来的代码仓库，填入小程序的 appid（使用云开发能力必须填写 appid）。

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

- 上传云函数
在云函数函数目录下（每个AI函数下面）安装依赖，并用开发 `IDE` 上传
```javascript
npm install --production
```

完成上以步骤，你便可以用微信开发者 `IDE` 预览该小程序的 `DEMO`

## 体验
点击小程序开发IDE中的“预览”，用微信扫一扫即可体验
