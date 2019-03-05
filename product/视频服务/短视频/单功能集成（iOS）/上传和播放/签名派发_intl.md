Client Video Upload means that the end users of an App upload local videos to Tencent Cloud VOD. For more information, please see [How to Upload Videos from Client](https://cloud.tencent.com/document/product/266/9219). This document introduces how to generate a signature for client video upload in a concise manner.

## Overview
The overall process of client video upload is shown as below:


![figure description](https://main.qcloudimg.com/raw/3c9b427ba32f5f23c352d339a3e45af8.jpg)


To support client video upload, developers need to build two backend services: signature distribution service and event notification receiving service.

* The client first sends a request for an upload signature to the signature distribution service.
* The signature distribution service verifies whether the user has upload permission. If the verification succeeds, the signature is generated and distributed. Otherwise, an error code is returned and the upload process ends.
* The client uploads the video using the upload feature integrated in the short video SDK after obtaining the signature.
* After the upload is completed, the VOD backend sends an [Event Notification of Completion of Video Upload](https://cloud.tencent.com/document/product/266/7830) to the developer's event notification receiving service.
* If the signature distribution service specifies the video processing [task flow](https://cloud.tencent.com/document/product/266/11700) in the signature, the VOD service automatically processes the video according to the specified flow after it is uploaded. In short video scenarios, [AI Porn Detection](https://cloud.tencent.com/document/product/266/11701#.E8.A7.86.E9.A2.91.E9.89.B4.E9.BB.84) is generally performed when processing videos.
* After the video processing is completed, the VOD backend sends an [Event Notification for Task Flow Status Change](https://cloud.tencent.com/document/product/266/9636) to the developer's event notification receiving service.

Now, the entire process from video upload to processing is completed.

## Signature Generation
For more information on the signature for client video upload, please see VOD's [Signature for Client Video Upload](https://cloud.tencent.com/document/product/266/9221).

## Example of Signature Distribution Service Implementation

``` 
/**
 * Calculate signature
 */
function createFileUploadSignature({ timeStamp = 86400, procedure = '', classId = 0, oneTimeValid = 0, sourceContext = '' }) {
    // Determine the current time and expiration time for the signature
    let current = parseInt((new Date()).getTime() / 1000)
    let expired = current + timeStamp;  // Validity period: 1 day
    // Enter parameters into the parameter list
    let arg_list = {
        //required
        secretId: this.conf.SecretId,
        currentTimeStamp: current,
        expireTime: expired,
        random: Math.round(Math.random() * Math.pow(2, 32)),
        //opts
        procedure,
        classId,
        oneTimeValid,
        sourceContext
    }
    // Calculate signature
    let orignal = querystring.stringify(arg_list);
    let orignal_buffer = new Buffer(orignal, "utf8");
    let hmac = crypto.createHmac("sha1", this.conf.SecretKey);
    let hmac_buffer = hmac.update(orignal_buffer).digest();
    let signature = Buffer.concat([hmac_buffer, orignal_buffer]).toString("base64");
    return signature;
}
/**
 *Respond to signature request
 */
function getUploadSignature(req, res) {
    res.json({
        code: 0,
        message: 'ok',
        data: {
            //Specify the template parameter and the task flow for the uploaded video
            signature: gVodHelper.createFileUploadSignature({ procedure: 'QCVB_SimpleProcessFile({1,1,1,1})' })
        }
    });
}
``` 

