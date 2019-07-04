Artificial Audio Intelligence involves some basic concepts related to COS and speech recognition. To help you understand the follow-up content, we explain these concepts as follows:

**1. APPID**
Tencent Cloud application ID.
How to obtain: For new users, register and log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/), and then an APPID is generated immediately.
**2. ProjectId**
Tencent Cloud project ID. Default is 0.
How to obtain: Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/), and select "Project Management" under "User Center" to view the default project with the ProjectId of 0. Click "New" to create a project and obtain a new ProjectId.
**3. SecretId and SecretKey**
SecretId and SecretKey are Tencent Cloud security credentials. SecretId is used to identify an API caller, and SecretKey is used to encrypt the signature string and verify its key on the server. Users must keep their SecretKeys private to avoid disclosure.
How to obtain: <br>1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/), click "Cloud Products", and select "Cloud API Key" under "Monitoring and Management" to enter the cloud API key management page. <br>2) On the cloud API key management page, click "New" to create a pair of SecretId/SecretKey. Each account can have two pairs of SecretId/SecretKey at most. <br>
![1](https://mccdn.qcloud.com/img568f5fb824757.png)
![2](//mc.qcloudimg.com/static/img/0727c55969eabe8d2b0aba7b0e0e796c/image.png)
**4. Service Type**
Artificial Audio Intelligence provides four types of services, that is, Automatic Speech Recognition (ASR), Text to Speech (TTS), Voiceprint Recognize (VPR), and Customer Service Robot (CSR).
**5. Subservice Type**
The ASR, TTS, VRP, CSR services of Artificial Audio Intelligence are subdivided into several subservices, such as offline speech recognition and streaming speech recognition under ASR.
**6. Template**
A template consists of a set of parameters for voice processing. The name of a template must be unique within Project. The required parameters include APPID, ProjectId, service type, subservice type, as well as other parameters required in the subservice. You can create, modify and delete templates in the console. You can also specify templates to deal with requests submitted to Artificial Audio Intelligence.
**7. Bucket**
Bucket is the first-level directory under COS. Each Bucket has its own access domains (public, private, and accelerated domains), access permissions (public and private), origin-pull settings, hotlink protection settings, and other attribute configuration items.

