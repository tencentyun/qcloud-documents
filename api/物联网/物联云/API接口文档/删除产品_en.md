### 1. API Description

This API (DeleteProduct) is used to delete an IoT Cloud product.

Domain name for API request: `iotcloud.api.qcloud.com`

### 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](https://cloud.tencent.com/document/api/213/6976).

| Parameter Name | Required | Type | Description |
| --------- | ---- | ------ | ---------- |
| productID | Yes | String | ID of the product to be deleted |


### 3. Output Parameters

| Parameter Name | Type | Description |
| -------- | ------ | ---------------------------------------- |
| code | Int | Common error code. 0: successful; other values: failed. For more information, please see [Common Error Codes](https://cloud.tencent.com/document/product/634/12279). |
| message | String | Module error message description in the format of "(module error code) module error message". For more information, please see [Module Error Codes](#module_error_info) on this page. |
| codeDesc | String | Description of module error code |

### 4. Example

Input
<pre>
  https://iotcloud.api.qcloud.com/v2/index.php?Action=DeleteProduct
  &productID=ABCDE12345
  &<<a href="https://cloud.tencent.com/document/api/213/6976">Common request parameters</a>>
</pre>

Output
```
{
    "message": "",
    "codeDesc": "Success",
    "code": 0
}
```
<span id = "module_error_info"></span>
### 5. Module Error Codes

| Module Error Code | Description |
| ----- | --------------- |
| 1004 | Product to be deleted does not exist. |
| 1005 | Product to be deleted includes devices not deleted. |
| 1100 | Internal server error. Please contact technicians. |
| 1101 | Invalid request parameter |

