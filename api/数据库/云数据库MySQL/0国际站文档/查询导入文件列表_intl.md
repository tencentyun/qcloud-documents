## 1. API Description
This API (GetCdbImportSQLFileList) is used to query the uploaded list of files to be imported.
Domain for API request: <font style='color:red'>cdb.api.qcloud.com </font>


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, refer to <a href='/document/product/236/6921' title='Common Request Parameters'>Common Request Parameters</a>. The Action field for this API is GetCdbImportSQLFileList.

| Parameter Name | Required  | Type | Description |
|---------|---------|---------|---------|
| offset | No | Int | Record offset; default is 0 |
| Limit | No | Int | Number of returned results upon a single request; default is 20 |


## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code; 0: Succeeded; other values: Failed. For more information, please refer to <a href='https://intl.cloud.tencent.com/document/product/236/1743' title='Common Error Codes'>Common Error Codes</a> on the Error Code page.  |
| message | String | Module error message description depending on API.  |
| codeDesc | String | Error description |
| totalCount | Int | Total number of uploaded files |
| files | Array | Returned data |
Parameter files is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| fileId | String | Unique ID of a file | 
| fileName | String | File name | 
| fileSize | Int | File size (in bytes) | 
| uploadTime | String | File upload time | 
| isUploadFinished | Int | Indicate whether the entire file is successfully uploaded. Available values: 1: Succeeded, 0: Uploading | 
| uploadInfo | Array | File upload progress information | 
Parameter uploadInfo is composed as follows:

| Parameter Name | Type | Description |
|---------|---------|---------|
| allSliceNum | Int | Total number of slices that need to be uploaded of this file | 
| completeNum | Int | Number of slices that have been uploaded currently | 


## 4. Error Codes
The following error codes only include the business logic error codes for this API.

| Error Code | Error Message | Error Description |
|---------|---------|---------|
| 9003 | InvalidParameter | Incorrect parameter |


## 5. Example
Input

<pre>
https://cdb.api.qcloud.com/v2/index.php?Action=GetCdbImportSQLFileList
&<<a href="/document/product/236/6921">Common request parameters</a>>
</pre>

Output
```
{
    "code":"0",
    "message":"",
    "codeDesc":"Success",
    "totalCount": 1,
    "files": [
        {
            "fileId": "5596d7433fe211da4b487228db4e7c57",
            "fileName": "joellwang.sql",
            "fileSize": 8581633,
            "uploadTime": "2016-11-28 15:16:13",
            "isUploadFinished": 0,
            "uploadInfo": {
                "allSliceNum": 5,
                "completeNum": 3
            }
        }
    ]
}
```


