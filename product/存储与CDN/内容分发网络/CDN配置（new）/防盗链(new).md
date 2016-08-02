## 功能简介

防盗链是通过http referer过滤请求内容返回对应信息的配置。http referer是http请求包包头的一部分，当浏览器向web服务器发送请求时，会带上referer，告诉服务器此请求是从哪个链接而来，从而可进行信息的处理。

## 配置说明

您可在CDN接入时配置防盗链，或在CDN控制台的“域名管理”页面中点击域名右侧的“管理”进入“域名高级配置”页面中修改防盗链配置。

 ![](//mccdn.qcloud.com/static/img/59b0f12c6f5a10a9715be9313e10845d/image.png)

**1) referer白名单：**符合白名单内字符串内容的请求，CDN节点正常返回请求信息；当设置白名单时，CDN节点只能返回符合该白名单内字符串内容的请求；
若用户请求中referer信息不命中，则CDN节点拒绝返回请求信息（如：设置www.test.com 为referer白名单，CDN加速域名为：www.abc.com ，当用户通过referer信息=www.test.com 的http请求访问www.abc.com时 ，CDN节点才能正常返回该请求信息；若设置了referer白名单后，http请求包包头referer≠www.test.com 或referer为空时，CDN拒绝返回该请求信息）；

**2) referer黑名单：**符合黑名单内字符串内容的请求，CDN节点将拒绝返回该请求信息；当设置黑名单时， CDN节点拒绝返回符合该黑名单内字符串内容的请求;
若用户请求中referer信息不命中，则CDN节点正常返回该请求信息（如：设置www.test.com 为referer黑名单，CDN加速域名为：www.abc.com ，当用户通过referer信息=www.test.com 的http请求访问www.abc.com 时，CDN节点拒绝返回该请求信息；若设置了referer黑名单后，http请求包包头referer≠www.test.com 或referer为空时，CDN则正常返回该请求信息）；

#### **注意事项**

a) referer黑名单、白名单二者不兼容，同一时间只能生效一种类型；
b) 当防盗链黑、白名单为空时，等同于关闭防盗链，防盗链规则不生效；
c) 防盗链输入内容最多可输200条，以换行符相隔，一行输入一个；

**防盗链规则匹配的设定如下：**

①、支持域名/ip规则，且为前缀匹配。
如设置www.qq.com ，则referer中包含以下的都匹配：
http://www.qq.com
http://www.qq.com/123
http://www.qq.com.cn
如设置127.0.0.1，则referer中包含以下的都匹配：
http://127.0.0.1
http://127.0.0.1/123

②、 支持域名前缀通配符。
如设置*.qq.com, 则referer中包含以下的都匹配：
http://www.qq.com
http://a.qq.com
http://a.b.qq.com/123

③、referer为空（即指用户在浏览器中直接访问域名，则referer为空），空referer默认不匹配任何规则。
即：当referer为空时，若设置黑名单规则，空referer请求不会被黑名单规则拦截，CDN正常返回该请求信息；
当referer为空时，若设置白名单规则，空referer请求不会命中白名单规则，CDN拒绝返回该请求信息。

④、包含空referer
包含空referer即指：选择referer白名单时，白名单中包含空的referer(即：通过浏览器地址栏直接访问该资源URL)时，CDN将正常返回资源信息。