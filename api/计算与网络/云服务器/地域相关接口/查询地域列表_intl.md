## 1. API Description


This API (DescribeRegions) is used to query regions.

Domain name for API request: cvm.api.qcloud.com

* For more information on the definition of regions, please see [Region](https://intl.cloud.tencent.com/document/product/213/9456) product documentation.

## 2. Input Parameters

No API request parameters are available for this API. You can only specify common request parameters. For more information, please see [Common Request Parameters](/document/api/213/6976).
Note: You do not need to specify the parameter Region in the common request parameter for this API.


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Request ID. |
| TotalCount | Integer | Number of regions. |
| RegionSet | Array of [Region](https://intl.cloud.tencent.com/document/product/213/9456) object | Region list. |


## 4. Error Codes

For more information, please see [Error Codes](https://intl.cloud.tencent.com/document/product/213/11657).


## 5. Example

Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeRegions
&Version=2017-03-12
&<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

<pre>
{
    "Response": {
        "TotalCount": 10,
        "RegionSet": [
            {
                "Region": "ap-beijing",
                "RegionName": "North China (Beijing)",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-guangzhou",
                "RegionName": "South China (Guangzhou)",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-guangzhou-open",
                "RegionName": "South China (Guangzhou Open)",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-hongkong",
                "RegionName": "South China (Hong Kong)",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai",
                "RegionName": "East China (Shanghai)",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai-fsi",
                "RegionName": "East China (Shanghai Finance)",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shenzhen-fsi",
                "RegionName": "South China (Shenzhen Finance)",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-singapore",
                "RegionName": "Southeast Asia (Singapore)",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "na-siliconvalley",
                "RegionName": "Western U.S. (Silicon Valley)",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "na-toronto",
                "RegionName": "North America (Toronto)",
                "RegionState": "AVAILABLE"
            }
        ],
        "RequestId": "C563943B-3BEA-FE92-29FE-591EAEB7871F"
    }
}
</pre>

