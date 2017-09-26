## Preparations for Development

### Acquiring SDK

Android SDK for Cloud Object Storage (COS) can be downloaded from [Android SDK](https://github.com/tencentyun/cos_android_sdk).

For more examples, refer to [Android SDK Demo](https://github.com/tencentyun/cos_android_sdk/tree/master/COSDemo). 

## Preparations for Development

1. Android 2.2 or later version is supported for SDK;
2. Your mobile phone must be connected to such networks as GPRS, 3G or WIFI;
3. Some features may not function properly if there is not enough storage space on your mobile phone;
4. Get APP ID, SecretID and SecretKey from the Console. For more information, refer to Permission Control.

### Configuring SDK

Import the following jar packages into configuration project:

- cos-android-sdk1.4.2.jar
- okhttp-3.2.0.jar
- okio-1.6.0.jar

SDK needs some permissions related to network access. The following permission entries should be included in AndroidManifest.xml:

```html
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WAKE_LOCK"/>
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

## Initialization

You need to instantiate COSClient and COSClientConfig before performing operations:

#### Instantiating COSClientConfig

Instantiate COSClientConfig object by calling COSClientConfig() method.

```java
COSClientConfig config = new COSClientConfig();
```

#### Configuring COSClientConfig

| Method                                       | Description                                     |
| ---------------------------------------- | ---------------------------------------- |
| setEndPoint(COSEndPoint endPoint)        | Set the region: South China COSEndPoint.COS_GZ; North China COSEndPoint.COS_TJ; East China COSEndPoint.COS_SH. In SDK, default is South China. |
| setConnectionTimeout(int connectionTimeout) | Set connection timeout                                   |
| setSocketTimeout(int socketTimeout)      | Read timeout                                   |
| setMaxConnectionsCount(int maxConnectionsCount) | Maximum number of concurrent connections                                   |
| setMaxRetryCount(int maxRetryCount)      | Number of retry attempts for a failed request                                 |


#### Instantiating COSClient

Instantiate COSClient object by calling COSClient (Context context, String appid, COSClientConfig config, String peristenceId) method.

#### Parameter Description

| Parameter Name          | Type              | Required | Description                                     |
| :------------ | :-------------- | :--- | :--------------------------------------- |
| context       | Context         | Yes    | Context                                      |
| appid         | String          | Yes    | APPID registered with Tencent Cloud                              |
| config        | COSClientConfig | No    | Configuration setting                                     |
| persistenceId | String          | No    | Persistence ID. Each COSClient needs to be configured with an unique ID for the persistent storage of the list of unfinished tasks, so that the upload task can be resumed when you reenter the application after exit. If this field is Null, the list cannot be stored persistently |

#### Example

```Java
//Create COSClientConfig object, and modify default configuration parameters as required
COSClientConfig config = new COSClientConfig();
//Set the region
config.setEndPoint(COSEndPoint.COS_GZ);

Context context = getApplicationContext();
String appid =  "APPID registered with Tencent Cloud";
String peristenceId = "Persistence ID";

//Create COSlient object to perform operations on COS
COSClient cos = new COSClient(context,appid,config,peristenceId);
```

## Quick Start 

### Initializing COSClient

```java
String appid =  "APPID registered with Tencent Cloud";
Context context = getApplicationContext();
String peristenceId = "Persistence ID";

//Create COSClientConfig object, and modify default configuration parameters as required
COSClientConfig config = new COSClientConfig();
//For example, set the region
config.setEndPoint(COSEndPoint.COS_GZ);

COSClient cos = new COSClient(context,appid,config,peristenceId);
```

### Uploading a File

```java
String bucket = "cos space name";
String cosPath = "Remote path, i.e. the path stored on COS";
String srcPath = "Absolute path of local file";
String sign = "Signature. Multiple-time signature is used here";

PutObjectRequest putObjectRequest = new PutObjectRequest();
putObjectRequest.setBucket(bucket);
putObjectRequest.setCosPath(cosPath);
putObjectRequest.setSrcPath(srcPath);
putObjectRequest.setSign(sign);
putObjectRequest.setListener(new  IUploadTaskListener(){
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {

         PutObjectResult result = (PutObjectResult) cosResult;
         if(result != null){
             StringBuilder stringBuilder = new StringBuilder();
             stringBuilder.append(" Upload result: ret=" + result.code + "; msg =" +result.msg + "\n");
             stringBuilder.append(" access_url= " + result.access_url == null ? "null" :result.access_url + "\n");
             stringBuilder.append(" resource_path= " + result.resource_path == null ? "null" :result.resource_path + "\n");
             stringBuilder.append(" url= " + result.url == null ? "null" :result.url);
             Log.w("TEST",stringBuilder.toString());
          }
     }

     @Override
     public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
         Log.w("TEST","An error occurred during the upload: ret =" +cosResult.code + "; msg =" + cosResult.msg);
     }

     @Override
     public void onProgress(COSRequest cosRequest, final long currentSize, final long totalSize) {
         float progress = (float)currentSize/totalSize;
         progress = progress *100;
         Log.w("TEST","Progress: " + (int)progress + "%"); 
      }
});
```

### Downloading a File

```java
String downloadURl =  "URL for downloading the file";
String savePath = "The path under which the file is saved locally";
String sign = "Signature is required if token hotlink protection is enabled, otherwise it is not required";

GetObjectRequest getObjectRequest = new GetObjectRequest(downloadURl,savePath);
getObjectRequest.setSign(null);
getObjectRequest.setListener(new IDownloadTaskListener() {
    @Override
    public void onProgress(COSRequest cosRequest, final long currentSize, final long totalSize) {
        float progress =  currentSize / (float)totalSize;
        progress = progress * 100;
        progressText.setText("progress =" + (int) (progress) + "%");
        Log.w("TEST", "progress =" + (int) (progress) + "%");
   }

   @Override
   public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
       Log.w("TEST","code =" + cosResult.code + "; msg =" + cosResult.msg);
   }

   @Override
   public void onFailed(COSRequest COSRequest, COSResult cosResult) {
        Log.w("TEST","code =" + cosResult.code + "; msg =" + cosResult.msg);
   }
});

GetObjectResult getObjectResult = cos.getObject(getObjectRequest);                

```

## Generating Signature

**Signature Types:**

| Type   | Description            |
| ---- | ------------- |
| Multiple-time | It can be used multiple times before the expiration time   |
| One-time | It is bound to the source URL and only be used once |

**Acquiring Signature:**

This is the SIGN used in SDK. It is recommended to use the server-side SDK and send the request to business server from mobile device. For more information on how to generate and use SIGN, refer to [Access Permission](https:///doc/api/435/6054).


## Directory-related Operations 

### Creating a Directory

#### Method Prototype

You can create a directory under specified bucket by calling this API. The steps are as follows:

1. Instantiate CreateDirRequest object by calling CreateDirRequest();
2. Call createDir method of COSClient, input CreateDirRequest, and get the returned CreateDirResult object;

#### Parameter Description

| Parameter Name     | Type               | Required | Description            |
| :------- | :--------------- | :--- | :-------------- |
| appid    | String           | Yes    | APP ID of Tencent Cloud       |
| bucket   | String           | Yes    | Name of bucket to which the directory belongs   |
| cosPath  | String           | Yes    | The path under which the directory will be created        |
| biz_attr | String           | No    | Attribute bound to the directory. This is maintained by the user's personnel. |
| sign     | String           | Yes    | Signature information. Multiple-time signature is used here   |
| listener | ICmdTaskListener | No    | Result callback            |

#### Returned Result

Request result is returned through member variables of CreateDirResult object.

| Member Variable Name | Type            | Description   |
| :----- | :------------ | :----- |
| code   | String        | Result code    |
| msg    | String        | Detailed result information  |
| ctime  | long (Unix timestamp) | Creation time   |

#### Example

```
CreateDirRequest createDirRequest = new CreateDirRequest();
createDirRequest.setBucket(bucket);
createDirRequest.setCosPath(cosPath);
createDirRequest.setBiz_attr(biz_attr);
createDirRequest.setSign(sign);
createDirRequest.setListener(new ICmdTaskListener() {
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
        final CreateDirResult createDirResult = (CreateDirResult) cosResult;
        Log.w("TEST","Directory creation succeed: ret=" + createDirResult.code + "; msg=" + createDirResult.msg 
            +"ctime = " + createDirResult.ctime));
    }

    @Override
    public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
         Log.w("TEST","Directory creation failed: ret=" + cosResult.code + "; msg=" + cosResult.msg);
    }
});

CreateDirResult result = cos.createDir(createDirRequest);
```

### Querying List of Directories

#### Method Prototype

You can query the list of specified directories by calling this API. The steps are as follows:

1. Instantiate ListDirRequest object by calling ListDirRequest();
2. Call listDir method of COSClient, input ListDirRequest, and get the returned ListDirResult object;

#### Parameter Description

| Parameter Name     | Type               | Required | Description                                     |
| :------- | :--------------- | :--- | :--------------------------------------- |
| appid    | String           | Yes    | APP ID of Tencent Cloud                                |
| bucket   | String           | Yes    | Name of bucket to which the directory belongs                            |
| cosPath  | String           | Yes    | Remote relative path                                   |
| num      | int              | No    | Number of returned results. Both default and maximum are 1000                  |
| content  | String           | No    | Transparently transmitted field. This field must be left empty for the first pull. To pull next page, please transmit the context in the returned values of the previous page to the parameters in a transparent way |
| prefix   | String           | No    | Prefix query string                                 |
| sign     | String           | Yes    | Signature information. Multiple-time signature is used here                            |
| listener | ICmdTaskListener | No    | Result callback                                     |

#### Returned Result

The request results are returned through member variables of ListDirResult object.


| Member Variable Name   | Type           | Description                           |
| :------- | :----------- | :----------------------------- |
| code     | String       | Result code                            |
| msg      | String       | Detailed result  information                         |
| content  | String       | Transparently transmitted field                           |
| listover | boolean      | Identify whether the list is complete; true: The list is complete; false: The list is to be continued |
| infos    | List<String> | List attributes of files or folders in the list of directories               |

#### Example

```
ListDirRequest listDirRequest = new ListDirRequest();
listDirRequest.setBucket(bucket);
listDirRequest.setCosPath(cosPath);
listDirRequest.setNum(100);
listDirRequest.setContent("");
listDirRequest.setSign(sign);
listDirRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
    		//Query succeeded
        ListDirResult listObjectResult = (ListDirResult) cosResult;
        if(listObjectResult.infos != null && listObjectResult.infos.size() > 0){
        for(int i = 0; i < length; i++){
            String str = listObjectResult.infos.get(i);
            try {
                JSONObject jsonObject = new JSONObject(str);
                if(jsonObject.has("sha")){
                 //The search results are files
                }else{
                //The search results are folders
                }
            } catch (JSONException e) {
               e.printStackTrace();
           } 
     }
     }

   	 if (!listover) {
			// Next page exists. Save the status information of current page.
			String content = result.content;
		}
    }

    @Override
    public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
        Log.w("TEST",Directory query failed:ret=" + cosResult.code  + "; msg =" + cosResult.msg);
   }
});


// Prefix query is supported
listDirRequest.setPrefix(prefix);
ListDirResult result=cos.listDir(listDirRequest);
```

### Updating Directory

#### Method Prototype

You can update the information of specified directory by calling this API. The steps are as follows:

1. Instantiate UpdateObjectRequest object by calling UpdateObjectRequest();
2. Call updateObject method of COSClient, input UpdateObjectRequest, and get the returned UpdateObjectResult object;

#### Parameter Description

| Parameter Name     | Type               | Required | Description          |
| :------- | :--------------- | :--- | :------------ |
| appid    | String           | Yes    | APP ID of Tencent Cloud     |
| bucket   | String           | Yes    | Name of bucket to which the directory belongs |
| cosPath  | String           | Yes    | Remote relative path        |
| sign     | String           | Yes    | Signature information. One-time signature is used here |
| bizAttr  | String           | No    | Attributes bound to the directory     |
| listener | ICmdTaskListener | No    | Result callback          |

#### Returned Result

Request result is returned through member variables of UpdateObjectResult object.


| Member Variable Name | Type     | Description   |
| :----- | :----- | :----- |
| code   | String | Result code    |
| msg    | String | Detailed result information |

#### Example

```
UpdateObjectRequest updateObjectRequest = new UpdateObjectRequest();
updateObjectRequest.setBucket(bucket);
updateObjectRequest.setCosPath(cosPath);
updateObjectRequest.setBizAttr(biz_attr);
updateObjectRequest.setSign(onceSign);
updateObjectRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
        //Update successful
        Log.w("TEST", cosResult.code+" : "+cosResult.msg);
    }

     @Override
     public void onFailed(COSRequest COSRequest, COSResult cosResult) {
         //Update failed
         Log.w("TEST", cosResult.code+" : "+cosResult.msg);
     }
});

UpdateObjectResult result = cos.updateObject(updateObjectRequest);
```

### Querying a Directory

#### Method Prototype

You can query the information of specified directory by calling this API. The steps are as follows:

1. Instantiate GetObjectMetadataRequest object by calling GetObjectMetadataRequest() method;
2. Call getObjectMetadata method of COSClient, input GetObjectMetadataRequest, and get the returned GetObjectMetadataResult object;

#### Parameter Description
| Parameter Name     | Type               | Required | Description          |
| :------- | :--------------- | :--- | :------------ |
| appid    | String           | Yes    | APP ID of Tencent Cloud     |
| bucket   | String           | Yes    | Name of bucket to which the directory belongs |
| cosPath  | String           | Yes    | Remote relative path        |
| sign     | String           | Yes    | Signature information. Multiple-time signature is used here |
| listener | ICmdTaskListener | No    | Result callback          |

#### Returned Result

Request result is returned through member variables of GetObjectMetadataResult object.


| Member Variable Name   | Type            | Description      |
| :------- | :------------ | :-------- |
| code     | String        | Result code       |
| msg      | String        | Detailed result information    |
| biz_attr | String        | Attributes bound to the directory  |
| ctime    | long (Unix timestamp) | Creation time      |
| mtime    | long (Unix timestamp) | Last modification time |

#### Example

```
GetObjectMetadataRequest getObjectMetadataRequest = new GetObjectMetadataRequest();
getObjectMetadataRequest.setBucket(bucket);
getObjectMetadataRequest.setCosPath(cosPath);
getObjectMetadataRequest.setSign(sign);
getObjectMetadataRequest.setListener(new ICmdTaskListener() {
     @Override
     public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
         GetObjectMetadataResult result = (GetObjectMetadataResult) cosResult;
         StringBuilder stringBuilder = new StringBuilder();
         stringBuilder.append("code=" + result.code + "; msg=" +result.msg + "\n");
         stringBuilder.append("ctime =" +result.ctime + "; mtime=" +result.mtime + "\n" );
         stringBuilder.append("biz_attr=" + result.biz_attr == null ? "" : result.biz_attr );
         Log.w("TEST",stringBuilder.toString());
      }

      @Override
      public void onFailed(COSRequest cosRequest, final COSResult cosResult) {
          Log.w("TEST", cosResult.code+" : "+cosResult.msg);
       }

});

GetObjectMetadataRequest result = cos.getObjectMetadata(getObjectMetadataRequest);  
```
### Deleting a Directory

#### Method Prototype

You can delete specified directory by calling this API. The steps are as follows. Note: only empty directories can be deleted:

1. Instantiate RemoveEmptyDirRequest object by calling RemoveEmptyDirRequest() method;
2. Call removeEmptyDir method of COSClient, input RemoveEmptyDirRequest, and get the returned RemoveEmptyDirResult object;

#### Parameter Description

| Parameter Name     | Type               | Required | Description          |
| :------- | :--------------- | :--- | :------------ |
| appid    | String           | Yes    | APP ID of Tencent Cloud     |
| bucket   | String           | Yes    | Name of bucket to which the directory belongs |
| cosPath  | String           | Yes    | Remote relative path        |
| sign     | String           | Yes    | Signature information. One-time signature is used here |
| listener | ICmdTaskListener | No    | Result callback          |

#### Returned Result

Request result is returned through member variables of RemoveEmptyDirResult object.


| Member Variable Name | Type     | Description   |
| :----- | :----- | :----- |
| code   | String | Result code    |
| msg    | String | Detailed result information |

#### Example

```
RemoveEmptyDirRequest removeEmptyDirRequest = new RemoveEmptyDirRequest();
removeEmptyDirRequest.setBucket(bucket);
removeEmptyDirRequest.setCosPath(cosPath);
removeEmptyDirRequest.setSign(onceSign);
removeEmptyDirRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
        final DeleteObjectResult removeEmptyDirResult = (DeleteObjectResult) cosResult;
        Log.w("TEST","removeDir Result: ret=" + removeEmptyDirResult.code + "; msg=" + removeEmptyDirResult.msg );
    }

    @Override
    public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
        Log.w("TEST","Failed to delete directory:ret=" + cosResult.code  + "; msg =" + cosResult.msg);
    }
});

RemoveEmptyDirResult result = cos.removeEmptyDir(removeEmptyDirRequest); 

```

## File-related Operations 

### Uploading a File

#### Method Prototype

You can upload specified file by calling this API. The steps are as follows:

1. Instantiate PutObjectRequest object by calling PutObjectRequest() method;
2. Call putObject method of COSClient, input PutObjectRequest, and get the returned PutObjectResult object;

#### Parameter Description

| Parameter Name       | Type                  | Required | Description                                   |
| :--------- | :------------------ | :--- | :------------------------------------- |
| appid      | String              | Yes    | APP ID of Tencent Cloud                              |
| bucket     | String              | Yes    | Name of bucket to which the directory belongs                          |
| cosPath    | String              | Yes    | Remote relative path                                 |
| srcPath    | String              | Yes    | Local absolute path                                 |
| insertOnly | String              | No    | Whether to overwrite the file with the same name: "0": Allowed; "1": Not Allowed (default). |
| slice_size | int                 | No    | Size of a part in case of multipart upload. Default is 1M                  |
| sign       | String              | Yes    | Signature information. Multiple-time signature is used here                          |
| listener   | IUploadTaskListener | No    | Result callback                                   |

#### Returned Result

Request request is returned through member variables of PutObjectResult object.


| Member Variable Name     | Type     | Description     |
| :--------- | :----- | :------- |
| code       | String | Result code      |
| msg        | String | Detailed result information   |
| access_url | String | URL for file access |
| url        | String | URL for file operation |

#### Example

```
PutObjectRequest putObjectRequest = new PutObjectRequest();
putObjectRequest.setBucket(bucket);
putObjectRequest.setCosPath(cosPath);
putObjectRequest.setSrcPath(srcPath);
putObjectRequest.setSign(sign);

 /* Whether to overwrite the file with the same name: "0": Allowed; "1": Not Allowed;
putObjectRequest.setInsertOnly("1");

//Whether to enable multipart upload
putObjectRequest.setSliceFlag(true);//Whether to perform multipart upload: true: Multipart Upload; false: Simple File Upload
putObjectRequest.setSlice_size(1024*1024);//Size of a part in multipart upload
 */

putObjectRequest.setListener(new  IUploadTaskListener(){
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {

         PutObjectResult result = (PutObjectResult) cosResult;
         StringBuilder stringBuilder = new StringBuilder();
         stringBuilder.append(" Upload result: ret=" + result.code + "; msg =" +result.msg + "\n");
         stringBuilder.append(" access_url= " + result.access_url + "\n");
         stringBuilder.append(" resource_path= " + result.resource_path + "\n");
         stringBuilder.append(" url= " result.url);
         Log.w("TEST",stringBuilder.toString();
     }

    @Override
    public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
         Log.w("TEST","An error occurred during the upload: ret =" +cosResult.code + "; msg =" + cosResult.msg);
    }

    @Override
    public void onProgress(COSRequest cosRequest, final long currentSize, final long totalSize) {
         float progress = (float)currentSize/totalSize;
         progress = progress *100;
         Log.w("TEST","Progress: " + (int)progress + "%");
    }
});

PutObjectResult result = cos.putObject(putObjectRequest);
```
### Updating a File

#### Method Prototype

You can update the information of specified file by calling this API. The steps are as follows:

1. Instantiate UpdateObjectRequest object by calling UpdateObjectRequest() method;
2. Call updateObject method of COSClient, input UpdateObjectRequest, and get the returned UpdateObjectResult object;

#### Parameter Description

| Parameter Name           | Type                 | Required | Description                                     |
| :------------- | :----------------- | :--- | :--------------------------------------- |
| appid          | String             | Yes    | APP ID of Tencent Cloud                                |
| bucket         | String             | Yes    | Name of bucket to which the directory belongs                            |
| cosPath        | String             | Yes    | Remote relative path                                   |
| sign           | String             | Yes    | Signature information. One-time signature is used here                            |
| bizAttr        | String             | No    | Attributes bound to the directory                                |
| authority      | String             | No    | File operation permissions. Same as bucket permissions (COSAuthority.EINVALID); private read/write permissions (COSAuthority.EWRPRIVATE); public read permission and private write permission (COSAuthority.EWPRIVATERPUBLIC) |
| custom_headers | Map<String,String> | No    | Custom header of file: For example, Cache-Control, Content-Disposition, Content-Language, x-cos-meta-.  |
| listener       | ICmdTaskListener   | No    | Result callback                                     |

#### Returned Result

Request result is returned through member variables of UpdateObjectResult object.


| Member Variable Name | Type     | Description   |
| :----- | :----- | :----- |
| code   | String | Result code    |
| msg    | String | Detailed result information |

#### Example

```

UpdateObjectRequest updateObjectRequest = new UpdateObjectRequest();
updateObjectRequest.setBucket(bucket);
updateObjectRequest.setCosPath(cosPath);
updateObjectRequest.setBizAttr(biz_attr);
updateObjectRequest.setAuthority(authority);
updateObjectRequest.setCustomHeader(customer);
updateObjectRequest.setSign(onceSign);
updateObjectRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
        Log.w("TEST", cosResult.code+" : "+cosResult.msg);
    }

    @Override
    public void onFailed(COSRequest COSRequest, COSResult cosResult) {
                        Log.w("TEST", cosResult.code+" : "+cosResult.msg);
    }
});

UpdateObjectResult result= cos.updateObject(updateObjectRequest);
```

### Querying a File

#### Method Prototype

You can query the information of specified file by calling this API. The steps are as follows:

1. Instantiate GetObjectMetadataRequest object by calling GetObjectMetadataRequest() method;
2. Call getObjectMetadata method of COSClient, input GetObjectMetadataRequest, and get the returned GetObjectMetadataResult object;

#### Parameter Description

| Parameter Name     | Type               | Required | Description          |
| :------- | :--------------- | :--- | :------------ |
| appid    | String           | Yes    | APP ID of Tencent Cloud     |
| bucket   | String           | Yes    | Name of bucket to which the directory belongs |
| cosPath  | String           | Yes    | Remote relative path        |
| sign     | String           | Yes    | Signature information. Multiple-time signature is used here |
| listener | ICmdTaskListener | No    | Result callback          |

#### Returned Result

Request result is returned through member variables of GetObjectMetadataResult object.


| Member Variable Name          | Type                 | Description      |
| :-------------- | :----------------- | :-------- |
| code            | String             | Result code       |
| msg             | String             | Detailed result information   |
| biz_attr        | String             | Attributes bound to the directory |
| ctime           | long (Unix timestamp)      | Creation time      |
| mtime           | long (Unix timestamp)      | Last modification time  |
| sha             | String             | sha value of file   |
| customs_headers | Map<String,String> | Attribute of file header   |
| filelen         | int                | Length of file   |

#### Example

```
GetObjectMetadataRequest getObjectMetadataRequest = new GetObjectMetadataRequest();
getObjectMetadataRequest.setBucket(bucket);
getObjectMetadataRequest.setCosPath(cosPath);
getObjectMetadataRequest.setSign(sign);
getObjectMetadataRequest.setListener(new ICmdTaskListener() {
     @Override
     public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
         GetObjectMetadataResult result = (GetObjectMetadataResult) cosResult;
         StringBuilder stringBuilder = new StringBuilder();
         stringBuilder.append("code=" + result.code + "; msg=" +result.msg + "\n");
         stringBuilder.append("ctime =" +result.ctime + "; mtime=" +result.mtime + "\n" );
         stringBuilder.append("biz_attr=" + result.biz_attr == null ? "" : result.biz_attr );
         stringBuilder.append("sha=" + result.sha);
         Log.w("TEST",stringBuilder.toString());
      }

      @Override
      public void onFailed(COSRequest cosRequest, final COSResult cosResult) {
          Log.w("TEST", cosResult.code+" : "+cosResult.msg);
       }

});

GetObjectMetadataRequest result=cos.getObjectMetadata(getObjectMetadataRequest);  
```

### Deleting a File

#### Method Prototype

You can delete specified file by calling this API. The steps are as follows:

1. Instantiate DeleteObjectRequest object by calling DeleteObjectRequest() method;
2. Call deleteObject method of COSClient, input DeleteObjectRequest, and get the returned DeleteObjectResult object;

#### Parameter Description

| Parameter Name     | Type               | Required | Description          |
| :------- | :--------------- | :--- | :------------ |
| appid    | String           | Yes    | APP ID of Tencent Cloud     |
| bucket   | String           | Yes    | Name of bucket to which the directory belongs |
| cosPath  | String           | Yes    | Remote relative path        |
| sign     | String           | Yes    | Signature information. One-time signature is used here   |
| listener | ICmdTaskListener | No    | Result callback          |

#### Returned Result

Request result is returned through member variables of DeleteObjectResult object.


| Member Variable Name | Type     | Description   |
| :----- | :----- | :----- |
| code   | String | Result code    |
| msg    | String | Detailed result information |

#### Example

```
DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest();
deleteObjectRequest.setBucket(bucket);
deleteObjectRequest.setCosPath(cosPath);
deleteObjectRequest.setSign(onceSign);
deleteObjectRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
         Log.w("TEST", cosResult.code+" : "+cosResult.msg);
    }

    @Override
    public void onFailed(COSRequest COSRequest, COSResult cosResult) {
        Log.w("TEST", cosResult.code+" : "+cosResult.msg);
   }
});

DeleteObjectResult result = cos.deleteObject(deleteObjectRequest); 
```

### Downloading a File

#### Method Prototype

You can download specified file by calling this API. The steps are as follows:

1. Instantiate GetObjectRequest object by calling GetObjectRequest(String downloadURl, String savePath) method;
2. Call getObject method of COSClient, input GetObjectRequest, and get the returned GetObjectResult object;

#### Parameter Description

| Parameter Name        | Type                    | Required | Description                 |
| :---------- | :-------------------- | :--- | :------------------- |
| downloadUrl | String                | Yes    | URL for file download             |
| localPath   | String                | Yes    | Absolute path under which the file is saved locally          |
| sign        | String                | No    | Signature information.It is required if hotlink protection is enabled, otherwise it is not required. |
| listener    | IDownloadTaskListener | No    | Result callback                 |

#### Returned Result

Request result is returned through member variables of GetObjectResult object.


| Member Variable Name | Type     | Description   |
| :----- | :----- | :----- |
| code   | String | Result code    |
| msg    | String | Detailed result information |

#### Example

```
GetObjectRequest getObjectRequest = new GetObjectRequest(downloadURl,savePath);
getObjectRequest.setSign(null);
getObjectRequest.setListener(new IDownloadTaskListener() {
    @Override
    public void onProgress(COSRequest cosRequest, final long currentSize, final long totalSize) {
        float progress =  currentSize / (float)totalSize;
        progress = progress * 100;
        progressText.setText("progress =" + (int) (progress) + "%");
        Log.w("TEST", "progress =" + (int) (progress) + "%");
                            
    }

    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
         Log.w("TEST","code =" + cosResult.code + "; msg =" + cosResult.msg);
    }

    @Override
    public void onFailed(COSRequest COSRequest, COSResult cosResult) {
                        Log.w("TEST","code =" + cosResult.code + "; msg =" + cosResult.msg);
    }
});


GetObjectResul result = cos.getObject(getObjectRequest);
```

