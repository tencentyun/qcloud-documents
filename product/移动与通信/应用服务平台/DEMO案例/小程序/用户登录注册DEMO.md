# 小程序用户管理 DEMO

基于 TCB 开发的用户登陆注册 DEMO,介绍如何通过 TCB 构建用户登录注册服务。

![预览](https://ask.qcloudimg.com/draft/1011618/piih5pivk8.png)


## 手动部署
### 下载或clone代码仓库
```javascript
git clone https://github.com/TencentCloudBase/tcb-demo-user.git
```

## 项目结构

```
|- client 小程序客户端代码
    |- components
        |- login 登录/注册自定义组件的相关逻辑
    |- pages
        |- index
        |- main 登录之后主页

|- cloud 云端代码
    |- database 数据库
    |- functions 云函数代码
        |- verifyIdentity   verifyIdentity
            |- lib      一些工具函数
                |- db.js  数据库初始化
                |- res.js 响应数据构造函数
            |- index.js 云函数入口
            |- config
                |- index.js   配置项
                |- example.js 配置样例项
            |- package.json   依赖项
        |- loginSteam   处理登录注册注销
            |- lib      一些工具函数
                |- db.js  数据库初始化
                |- res.js 响应数据构造函数
                |- create_session.js 生成自定义态的session
            |- index.js 云函数入口
            |- config
                |- index.js   配置项
                |- example.js 配置样例项
            |- package.json   依赖项
```
## 预览 DEMO

### 填入小程序 appid

`project.config.json`
```javascript
...
    "libVersion": "2.2.4",
    "appid": "your appid here",
    "projectname": "tcb-component-user",
...
```

### 创建 Collection
在云开发控制台中，创建 `users` 和 `status` 两个 `collection`，用于存储登陆态以及用户资料。

### 填入云开发环境 id

云函数的相关配置，请参考 `cloud/functions下/**/config` 目录下的 `example.js`，建立 `index.js` 文件写相关配置配置详见 `example`。

本demo中，自定义登录态的有效时间是在 `loginRegister` 函数中的配置中的有效时间结合微信的 `session_key` 有效时间的，数据库存放当前的 `session` 最长有效时间（相应的可在 `loginRegister` 相应的 `config.js` 中进行配置）、客户端也在`onLoad` 中检测 `session` 是否有效。[文档参考](https://developers.weixin.qq.com/miniprogram/dev/api/api-login.html)

### 安装依赖及上传云函数
使用 `npm i --production` 给 `loginRegister` 和 `verifyIdentity` 安装依赖，完成后在开发 `IDE` 里将两个云函数上传。

