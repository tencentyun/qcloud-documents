## 1. API Description

This API (DescribeVodInfo) is used to acquire video information. Acquire video information list according to certain information of the video, such as ID, duration or status.

Domain: vod.api.qcloud.com

 

## 2. Input Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Required</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileIds.n
<td> No
<td> String
<td> Video ID list. Batch operation is currently not supported
<tr>
<td> from
<td> No
<td> String
<td> Start time. Default is 1970-1-1 00:00:00
<tr>
<td> to
<td> No
<td> String
<td> End time. Default is 2038-1-1 00:00:00
<tr>
<td> classId
<td> No
<td> Int
<td> Video category ID, used for filtering
<tr>
<td> status
<td> No
<td> Int
<td> Video status, used for filtering. -1: Upload incomplete, does not exist; 0: Initialize, not in use; 1: Verification failed, not in use; 2: Normal; 3: Paused; 4: Transcoding; 5: Publishing; 6: Deleting; 7: Transcoding failed; 10: Waiting to be transcoded; 11:  Transcoding partially completed; 100: Deleted
<tr>
<td> orderby
<td> No
<td> Int
<td> Order of the results. By default, the results are sorted in descending order by time. 0: Ascending order by time; 1: Descending order by time
<tr>
<td> pageNo
<td> No
<td> Int
<td> Page number
<tr>
<td> pageSize
<td> No
<td> Int
<td> Page size, value range: 10-100
</tbody></table>

 

## 3. Output Parameters
 
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> code
<td> Int
<td> Error code. 0:  Succeeded,  values:  Failed
<tr>
<td> message
<td> String
<td> Error Message
<tr>
<td> totalCount
<td> Int
<td> Total number of videos
<tr>
<td> fileSet
<td> Array
<td> Video list result set
<tr>
<td> cdnStatus
<td> int
<td> Whether CDN publishing operation has been performed in the API. 0 - Not been published; 1 - Publishing, 2 - Successful, 3 - Publishing failed, 4 - Terminated (not in use), 5 - Deleted
</tbody></table>
</b></th>fileSet video list result set</b></th>
<table class="t"><tbody><tr>
<th><b>Parameter Name</b></th>
<th><b>Type</b></th>
<th><b>Description</b></th>
<tr>
<td> fileId
<td> String
<td> Video ID
<tr>
<td> fileName
<td> String
<td> Video name
<tr>
<td> fileIntro
<td> String
<td> Video description
<tr>
<td> size
<td> String
<td> Video size
<tr>
<td> duration
<td> String
<td> Video duration
<tr>
<td> status
<td> String
<td> Video status. -1: Upload incomplete, does not exist; 0: Initialize, not in use; 1: Verification failed, not in use; 2: Normal; 3: Paused; 4: Transcoding; 5: Publishing; 6: Deleting; 7: Transcoding failed; 10: Waiting to be transcoded; 100: Deleted
<tr>
<td> vid
<td> String
<td> Unique ID of the video
<tr>
<td> createTime
<td> String
<td> Video creation time
<tr>
<td> updateTime
<td> String
<td> Video modification time
<tr>
<td> classId
<td> String
<td> Category ID of the video
<tr>
<td> className
<td> String
<td> Category name of the video
<tr>
<td> imageUrl
<td> String
<td> Video cover image
<tr>
<td> tags
<td> Array
<td> List of tags of the video
<tr>
<td> description
<td> string
<td> Description
</tbody></table>


 

## 4. Example
 
 Query by a video ID 
Input
<pre>
  https://domain/v2/index.php?Action=DescribeVodInfo
  &fileIds.1=1976554120332374777
  &<a href="https://cloud.tencent.com/doc/api/229/6976">Common request parameters</a>
</pre>
Output
```

{
    "code" : 0,
    "message" : "",
    "fileSet" : [
        {
            "fileId" : "1976554120332374777",
            "fileName" : "Blue Jasmine(01h35m56s-01h38m23s)",
            "fileIntro" : "",
            "size" : "7865592",
            "duration" : "147",
            "status" : "2",
            "vid" : "1200_1870483a9a6011e4a137dfa495b17abf",
            "createTime" : "2015-01-12 21:37:11",
            "updateTime" : "2015-01-13 11:23:01",
            "classId" : "0",
            "className" : "Others",
            "imageUrl" : "http://p.qpic.cn/videoyun/0/1200_1870483a9a6011e4a137dfa495b17abf_1/640",
            "tags" : [
                "Others",
            ],
        }
    ]
}

```


