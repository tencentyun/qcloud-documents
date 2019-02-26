# Encryption Context Description
- If this parameter is specified in the process of encryption (Encrypt, GenerateDataKey), the ciphertext can be correctly decrypted only if an equivalent parameter is passed.
- The valid value for Encryption Context is a JSON string with a maximum length of 8,192 characters and a format of String-String only. When you directly call the API to enter Encryption Context, be sure to escape the characters.

**Example of invalid Encryption Context**

```
[{"Key":"Value"}] //JSON Array
{"Key":12345} //String-int
{"Key":["value1","value2"]} //String-Array
```


**Equivalent Encryption Context**

```
{"Key1":"Value1","Key2":"Value2"} is equivalent to {"Key2":"Value2","Key1":"Value1"}
```

