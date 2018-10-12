
## Preliminary Information
### Supported platforms for H5

| OS Platform  | Browser /webview  | Required Version  | Notes           |
| ------------ | --------------- | -------- | ------------- |
| iOS          | Safari (Only) | 11.1.2   | |
| Android      | Chrome | 60+      | Support for H264 |
| Mac          | Chrome          | 47+      |               |
| Mac          | Safari          | 11+      |               |
| Windows(PC)  | Chrome          | 52+      |               |

## Glossary
Tencent Cloud account information

| Term | Meaning |
| ----------- | ------------------------------------------------------------ |
| appid       | After a vendor is registered with Tencent Cloud, a unique ID (appId) on Tencent Cloud is generated. |
| sdkappid    | Vendors can create multiple projects on the TRTC console to correspond to their own Apps. Each project is represented by a SdkAppid. |
| accounttype | Each SdkAppid has an AccountType parameter in the account system page, which is used during login. |

"appId" is in the format of 125xxxxxxx and can be obtained at the top of the TRTC console.
"SdkAppid" is in the format of 14000xxxxx. It can be viewed in **App Basic Settings** after you create a project on the TRTC console.
You can see AccountType in **App Basic Settings** -> **Account Integration System** after creating a project on the TRTC console (if not, edit and save it)

User information

| Term | Meaning |
| ------- | ------------------------------------------------------------ |
| userId  | Identifies users in the App, also known as user name. |
| userSig | Identity signature, which functions as a login password. Each userId has a corresponding signature with a certain validity period, which is added in the request to help Tencent Cloud identify users. |

Video call information

| Term | Meaning |
| ------------- | ------------------------------------------------------------ |
| Spear role | The name of a collection of a video user's configurations, such as resolution, bitrate, and frame rate, which can be maintained on the Spear engine page of the project. |
| roomId        | Identifies a video chat room. Users with the same roomId can see each other. |
| privateMapKey | Room permission key, which functions as the key for joining a room with the specified roomId |
Download [sign_src.zip](http://dldir1.qq.com/hudongzhibo/mlvb/sign_src_v1.0.zip) to obtain the calculation code for the server to issue UserSig and privateMapKey (the signature algorithm for generating UserSig and privateMapKey is ECDSA-SHA256).

## Integration Preparations
1. Register a Tencent Cloud account and contact the Sales to activate the TRTC business.
2. Create a new project on the TRTC page. Get SdkAppid and AccountType.
3. See [UserSig Calculation Documentation](https://intl.cloud.tencent.com/document/product/268/7656) to calculate the UserSig of the test user name.
4. If you have configured a firewall for your network, make sure you open the following ports:

| Protocol | Port |
| ---- | ------------------- |
| TCP  | 8687                |
| UDP  | 8000, 8800 and 443 |

Introduce SDK using CDN.
### Introduce WebRTCAPI.min.js on the page

`<script src="https://sqimg.qq.com/expert_qq/webrtc/2.6/WebRTCAPI.min.js"></script>`
### Update Log
2.6
Added the SoundMeter API
Added a field for reporting log
Adjusted the initialization API

