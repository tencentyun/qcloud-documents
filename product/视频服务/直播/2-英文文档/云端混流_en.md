## 1. API Description

### 1.1. Send a request for the API CGI using HTTP protocol

<br  />

    http://fcgi.video.qcloud.com/common_access

### 1.2. Pass the authentication parameter using URI

<br  />

    http://fcgi.video.qcloud.com/common_access?appid=1252500000&interface=Mix_StreamV2&t=t&sign=sign

**Parameter Description:**

| Parameter | Description | Type | Note | Required
|---------|---------|---------|---------|---------|
| appid | Customer ID | int | Enter LVB APPID used for differentiating the identity of different customers | Y |
| interface | Interface name | string | Stream mixing API name is always entered with: Mix_Stream | Y |
| t | Validity period | int | UNIX time stamp, that is, the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT). This field indicates the validity period of request. You need to add 60 seconds of offset to the current time (in sec) | Y |
| sign | Security signature | string | sign = MD5(key + t), that is, to calculate the MD5 value by concatenating the strings of the encryption key and t. Here, the key is the API authentication key you set on the Tencent Cloud LVB console | y |

<br  />

Example on how to calculate the security signature "sign"

<br  />

    key = "40328529ca4381a80c6ecf2e6aa57438"                    //API authentication key 
    t = 1490858347                                              //t (validity period)
    key + t = "40328529ca4381a80c6ecf2e6aa574381490858347"      //concatenate the strings of the encryption key and t
    sign = MD5 (key + t) = "7f29ed83c61b77de1b0d66936fd4fd44"   //calculate the MD5 value with concatenated strings

<br  />

HTTP request description

    POST /common_access?interface=mix_streamv2.start_mix_stream_advanced&sign=xxxxxxxxx&appid=125250000 HTTP/1.0
    Content-Length:  741
    ...

### 1.3 Send stream mixing body using POST method

<br  />

Example

<br  />

    {
        "timestamp":int(time.time()),           # UNIX time stamp, that is, the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT)
        "eventId":int(time.time()),             # You can use a random number to identify a network request
        "interface":
        {
            "interfaceName":"Mix_StreamV2",        # Fixed value: "Mix_StreamV2"
            "para":
            {
                "app_id": appid,                # Enter LVB APPID
                "interface": "mix_streamv2.start_mix_stream_advanced",  # Fixed value"mix_streamv2.start_mix_stream_advanced"
                "mix_stream_session_id" : "5000_enson",                # Enter steam ID of primary VJ
                "output_stream_id": "5000_enson11",                      # Enter steam ID of primary VJ
                "output_stream_type": 0,                                          # Enter output stream type
                "input_stream_list":
                [
                    # Primary VJ: Background image
                    {
                        "input_stream_id":"5000_enson11",    # Steam ID
                        "layout_params":
                        {   
                            "image_layer": 1                # Image layer ID: Primary VJ: 1; Secondary VJ: 2, 3, 4, 5, 6 in sequence
                        }   
                    },
                    # Secondary VJ 1
                    {
                        "input_stream_id":"5000_enson22",    # Steam ID
                        "layout_params":
                        {   
                            "image_layer": 2,               # Image layer ID
                            "image_width": 160,             # Secondary VJ image width
                            "image_height": 240,            # Secondary VJ image height
                            "location_x": 380,              # x offset: Lateral offset from the top left corner of primary VJ's background image
                            "location_y": 630               # y offset: Vertical offset from the top left corner of primary VJ's background image
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

**Parameter Description**

| Parameter | Description | Type | Note | Required |
|---------|---------|---------|---------|---------|
| timestamp  | Time stamp | int  | You can use the current time (in sec) | Y |
| eventId  | Event ID | int  | You can use a random number, to identify a network request | Y |
| interfaceName  | API ID | string | Stream mixing API name is entered with: Mix_StreamV2 | Y |
| app_id | LVB ID | int | LVB APPID | Y |
| interface | API name | string | This is always entered with mix_streamv2.start_mix_stream_advanced | Y |
| mix_stream_session_id | Stream mixing operation ID | string | Enter a string with a length limited to 80 bytes, containing letters, numbers and underscores only | Y |
| output_stream_id | ID of output stream for stream mixing | string | Specified output stream ID | Y
| output_stream_type | Type of output stream for stream mixing | int | Specified output stream type. Enter 0 if the output stream is a stream in the list of input streams; enter 1 if the output stream is new and not included in the list of input streams. Default is 0 if this is left empty. | N |
| mix_stream_template_id | Stream mixing template | int | Enter tamplate ID. Available values for two input sources are: 10, 20, 30, 40; three input sources: 310, 390, 391; four input sources: 410; five input sources: 510, 590; and six input sources: 610. Default is 0 if this is left empty. | N |
| input_stream_id | ID of input stream for stream mixing | string | Specified input stream ID | Y |
| image_layer | Input stream image layer ID | int  | Image layer ID. Available value range: 1-6. | Y |  
| input_type | Type of input source for stream mixing | int | Input source ID. 0 means that the input source is a stream, and 3 means that the input source is a canvas. | N | 
| image_width  | Width of input source for stream mixing (in pixels) |  int | Width of input image. Available value range: 0-3,000. | N | 
| image_height  | Height of input source for stream mixing (in pixels) | int | Height of input image. Available value range: 0-3,000.  | N |
| location_x | Absolute position of x-coordinate | int| x offset: Lateral offset from the top left corner of primary VJ's background image. |  N | 
| location_y | Absolute position of y-coordinate | int| y offset: Vertical offset from the top left corner of primary VJ's background image.  | N |
| color | Color of canvas |  string| The color is required if the input source is canvas. | N |

**Common colors:**

Red: 0xcc0033

Yellow: 0xcc9900

Green: 0xcccc33

Blue: 0x99CCFF

Black: 0x000000

White: 0xFFFFFF

Gray: 0x999999

<br  />

### 1.4 Message returned by API

<br  />

    {"code":0, "message":"Success!", "timestamp":1490079362}

<br  />

**Parameter Description**

| Parameter Name | Description | Type | Note |
|---------|---------|---------|---------|
| code  | Returned error code | int | 0: Successful; other values: Failed |
| message | Error message | string |  Returned error message |
| timestamp | Time stamp | Long int | Returned time |

**Common error Codes:**

| Error Code | Description | 
|---------|---------|
| -27, -29 | The current query for input stream failed |
| -21 | The parameter of secondary screen position entered currently is invalid. The secondary screen falls out of the boundary of the primary screen |
|-9, -103| The mixing of the input stream under the current sessionid is not cancelled. Meanwhile, this sessionid is used to work with other output streams. |
| Other | Other error codes. To solve these errors, contact Tencent commercial personnel or submit a ticket. Tel: 4009-100-100 | |


### 1.5 Cancellation of stream mixing

<br  />

    {
        "timestamp":int(time.time()),           # UNIX time stamp, that is, the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT)
        "eventId":int(time.time()),             # Stream mixing event ID. Use the time stamp at the backend
        "interface":
        {
            "interfaceName":"Mix_StreamV2",        # Fixed value: "Mix_StreamV2"
            "para":
            {
                "app_id": appid,                # Enter LVB APPID
                "interface": "mix_streamv2.start_mix_stream_advanced",  # Fixed value"mix_streamv2.start_mix_stream_advanced"
                "mix_stream_session_id" : "5000_enson",                # Enter steam ID of primary VJ
                "output_stream_id": "5000_enson11",                      # Enter steam ID of primary VJ
                "input_stream_list":
                [
                    # Primary VJ: Background image
                    {
                        "input_stream_id":"5000_enson11",    # Steam ID
                        "layout_params":
                        {   
                            "image_layer": 1                # Image layer ID: Primary VJ: 1; Secondary VJ: 2, 3, 4 in sequence
                        }   
                    }
                ]
             }
        }
    }  

<br  />

Note: The mixing can be cancelled by working with the current input stream using the current sessionid. You can work with other output streams with this sessionid after a half minute

<br  />

## 2. Scenarios and Notes on Special Operations

### 2.1 Common templates

Common templates include 10, 20, 30, 40, 310, 410, 510, 610. When using the above templates, you don't need to enter the position and length parameters for the input stream, which are scaled proportionally to the original image. Only template ID needs to be passed.


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

### 2.2 Notes on special templates

<br  />

To meet the needs of some users for split screen comparison, we provide three special templates: 390, 391 and 590

<br  />

Template 390 preview:
![](https://mc.qcloudimg.com/static/img/e33d616ef0eeea4695b32ae70b0e3e6b/390.png)


<br  />

Template 391 preview:
![](https://mc.qcloudimg.com/static/img/ccb23cfad471444edf75ba0b38c1a88f/391.png)


<br  />

Template 590 preview:
![](https://mc.qcloudimg.com/static/img/bacb9a8107ef3f28cd2d8818c3970261/590.png)


<br  />

Note: When you use the above templates, the input source with the image layer ID being 1 must be passed into the canvas. The color can be customized

<br  />

2.3 How to enter the custom position parameter

<br  />

Figure:
![](https://mc.qcloudimg.com/static/img/63d5f94f2ab6d271ab23aa5114f7ec54/weizhi.jpg)


<br  />

As shown in the figure above, please note:

<br  />

a. Both height and position parameters you entered are absolute pixel values. For streams with different resolutions need to be processed in a different way.

b. The position parameters location_x and location_y are the absolute pixel distance of the top left corner of secondary screen relative to the top left corner of background image.


