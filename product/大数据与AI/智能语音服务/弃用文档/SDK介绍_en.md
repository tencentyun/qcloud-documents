## Signature
You need to use API AbsCredentialProvider to compute signature. The function for computing signature is as follows:
```
String getAudioRecognizeSign(String source);
```
How the final signature is computed:
Perform an HMAC-SHA1 encryption on source with SecretKey, then perform Base64 encoding on the ciphertext to obtain the final signature string: sign=Base64Encode(HmacSha1(source,secretKey)).
To make it easier for users to conduct testing, the SDK already has an implementation class LocalCredentialProvider. However, in order to ensure the security of SecretKey, it should only be used in the testing environment. For the official version, please obtain the signature on the third-party server.

## Initialize AAIClient
AAIClient is the core class for voice services. You can call the class to start, stop, and cancel speech recognition.
```
public AAIClient(Context context, int appid, int projectId, String secreteId, AbsCredentialProvider credentialProvider) throws ClientException
```
| Parameter Name | Type | Required | Description |
--|--|--|--
| context | Context | Yes | Context |
| APPID | int | Yes | APPID registered with Tencent Cloud |
| projectId | int | No | User's projectId |
| secreteId | String | Yes | User's SecreteId |
| credentialProvider | AbsCredentialProvider | Yes | Authentication class |
Example
```
try {
    AaiClient aaiClient = new AAIClient(context, appid, projectId, secretId, credentialProvider);
} catch (ClientException e) {
    e.printStackTrace();
}
```
If aaiClient is no longer needed, call the release() method to release resources:
```
aaiClient.release();
```
## Configure Global Parameters
You can call the static method of the ClientConfiguration class to modify the global configuration.

| Method | Description | Default | Valid Value Range |
--|--
| setServerProtocolHttps | Set HTTPS/HTTP protocol | true(Https) | false/true |
| setMaxAudioRecognizeConcurrentNumber | Maximum number of concurrent requests for speech recognition | 2 | 1-5 |
| setMaxRecognizeSliceConcurrentNumber | Maximum number of concurrent speech recognition shards | 5 | 1-5 |
| setAudioRecognizeSliceTimeout | HTTP read timeout threshold | 5000ms | 500-10000ms |
| setAudioRecognizeConnectTimeout | HTTP connection timeout threshold | 5000ms | 500-10000ms |
| setAudioRecognizeWriteTimeout | HTTP write timeout threshold | 5000ms | 500-10000ms |
Example
```
ClientConfiguration.setServerProtocolHttps(true);
ClientConfiguration.setMaxAudioRecognizeConcurrentNumber(2)
ClientConfiguration.setMaxRecognizeSliceConcurrentNumber(5)
ClientConfiguration.setAudioRecognizeSliceTimeout(2000)
ClientConfiguration.setAudioRecognizeConnectTimeout(2000)
ClientConfiguration.setAudioRecognizeWriteTimeout(2000)
```
## Set Result Listener
AudioRecognizeResultListener can be used to listen for the result of speech recognition. It involves the following four APIs:
- Callback API for speech recognition result of speech shard

```
void onSliceSuccess(AudioRecognizeRequest request, AudioRecognizeResult result, int order);
```

| Parameter | Type | Description | 
--|--
| request | AudioRecognizeRequest | Speech recognition request | 
| result | AudioRecognizeResult | Speech recognition result of speech shard |
| order | int | The sequence number of the speech stream to which the speech shard belongs |

- Callback API for speech recognition result of speech stream

```
void onSegmentSuccess(AudioRecognizeRequest request, AudioRecognizeResult result, int order);
```

| Parameter | Type | Description | 
--|--
| request | AudioRecognizeRequest | Speech recognition request | 
| result | AudioRecognizeResult | Speech recognition result of speech shard |
| order | int | The sequence number of the speech stream |

- API for returning all the recognition results

```
void onSuccess(AudioRecognizeRequest request, String result);
```

| Parameter | Type | Description | 
--|--
| request | AudioRecognizeRequest | Speech recognition request | 
| result | String | All the recognition results |

- Callback API for the failure of speech recognition request

```
void onFailure(AudioRecognizeRequest request, ClientException clientException, ServerException serverException);
```

| Parameter | Type | Description | 
--|--
| request | AudioRecognizeRequest | Speech recognition request | 
| clientException | ClientException | Client exception |
| serverException | ServerException | Server exception |
For the sample code, please see "Quick Start".

## Set Speech Recognition Parameters
By building the AudioRecognizeConfiguration class, you can set the configuration for speech recognition:

| Parameter Name | Type | Required | Description | Default |
--|--|--|--
| enableSilentDetect | boolean | No | Whether to enable silence detection. If it is enabled, the silence before speech is not recognized | true |
| enableFirstAudioFlow | boolean | No | Whether to enable the detection of speech start timeout. If it is enabled, recording stops automatically when timeout occurs | false |
| enableNextAudioFlow | boolean | No | Whether to enable the detection of speech end timeout. If it is enabled, recording stops automatically when timeout occurs | false |
| minAudioFlowSilenceTime | int | No | Minimum time interval between two speech streams | 1500ms |
| maxAudioFlowSilenceTime | int | No | Speech end timeout threshold | 10000ms |
| maxAudioStartSilenceTime | int | No | Speech start timeout threshold | 2000ms |
| minVolumeCallbackTime | int | No | Volume callback time | 80ms |
| sensitive | float | No | Speech recognition sensitivity. A smaller value means a higher sensitivity (value range: 1-5) | 3 |

Example:
```
AudioRecognizeConfiguration audioRecognizeConfiguration = new AudioRecognizeConfiguration.Builder()
	.enableAudioStartTimeout(true) // Whether to stop recording when the start timeout occurs
    .enableAudioEndTimeout(true) // Whether to stop recording when the end timeout occurs
    .enableSilentDetect(true) // Whether to enable silence detection (true means no silence detection is performed)
    .minAudioFlowSilenceTime(1000) // Interval between speech streams during recognition
    .maxAudioFlowSilenceTime(10000) // Speech end timeout threshold
    .maxAudioStartSilenceTime(2000) // Speech start timeout threshold
    .minVolumeCallbackTime(80) // Volume callback time
	.sensitive(2.8) // Recognition sensitivity
    .build();

// Enable speech recognition
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null) {
            aaiClient.startAudioRecognize(audioRecognizeRequest, audioRecognizeResultListener, audioRecognizeConfiguration);
        }
    }
}).start();
```

## Configure Status Listener
AudioRecognizeStateListener can be used to listen for the status of speech recognition. It involves the following seven APIs

| Method | Description | 
--|--
| onStartRecord | Start recording |
| onStopRecord | End recording |
| onVoiceFlowStart | The start of speech stream is detected | 
| onVoiceFlowFinish | The end of speech stream is detected | 
| onVoiceFlowStartRecognize | Speech stream recognition starts |
| onVoiceFlowFinishRecognize | Speech stream recognition ends | 
| onVoiceVolume | Volume | 

## Set Timeout Listener
AudioRecognizeTimeoutListener can be used to listen for the timeout of speech recognition. It involves the following two APIs:

| Method | Description | 
--|--
| onFirstVoiceFlowTimeout | Detect the first speech stream timeout |
| onNextVoiceFlowTimeout | Detect the next speech stream timeout |

Example:
```
AudioRecognizeStateListener audioRecognizeStateListener = new AudioRecognizeStateListener() {
    @Override
    public void onStartRecord(AudioRecognizeRequest audioRecognizeRequest) {
        // Start recording
    }

    @Override
    public void onStopRecord(AudioRecognizeRequest audioRecognizeRequest) {
		// End recording
    }

    @Override
    public void onVoiceFlowStart(AudioRecognizeRequest audioRecognizeRequest, int i) {
		// Speech stream starts
    }

    @Override
    public void onVoiceFlowFinish(AudioRecognizeRequest audioRecognizeRequest, int i) {
		// Speech stream ends
    }

    @Override
    public void onVoiceFlowStartRecognize(AudioRecognizeRequest audioRecognizeRequest, int i) {
		// Speech stream recognition starts
    }

    @Override
    public void onVoiceFlowFinishRecognize(AudioRecognizeRequest audioRecognizeRequest, int i) {
		// Speech stream recognition ends
    }

    @Override
    public void onVoiceVolume(AudioRecognizeRequest audioRecognizeRequest, int i) {
		// Volume callback
    }
};

AudioRecognizeTimeoutListener audioRecognizeTimeoutListener = new AudioRecognizeTimeoutListener() {
    @Override
    public void onFirstVoiceFlowTimeout(AudioRecognizeRequest audioRecognizeRequest) {
        // Detect speech start timeout
    }

    @Override
    public void onNextVoiceFlowTimeout(AudioRecognizeRequest audioRecognizeRequest) {
		// Detect speech end timeout
    }
};

// Enable speech recognition
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null) {
            aaiClient.startAudioRecognize(audioRecognizeRequest, audioRecognizeResultListener, audioRecognizeStateListener,audioRecognizeTimeoutListener, audioRecognizeConfiguration);
        }
    }
}).start();
```



## Other Important Classes

### AudioRecognizeRequest
If both templateName and customTemplate are set, the value of templateName is used. 

| Parameter Name | Type | Required | Description | Default |
--|--|--|--
| pcmAudioDataSource | PcmAudioDataSource | Yes | Audio data source | None |
| templateName | String | No | Template name set by the user on console | None |
| customTemplate | AudioRecognizeTemplate | No | User-defined template | (1, 0, 1) |
### AudioRecognizeResult
This the speech recognition result object, which corresponds to the AudioRecognizeRequest object and is used to return the result of speech recognition.

| Parameter Name | Type | Description |
--|--|--|--
| code | int | Status recognition code |
| message | String | Recognition message |
| text | String| Recognition result |
| seq | int | The sequence number of speech shard |
| voiceId | String | ID of the speech stream to which the speech shard belongs |
| cookie | String | cookie value |

## AudioRecognizeTemplate
For custom speech templates, the required parameters include:

| Parameter Name | Type | Required | Description |
--|--|--|--
| engineModelType | int | Yes | Engine model type |
| resultTextFormat | int | Yes | Encoding for the result text. Available values: UTF-8, GB2312, GBK, BIG5
| resType | int | Yes | The way that the result is returned |
Example:
```
AudioRecognizeTemplate audioRecognizeTemplate = new AudioRecognizeTemplate(1,0,1);
```
## PcmAudioDataSource
You can implement this API to recognize single-channel PCM audio data with a 16k sampling rate. It involves the following APIs:

- Add data to the speech recognizer; copy the data with a length of "length" value to the audioPcmData array, with subscripts starting with 0; and return the length of the actually copied data.

```
int read(short[] audioPcmData, int length);
```
- Callback function used upon start of recognition. You can perform initialization here.

```
void start() throws AudioRecognizerException;
```
- Callback function used upon end of recognition. You perform clean-up here.

```
void stop();
```
- Set the maximum data amount the speech recognizer reads each time.

```
int maxLengthOnceRead();
```
## AudioRecordDataSource
Implementation class of API PcmAudioDataSource. It is used to directly read the audio data input by microphone for real-time recognition.
## AudioFileDataSource
Implementation class of PcmAudioDataSource. It is used to directly read the single-channel PCM audio data with a 16k sampling rate.
>**Note:**
> Data in other formats cannot be correctly recognized.

## AAILogger
You can use AAILogger to control the output of logs, selectively outputting the debug, info, warn and error-level log information.
```
public static void disableDebug();
public static void disableInfo();
public static void disableWarn();
public static void disableError();
public static void enableDebug();
public static void enableInfo();
public static void enableWarn();
public static void enableError();
```
