Below are Tencent Cloud Object Storage (COS) service related APIs and their descriptions:

## About Service Operation
<style rel="stylesheet">
table th:nth-of-type(1) {
width: 350px;	
}
table th:nth-of-type(2) {
width:550px;	
}
</style>

| API | Description |
|---------|---------|
| [Get Service](https://cloud.tencent.com/document/product/436/8291) | List all Buckets under this account | 

## About Bucket Operations

| API | Description |
|---------|---------|
| [Get Bucket](https://cloud.tencent.com/document/product/436/7734) | List some or all of the Objects under the specified Bucket | 
| [Get Bucket ACL](https://cloud.tencent.com/document/product/436/7733) | Obtain the ACL table of the Bucket | 
| [Get Bucket CORS](https://cloud.tencent.com/document/product/436/8274) | Obtain the cross-domain access configuration of the Bucket | 
| [Get Bucket Location](https://cloud.tencent.com/document/product/436/8275) | Obtain the region of the Bucket | 
| [Get Bucket Lifecycle](https://cloud.tencent.com/document/product/436/8278) | Read lifecycle management configurations | 
| [Put Bucket](https://cloud.tencent.com/document/product/436/7738) | Create a Bucket under the specified account | 
| [Put Bucket ACL ](https://cloud.tencent.com/document/product/436/7737)| Write to the ACL table of the Bucket | 
| [Put Bucket CORS](https://cloud.tencent.com/document/product/436/8279) | Configure the cross-domain access permission of the Bucket | 
| [Put Bucket Lifecycle](https://cloud.tencent.com/document/product/436/8280) | Set the features for lifecycle management | 
| [Delete Bucket](https://cloud.tencent.com/document/product/436/7732) | Delete the Bucket under the specified account | 
| [Delete Bucket CORS](https://cloud.tencent.com/document/product/436/8283) | Delete the cross-domain access configuration of the Bucket | 
| [Delete Bucket Lifecycle](https://cloud.tencent.com/document/product/436/8284) | Delete lifecycle management |
| [Head Bucket](https://cloud.tencent.com/document/product/436/7735) | Confirm whether a specified Bucket exists under the specified account | 
| [List Multipart Uploads](https://cloud.tencent.com/document/product/436/7736) | Query the ongoing multipart upload | 

## About Object Operations

| API | Description |
|---------|---------|
| [Append Object](https://cloud.tencent.com/document/product/436/7741) | Upload an Object (file/object) to the specified Bucket via multipart upload method | 
| [Get Object](https://cloud.tencent.com/document/product/436/7753) | Download an Object (file/object) to the local computer | 
| [Get Object ACL](https://cloud.tencent.com/document/product/436/7744) | Obtain the ACL table of the Object (file/object) | 
| [Put Object](https://cloud.tencent.com/document/product/436/7749) | Upload an Object (file/object) to the specified Bucket | 
| [Put Object ACL](https://cloud.tencent.com/document/product/436/7748) | Write to the ACL table of the Object (file/object) | 
| [Delete Object](https://cloud.tencent.com/document/product/436/7743) | Delete the specified Object (file/object) in the Bucket | 
| [Delete Multiple Object](https://cloud.tencent.com/document/product/436/8289) | Delete Objects (files/objects) in batch in the Bucket | 
| [Head Object](https://cloud.tencent.com/document/product/436/7745) | Obtain the meta information of the Object | 
| [Options Object](https://cloud.tencent.com/document/product/436/8288) | A preflight request for cross-domain access | 
| [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746) | Initialize the Multipart Upload operation | 
| [List Multipart Uploads](https://cloud.tencent.com/document/product/436/7750) | Multipart upload files | 
| [List Parts](https://cloud.tencent.com/document/product/436/7747) | Query the uploaded parts in a specific multipart upload operation | 
| [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742) | Complete the multipart upload of the entire file | 
| [Abort Multipart Upload](https://cloud.tencent.com/document/product/436/7740) | Abort a multipart upload operation and delete the uploaded parts | 
| [Put Object Copy](https://cloud.tencent.com/document/product/436/10881) | Copy a file from the source path to the destination path | 



