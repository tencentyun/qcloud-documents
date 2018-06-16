## Overview

Tencent Cloud Video Transcoding Service provides the API for [Video Processing](/document/product/266/15571). Developers can perform transcoding on videos stored in COS by calling this API.

This solution provides a method for developers to initiate a video transcoding task without having to call the API. By making simple configurations on the COS, a preset operation is triggered to automatically initiate the video processing task when developers upload files to the COS.

## How Does It Work

The solution mainly includes the following three Tencent Cloud services:
1. [Cloud Object Storage](https://cloud.tencent.com/product/cos) (COS)
2. [Serverless Cloud Function](https://cloud.tencent.com/product/scf) (SCF)
3. Video transcoding

![SCF call transcoding framework](https://main.qcloudimg.com/raw/7ddb98640a9f0c1de45cffba447792a4.jpg)

As shown in the above flow chart, the solution works as follows:
1. Developers upload a video file to the input bucket of COS.
2. COS automatically informs SCF of the uploaded new file.
3. SCF automatically initiates a video processing request to the transcoding service.
4. The transcoding service reads the new file from the input bucket of COS and performs the transcoding operation.
5. The transcoding service writes the transcoded file to the output bucket of COS.

In the entire process, developers only need to upload the file, and the remaining steps are automatically completed by Tencent Cloud.

## Configuration Procedure

Developers must configure COS and SCF before using the above feature. They only needs to perform the configuration operation once, unless the requirement for the transcoding service changes (for example, modifying the input/output bucket, the output path, the transcoding specification).

### COS bucket configuration

Developers need to create an input bucket and an output bucket with their own accounts, and complete the bucket configuration. For more information, please see [Bucket Configuration](/document/product/266/16923).


### SCF configuration

The solution provides an SCF template. Developers can configure the template based on their needs for video processing. After the template has been configured, they upload it and create a trigger in the SCF console.

#### 1. Obtain SecretId and SecretKey of the key
SecretId and SecretKey can be found in the [CAM console](https://console.cloud.tencent.com/cam/capi). [Apply for a key](/document/api/213/6984#1.-.E7.94.B3.E8.AF.B7.E5.AE.89.E5.85.A8.E5.87.AD.E8.AF.81) if you have not created one.

#### 2. Enter the SCF template
Download the [SCF template](https://main.qcloudimg.com/raw/38e2258e7ca2716fe993425740cc6dc3.zip) and complete the configuration file **config.json** according to the table content. The parameters in the configuration file are described as follows:

| Name | Required | Type | Description |
|---|---|---|---|---|
| SecretId | Yes | String | The SecretId in the API key |
| SecretKey | Yes | String | The SecretKey in the API key |
| Para | Object | Yes | See [Parameters for Task Execution](#para.EF.BC.88.E6.89.A7.E8.A1.8C.E4.BB.BB.E5.8A.A1.E5.8F.82.E6.95.B0.EF.BC.89) |

##### Para (parameters for task execution)
| Name | Required | Type | Description |
|---|---|---|---|---|
| output | Yes | Object | See [Output File Information Parameters](/document/product/266/15571#output.EF.BC.88.E8.BE.93.E5.87.BA.E6.96.87.E4.BB.B6.E4.BF.A1.E6.81.AF.E5.8F.82.E6.95.B0.EF.BC.89) |
| mediaCheck | No | Object | See [Porn Detection Parameters](/document/product/266/15571#mediacheck.EF.BC.88.E8.A7.86.E9.A2.91.E9.89.B4.E9.BB.84.E5.8F.82.E6.95.B0.EF.BC.89) |
| mediaProcess | No | Object | See [Video Processing Parameters](/document/product/266/15571#mediaprocess.EF.BC.88.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E5.8F.82.E6.95.B0.EF.BC.89) |
| taskAttribute | No | Object | See [Task Attribute Configuration Parameters](/document/product/266/15571#taskattribute.EF.BC.88.E4.BB.BB.E5.8A.A1.E5.B1.9E.E6.80.A7.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0.EF.BC.89) |

##### Example
Perform transcoding for the input file. The transcoding template IDs include **210**, **220** and **230**.
The transcoded file is output to the **/output/test/** directory of the **myoutputbucket** bucket.

```json
{
    "SecretId":"AKIDgJoxxxxxxxxxxxxxxxxxxxxxxsW78G9r",
    "SecretKey":"f8OTP9xxxxxxxxxxxxxxxxxxCh186sUy",
    "Para": {
        "output": {
            "bucket": "myoutputbucket",
            "dir": "/output/test/"
        },
        "mediaProcess":{
            "transcode":{
                "definition":[210,220,230]
            }
        }
    }
}
``` 

After configuring **config.json**, package the modified template into a zip file named **RequestVideoTranscode.zip**.

#### 3. Create a SCF trigger
1. Log in to the [SCF console](https://console.cloud.tencent.com/scf), select the same region as that of the input file bucket (if the input file bucket belongs to Guangzhou, select **Guangzhou**), and click **New**.
2. Go to the **Function Configuration** section, enter **RequestVideoTranscode** as the function name, select **Nodejs 6.10** for the **Runtime Environment**, set **Timeout** to **10s**, and keep default settings for the other options, and then click **Next**.
3. Go to the **Function Code** section, and select **Upload local zip file**. Enter **index.main_handler** for the execution method, select the **RequestVideoTranscode.zip** created in the previous step, and click **Next**.
4. Go to the **Trigger Method** section, click **Add Trigger**, select **COS Trigger** for the trigger method, enter a name of the input file bucket for **COS Bucket** (e.g. **myinputbucket**), select **File Upload** for **Event Type**, then click **Save** to complete the creation process, and finally click **Finish**.

## Verification Mode
This section describes how to verify whether uploading files to COS triggers video processing to obtain the transcoded video file.
1. According to the [configuration process](/document/product/266/16923), complete the configuration of the COS Bucket and SCF, and assume that:
The name of the input file bucket is **myinputbucket**.
The name of the output file bucket is **myoutputbucket**.
The IDs of target transcoding templates are **30**, **40** and **50**.
2. Go to the **Bucket List** in the COS console, select **myinputbucket**, click **Upload File** to upload a video file to the input file bucket.
3. Go to the **Function Service** in the [SCF Console](https://console.cloud.tencent.com/scf), enter the **RequestVideoTranscode** function, and click **Log** to view the request parameters and the returned results.
4. After the transcoding is completed, the transcoded file can be found in the **myoutputbucket** of the COS.

![](https://main.qcloudimg.com/raw/2edf0c22ae509d397c8293a0821e486b.png)


***Note:***

1. The input file bucket, the output file bucket and SCF must be in the same region.
2. The solution is supported in **Beijing**, **Shanghai** and **Guangzhou**. Other regions will be available soon.
3. Original or transcoded video files should not be stored directly in the bucket's root directory, otherwise an error may occur (at least one sub-directory is created).
4. After a bucket is created in the console, it takes 1-2 minutes for the bucket to appear in the configuration options of the SCF.
