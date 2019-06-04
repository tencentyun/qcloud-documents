智能语音服务涉及到对象存储以及语音识别的相关基本概念，为了帮助用户理解后续内容，将智能语音服务涉及的基本概念作如下说明。

**1. APPID**
腾讯云应用 ID。
获取途径：新用户注册并登录 [腾讯云管理中心控制台](https://console.cloud.tencent.com/)，立即生成 APPID。
**2. ProjectId**
腾讯云项目 ID，默认项目 ID 为 0。
获取途径：用户登录 [控制台](https://console.cloud.tencent.com/)，选择【用户中心】栏下的【项目管理】，可查看默认项目，默认项目 ProjectId = 0。单击【新建】即可创建新项目，并获取新的 ProjectId。
**3. SecretId 和 SecretKey**
腾讯云安全凭证，其中，SecretId 是用于标识 API 调用者身份的，而 SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。用户应严格保管其 SecretKey，避免泄露。
获取途径：<br>1) 用户登录 [控制台](https://console.cloud.tencent.com/)，单击【云产品】，选择【监控与管理】栏下的【云 API 密钥】，进入云 API 密钥管理页面。<br>2) 在云 API 访问密钥管理页面，单击【新建】即可以创建一对 SecretId/SecretKey，每个帐号最多可以拥有两对 SecretId/SecretKey。<br>
![1](https://mccdn.qcloud.com/img568f5fb824757.png)
![2](//mc.qcloudimg.com/static/img/0727c55969eabe8d2b0aba7b0e0e796c/image.png)
**4. 服务类型**
智能语音提供的四种服务类型，包括语音识别（Automatic Speech Recognition，ASR）、语音合成（Text to Speech，TTS）、声纹识别（Voiceprint Recognize，VPR）、客服机器人（Customer Service Robot，CSR）。
**5. 子服务类型**
在智能语音服务 ASR、TTS、VRP、CSR 服务层级下，还细分出了服务子类型。例如：语音识别子服务类型当前包括离线语音识别和实时流式语音识别。
**6. 模板**
模板由一组指定语音处理的参数定义而成，模板的命名需要在 Project 内唯一，必备的参数包括 APPID，ProjectId，服务类型、子服务类型，除此之外还包括对应子服务类型需要的其他处理参数。用户可以在控制台进行模板的创建、修改和删除。提交到智能语音服务的请求，可以通过指定模板的形式，来指定如何处理语音。
**7. Bucket**
用户存储在对象储存下的第一级目录。每个 Bucket 拥有自己的访问域名（外网、内网、加速访问域名）、访问控制权限（公有、私有）、回源设置、防盗链设置等属性配置项目。
