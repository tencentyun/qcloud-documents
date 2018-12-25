With these APIs, you can experience the features of initiating push/pull, controlling video collection during the push process, and switching audio/video parameter settings. The detailed API descriptions are as follows:
## WebRTCAPI.startRTC
This API is used to initiate push/pull actively.
Parameter:

| Parameter 	| Type 	| Required | Description |
|---|---|---|---|
|opt	|object | Yes ||
|succ|function | No | Callback successful |
|fail	|function | No | Callback failed |

Parameter definitions of opts:

| Parameter | Type | Required | Description |
|---|---|---|---|
|stream| MediaStream | No | Audio/video stream, [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)|
|role	|string | No | Role name, which determines the bitrate control for the server to receive the video stream |

Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.startRTC({
        role: '',
        stream: stream
    }, function(){
        //Successful
    },function(){
        //Failed
    });
		
## WebRTCAPI.stopRTC
This API is used to stop the push.

| Parameter | Type | Description |
|---|---|---|
|opt	|object | Reserved field, and the empty object can be passed |
|succ|function | Callback successful |
|fail|function | Callback failed |

Syntax example

    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.stopRTC({}, function(){
        console.debug('stop succ')
    }, function(){
        console.debug('stop end')
    });
		
## WebRTCAPI.getLocalStream
This API is supported in version 2.5 or above
This API is used to get local audio/video streams.

| Parameter | Type | Required | Description |
|---|---|---|---|
|opts	|Object | No | Empty object can be passed {}|
|succ|function | Yes | Callback successful |
|fail	|function | No | Callback failed |

Parameter definitions of opts:

| Parameter | Type | Required | Description |
|---|---|---|---|
|audio	|Boolean | No | Whether to collect audio. Defaults to true |
|video	|Boolean | No | Whether to collect video. Defaults to true |
|screen	|Boolean | No | Whether to collect screen sharing. Defaults to false |
|screenSources	|string | No | The media collected by the screen sharing are separated by commas. Optional options include screen window tab audio |
|attributes	|object | No | Attributes of push related configuration |
|videoDevice	|Device | No | Specified device. The video device obtained by getVideoDevices |
|audioDevice|Device | No | Specified device. The audio device obtained by getAudioDevices |
|needRetry|Boolean | No | Whether to allow downgrade to remove the configuration and retry when it fails to obtain some items using the parameter configuration. Defaults to true |

Parameter definitions of attributes:

| Parameter | Type | Required | Description |
|---|---|---|---|
|width	|Integer | No | Resolution width |
|height	|Integer | No | Resolution height |
|frameRate|Integer | No | Frame rate |

succ callback (Object):

| Parameter | Type | Description |
|---|---|---|
|stream	|MediaStream |Audio/video stream [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)	|

Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.getLocalStream({
        video:true,
        audio:true,
        attributes:{
            width:640,
            height:480,
            frameRate:20
        }
    },function( info ){
        // info { stream }
        var stream = info.stream;
        document.getElementById("localVideo").srcObject = stream
    },function ( error ){
        console.error( error )
    });
		
## WebRTCAPI.updateStream
This API is supported in version 2.5.3 or above
This API is used to stop the push.

| Parameter | Type | Description |
|---|---|---|
|opt	|object | Parameter |
|succ	|function | Callback successful |
|fail|function | Callback failed |

opt:

| Parameter | Type | Description |
|---|---|---|
|stream|MediaStream | Reserved field, and the empty object can be passed |
|role	|string | Optional. This parameter is required if you need to update the screen role settings when updating the stream |

Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.updateStream({
        role: "user",
        stream: stream
    }, function(){
        console.debug('updateStream succ')
    }, function(){
        console.debug('updateStream failed')
    });
		
## WebRTCAPI.closeAudio
Do not perform the audio collection (mute).
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.closeAudio();
		
## WebRTCAPI.openAudio
Audio collection identification (unmute).
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.openAudio();
		
## WebRTCAPI.closeVideo
Do not perform the video collection.
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.closeVideo();
		
## WebRTCAPI.openVideo
Enable the video collection.
The openVideo API enables the video collection when the audio/video is being pushed and the video is turned off.
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.openVideo();
		
## WebRTCAPI.getLocalMediaStatus
This API is used to obtain the current video collection configuration.
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    var status = RTC.getLocalMediaStatus();
    //status.video true | false (indicates whether the current configuration collects video)
    //status.audio true | false (indicates whether the current configuration collects audio)
		
## WebRTCAPI.changeSpearRole
This API is used to switch the user role in the Screen Setting.
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.changeSpearRole( "role_name" );
    //status.video true | false (indicates whether the current configuration collects video)
    //status.audio true | false (indicates whether the current configuration collects audio)
		
## WebRTCAPI.getVideoDevices
This API is used to enumerate cameras.
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.getVideoDevices( function(devices){
        //"devices" is an array that enumerates the video input devices of the current device (DeviceObject)
        //For example: [device,device,device]
        //These devices will be used when selecting cameras
    })
		
## WebRTCAPI.chooseVideoDevice
This API is used to select a camera.
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.chooseVideoDevice( device );
		
## WebRTCAPI.getAudioDevices
This API is used to enumerate microphones.
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.getAudioDevices( function(devices){
        //"devices" is an array that enumerates the audio input devices of the current device (DeviceObject)
        //For example: [device,device,device]
        //These devices will be used when selecting microphones
    })
		
## WebRTCAPI.chooseAudioDevice
This API is used to select a microphone.
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.chooseAudioDevice( device );
		
## WebRTCAPI.getSpeakerDevices
This API is supported in version 2.6 or above
This API is used to enumerate audio output devices
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.getSpeakerDevices( function(devices){
        //"devices" is an array that enumerates the audio input devices of the current device (DeviceObject)
        //For example: [device,device,device]
        //These devices will be used when selecting microphones
    })
		
## WebRTCAPI.chooseSpeakerDevice
This API is supported in version 2.6 or above

| Parameter | Type | Description |
|---|---|---|
|media	|HTMLMediaElement|Audio / Video|
|device|DeviceElement|	Audio / Video|
|succ	|function | Callback successful |
|fail|function | Callback failed |

This API is used to select an audio output device
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    var speakerList = [];
    RTC.getSpeakerDevices( function(devices){
        speakerList = devices;
    })
    ....

    document.querySelectorAll("video").forEach( function(video){ 
        console.debug(video); 
        RTC.chooseSpeakerDevice( device, speakerList[1],function(){
            console.debug('change speaker succ ')
        } ,function(error){
            console.error('change speaker error ', error)
        } );
    });
		
## WebRTCAPI.getStats
This API is used to obtain statistics and stop obtaining APIs

| Parameter | Type | Required | Description |
|---|---|---|---|
|opt	|object | Yes| |
|succ	|function | Yes | Callback successful |
|fail	|function | No | Callback failed |

Details of opt parameters:

| Parameter | Type | Required | Description |
|---|---|---|
|userId	|String | No | The user ID of the statistics of the audio/video stream to be obtained; if it is null, the user's own statistics will be obtained |
|interval	|integer | No | Timer (in milliseconds), indicates the time interval for obtaining statistics. If it is left empty, the statistics will be obtained from time to time. |

Details of result:

    //Send a stream
    {
        video:{
            ssrc        : "", //Data source ID
            codec       : "", //Encoding protocol
            packetsSent : "", //Number of video packets sent
            packetsLost : "", //Number of video packets lost
            width       : "", //Video resolution - width
            height      : "", //Video resolution - height
        }
        audio:{
            ssrc        : "", //Data source ID
            codec       : "", //Encoding protocol
            packetsSent : "", //Number of audio packets sent
        }
    }

    //Receive a stream
    {
        video:{
            ssrc            : "", //Data source ID
            codec           : "", //Encoding protocol
            packetsReceived : "", //Number of video packets received
            packetsLost     : "", //Number of video packets lost
            width           : "", //Video resolution - width
            height          : "", //Video resolution - height
        }
        audio:{
            ssrc            : "", //Data source ID
            codec           : "", //Encoding protocol
            packetsReceived : "", //Number of audio packets received
            packetsLost     : "", //Number of audio packets lost
        }
    }
Syntax example:

    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.getStats( {
        interval:2000//Obtain the statistics every 2 seconds
    },function( result ){
        console.debug( result );
        // test code 
        setTimeout( function(){
            //No more statistics are collected
            result.nomore(); 
        },20000);
    } ,function( error ){
        console.error( error );
    } );
		
## WebRTCAPI.SoundMeter
This API is used to detect the volume
Syntax example
This API is supported in version 2.5.3 or above
Syntax example:
` var soundMeter = WebRTCAPI.SoundMeter( opts )`
		
opts:

| Parameter | Type | Required | Description |
|---|---|---|---|
|stream	|object | Yes|MediaStream|
|onprocess	|function | Yes | Audio stream monitoring callback |

Callback parameters for oonprocess:

| Parameter | Type | Description |
|---|---|---|
|volume	|String | Volume (for example: 0.02) |
|status	|function|volume >= 0.01 ? "speaking" : "silence"|
|event	|AudioProcessingEventObject |         	

The criterion for "speaking" and "silence" is the volume value. If the value >= 0.01, it is "speaking"; if the value <0.01, it is "silence". You can also make your own judgment.

    //Analyze the audio stream
    var meter = WebRTCAPI.SoundMeter({
        stream: info.stream,
        onprocess: function( data ){
            $("#volume").val( data.volume)
            $("#volume_str").text( "volume: "+ data.volume)
            $("#status").text( data.status )
        }
    })

    //Stop analyzing the audio stream
    meter.stop();

