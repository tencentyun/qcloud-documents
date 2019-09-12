## 功能描述

GET Bucket website 请求用于获取与存储桶关联的静态网站配置信息。

## 请求

#### 请求示例

```shell
GET /?website HTTP/1.1
Host:<BucketName-APPID>.<Region>.myqcloud.com
Date:date
Authorization: Auth String
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

#### 公共响应头

该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该响应无特殊的响应头。

#### 响应体

该响应体返回为 application/xml 数据，包含完整节点数据的内容展示如下：

```shell
<WebsiteConfiguration>
	<IndexDocument>
		<Suffix>index.html</Suffix>
	</IndexDocument>
	<RedirectAllRequestsTo>
		<Protocol>https</Protocol>
	</RedirectAllRequestsTo>
	<ErrorDocument>
		<Key>Error.html</Key>
	</ErrorDocument>
	<RoutingRules>
		<RoutingRule>
			<Condition>
				<HttpErrorCodeReturnedEquals>404</HttpErrorCodeReturnedEquals>
			</Condition>
			<Redirect>
				<Protocol>https</Protocol>
				<ReplaceKeyWith>404.html</ReplaceKeyWith>
			</Redirect>
		</RoutingRule>
		<RoutingRule>
			<Condition>
				<KeyPrefixEquals>docs/</KeyPrefixEquals>
			</Condition>
			<Redirect>
				<Protocol>https</Protocol>
				<ReplaceKeyPrefixWith>documents/</ReplaceKeyPrefixWith>
			</Redirect>
		</RoutingRule>
		<RoutingRule>
			<Condition>
				<KeyPrefixEquals>img/</KeyPrefixEquals>
			</Condition>
			<Redirect>
				<Protocol>https</Protocol>
				<ReplaceKeyWith>demo.jpg</ReplaceKeyWith>
			</Redirect>
		</RoutingRule>
	</RoutingRules>
</WebsiteConfiguration>
```

具体内容描述如下：

| 名称                        | 父节点                | 描述                                                         | 类型      | 必选 |
| --------------------------- | --------------------- | ------------------------------------------------------------ | --------- | ---- |
| WebsiteConfiguration        | 无                    | 静态网站配置，包括索引文档、错误文档、协议转换和重定向规则   | Container | 是   |
| IndexDocument               | WebsiteConfiguration  | 索引文档                                                     | Container | 是   |
| Suffix                      | IndexDocument         | 指定索引文档                                                 | String    | 是   |
| ErrorDocument               | WebsiteConfiguration  | 错误文档                                                     | Container | 否   |
| Key                         | ErrorDocument         | 指定通用错误返回                                             | String    | 否   |
| RedirectAllRequestsTo       | WebsiteConfiguration  | 重定向所有请求                                               | Container | 否   |
| Protocol                    | RedirectAllRequestsTo | 指定全站重定向的协议，只能设置为 https                        | String    | 否   |
| RoutingRules                | WebsiteConfiguration  | 设置重定向规则，最多设置100条 RoutingRule                     | Container | 否   |
| RoutingRule                 | RoutingRules          | 设置单条重定向规则，包括前缀匹配重定向和错误码重定向         | Container | 否   |
| Condition                   | RoutingRule           | 指定重定向发生的条件，前缀匹配重定向和错误码重定向只能指定一个 | Container | 否   |
| HttpErrorCodeReturnedEquals | Condition             | 指定重定向错误码，只支持配置4XX返回码，优先级高于ErrorDocument | Interger  | 否   |
| KeyPrefixEquals             | Condition             | 指定前缀重定向的路径，替换指定的 folder/                      | String    | 否   |
| Redirect                    | RoutingRule           | 指定满足重定向 conditon 时重定向的具体替换规则                 | Container | 否   |
| ReplaceKeyWith              | Redirect              | 替换整个 Key 为指定的内容                                      | String    | 否   |
| ReplaceKeyPrefixWith        | Redirect              | 替换匹配到的前缀为指定的内容，Conditon 为 KeyPrefixEquals 才可设置 | String    | 否   |

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
GET /?website HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Date:Thu, 21 Sep 2017 13:09:53 +0000
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484815944;32557711944&q-key-time=1484815944;32557711944&q-header-list=host&q-url-param-list=website&q-signature=a2d28e1b9023d09f9277982775a4b3b705d0e23e
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 751
Connection: keep-alive
Date: Thu, 21 Sep 2017 13:15:39 GMT
Server: tencent-cos
x-cos-request-id: NTljM2JiN2FfMjQ4OGY3MGFfNzk4OV84Mg==

<WebsiteConfiguration>
	<IndexDocument>
		<Suffix>index.html</Suffix>
	</IndexDocument>
	<RedirectAllRequestsTo>
		<Protocol>https</Protocol>
	</RedirectAllRequestsTo>
	<ErrorDocument>
		<Key>Error.html</Key>
	</ErrorDocument>
	<RoutingRules>
		<RoutingRule>
			<Condition>
				<HttpErrorCodeReturnedEquals>404</HttpErrorCodeReturnedEquals>
			</Condition>
			<Redirect>
				<Protocol>https</Protocol>
				<ReplaceKeyWith>404.html</ReplaceKeyWith>
			</Redirect>
		</RoutingRule>
		<RoutingRule>
			<Condition>
				<KeyPrefixEquals>docs/</KeyPrefixEquals>
			</Condition>
			<Redirect>
				<Protocol>https</Protocol>
				<ReplaceKeyPrefixWith>documents/</ReplaceKeyPrefixWith>
			</Redirect>
		</RoutingRule>
		<RoutingRule>
			<Condition>
				<KeyPrefixEquals>img/</KeyPrefixEquals>
			</Condition>
			<Redirect>
				<Protocol>https</Protocol>
				<ReplaceKeyWith>demo.jpg</ReplaceKeyWith>
			</Redirect>
		</RoutingRule>
	</RoutingRules>
</WebsiteConfiguration>
```
