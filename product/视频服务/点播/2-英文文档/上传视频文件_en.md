## API Name

### API Used to Upload Small Files (< 20 MB)
1. [Simple File Upload](https://cloud.tencent.com/document/api/436/6066)

### API Used to Upload Large Files (> 20 MB)
1. [Initiate Multipart Upload](https://cloud.tencent.com/document/api/436/6067)
2. [Upload Parts One by One](https://cloud.tencent.com/document/api/436/6068)
3. [Finish Multipart Upload](https://cloud.tencent.com/document/api/436/6074)

## Feature Description
1. Upload videos and image cover files.
2. For which step of the server upload the API is in, please see [Server Upload Overview](https://cloud.tencent.com/document/product/266/9759#.E4.B8.8A.E4.BC.A0.E6.B5.81.E7.A8.8B).

## SDK
It is recommended to use [JSON-based API encapsulation SDK](https://cloud.tencent.com/document/product/436/6474) to call the API.

## Usage

To learn how to use the above APIs, open the above links to see their documentations. The syntax for each API is:
```
POST /files/v2/<appid>/<bucket_name>[/dir_name]/<file_name>  HTTP/1.1
Host: <Region>.file.myqcloud.com
Content-Type: multipart/form-data
Authorization: <multi_effect_signature>
```

The variable values in the syntax are the [results of VOD-initiated uploads](https://cloud.tencent.com/document/product/266/9756#.E6.8E.A5.E5.8F.A3.E5.BA.94.E7.AD.94):
```<bucket_name>```is **storageBucket**; ```<Region>``` is **storageRegion**; ```/<bucket_name>[/dir_name]/<file_name>``` is **video.storagePath** (for the cover image file of **cover.storagePath**).
Values for other variables:
```<appid>```is 10022853; ```<multi_effect_signature>``` generates signatures according to API requirements.
