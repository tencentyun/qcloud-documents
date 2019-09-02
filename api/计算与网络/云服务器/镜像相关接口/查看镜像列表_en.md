## 1. API Description

This API (DescribeImages) is used to view the image list.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>.

* You can query the details of the specified images by specifying image IDs, or set filters to query the details of the images that satisfy the filter conditions.
* You can specify Offset and Limit to select a part of the results. The information of the first 20 images satisfying the condition is returned by default.


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| ImageIds.N |  array of Strings |No | List of image IDs such as `img-gvbnzy6f`. For the format of array parameter, please see [API Introduction](/document/api/213/11646). Image ID can be obtained by either of the following ways:<br><li>Obtained from the `ImageId` field in the returned values of API [DescribeImages](/document/api/213/9418);<br><li>Obtained via [image console](https://console.cloud.tencent.com/cvm/image).|
| Filters.N |array of [Filter](/document/api/213/9451#filter) objects|No | Filter conditions. For more information, please see the Table of Image Filter Conditions below. The maximum number is 10 for Filters, and is 5 for Filters.Values. ImageIds and Filters cannot be specified at the same time. Available values include `image-id` and `image-type`.|
| Offset |  Integer |No | Offset. Default is 0. For more information on Offset, please see [API Introduction](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).|
| Limit |  Integer |No | Limit on the number of results. Default is 20, and maximum is 100. For more information on Limit, please see [API Introduction](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).|

Table of Image Filter Conditions

| Parameter Name | Type | Description |
|---------|--------|---------|
|image-id|String|(Filter condition) Filter by image ID, such as `img-gvbnzy6f`.|
|image-type|String|(Filter condition) Filter by [image type](/document/api/213/9452#image_type).|
|image-name|String|(Filter condition) Filter by image name.|

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique RequestId is returned for each request. The value of RequestId need to be provided to the backend developer if you fail to call the API. |
| ImageSet |array of [Images](/document/api/213/9451#image).| An array of the details of an image, including the main statuses and attributes of the image. |
| TotalCount | Integer | Number of images satisfying the filter conditions.


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](/document/api/213/10146).

| Error code | Description |
|---------|---------|
|InvalidFilter|Invalid filter.|
|InvalidParameter.InvalidParameterCoexistImageIdsFilters|ImageIds and Filters cannot be specified at the same time.|
|InvalidParameterValue.InvalidParameterValueLimit|Incorrect parameter value.|

## 5. Example
Example 1
>**Query images by image IDs**:<br>
> Query the information of an image by the known image ID

Request Parameters
<pre>
https://image.api.qcloud.com/v2/index.php?Action=DescribeImages
&Version=2017-03-12
&ImageIds.0=img-pmqg1cw7
&<<a href="/doc/api/229/6976">Common request parameters</a>>
</pre>

Response Parameters
<pre>
{
    "Response": {
        "ImageSet": [
            {
                "ImageId": "img-pmqg1cw7",
                "ImageOsName": "centos6.6x86_32",
                "ImageType": "PUBLIC_IMAGE",
                "ImageCreateTime": "1970-01-01T00:00:00+00:00",
                "ImageStatus": "NORMAL",
                "ImageName": "Centos 6.6 32-bit",
                "ImageDescription": "Centos 6.6 32-bit",
                "Creator": "PUBLIC"
            }
        ],
        "TotalCount": 1,
        "RequestID": "5920380e-277a-420a-a221-0caac3eb7159"
    }
}
</pre>

Example 2
>**Query images by image types**:<br>
> Query all the private images under the account.

Request Parameters
<pre>
https://image.api.qcloud.com/v2/index.php?Action=DescribeImages
&Version=2017-03-12
&Filters.1.Name=image-type
&Filters.1.Values.1=PRIVATE_IMAGE
&<<a href="/doc/api/229/6976">Common request parameters</a>>
</pre>

Response Parameters
<pre>
{
    "Response": {
        "ImageSet": [
            {
                "ImageId": "img-pmqg1cw7",
                "ImageOsName": "centos6.6x86_32",
                "ImageType": "PUBLIC_IMAGE",
                "ImageCreateTime": "1970-01-01T00:00:00+00:00",
                "ImageStatus": "NORMAL",
                "ImageName": "Centos 6.6 32-bit",
                "ImageDescription": "Centos 6.6 32-bit",
                "Creator": "PUBLIC"
            }
        ],
        "TotalCount": 1,
        "RequestID": "5920380e-277a-420a-a221-0caac3eb7159"
    }
}
</pre>

