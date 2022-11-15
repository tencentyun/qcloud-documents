**Request** 代表 HTTP 请求对象，基于标准 Request 进行了扩展，请参考 MDN 官方文档 [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request)。在边缘函数中，可通过两种方式获得 Request 对象：

- 使用 Request 构造函数创建一个 Request 对象，用于 Fetch API 的操作。
- 通过 FetchEvent 对象的 request 属性，获得当前请求的 Request 对象。

## 构造函数

```typescript
const request = new Request(input [, options])
```

### 参数

| <div style="width: 100px">参数名称</div> | <div style="width: 160px">类型</div> | <div style="width: 60px">必填</div> | 说明                                                                                                                                                 |
| ---------------------------------------- | ------------------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| input                                    | `string` &#124; `Request`            | 是                                  | 一个直接包含资源 url 的字符串<br/> 或拷贝已存在的 Request 对象，若 options 对象的 copyHeaders 属性为 false，则引用传入的 Request 对象的 headers 属性 |
| options                                  | `RequestInit`                        | 否                                  | 初始化 Request 对象的属性值的选项                                                                                                                    |

#### RequestInit

初始化 Request 对象的属性值选项
| <div style="width: 100px">属性名</div> | <div style="width: 140px">类型</div> | <div style="width: 60px">必填</div> | <div style="width: 80px">默认值</div> | 说明 |
| ---- | --- | --- | --- | --- |
| method | `string` | 否 | GET | 请求方法，支持 `GET`、`POST`、…… |
| headers | [`Headers`](https://cloud.tencent.com/document/product/1552/81903) | 否 | | 请求的头部信息 |
| body | `string` &#124; <br/> `Blob` &#124; <br/> `ArrayBuffer` &#124; <br/>`ArrayBufferView` &#124; <br/> [`ReadableStream`](https://cloud.tencent.com/document/product/1552/81914) | 否 | | 请求体 |
| redirect | `string` | 否 | follow | 重定向策略，支持 `manual`、`error` 和 `follow`（自动跟随重定向） |
| maxFollow | `number` | 否 | 12 | 最大可重定向次数 |
| version | `string` | 否 | HTTP/1.1 | HTTP 版本，支持 `HTTP/1.0`、`HTTP/1.1` 和 `HTTP/2.0` |
| copyHeaders | `boolean` | 否 | | <b>非标准选项</b>，表示是否拷贝传入的 Request 对象的 headers 属性 |
| cf | `RequestInitCfProperties` | 否 | | <b>非标准选项</b>，用于控制边缘函数处理该请求的行为 |

#### RequestInitCfProperties

非标准选项，用于控制边缘函数处理该请求的行为
| <div style="width: 100px">属性名</div> | <div style="width: 200px">类型</div> | <div style="width: 60px">必填</div> | 说明 |
| --- | --- | --- | --- |
| resolveOverride | `string` | 否 | 在使用 fetch(event.request) 进行 CDN 回源时，用于指定源站域名（仅支持域名，如 www.qq.com，不支持指定 HTTP 协议或者端口号) |
| cacheEverything | `boolean` | 否 | 缓存相关，用于指定缓存响应的所有头部 |
| cacheKey | `string` | 否 | 缓存相关，用于指定自定义的缓存 key |
| cacheTtl | `number` | 否 | 缓存相关，用于指定缓存时长(单位 s)，必需大于等于 0，等于 0 不缓存 |
| cacheTtlByStatus | `{[key: string]: number}` | 否 | 缓存相关，用于根据状态码指定缓存时长(单位 s)，小于等于 0 不缓存 |

## 实例属性

### body

`readonly` `body：ReadableStream`

请求体，[ReadableStream](https://cloud.tencent.com/document/product/1552/81914)

### bodyUsed

`readonly` `bodyUsed: boolean`

标识请求体是否已读取

### headers

`readonly` `headers: Headers`

请求头部，[Headers](https://cloud.tencent.com/document/product/1552/81903)

### method

`readonly` `method: string`

请求方法，默认值为`GET`

### redirect

`readonly` `redirect: string`

请求被重定向后的处理方式，可取值为：follow、error、manual；默认为 manual。

### maxFollow

`readonly` `maxFollow: number`

请求最多可重定向的次数

### url

`readonly` `url: string;`

请求的 url

### version

`readonly` `version: string`

请求使用的 HTTP 协议版本

### cf

`readonly` `cf: IncomingRequestCfProperties`

一个对象，其中包含了由边缘安全加速平台提供的与客户请求相关的属性

#### IncomingRequestCfProperties

除了标准 [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) 对象的属性外，客户端请求的 `request.cf` 对象中还包含由边缘安全加速平台提供的与请求相关的一些其他信息。包含如下信息：
| 属性名 | 类型 | 说明 | 示例值 |
| --- | --- | --- | --- |
| geo | `GeoProperties` | 一个对象，用于描述客户请求的位置 | |

#### GeoProperties

一个对象，用于描述客户请求的位置
| 属性名 | 类型 | 说明 | 示例值 |
| --- | --- | --- | --- |
| asn | `number` | 自治区号 | 12271 |
| countryName | `string` | 国家名 | United States of America |
| countryCodeAlpha2 | `string` | 国家的 ISO-3611 alpha2 代码 | US |
| countryCodeAlpha3 | `string` | 国家的 ISO-3611 alpha3 代码 | USA |
| countryCodeNumeric | `string` | 国家的 ISO-3611 numeric 代码 | 840 |
| regionName | `string` | 区域名 | New York |
| regionCode | `string` | 区域代码 | US-NY |
| cityName | `string` | 城市名 | new york |
| latitude | `number` | 经度 | 40.742802 |
| longitude | `number` | 纬度 | -73.971199 |

## 实例方法

### arrayBuffer

`arrayBuffer(): Promise<ArrayBuffer>`

返回一个 Promise，包含一个 [ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) 对象，表示整个请求体。

### blob

`blob(): Promise<Blob>`

返回一个 Promise，包含一个 [Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob) 对象，表示整个请求体。

### clone

`clone(copyHeaders?: boolean): Request`

创建当前请求对象的副本，若未设置 copyHeaders 或者 copyHeaders 为 false，返回的副本 Request 对象将会引用 headers 成员。（标准未提供 copyHeaders 参数，添加此参数主要是出于性能的考虑，避免无意义的拷贝）

### json

`json(): Promise<object>`

返回一个 Promise，包含一个 JSON 对象，表示整个请求体。

### text

`text(): Promise<string>`

返回一个 Promise, 包含一个 string，表示整个请求体。

### getCookies

`getCookies(): Cookies`

获取 [Cookies](https://cloud.tencent.com/document/product/1552/81905) 对象，会自动解析 Cookie 头部，绑定 Cookies 对象到 Request。

### setCookies

`setCookies(values: Cookies): boolean`

设置 [Cookies](https://cloud.tencent.com/document/product/1552/81905) 对象，会忽略已有 Cookie 头部，以新设置的 Cookies 对象生成新的 Cookie 头部。

## 示例代码

```typescript
async function handleRequest() {
    const request = new Request('https://www.qq.com');
    const resA = await fetch(request);
}

addEventListener('fetch', (event) => {
  return event.respondWith(handleRequest(event));
}
```

## 参考

- [MDN 文档：Request](https://developer.mozilla.org/en-US/docs/Web/API/Request)
- [代码案列：修改请求头](https://cloud.tencent.com/document/product/1552/81938)
