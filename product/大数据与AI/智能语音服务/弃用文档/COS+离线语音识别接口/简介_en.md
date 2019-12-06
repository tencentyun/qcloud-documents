## How It Works
Four steps are involved in the technical framework:
1. The user uploads a voice file to Tencent COS source Bucket.
2. COS calls back the voice data to the speech recognition system to trigger auto speech recognition.
3. The speech recognition system uploads the recognized result (text file) to the target COS Bucket.
4. The speech recognition system notifies the user by calling back the API, and sends the result text as well as the download path to the user.
The overall technical framework is shown below:
![1](https://mc.qcloudimg.com/static/img/86dfde5750489472573a8180be24c6d3/cos.png)
## Access Guidelines
To achieve auto interaction of COS and speech recognition system, you need to create a template in the Artificial Audio Intelligence console for the configuration of COS and speech recognition service.

**Step 1**: You can enter the template management page via ["Console"](https://console.cloud.tencent.com/) -> "Artificial Audio Intelligence" -> "Template Management".

**Step 2**: Click **Add** to create a template, and then select the speech recognition service and the subservice, offline speech recognition.

**Step 3**: Select the model, number of channels, and text encoding method based on your business.

**Step 4**: Select COS Bucket as the speech input source (only Shanghai (East China) is supported as the Bucket region called by speech recognition), and then select the Bucket to which the speech is input and the target Bucket from which the text result is output.

**Step 5**: The callback URL is optional. If it is left empty, you need to go to the target COS Bucket to view the recognized result instead of receiving the recognized result automatically.





