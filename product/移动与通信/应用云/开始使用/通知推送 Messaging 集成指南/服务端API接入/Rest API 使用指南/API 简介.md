请求 URL 结构为：` http://接口域名/v2/class/method?params`

|字段名|	用途|	备注|
|-|-|-|
|接口域名|	接口域名|	统一使用 openapi.xg.qcloud.com|
|v2|	表示当前 API 的版本号|	无|
|class|	提供的接口类别|	无|
|method	|每个接口大类提供的具体操作接口|	如查询、设置、删除等|
|params|	以 GET 方式调用接口时传递的参数|	包括通用参数和 API 相关特定参数。所有的参数都必须为 utf 8 编码，params 字符串应进行 url encode|

>**注意：**
>以 POST 方式调用接口时，参数应以 POST 参数形式传递，内容要求同 params 字段。HTTP HEADER 中“Content-type”字段要设置为“application/x-www-form-urlencoded”。
