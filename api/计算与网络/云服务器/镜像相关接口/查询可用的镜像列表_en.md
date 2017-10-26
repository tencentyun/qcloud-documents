## 1. API Description
 

This API (DescribeImages) is used to obtain the images that are available for users, which can be used to create CVM instances.

Domain name for API request: <font style="color:red">image.api.qcloud.com</font>

* You can make a query by image ID (a maximum of 10 image IDs can be specified). You can also filter images by their statuses or types.
* There are 5 image statues, by which you can filter images according to your need: 
	* 1: Creating... 
	* 2: Normal 
	* 3: In Use
	* 4: Synchronizing... 
	* 5: Copying...
* There are four image types, by which you can filter images according to your need: 
  * 1: Private Images (images created by current account) 
	* 2: Public Images (images from Tencent Cloud) 
	* 3: Service Marketplace Images (images provided by Service Marketplace) 
	* 4: Shared Images (images shared by other accounts to current account)

* Service Marketplace Images do not apply to North America region.

* List of commonly used public image IDs:

| Image Name | unImgId/unImageId |
|---------|-------------------------------------|
| CentOS 5.8 32-bit | img-7br3ouzr |
| CentOS 5.8 64-bit | img-4cq5l3u1 |
| CentOS 5.11 32-bit | img-ko6c8e6f |
| CentOS 5.11 64-bit | img-ailu7ftt |
| CentOS 6.2 64-bit | img-50mr2ow7 |
| CentOS 6.3 32-bit | img-1afi29f3 |
| CentOS 6.3 64-bit | img-4w43a15z |
| CentOS 6.4 32-bit | img-k09t26i1 |
| CentOS 6.4 64-bit | img-jlo93805 |
| CentOS 6.5 32-bit | img-7uq6rrhr |
| CentOS 6.5 64-bit | img-7fwdvfur |
| CentOS 6.6 32-bit | img-5jbd8jxn |
| CentOS 6.6 64-bit | img-h5le2uy5 |
| CentOS 6.7 32-bit | img-ljriodz5 |
| CentOS 6.7 64-bit | img-9iwld2rx |
| CentOS 7.0 64-bit | img-b1ve77s9 |
| CentOS 7.1 64-bit | img-9q2lxkar |
| CentOS 7.2 64-bit | img-31tjrtph |
| Debian 7.4 64-bit | img-c1l6bgb1 |
| Debian 7.8 32-bit | img-2p1g2wjv |
| Debian 7.8 64-bit | img-feqctcrx |
| Debian 8.2 32-bit | img-ez7jwngr |
| Debian 8.2 64-bit | img-hi93l4ht |
| Ubuntu Server 12.04 LTS 64-bit (Docker) | img-aa9z7opt |
| Ubuntu Server 14.04.1 LTS 32-bit | img-qpxvpujt |
| Ubuntu Server 14.04.1 LTS 64-bit | img-3wnd9xpl |
| openSUSE 12.3 32-bit | img-8bf2kz5x |
| openSUSE 12.3 64-bit | img-1p6m0vz5 |
| openSUSE 13.2 64-bit | img-pmhtrjdx |
| SUSE Linux Enterprise Server 11 SP3 64-bit | img-mg89zx1h |
| SUSE Linux Enterprise Server 12 64-bit | img-d5304izr |
| FreeBSD 10.1 64-bit | img-871lthrb |
| CoreOS 717.3.0 64-bit | img-6mre94jv |
| Windows Server 2008 R2 Enterprise Edition SP1 64-bit | img-0vbqvzfn |
| Windows Server 2012 R2 Standard Edition 64-bit English | img-lkxqa4kj |
| Windows Server 2012 R2 Standard Edition 64-bit Chinese | img-egif9bvl |
| Windows Server 2012 R2 Datacenter Edition 64-bit English | img-2tddq003 |
| Windows Server 2012 R2 Datacenter Edition 64-bit Chinese | img-29hl923v |
## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Common Request Parameters](/document/api/213/6976) page.
 
| Parameter Name | Required | Type | Description |
|---------|---------|---------|------------------|
| imageType | Yes | Int | Filter by image type. For parameter values, see the above list.
| imageIds.n | No | String | Filter by image ID; imageType is required if an image ID is specified. (This API allows passing multiple IDs at a time. For the format of this parameter, refer to `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568)).
| status | No | Int | Filter by image status. The default is 0, which indicates querying all images. For parameter values, see the above list.
| offset | No | Int | Offset; The default is 0. For more information about `offset`, refer to the relevant sections in API [Introduction](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).
| limit | No | Int | Number of returned results. The default is 20, and the maximum is 100. For more information on `limit`, refer to relevant sections in API [Introduction](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89).

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| totalCount | Int | Number of images matching the criteria.
| imageSet | Array | Information of images matching the criteria.


imageSet stores details of images with the following structure:

| Parameter Name | Type | Description |
|---------|---------|---------|
| unImgId | String | Hard disk image ID in the format "img-xxxxxxxx", which is used to identify the image.
| imageName | String | Hard disk image name.
| imageDescription | String | Description information.
| imageType | Int | Image type. For parameter values, see the above list.
| osName | String | Operating system name.
| createTime | String | Time of creation.
| creator | String | Creator's account ID.
| status | Int | Image status. For parameter values, see the above list.

## 4. Example
 
Input
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeImages
  &imageType=1
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

```

{
    "code" : 0,
    "message" : "",
    "totalCount" : 1,
    "imageSet" : [
        {
            "unImgId" : "img-1234test",
            "imageName" : "test",
            "imageDescription" : "test",
            "osName" : "Ubuntu 12.04 64bit",
            "imageType" : 1,
            "createTime" : "2014-09-27 10:11:00",
            "createor" : "1000",
            "status" : 2
        }
    ]
}
```



