## 1. API Description

### 1.1 Send a request to the API CGI using HTTP protocol

**Address:** `http://fcgi.video.qcloud.com/common_access`.
**Purpose:** To mix several input streams into one stream on the cloud for output.

### 1.2 Pass the authentication parameter using URI

```
http://fcgi.video.qcloud.com/common_access?appid=1252500000&interface=Mix_StreamV2&t=t&sign=sign

```
**Parameter description:**

| Parameter | Description | Type | Note | Required
|---------|---------|---------|---------|---------|
| appid | Customer ID | int |The LVB APPID, which is used to identify different customers | Y |
| interface |API name | string | The stream mixing API name is always Mix_StreamV2 |Y |
| t |Validity period |int |UNIX timestamp, which is the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT). This field indicates the expiration time of requests. You need to add 60 seconds of offset to the current time (in sec) |Y|
| sign |Security signature |string|sign = MD5(key + t). This means computing the MD5 value by concatenating the encryption key and t. The encryption key is the API authentication key set on the Tencent Cloud LVB console. |y |

Example on how to compute the security signature "sign":

```
key = "40328529ca4381a80c6ecf2e6aa57438"                    //API authentication key 
t = 1490858347                                              //t (expiration time)
key + t = "40328529ca4381a80c6ecf2e6aa574381490858347"      //Concatenate the strings of the key and t
sign = MD5(key + t) = "7f29ed83c61b77de1b0d66936fd4fd44"   //Compute the MD5 value for concatenated string
```

HTTP request description:

```
POST /common_access?interface=Mix_StreamV2&sign=xxxxxxxxx&appid=125250000 HTTP/1.0 Content-Length: 741
```

### 1.3 Send the stream mixing body using POST method

**Example:**
```
    {
        "timestamp":int(time.time()),           # UNIX timestamp, which is the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT)
        "eventId":int(time.time()),             # You can use a random number to identify a network request
        "interface":
        {
            "interfaceName":"Mix_StreamV2",        # Fixed value: "Mix_StreamV2"
            "para":
            {
                "app_id": appid,                # Enter the LVB APPID
                "interface": "mix_streamv2.start_mix_stream_advanced",  # Fixed value"mix_streamv2.start_mix_stream_advanced"
                "mix_stream_session_id" : "5000_enson",                # Enter the stream ID of the primary VJ
                "output_stream_id": "5000_enson11",                      # Enter the stream ID of the primary VJ
                "output_stream_type": 0,                                          # Enter the output stream type
                "input_stream_list":
                [
                    # Primary VJ: Background image
                    {
                        "input_stream_id":"5000_enson11",    # Stream ID
                        "layout_params":
                        {   
                            "image_layer": 1                # Image layer ID: Primary VJ: 1; Secondary VJ: 2, 3, 4, 5, 6 in sequence
                        }   
                    },
                    # Secondary VJ 1
                    {
                        "input_stream_id":"5000_enson22",    # Stream ID
                        "layout_params":
                        {   
                            "image_layer": 2,               # Image layer ID
                            "image_width": 160,             # Secondary VJ image width
                            "image_height": 240,            # Secondary VJ image height
                            "location_x": 380,              # x offset: Lateral offset from the top left corner of the primary VJ's background image
                            "location_y": 630               # y offset: Longitudinal offset from the top left corner of the primary VJ's background image
                        }   
                     },
                    # Secondary VJ 2
                     {
                         "input_stream_id":"5000_enson33",
                         "layout_params":
                         {
                             "image_layer": 3,
                             "image_width": 160,
                             "image_height": 240,
                             "location_x": 380,
                             "location_y": 390
                         }
                     },
                    # Secondary VJ 3
                     {
                         "input_stream_id":"5000_enson44",
                         "layout_params":
                         {
                             "image_layer": 4,
                             "image_width": 160,
                             "image_height": 240,
                             "location_x": 380,
                             "location_y": 150
                         }
                     }
                ]
            }
        }
    }
```

**Parameter description**
>Required parameter description

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
|timestamp|	Current time	|int|	Enter the current time (in sec) |	Y|
|eventId	|Identifies a network request |	int	|Enter a random number |	Y|
|interfaceName	|API ID |string|	Mix_StreamV2, a fixed value |	Y|
|app_id|	LVB APPID |	int	|LVB APPID |	Y|
|interface|	Stream mixing API name	|string	|Enter mix_streamv2.start_mix_stream_advanced, which is fixed |	Y|
|mix_stream_session_id	|Stream mixing operation ID |string|	Enter a string with a length limited to 80 bytes, containing letters, numbers and underscores only |	Y|
|output_stream_id|	Output stream ID |	string	|Specified output stream ID. <br/>It must be a string with a length limited to 80 bytes containing letters, numbers and underscores only.	<br/>If this parameter is one of the input streams, output_stream_type =0; if this parameter is not one of the input streams, output_stream_type =1 |Y|
|input_stream_id	|Input source ID	|string	|Specified input source ID |	Y|
|image_layer	|Image layer ID	|int|	1-6 is supported for video input sources, and 1-8 for audio input sources |	Y|

>Optional parameter description

| Parameter Name | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
|output_stream_type	|Output stream type	|int	|Enter 0 if the output stream is a stream in the list of input streams; <br/>enter 1 if the output stream is not in the list of input streams. <br/>It defaults to 0 if left empty. <br/>Note: Please consult with customer service if you select 1 for this parameter. |	N|
|mix_stream_template_id| Input template ID |	int|	Available values for two input sources are: 10, 20, 30, 40; <br/>three input sources: 310, 390, 391; <br/>four input sources: 410; <br/>five input sources: 510, 590; and <br/>six input sources: 610. <br/>It defaults to 0 if left empty. |	N|
|input_type|	Input source type |	int	|Available values: <br/>0 indicates the input source is an audio or video; <br/>3 indicates canvas; <br/>4 indicates an audio; and <br/>5 indicates a video. |	N|
|image_width	|Input image width	|double|	The recommended pixel is between 0-3000, and percentage between 0.01-0.99. |	N|
|image_height	|Input image height	|double|	The recommended pixel is between 0-3000, and percentage between 0.01-0.99. |	N|
|location_x	|x offset	|double	|Lateral offset from the top left corner of the primary VJ's background image. The recommended pixel is between 0-3000, and percentage between 0.01-0.99.	|N|
|location_y|	y offset|	double|	Longitudinal offset from the top left corner of the primary VJ's background image. The recommended pixel is between 0-3000, and percentage between 0.01-0.99.	|N|
|color|	Color	|string	|The commonly used colors of canvas are: <br/>Black: 0x000000;<br/>White: 0xFFFFFF;<br/>Blue: 0x99CCFF. |	N|
|crop_width|Cropped source image width	|int|	The recommended pixel is between 0-3000. |	N|
|crop_height	|Cropped source image height	|int	|	The recommended pixel is between 0-3000. |	N|
|crop_x	|Lateral offset from the top left corner of the cropped source image. |	int  |	The recommended pixel is between 0-3000. 	|N|
|crop_y	|Longitudinal offset from the top left corner of the cropped source image. |	int|	The recommended pixel is between 0-3000. |N|


**Common colors:**
Red: 0xcc0033
Yellow: 0xcc9900
Green: 0xcccc33
Blue: 0x99CCFF
Black: 0x000000
White: 0xFFFFFF
Gray: 0x999999

### 1.4 Message returned by API

```
{"code":0, "message":"Success!", "timestamp":1490079362}
```

**Parameter description**

| Parameter Name | Description | Type | Note |
|---------|---------|---------|---------|
| code  |Returned error code |int|0: Successful. Other values: Failed |
|message |Error message |string|  Returned error message |
|timestamp|Timestamp | Long int | Returned time |

**Common error codes:**

| Error Code | Description |
|---------|---------|
|-505 | The current query for input stream failed |
|-21 |The parameter for the secondary screen position entered is invalid. The secondary screen falls out of the boundary of the primary screen |
|-30xxx| The sessionid is used to operate on other output streams before the mixing of input streams under the sessionid is cancelled. |
| Other | Other errors. Please contact customer service for technical support. |

### 1.5 Cancellation of stream mixing

```
{
        "timestamp":int(time.time()),           # UNIX timestamp, which is the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT)
        "eventId":int(time.time()),             # Stream mixing event ID. Use the timestamp at the backend
        "interface":
        {
            "interfaceName":"Mix_StreamV2",        # Fixed value: "Mix_StreamV2"
            "para":
            {
                "app_id": appid,                # Enter the LVB APPID
                "interface": "mix_streamv2.start_mix_stream_advanced",  # Fixed value"mix_streamv2.start_mix_stream_advanced"
                "mix_stream_session_id" : "5000_enson",                # Enter the stream ID of the primary VJ
                "output_stream_id": "5000_enson11",                      # Enter the stream ID of the primary VJ
                "input_stream_list":
                [
                    # Primary VJ: Background image
                    {
                        "input_stream_id":"5000_enson11",    # Stream ID
                        "layout_params":
                        {   
                            "image_layer": 1                # Image layer ID: Primary VJ: 1; Secondary VJ: 2, 3, 4 in sequence
                        }   
                    }
                ]
             }
        }
    }  
```

>**Note:**
>To cancel a stream mixing task, you can operate on the current input stream using the current sessionid. Operations on other output streams with this sessionid can be performed after half a minute.

## 2. Scenarios and Notes on Special Operations

### 2.1 Supported features

**Features**

| Feature Description	| Using Condition	| demo File Name |
|---------|---------|---------|
| Mixing of 2-6 audio-video streams	| The input sources are audios and videos |	test_video_and_audio.py|
| Mixing of 2-6 audio-video streams and canvas	| The input sources are audios, videos and canvas |test_stream_and_canvas.py|
| Mixing of 2-6 audio-video streams and video-only streams	| The input sources are audio-video streams and video-only streams |	test_stream_and_video.py|
| Mixing of 2-6 audio-video streams and audio-only streams	| The input sources are audio-video streams and audio-only streams |	test_stream_and_audio.py|
| Cropping on the cloud |	The input sources are audio-video streams or video-only streams |	test_stream_crop.py|
| Mixing of 2-8 audio-only streams | The input sources are audios only |	test_audio_only.py|


### 2.2 Common templates

Common templates include 10, 20, 30, 40, 310, 410, 510, and 610. When using the above templates, you don't need to enter position and length and width parameters for input streams, which are scaled in proportion to the original images. Only template ID needs to be passed.


Template 10 preview:
![](https://mc.qcloudimg.com/static/img/1165deb7f41c182acce7175983fabdb7/t10.png)
<br  />

Template 20 preview:
![](https://mc.qcloudimg.com/static/img/643d7cdb2e5359d226b6ae74bb2c46f7/t20.png)
<br  />

Template 30 preview:
![](https://mc.qcloudimg.com/static/img/0e3e6e5063db197331d8bc33110cbd9e/t30.png)
<br  />

Template 40 preview:
![](https://mc.qcloudimg.com/static/img/b706bf7f2424f953893ae7884309a693/t40.png)
<br  />

Template 310 preview:
![](https://mc.qcloudimg.com/static/img/6c09ec743e7151947ff0cc0e14d53845/t310.png)
<br  />

Template 410 preview:
![](https://mc.qcloudimg.com/static/img/c7e1ea8da4076b40f1572ac39df0e355/tt410.png)
<br  />

Template 510 preview:
![](https://mc.qcloudimg.com/static/img/60882af92ec703a08f463a276cbbef53/t510.png)
<br  />

Template 610 preview:
![](https://mc.qcloudimg.com/static/img/20dcad307192885fca4fd604b1fafad0/t610.png)
<br  />

### 2.3 Notes on special templates
To meet the needs of some users for split screen comparison, we provide three special templates: 390, 391 and 590.
Template 390 preview:
![](https://mc.qcloudimg.com/static/img/e33d616ef0eeea4695b32ae70b0e3e6b/390.png)
Template 391 preview:
![](https://mc.qcloudimg.com/static/img/ccb23cfad471444edf75ba0b38c1a88f/391.png)

Template 590 preview:
![](https://mc.qcloudimg.com/static/img/bacb9a8107ef3f28cd2d8818c3970261/590.png)
>**Note:**
>When you use these templates, the input source with the image layer ID being 1 must be canvas, and its color can be customized.

### 2.4 How to enter custom position parameters

**Diagram:**
![](https://main.qcloudimg.com/raw/fe5e7b85563a891e371cfd81e4c766cd.png)
As shown in the diagram above, the position parameters location_x and location_y are the absolute pixel distance from the top left corner of the secondary screen to that of the background image.

### 2.5 How to enter cropping position parameters

**Diagram:**
![](https://main.qcloudimg.com/raw/ed98b1d8f496cbc11e8564491a3eb887.png)
As shown in the diagram above:  
a. Both the width and height and the position parameters you entered are absolute pixel values. Streams of different pixels are handled differently. 
B. The position parameters crop_x and crop_y represent the absolute pixel distance from the top left corner of the original stream.

### 2.6 Demo downloading

**Download the stream mixing demo:** Click [here](https://mc.qcloudimg.com/static/archive/979c7ef4396772089532cc9d5a25619e/demo.zip) to download the demo.

