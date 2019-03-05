### 1	云图上传下载接口每天的调用次数有没有限制
没有限制。
### 2 js跨域访问失败。
请不要使用header添加authorization的方式，会出现跨域访问限制。使用url?sign=xxx的方式可以解决问题。
### 3 token防盗链下载时，签名经常性错误。
token防盗链下载图片的方式为url?sign=xxx，需要对签名xxx进行urlencode。