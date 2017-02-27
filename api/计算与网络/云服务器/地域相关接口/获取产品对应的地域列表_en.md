## 1. API Description

This API (DescribeProductRegionList) is used to get a list of regions where the product is available.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>


* You can directly view the [Region section](https://www.qcloud.com/doc/product/213/497#1.-.E5.9C.B0.E5.9F.9F) in the product documentation to learn what role the region attribute plays in the product.
* In addition to region restrictions, there are also restrictions on purchase quantity of CVM products. For more information, refer to [Restrictions on CVM Instance Purchase](https://www.qcloud.com/doc/product/213/2664).


## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceType | Yes | Int | Instance type. <br>1: Cloud Virtual Machine<br>2: Cloud Database<br>3: Cloud Load Balance|

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, refer to [Common Error Codes](https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://www.qcloud.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page |
| availableRegion | Array | Get a list of regions where the product is available. The parameter Region that may be used by other APIs can be obtained here, such as gz for Guangzhou, sh for Shanghai, and hk for Hong Kong.

## 4. Example
Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeProductRegionList
 &instanceType=1
 &<<a href="https://www.qcloud.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output

```
 {
      "code":0,
      "message": "",
      "availableRegion ":
      {
          "gz":"Guangzhou",
          "sh":"Shanghai",
          "hk":"Hong Kong"
     }
  }
```




