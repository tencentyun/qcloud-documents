### App&H5 联动分析接入
需要统计 App webview 的基础访问、点击事件时，请在 webview 里加入以下 js 代码：
```html
<script src="//pingjs.qq.com/mta/app_link_h5_stats.js" name="MtaLinkH5"></script>
```
>**注意：**
>后续的方法上报都必须保证已加载以上 js sdk。

### 手动上报页面访问统计

访问页面时，上报页面访问情况：

```js
MtaLinkH5.pageBasicStats({
  'title': '必填-每页要求不重复'
});
```
>**注意：**
>确定联动分析 js sdk 已载入，并且设置了 title 名称；
>title 为必填项目，并且每页的 title 都要求不重复，重复影响统计。

### 设置登录帐号
用于设置用户登录帐号信息：

```js
MtaLinkH5.setLoginUin(uin);
```
>**注意：**
>确定联动分析 js sdk 已载入；
>uin 为设置的用户帐号，string 类型。

### 自定义事件
用于页面自定义事件埋点上报：

```js
MtaLinkH5.eventStats(event_id, param_json);
```

>**注意：**
>确定联动分析 js sdk 已载入；
>event_id 为事件 ID，在事件中添加后拷贝过来；
>param_json 为事件参数以及事件参数值，每个参数对应一个参数值，为 json 格式。

#### 例子：
```html
<button onclick="MtaLinkH5.eventStats('test_event')">事件-不带参数</button>
<button onclick="MtaLinkH5.eventStats('test_event', {'param1':'value1'})">事件-单个参数</button>
<button onclick="MtaLinkH5.eventStats('test_event', {'param1':'value1','param2':'value2'})">事件-多个参数-参数建议最多不超过5个</button>
```
