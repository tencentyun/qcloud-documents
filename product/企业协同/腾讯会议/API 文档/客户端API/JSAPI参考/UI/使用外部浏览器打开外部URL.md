## 使用场景
- 业务方需要用浏览器打开外部的链接地址。
- 通过浏览器实现下载文件。
>!使用此方法时，浏览器打开可信域名的 URL 时，将会向用户弹框来获取用户的许可，界面如下：
<img style="width:500px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/12a9a67cb92f84479471a319599663cc.png" />

## 操作步骤
### 步骤一：配置 H5 可信域名
在应用管理后台 > 安全配置 > H5 可信域名，添加应用需要访问的 URL 的可信域名。
![](https://qcloudimg.tencent-cloud.cn/raw/7253cc2403aebf9e3643d6aee295d90f.png)

### 步骤二：JS-API 调用
- JSAPI 接口
wemeet.ui.openExternalPage
- 支持版本：3.13.0
- 是否需要鉴权：否

### 代码示例
```js
wemeet.ui.openExternalPage({
 url: 'https://xxxxxxxx',
 success: () => {
   console.log('openExternalPage success');
 },
 fail: (err) => {
   console.log('openExternalPage canceled', err);
 }
})
 .catch(err => {
   console.error('openExternalPage error');
 })
```

## 参数说明
param：OpenUrlParam 打开 webview 的地址，只支持 HTTPS 协议。

## 错误码

| 错误码 | 说明 | 
|---------|---------|
| 10 | 参数错误 | 
| 2006、2007 | 应用已下架 | 
| 2011 | 跳转链接只支持 HTTPS 协议 | 
| 2009 | 跳转链接不合法，仅支持可信域名内的链接 | 
| 20 | 服务异常 | 

