This API is used to set tag information in batches.
URL path: `http://domain name for API/v2/tags/batch_set`

### Request Parameters
In addition to the [common parameters](https://cloud.tencent.com/document/product/548/14705), the following parameters are needed:

| Parameter Name | Type | Required | Default | Description |
|-|-|-|-|-|
| tag_token_list | String | Yes | None | A json string containing several tag-token pairs. The tag corresponding to the token in each tag-token pair will be set in the backend. A maximum of 20 pairs can be set for each call with the tag placed before the token. Note that the tag cannot exceed 50 bytes in length and cannot contain spaces; the real token is at least 40 bytes in length. Example (the token value is for illustration only): [["tag 1", "token 1"], ["tag 2", "token 2"]] |

### Response Parameters
In the common response parameters, the json of the field "result" is empty.

### Example
Before MD5 encryption, URL is used to generate sign, and Rest API URL is the URL of the final request. The following is an example of push to Android, in which the common parameters need to be replaced.
#### Before MD5 encryption:

```
GETopenapi.xg.qq.com/v2/tags/batch_setaccess_id=2100240957tag_token_list=[["easonshitag1","76501cd0277cdcef4d8499784a819d4772e0fdde"]]timestamp=1502361905f255184d160bad51b88c31627bbd9530
```
#### Rest API URL:

```
http://openapi.xg.qq.com/v2/tags/batch_set?access_id=2100240957&tag_token_list=[["easonshitag1","76501cd0277cdcef4d8499784a819d4772e0fdde"]]&timestamp=1502361905&sign=3c0ea17401f02fed8397eef9230fb607
```

