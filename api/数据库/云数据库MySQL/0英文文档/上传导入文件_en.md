## 1. API Description
This API (UploadCdbImportSQLFile) is used to upload files to be imported.
API request address: This API is used to upload files, and the request address is <font style='color:red'>https://up-cdb.qcloud.com/api/index</font>

1. <font style='color:red'>The parameters of the API are passed with the GET method, and the file content is passed with the POST method.</font>
2. When getting a <a href='/document/product/236/1738' title='Signature method'>signature</a>, use POST as the "Request Method". (File content is not used as signature)
3. The file content should be sliced prior to the upload, with each slice sized 2 MB. The first slice ID is 1, the second slice ID 2, and so on. The size of the last slice can be less than 2 MB.
4. You must call API <a href='/document/product/236/8377' title='Query the List of Files to Be Imported'>Query the List of Files to Be Imported</a> before the upload to check whether there is a file with the same name:
  1) If there is no file with the same name, the upload starts from the first slice. The system will generate a unique ID for the file (fileId) automatically after the first slice is uploaded.
  2) If there is a file with the same name which has been uploaded, the file to be uploaded should be renamed first.
  3) If there is a file with the same name which is being uploaded, you need to check whether the file being uploaded and the file to be uploaded are identical. If they are the same file, the upload can be started from the next slice of the uploaded one; if they are not the same file, rename the file before uploading it.


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is UploadCdbImportSQLFile.

GET parameters:

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| fileName | Yes | String | File name |
| fileSize | Yes | Int | Total size of the file (in bytes) |
| sliceId | Yes  | Int | File slice ID, starting from 1 |

POST parameters:

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| fileSlice | Yes | Binary streams | File slice content (this parameter is not used as signature) |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| data | Array | Returned data |
Parameter data is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| fileId | String | Unique ID of a file | 
| fileName | String | File name | 
| allSliceNum | Int | Total number of slices of this file | 
| completeNum | Int | Number of uploaded slices. If completeNum equals allSliceNum, it means that the file has been completely uploaded | 


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |
| 9701 | InternalFailure | File upload internal error |
| 9702 | OperationDenied | The file has been uploaded and cannot be uploaded again |


## 5. Example
Input
<pre>
API request address and GET parameters:
https://up-cdb.qcloud.com/api/index?Action=UploadCdbImportSQLFile
&<<a href="/document/product/236/6921">Common request parameters</a>>
&fileName=cdb.sql
&fileSize=17
&sliceId=1
</pre>

<pre>
HEADER:
Content-Length:1154
Content-Type:multipart/form-data; boundary=----myBoundary
</pre>

<pre>
POST:
------myBoundary
Content-Disposition: form-data; name="fileSlice"; filename="blob"
Content-Type: application/octet-stream
[File binary streams]
------myBoundary--
</pre>


Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "data": {
            "fileId": "5596d7433fe211da4b487228db4e7c57",
            "fileName": "cdb.sql",
            "allSliceNum": 1,
            "completeNum": 1
     }
}
```


