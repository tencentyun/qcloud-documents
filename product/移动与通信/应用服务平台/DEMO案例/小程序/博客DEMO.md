## 预览 DEMO

### 下载或clone代码包
```javascript
git clone https://github.com/TencentCloudBase/tcb-demo-blog.git
```

### 配置小程序 id
用[微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/devtools.html)，打开上一步下载下来的代码仓库，填入小程序的 appid（使用云开发能力必须填写 appid）。

### 安装云函数依赖

```javascript
// 安装依赖
cd cloud/functions/addblog/
npm install --production
```

### 上传云函数
在IDE中，右键云函数对应的文件夹，点击“上传并部署”菜单

### 新建collection
在小程序开发IDE中的，[云开发控制台] -> [数据库] 中，添加集合 `blog`。
![](https://user-images.githubusercontent.com/3348398/44449753-993f6380-a621-11e8-900e-34706eb7a39b.png)

## 体验
点击小程序开发IDE中的“预览”，用微信扫一扫即可体验
