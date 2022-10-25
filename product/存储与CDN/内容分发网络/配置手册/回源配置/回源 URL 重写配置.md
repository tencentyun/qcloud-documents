
若您需要将回源请求 URL 修改为与源站匹配的 URL，腾讯云 CDN 为您提供了回源 URL 重写配置功能。

## 适用场景
1. 源站的资源路径发生了变更，但是用户仍然使用原 URL 进行请求，可通过回源 URL 重写将原 URL 指向新的资源路径内；
2. 源站内有同样的资源复用在多个站点内，可以通过回源 URL 重写将资源指向指定的资源路径内。

## 注意事项
1. ECDN 域名暂不支持此功能配置；
2. 如果您需要指定将不同路径文件回源指向不同的源站内，可使用 [高级回源配置](https://cloud.tencent.com/document/product/228/51108) 功能，高级回源配置支持根据 Client IP、文件后缀、文件目录、全路径文件、首页等规则指向指定的源站内；
3. 若您有多个源站，配置有不同路径回源规则，配合回源 URL 重写可实现分路径回源的同时重写回源 URL 路径，因此在使用回源 URL 重写的同时请注意是否配置有高级回源配置，以防止您的回源指向不准确导致访问失败。

## 配置说明

### 域名管理内配置
1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)；
2. 单击左侧菜单内的**域名管理**，进入域名管理列表；
3. 选择需要配置的域名，单击**管理**进入域名配置页面；
4. 单击**回源配置**，切换至回源配置标签页，在标签页中，即可看到回源 URL 重写配置项；
![](https://qcloudimg.tencent-cloud.cn/raw/7ffe2bc93b5b82c17955e96595b8033b.png)
5. 单击**新增规则**，新增一条回源 URL 重写配置规则，规则内填写约束如下：

|配置项|	说明|
|--|--|
|匹配设置|	1.默认为前缀匹配，例如：待重写回源 URL 为 /test，则将匹配 /test 下路径下的所有文件；<br>2.若勾选全路径匹配，则精准匹配至指定的文件路径，例如：待重写回源 URL 为 /test/a.jpg，则将精准匹配 /test/a.jpg 文件。|
|待重写回源 URL|	1.以/开头，默认为前缀匹配，支持使用通配符 \* 匹配（例如：/test/\*/\*.jpg）。若指定文件目录，不能以“/”结尾（例如：/test）；<br>2.通配符 \* 也可以用于匹配 URL 的带参内容，例如 URL 为：/test/a.jpg?imageMogr2/thumbnail/!50px，可使用 /test/a.jpg\*，此处的通配符 \* 代表问号后所有参数内容；<br>3.在全路径匹配模式下，不支持通配符 \*。|
|目标回源 HOST	|回源 Host 决定了回源请求访问到源站时访问的具体站点，默认为当前回源HOST；<br>1. 如果您回源的目标为腾讯云COS对象存储或第三方对象存储，建议指定回源HOST与当前回源HOST保持一致，否则可能会导致回源失败；<br>2. 如果您的回源目标为自有服务器源站内的其它站点，可修改回源HOST为对应站点域名，填写不包含`http://`或`https://`头。|
|目标回源 Path|	以 / 开头（例如：/newtest/b.jpg），通配符 \* 可通过 $n 捕获（n=1,2,3....)，例如：<br>待重写回源URL配置为/test/\*/\*.jpg，目标回源Path配置为/newtest/$1/$2.jpg，则用户访问请求的回源URL为/test/a/b.jpg时，根据$1将捕获第一个通配符内容，即为a；$2将捕获第二个通配符内容，即为b，则实际回源URL将被改写为/newtest/a/b.jpg。|

### 配置约束
单个域名至多可添加100条重写规则；
多条规则支持调整优先级：底部优先级大于顶部。

## 配置示例

**示例一**
用户访问域名为：example.com，源站服务器地址为1.1.1.1，回源规则配置如下：
![](https://qcloudimg.tencent-cloud.cn/raw/cbd958f4057964548165747df29fa0b4.png)
- 当用户访问URL为：`http://example.com/test/a.jpg` 时，命中最下方的规则，根据所指定的 HOST 配置，则回源将指向源站1.1.1.1的 `image.example.com` 站点内资源，最终回源访问路径为1.1.1.1服务器下的 `http://image.example.com/test/image/a.jpg`。
- 当用户访问URL为：`http://example.com/test/a/b.jpg` 时，命中最上方的规则，根据所指定的 HOST 配置，则回源将指向源站1.1.1.1的 `image.example.com` 站点内资源，同时根据通配符捕获的规则，最终回源访问路径为1.1.1.1服务器下的：`http://image.example.com/newtest/a/b.jpg`

**示例二**
用户访问域名为：example.com，并且配置了高级回源规则如下：
![](https://qcloudimg.tencent-cloud.cn/raw/61305c6760c89ebe76c9bbfe25c5f650.png)
同时配置回源 URL 重写规则如下：
![](https://qcloudimg.tencent-cloud.cn/raw/30742e2c63ca21b27c78c58275ab5854.png)
- 则当用户访问 URL 为：`http://example.com/test/a.jpg` 时，因高级回源规则配置，底部优先级最高，优先匹配文件目录回源规则，则该请求会回源至1.1.1.2源站服务器内；又由于回源 URL 重写规则，匹配最下方的规则，根据指定的回源 HOST 配置，回源将指向源站1.1.1.2的 `image.example.com` 站点内资源，所以最终回源访问路径为1.1.1.2服务器下的 `http://image.example.com/test/image/a.jpg`。
- 当用户访问 URL 为：`http://example.com/test/a/b.jpg` 时，因高级回源规则配置，命中文件后缀规则，则该请求将回源至1.1.1.3源站服务器内；又由于回源 URL 重写配置规则，匹配第一条规则，根据所制定的 HOST 配置，则回源将指向源站1.1.1.3的 `image.example.com` 站点内资源，同时根据通配符捕获的规则，最终回源访问路径为1.1.1.3服务器下的：`http://image.example.com/newtest/a/b.jpg`。

**示例三**
用户访问域名为：example.com，源站服务器地址为1.1.1.1，回源 URL 重写配置规则如下：
![](https://qcloudimg.tencent-cloud.cn/raw/c3f3d2ff75817def695dc008bd04a80e.png)
当用户访问 URL 为：`http://example.com/test/a.jpg?imageMogr2/thumbnail/!50px` 时，命中回源URL重写的规则，根据所指定的 HOST 配置，则回源将指向源站1.1.1.1的 example.com 站点内资源，同时通过 $1 捕获通配符 \* 的所有内容，即原 URL 所携带的参数内容，最终回源访问路径为1.1.1.1服务器下的 `http://example.com/new/test/image/a.jpg?imageMogr2/thumbnail/!50px`。
