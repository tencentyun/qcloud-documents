# 小程序模板消息服务 DEMO
基于 TCB 开发的模板消息 DEMO，介绍如何通过 TCB 构建模板消息服务。

![界面展示](https://ask.qcloudimg.com/draft/1011618/a51x8b25ql.jpg)


## 手动部署
### 下载或clone代码仓库
```javascript
git clone https://github.com/TencentCloudBase/tcb-demo-message.git
```


## 项目结构
```
project
 ├── client               # 客户端代码
 │    ├── lib             # 外部库
 │    ├── pages           # demo 页面
 │    ├── components      # 消息组件代码
 │    └── utils           # 工具
 ├── cloud                # 腾讯云服务相关文件
 │    └── functions       # 云函数
 ├── config               # 配置文件
 ├── server               # 服务端代码
 └── project.config.json  # 项目配置文件
```

## 预览 DEMO

### 填入小程序 appid

`project.config.json`
```javascript
...
    "libVersion": "2.2.4",
    "appid": "your appid here",
    "projectname": "tcb-message-component",
...
```

### 填入云开发环境 id

`client/app.js`
```javascript
App({
    onLaunch: function () {
        wx.cloud.init({
            env: 'your envid here',
            traceUser: true
        });
    },
});
```

### 为云函数填入模板消息相关配置

`cloud/functions/wxmessage/index.js`
```javascript
...
const secret = 'secret' // 小程序 secret id
const templateId = 'template_id' // 模板 id，非必填，也可以从小程序端上传
...
```

### 上传云函数
在云函数函数`wxmessage`目录下安装依赖，并用开发 `IDE` 上传

```bash
$ npm install --production
```

完成上以步骤，你便可以用微信开发者 `IDE` 预览该小程序的 `DEMO`

## 使用组件
如果你想使用小程序模板消息自定义组件，你可以按照以下步骤进行：

### 复制并上传云函数
将 `cloud/functions` 复制到你的项目中的指定云函数目录下。该目录可以在 `project.config.json` 中配置 `cloudfunctionRoot`。复制后，请安装依赖并右键上传云函数。
    
`project.config.json`
```json
{
    "cloudfunctionRoot": "path/to/cloud/functions",
}
```

### 复制并使用自定义模板消息组件
将 `client/components/wxmessage` 组件复制到你的项目中的组件存放位置（lib目录也需要复制，因为用到了 `weui` 的样式)，在页面的 `json` 文件中进行引用声明。

```json
{
    "usingComponents": {
        "message-component": "path/to/wxmessage"
    }
}
```
然后在页面 `wxml` 文件中使用组件，具体参数，见下节的 API 文档

```xml
<wxmessage
    formData="{{formData}}"
    template_id=""
/>
```

在 `js` 文件中定义表单格式
```javascript
Page({
    data: {
        formData: [
            { title: '报名项目', name: 'keyword1', defaultValue: '团建' },
            { title: '联系方式', name: 'keyword2', placeholder: '请填写手机' },
            { title: '报名时间', name: 'keyword3', defaultValue: '2018-05-29', hidden: true },
            { title: '报名姓名', name: 'keyword4', defaultValue: 'heyli' },
        ]
    }
})
```

## API 文档

### message-component 组件

#### 属性

|属性名|含义|数据类型|必填|默认值|
|--|--|--|--|---|
|formData|表单信息|Array&lt;Object>|是|-|
|templateId|模板 id，如果不填则需要在云函数中配置|String|否|-|

#### formData 属性

|属性名|含义|数据类型|必填|
|--|--|--|--|
|title|呈现在页面上的名字|String|是|
|name|模板消息中使用的字段名，不填则不出现在模板消息中|String|否|
|defaultValue|字段默认值|String|否|
|placeholder|占位符|String|否|
|hidden|是否将该字段呈现在表单上|Boolean|否|

### wxmessage 云函数

```javascript
wx.cloud.callFunction({
    name: 'wxmessage',
    data: {
        code: 'xxx',
        formId: 'xxx',
        templateId: 'xxx',
        data: {
            keyword1: {
                value: 'xxx'
            },
            keyword2: {
                value: 'xxx'
            }
        }
    }
}).then((res) => {

})
.catch((err) => {

})
```
#### 属性

|属性名|含义|数据类型|必填|默认值|
|--|--|--|--|---|
|code|用户登录凭证，用于openId拿不到的情况|String|否|-|
|formId|表单提交中携带的 from_id|String|否|-|
|prepayId|支付场景中的 prepayId，formId和prepayId二选一|String|否|-|
|data|模板内容|Object|是|-|
|page|点击模板卡片后的跳转页|String|否|-|
|templateId|模板 id|String|否|-|

#### data 属性
```javascript
{
    keyword1: {
        value: 'xxx'
    },
    keyword2: {
        value: 'xxx'
    },
    /*** 更多 keyword 与对应的值 ***/
}
```
