Tencent Cloud's stream mixing technology is about superimposing the video streams of one or more (1+3 is supported now) secondary VJs on the video stream of primary VJ (including audio mixing). This solution allows viewers to watch the joint broadcasting without changing the player.


## Procedures
### 1. Tencent Cloud stream-mixing API address

```
http://fcgi.video.qcloud.com/common_access
```

### 2. Pass the authentication parameters using GET method

```
http://fcgi.video.qcloud.com/common_access?cmd=appid&interface=Mix_StreamV2&t=t&sign=sign
```

- **cmd**: Enter LVB APPID, which is used to identify the identities of different customers.
- **interface**: Always enter Mix_StreamV2.
- **t (expiration time)**: UNIX timestamp, which is the number of seconds that have elapsed since January 1, 1970 (Midnight in UTC/GMT). This field indicates the expiration time of request. Please add an offset of 60 seconds to the current time (in sec)
- **sign (security signature)**: sign = MD5(key + t). This means computing the MD5 value by concatenating the encryption key and t. The encryption key is the API authentication key set on the Tencent Cloud LVB [Console](https://console.cloud.tencent.com/live/livecodemanage).

Example on how to compute security signature **sign** 

```
key = "40328529ca4381a80c6ecf2e6aa57438"                    //API authentication key 
t = 1490858347                                              //t (expiration time)
key + t = "40328529ca4381a80c6ecf2e6aa574381490858347"      //Concatenate the strings of the key and t
sign = MD5(key + t) = "7f29ed83c61b77de1b0d66936fd4fd44"   //Compute the MD5 value for concatenated string
```


### 3. Pass stream-mixing parameters using POST method

Stream-mixing parameters are strings in a JSON format, used to specify the video streams to be mixed and the method of stream mixing, as shown in the example below.

```
{
    "timestamp":int(time.time()),           # UNIX timestamp, which is the number of seconds that have elapsed since January 1, 1970
    "eventId":int(time.time()),             # Stream-mixing event ID. Use the timestamp at the backend
    "interface":
    {
        "interfaceName":"Mix_StreamV2",	     # Enter the value as shown in the example
        "para":
        {
            "app_id": appid,                   # Enter LVB APPID
            "interface": "mix_streamv2.start_mix_stream_advanced",  # Enter the value as shown in the example
            "mix_stream_session_id" : "8888_denny",                # Enter the steam ID of primary VJ
            "output_stream_id": "8888_denny",                      # Enter the steam ID of primary VJ
            "input_stream_list":
            [
                # Primary VJ: Background image
                {
                    "input_stream_id":"8888_denny",    # Steam ID
                    "layout_params":
                    {   
                        "image_layer": 1                # Image layer ID: enter 1 for the primary image, and 2, 3 and 4 for secondary images
                    }   
                },
                # Secondary VJ 1
                {
                    "input_stream_id":"8888_rex",    # Steam ID
                    "layout_params":
                    {   
                        "image_layer": 2,              # Image layer ID: Enter 1 for the primary image, and 2, 3 and 4 for secondary images
                        "image_width": 160,            # Secondary VJ image width
                        "image_height": 240,           # Secondary VJ image height
                        "location_x": 380,             # x offset: Lateral offset from the top left corner of primary VJ's background image
                        "location_y": 630              # y offset: Longitudinal offset from the top left corner of primary VJ's background image
                    }   
                 },
                # Secondary VJ 2
                 {
                     "input_stream_id":"8888_link",
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
                     "input_stream_id":"8888_shock",
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


Descriptions of stream-mixing parameters:

- In the above stream-mixing parameters, the fields starting with # are annotations in a python format;

- Enter the current time (in sec) for timestamp and eventId;

- Enter the stream ID of primary VJ for both mix_stream_session_id and output_stream_id;

- input_stream_list is an array containing the information of video streams to be mixed. It must contain the primary VJ's video streams. The number of streams is limited to 4, because a maximum of 4 video streams are allowed to be mixed at the backend;

- layout_params is used to configure the layout of video streams. The image of primary VJ spreads across the full screen by default. You only need to enter 1 in image_layer, and other fields are not required. image_layer is the image layer ID. For images of secondary VJs, enter 2, 3 or 4 in turn;

- image_width, image_height, location_x and location_y are used to define the positions of secondary images relative to the primary image. Please note that, the top, bottom, left and right coordinates of a secondary image cannot go beyond the primary image. This means that: the value of location_x is between 0 and the width of primary image; 

- the value of location_y is between 0 and the height of primary image; the sum of location_x and image_width cannot exceed the width of primary image; and the sum of location_y and image_height cannot exceed the height of primary image.


### 4. Tencent Cloud response to the call

```
{"code":0, "message":"Success!", "timestamp":1490079362}
```


- **code**: Error code; 0: Successful; other values: Failed.
- **message**: Error description.
- **timestamp**: Timestamp, which is same as the timestamp in stream-mixing parameters

## Notes
- Stream mixing CGI does not explicitly define when to start or end stream mixing. "Whether to perform stream mixing" and "the number of streams to be mixed" depend on the number of video streams in the input_stream_list array. If the number of video streams is greater than 1, the stream mixing starts, and if there is only one video stream of primary VJ, the stream mixing ends.

- For the reason of confidentiality, it is recommended to generate the authentication parameters (authentication key) at your APP's backend, instead of frontend. You're also advised to generate the stream-mixing parameters at the primary VJ side, because only the primary VJ knows "whether a joint broadcasting starts (whether to enable stream mixing)" and "which secondary VJ(s) join the broadcasting (which video streams need to be mixed)". The stream-mixing CGI request can be initiated either from backend (send the stream-mixing parameters to backend for sending the request for stream mixing), or at primary VJ side (request the authentication parameters from backend);

- Make sure the pushes by the primary VJ and secondary VJs are all successful before starting stream-mixing. This means you can call the stream-mixing CGI only after receiving the push success event PUSH_EVT_PUSH_BEGIN. Otherwise, the call will fail, and the field "code" in CGI response packet is not 0.

- When a failure message is returned even if you call the stream-mixing CGI after receiving the event PUSH_EVT_PUSH_BEGIN, you can use retry policy. Make a retry attempt every 2 seconds. A maximum of 5 retries are allowed. The reason for this is: PUSH_EVT_PUSH_BEGIN event only indicates that the SDK has successfully sent the first video key frame to the server and there will be a lag of stream status synchronization at the video cloud backend.

