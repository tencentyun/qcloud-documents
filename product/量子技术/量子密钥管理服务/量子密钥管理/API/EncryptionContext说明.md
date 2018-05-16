### Encryption Context 说明
- 当在加密（Encrypt、GenerateDataKey）时指定了该参数时，解密（Decrypt）密文时，需要传入等价的参数，才能正确的解密。
- Encryption Context 的有效值是一个总长度在 8192 个字符数以内的 json 字符串，并且只能是 String-String 形式的。当您直接调用 API 填 Encryption Context 的时候，请注意转义的问题。

<<<<<<< HEAD
**无效的 Encryption Context 举例**
=======
#### 无效的 Encryption Context举例 
>>>>>>> 27ba435c36845c884b418edf1b2a5713b13f6b95

```
[{"Key":"Value"}] //json 数组
{"Key":12345} //String-int
{"Key":["value1","value2"]} //String- 数组
```


<<<<<<< HEAD
**等价的 Encryption Context**
=======
#### 等价的 Encryption Context 
>>>>>>> 27ba435c36845c884b418edf1b2a5713b13f6b95

```
{"Key1":"Value1","Key2":"Value2"} 与 {"Key2":"Value2","Key1":"Value1"} 等价
```
