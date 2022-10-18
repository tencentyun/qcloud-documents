加密过程：
```plaintext
const crypto = require('crypto')
const urlencode = require('urlencode')
 
// ************************************
// params 为请求加密参数
// key 为加密密钥，比如：secretKey
// ************************************
function sigCode(params: any, key: string) {
  try {
    let queryDataTmp = Object.assign({}, params)
    delete queryDataTmp.sig
    delete queryDataTmp.host
    // 第一步：将所有参数按key进行字典升序排列
    let paramtmp = Object.keys(queryDataTmp).sort()
    let parmaSort = ''
    // 第二步：将重新排序后的参数(key=value)用&拼接起来，得到源串
    for (const item of paramtmp) {
      // 对象和数组进行字符串化
      let itemValue = queryDataTmp[item]
      let changeType = ['object', 'array']
      if (changeType.indexOf(typeof itemValue) >= 0) {
        itemValue = JSON.stringify(itemValue)
      }
      parmaSort = parmaSort + item + '=' + itemValue + '&'
    }
    parmaSort = urlencode(parmaSort.substr(0, parmaSort.length - 1))
    // 第三步：使用HMAC-SHA256加密算法，通过密钥（secretKey或appkey）对源串加密
    const sig = crypto.createHmac('sha256', key).update(parmaSort)
    return sig.digest('hex')
  } catch (error) {
    console.log('codeSig error:', error)
    return false
  }
}

```

## 签名过程示例
请求参数：
```plaintext
{
    "id": "611f6b5b01af259c18954808",
    "secretId": "ca355ab0019211ecaed0ed79aa4a58cf",
    "users": [{"name": "javinz", "age": 18}],
}

```


排序并且字符串格式化后得到（用 `&` 连接每一个参数）：
```plaintext
id=611f6b5b01af259c18954808&secretId=ca355ab0019211ecaed0ed79aa4a58cf&users=[{"name":"javinz","age":18}]

```

urlencode 编码后得到：
```plaintext
id%3D611f6b5b01af259c18954808%26secretId%3Dca355ab0019211ecaed0ed79aa4a58cf%26users%3D%5B%7B%22name%22%3A%22javinz%22%2C%22age%22%3A18%7D%5D
```

假设加密密钥 key 为：taidc，那么最后得到的 sig 为：
```plaintext
1c55d09921cad5a44de7cc983fe3de4e8ef6d7f98fd054b5335d729eb9ee3534
```
