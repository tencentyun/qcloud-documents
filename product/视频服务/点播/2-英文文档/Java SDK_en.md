Tencent Cloud VOD provides Java SDK for the scenario of uploading videos from server. For more information about upload process, please see [Upload Videos from Server](/document/product/266/9759).

## Integration Method

### Introducing Maven Dependency

Add VOD SDK dependency in the pom.xml file of the project.

```
<dependency>
    <groupId>com.qcloud</groupId>
    <artifactId>vod_api</artifactId>
    <version>1.1.1</version>
</dependency>
```

### Importing Jar Package

If Maven is not used for dependency management in the project, you can directly download the source code and import it into the project:

| jar file | Description |
| ------------ | ------------ | 
| vod_api-1.1.0.jar | VOD SDK |
| jackson-annotations-2.8.0.jar,jackson-core-2.8.5.jar,jackson-databind-2.8.5.jar | Open-source JSON library |
| cos_api-5.1.9.jar | Tencent Cloud COS SDK |
| qcloud-java-sdk-2.0.1.jar | Tencent Cloud API SDK |
| commons-codec-1.10.jar,commons-logging-1.2.jar,log4j-1.2.17.jar,slf4j-api-1.7.21.jar,slf4j-log4j12-1.7.21.jar | Open-source log library |
| httpclient-4.5.3.jar,httpcore-4.4.6.jar,httpmime-4.5.2.jar | Open-source http processing library |
| joda-time-2.9.6.jar | Open-source time processing library |

Click the following link to download jar package. You can use the package by importing it into the project.

[VOD Java SDK Jar package](https://github.com/tencentyun/vod-java-sdk/raw/master/packages/vod-sdk-jar.zip)


## Simple Upload of Video
### Initializing an Upload Object
Initialize VodApi instance using the Cloud API key
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
```

### Calling Upload
Pass video address to start uploading
```
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv");
System.out.println(response.getFileId());
```

## Advanced Features
### Uploading Cover
Call the upload overloading method to pass the cover address
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv", "/data/videos/Wildlife.jpg");
System.out.println(response.getFileId());
```

### Specifying Task Flow
Call the upload overloading method to pass the task flow parameter. For more information, please see [Overview of Task Flow](/document/product/266/11700). The task flow will be processed automatically after the video is uploaded.
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv", "/data/videos/Wildlife.jpg", "QCVB_SimpleProcessFile(1, 1)");
System.out.println(response.getFileId());
```

### Specifying Upload Region
Call the upload overloading method to pass a specified region ID, so as to upload a video to the specified region. For more information, please see [Upload Videos from Server](/document/product/266/9759).
```
VodApi vodApi = new VodApi("your secretId", "your secretKey");
Map<String, Object> extraParams = new HashMap<String, Object>();
extraParams.put("storageRegion", "tj");
VodUploadCommitResponse response = vodApi.upload("/data/videos/Wildlife.wmv", "/data/videos/Wildlife.jpg", extraParams);
System.out.println(response.getFileId());
```

## API Description
Initialize upload object `VodApi`

| Parameter Name | Description | Type | Required |
| --------- | ---------------------- | ------- | ---- |
| secretId | Cloud API Key ID | String | Yes |
| secretKey | Cloud API Key | String | Yes |

Upload method `VodApi.upload(String videoPath)`

| Parameter Name | Description | Type | Required |
| --------- | ---------------------- | ------- | ---- |
| videoPath | Video path | String | Yes |

Upload overloading method `VodApi.upload(String videoPath, String coverPath)`

| Parameter Name | Description | Type | Required |
| --------- | ---------------------- | ------- | ---- |
| videoPath | Video path | String | Yes |
| coverPath | Cover path | String | Yes |

Upload overloading method `VodApi.upload(String videoPath, String coverPath, String procedure)`

| Parameter Name | Description | Type | Required |
| --------- | ---------------------- | ------- | ---- |
| videoPath | Video path | String | Yes |
| coverPath | Cover path | String | Yes |
| procedure | Task flow | String | Yes |

Upload overloading method `VodApi.upload((String videoPath, String coverPath, Map<String, Object> extraParams)`

| Parameter Name | Description | Type | Required |
| --------- | ---------------------- | ------- | ---- |
| videoPath | Video path | String | Yes |
| coverPath | Cover path | String | Yes |
| extraParams | Task flow | Map | Yes |

The following parameters are supported for extraParams:

| Parameter Name | Description | Type |
| ------------ | ------------ |  ------------ | 
| sourceContext | User-defined context | String | 
| storageRegion | Specified storage region | String | 
| procedure | Task flow | String | 

Upload result `VodUploadCommitResponse`

| Member Variable Name | Description | Type |
| -------- | --------- | ------ |
| code | Result code | Int |
| message | Error description of failed upload | String |
| fileId | VOD file ID | String |
| video | Video storage information | Object |
| video.url | Address where the video is stored | String |
| video.verify_content | Verification information on video storage | String |
| cover | Cover storage information | Object |
| cover.url | Address where the cover is stored | String |
| cover.verify_content | Verification information on cover storage | String |

## Error Codes
After calling SDK to upload a video, you can check the video upload status with the code in `VodUploadCommitResponse`.

| Status code | Description |
| ----------- | ----------------- |
| 0 | Uploaded successfully |
| 31001 | Invalid session_key in user request |
| 31002 | The VOD signature in user request already exists |
| 31003 | The file to be uploaded does not exist |
| 32001 | Service error |
