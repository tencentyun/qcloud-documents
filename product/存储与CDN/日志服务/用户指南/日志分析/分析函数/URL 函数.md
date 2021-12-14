本文介绍 URL 函数的语法及示例。


## 语法格式

URL 函数支持从标准 HTTP URL 路径中提取字段，一个标准的 URL 如下：

```
[protocol:][//host[:port]][path][?query][#fragment]
```

>! 提取的字段中不包含 URL 分割符 `:` 或 `?`。
>


## 常见 URL 函数

| 函数名              | 说明                                 | 示例                              | 输出结果                                |
| ---------------- | ---------------------------- | ------------------------- | --------------------------------- |
| url_extract_fragment(url)        | 提取出 URL 中的 fragment，结果为 varchar 类型。                   | `* | select url_extract_fragment('https://console.cloud.tencent.com/#/project/dashboard-demo/categoryList')` | `/project/dashboard-demo/categoryList`                       |
| url_extract_host(url)            | 提取出 URL 中的 host，结果为 varchar 类型。                       | `* | select url_extract_host('https://console.cloud.tencent.com/cls')` | `console.cloud.tencent.com`                                  |
| url_extract_parameter(url, name) | 提取出 URL 中的 query 中那么对应的参数值，结果为 varchar 类型。    | `* | select url_extract_parameter('https://console.cloud.tencent.com/cls?region=ap-chongqing','region')` | `ap-chongqing`                                               |
| url_extract_path(url)            | 提取出 URL 中的 path，结果为 varchar 类型。                       | `* | select url_extract_path('https://console.cloud.tencent.com/cls?region=ap-chongqing')` | `cls`                                                        |
| url_extract_port(url)            | 提取出 URL 中的端口，结果为 bigint 类型。                        | `* | select url_extract_port('https://console.cloud.tencent.com:80/cls?region=ap-chongqing')` | `80`                                                         |
| url_extract_protocol(url)        | 提取出 URL 中的协议，结果为 varchar 类型。                       | `* | select url_extract_protocol('https://console.cloud.tencent.com:80/cls?region=ap-chongqing')` | `https`                                                      |
| url_extract_query(url)           | 提取出 URL 中的 query，结果为 varchar 类型。                      | `* | select url_extract_query('https://console.cloud.tencent.com:80/cls?region=ap-chongqing')` | `region=ap-chongqing`                                        |
| url_encode(value)                | 对 value 进行转义编码，使之能应用在 URL_query 中。<ul  style="margin: 0;"><li>字母不会被解码。</li><li>.-\*\_不会被编码。</li><li>空格被解码为+。</li><li>其他字符被解码为 UTF8 格式。</li></ul> | `* | select url_encode('https://console.cloud.tencent.com:80/cls?region=ap-chongqing')` | `https%3A%2F%2Fconsole.cloud.tencent.com%3A80%2Fcls%3Fregion%3Dap-chongqing` |
| url_decode(value)                | 对 URL 进行解码。                                              | `* | select url_decode('https%3A%2F%2Fconsole.cloud.tencent.com%3A80%2Fcls%3Fregion%3Dap-chongqing')` | `https://console.cloud.tencent.com:80/cls?region=ap-chongqing` |




