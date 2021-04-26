- 当在加密（Encrypt、GenerateDataKey）时指定了该参数时，解密（Decrypt）密文时，需要传入等价的参数，才能正确的解密。
- Encryption Context 的有效值是一个总长度在8192个字符数以内的json字符串，并且只能是 String-String 形式的。当您直接调用 API 填 Encryption Context 的时候，请注意转义的问题。

**无效的 Encryption Context 举例**

```
[{"Key":"Value"}] //json数组
{"Key":12345} //String-int
{"Key":["value1","value2"]} //String-数组
```


**等价的 Encryption Context**

```
{"Key1":"Value1","Key2":"Value2"} 与 {"Key2":"Value2","Key1":"Value1"} 等价
```
