## Preparations for Development
## Downloading SDK
You can download Artificial Audio Intelligence Android SDK and demos for streaming speech recognition at [Android SDK](https://mc.qcloudimg.com/static/archive/6600e4e3ed5d41a5b9bfd649a4f7a3aa/aai-android-sdk-v2.x.zip)

### Before Development
1. Before using streaming recognition, developers need to register on Tencent Cloud - [Console](https://console.cloud.tencent.com/) to obtain APPID, SecretId, SecretKey, etc.
2. Your mobile phone must be connected to such networks as GPRS, 3G or WiFi.
3. Android 4.0 and later are supported.

### Operating Environment Configuration

##### Introducing .so file
- libWXVoice.so: Tencent Cloud speech recognition "so" library

##### Introducing jar package
- aai-2.1.2.jar: Tencent Cloud Artificial Audio Intelligence SDK
- okhttp-3.2.0.jar
- okio-1.6.0.jar
- slf4j-android-1.6.1-RC1.jar

Tencent Cloud Artificial Audio Intelligence SDK can be built locally or remotely.
#### Local Building
You can directly download Android SDK and demos, and then integrate "so" file and jar package from the sdk-source directory as well as okhttp3, okio and slf4j libraries to the application.
#### Remote Building
Add the followings in build.gradle file:
```
compile 'com.tencent.aai:aai:2.1.2:@aar'
compile 'com.squareup.okhttp3:okhttp:3.6.0'
compile 'org.slf4j:slf4j-android:1.6.1-RC1'
```
If you can use gradle, we recommend that you build your application remotely.

#### Add the following permissions in AndroidManifest.xml:
```
< uses-permission android:name="android.permission.RECORD_AUDIO"/>
< uses-permission android:name="android.permission.INTERNET"/>
< uses-permission android:name="android.permission.WRITE_SETTINGS" />
< uses-permission android:name="android.permission.READ_PHONE_STATE"/>
< uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
< uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS"/>
```
## Quick Start

### To Enable Speech Recognition
```
int appid = XXX;
int projectid = XXX;
String secretId = "XXX";

// The SDK provides local signatures to help users with testing. But for the security of secretKey, generate the signature on a third party server in formal environment.
AbsCredentialProvider credentialProvider = new LocalCredentialProvider("your secretKey");

final AAIClient aaiClient;
try {
    // 1. Initialize AAIClient object.
    aaiClient = new AAIClient(this, appid, projectid, secretId, credentialProvider);

    // 2. Initialize the speech recognition request.
    final AudioRecognizeRequest audioRecognizeRequest = new AudioRecognizeRequest.Builder()
            .pcmAudioDataSource(new AudioRecordDataSource()) // set the audio source to microphone input
            .build();

    // 3. Initialize the speech recognition result listener.
    final AudioRecognizeResultListener audioRecognizeResultListener = new AudioRecognizeResultListener() {
        @Override
        public void onSliceSuccess(AudioRecognizeRequest audioRecognizeRequest, AudioRecognizeResult audioRecognizeResult, int i) {
			// Return recognized results of audio clips
        }

        @Override
        public void onSegmentSuccess(AudioRecognizeRequest audioRecognizeRequest, AudioRecognizeResult audioRecognizeResult, int i) {
			// Return the recognized result of an audio stream
        }

        @Override
        public void onSuccess(AudioRecognizeRequest audioRecognizeRequest, String s) {
			// Return all recognized results
        }

        @Override
        public void onFailure(AudioRecognizeRequest audioRecognizeRequest, ClientException e, ServerException e1) {
			// Recognition failed
        }
    };

    // 4. Enable speech recognition
    new Thread(new Runnable() {
        @Override
        public void run() {
            if (aaiClient!=null) {
                aaiClient.startAudioRecognize(audioRecognizeRequest, audioRecognizeResultListener);
            }
        }
    }).start();

} catch (ClientException e) {
    e.printStackTrace();
}
```
### To Stop Speech Recognition
```
// 1. Obtain the request ID
final int requestId = audioRecognizeRequest.getRequestId();
// 2. call stop
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null){
            aaiClient.stopAudioRecognize(requestId);
        }
    }
}).start();
```
### To Cancel Speech Recognition
```
// 1. Obtain the request ID
final int requestId = audioRecognizeRequest.getRequestId();
// 2. Call cancel
new Thread(new Runnable() {
    @Override
    public void run() {
        if (aaiClient!=null){
            aaiClient.cancelAudioRecognize(requestId);
        }
    }
}).start();
```

