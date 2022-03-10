## 删除metric

- [请求地址](跳转超链接)
- [请求路径和方法](跳转超链接)
- [请求参数](跳转超链接)
- [请求内容](跳转超链接)
- [返回内容](跳转超链接)
- [CURL 示例说明](跳转超链接)

#### 请求地址

地址为实例的 IP 和 PORT，可从控制台获取到，例如10.13.20.15:9200。

#### 请求路径和方法

路径：`/_metric/${metric_name}`，`${metric_name}`为需要删除的 metric 的名称。
方法：DELETE

#### 请求参数

无

#### 请求内容

无

#### 返回内容

需要通过 error 字段判断请求是否成功，若返回内容有 error 字段则请求失败，具体错误详情请参照 error 字段描述。

#### CURL 示例说明

请求：
`DELETE /_metric/ctsdb_test1`
请求：
`curl -u root:le201909 -H 'Content-Type:application/json' -X DELETE 172.16.345.14:9201/_metric/ctsdb_test1`

返回：

```
{
   "acknowledged": true,
   "message": "delete metric ctsdb_test1 success!"
}
```
