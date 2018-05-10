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
| [GET Service](https://cloud.tencent.com/document/product/436/8291) | List all Buckets under this account | 

## About Bucket Operations

| API | Description |
|---------|---------|
| [GET Bucket](https://cloud.tencent.com/document/product/436/7734) | List some or all of the Objects under the specified Bucket | 
| [GET Bucket acl](https://cloud.tencent.com/document/product/436/7733) | Obtain the ACL table of the Bucket | 
| [GET Bucket cors](https://cloud.tencent.com/document/product/436/8274) | Obtain the cross-domain access configuration of the Bucket | 
| [GET Bucket location](https://cloud.tencent.com/document/product/436/8275) | Obtain the region of the Bucket | 
| [GET Bucket lifecycle](https://cloud.tencent.com/document/product/436/8278) | Read lifecycle management configurations | 
| [PUT Bucket](https://cloud.tencent.com/document/product/436/7738) | Create a Bucket under the specified account | 
| [PUT Bucket acl ](https://cloud.tencent.com/document/product/436/7737)| Write to the ACL table of the Bucket | 
| [PUT Bucket cors](https://cloud.tencent.com/document/product/436/8279) | Configure the cross-domain access permission of the Bucket | 
| [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/8280) | Set the features for lifecycle management | 
| [DELETE Bucket](https://cloud.tencent.com/document/product/436/7732) | Delete the Bucket under the specified account | 
| [DELETE Bucket cors](https://cloud.tencent.com/document/product/436/8283) | Delete the cross-domain access configuration of the Bucket | 
| [DELETE Bucket lifecycle](https://cloud.tencent.com/document/product/436/8284) | Delete lifecycle management |
| [HEAD Bucket](https://cloud.tencent.com/document/product/436/7735) | Confirm whether a specified Bucket exists under the specified account | 
| [List Multipart Uploads](https://cloud.tencent.com/document/product/436/7736) | Query the ongoing multipart upload | 

## About Object Operations

| API | Description |
|---------|---------|
| [Append Object](https://cloud.tencent.com/document/product/436/7741) | Upload an Object (file/object) to the specified Bucket via multipart upload method | 
| [GET Object](https://cloud.tencent.com/document/product/436/7753) | Download an Object (file/object) to the local computer | 
| [GET Object acl](https://cloud.tencent.com/document/product/436/7744) | Obtain the ACL table of the Object (file/object) | 
| [PUT Object](https://cloud.tencent.com/document/product/436/7749) | Upload an Object (file/object) to the specified Bucket | 
| [PUT Object acl](https://cloud.tencent.com/document/product/436/7748) | Write to the ACL table of the Object (file/object) | 
| [DELETE Object](https://cloud.tencent.com/document/product/436/7743) | Delete the specified Object (file/object) in the Bucket | 
| [DELETE Multiple Object](https://cloud.tencent.com/document/product/436/8289) | Delete Objects (files/objects) in batch in the Bucket | 
| [HEAD Object](https://cloud.tencent.com/document/product/436/7745) | Obtain the meta information of the Object | 
| [OPTIONS Object](https://cloud.tencent.com/document/product/436/8288) | A preflight request for cross-domain access | 
| [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746) | Initialize the Multipart Upload operation | 
| [List Multipart Uploads](https://cloud.tencent.com/document/product/436/7750) | Multipart upload files | 
| [List Parts](https://cloud.tencent.com/document/product/436/7747) | Query the uploaded parts in a specific multipart upload operation | 
| [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742) | Complete the multipart upload of the entire file | 
| [Abort Multipart Upload](https://cloud.tencent.com/document/product/436/7740) | Abort a multipart upload operation and delete the uploaded parts | 
| [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) | Copy a file from the source path to the destination path | 



