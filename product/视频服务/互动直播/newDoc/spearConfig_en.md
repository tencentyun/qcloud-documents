# SPEAR Engine Stream Control Configuration Introduction
### **Before commencing development, you need to configure stream control parameters in Tencent Cloud ILVB in order to acquire better video quality.**

# Entrance
Log in to Tencent Cloud and go to the configuration page from **Cloud Product** -> **ILVB**.
![](https://mc.qcloudimg.com/static/img/243044a017149d82e7cc10a1a81a7c80/image001.png)

You can see the corresponding configurations of your created APPIDs in the **ILVB** configuration page. Hover your cursor on **More** and select **SPEAR Engine Configuration**.

![](https://mc.qcloudimg.com/static/img/864d6de4bf6a052e3c3fb420be59713b/image002.png)

Enter the configuration to see detailed parameter configuration options. Detailed information about each configuration and how to configure the parameters will be explained below.

![](https://mc.qcloudimg.com/static/img/24d35157346b545e20eab9718f2e4856/image004.png)

# Configuration Instructions
## 1. Scenarios
Different configuration parameters are saved for different ILVB scenarios. You can configure a corresponding scenario for each APPID. When you switch the scenario, all audio/video parameters will be switched accordingly.
Currently, ILVB mainly supports two business scenarios: ILVB and instant messaging.

![](https://mc.qcloudimg.com/static/img/f183e7a8c76ca9895318ae912c917523/image006.png)
![](https://mc.qcloudimg.com/static/img/7587343a15d6a8c31d7fcf13ddb52cff/image007.png)

ILVB mainly aims for scenarios where one or a small number of VJs broadcast while a large number of viewers watch them. Only one or a few users send uplink data, all the rest of the users (several hundreds, thousands or more) only have downlink data and no uplink data at all.
Instant messaging mainly aims for chats or conferences with multiple participants. All participating users require real-time uplink and downlink data with as little latency as possible.
Parameter configurations suitable for each business scenario are provided for different scenarios.

## 2. Platform
Each scenario contains configurations meant for different platforms for which you can configure different parameters. Four platforms are currently supported: Windows, Web, iOS, Android (the parameter configurations are the same for Windows and Web). Once this is configured, Windows clients will automatically use the configuration from the Windows page, and iOS clients will use configuration from the iOS page, so on.

![](https://mc.qcloudimg.com/static/img/c90c047e8f64b4085aa5a90eaa0a18a7/image008.png)

## 3. Roles
You can add multiple roles to the configuration for a certain platform. Roles can have different configuration parameters on the same platform, that is to say, you can change configured audio/video policy on the same client by switching between different roles.
"user" is the default role, whose configuration will be used when no role is selected for the client.

![](https://mc.qcloudimg.com/static/img/7da63a7a27f54b153c31d838263e3c2c/image010.png)

You can add roles and configure their names at the bottom of the page. You can edit roles and delete roles created by you. You can also add multiple roles according to business requirement.

![](https://mc.qcloudimg.com/static/img/47ebdf9ebf1a765c0e3105c84fb59da8/image012.png)
![](https://mc.qcloudimg.com/static/img/69996113f9f8dcd94de3a6e6bf17c5d2/image014.png)


## 4. Difference Between Scenarios, Platforms and Roles
You can make different configuration strategies for scenarios, platforms and roles, so what are the differences between them?
Scenarios determine the differences at the App level, that is, whether an App is used for LVB or instant messaging. LVB scenarios have high requirement regarding video definition, fluency and latency; instant messaging scenarios have high requirement for latency. Thus, most configuration options for LVB and instant messaging are different. In most cases, the scenario for an App will no longer change once it has been determined. Platform is easier to understand, as it mainly holds different configurations related to different platforms. For example, PCs generally have better performance than mobile phones, Apps on mobile phones require permissions, and so on.

Differentiation between roles is to provide support for the business level. The configurable options and available value range for different roles are the same. How to configure them solely depends on the business. For instance, VJs use configurations that allow uplink data, and viewers use configurations that only have downlink data, devices with better performance use configurations with higher video definition, and so on.


## 5. Parameter Configuration
Parameters are divided into video parameters, audio parameters and network parameters. In ILVB scenarios, video parameters and most audio parameters (those in red box in the figure below) are mainly used for uplink data, that is, they only work for VJs and have no impact on viewers. While network parameters are used for both uplink and downlink data, they affect both VJs and viewers. In instance messaging scenarios, all users have uplink and downlink data, which means the three types of parameters affect all users.

![](https://mc.qcloudimg.com/static/img/6dd38ad1b956cd1c885bfdbf1b2ca4ce/image016.png)

Next, we discuss the configuration for each parameter type in details.
### (1) Video Parameters

![](https://mc.qcloudimg.com/static/img/263dff18fdaa2e01e1ff9f94bab43632/image018.png)


* Configuration mode: Three preset packaging modes are provided, "Standard Definition", "High Definition" and "Ultra High Definition". You don't need to configure the other parameters once this is selected. It is recommended to choose "High Definition". You can also choose "Custom" mode and configure the other parameters on your own.
* Encoding Format: "Adaption" means the SDK will adjust definition according to device performance and network condition. "Fixed Image Format" provides two fixed definitions, 4:3 and 16:9.
* Encoding Bitrate: "Adaption" means the SDK will adjust bitrate according to device performance and network condition. "Custom" is used to specify an available bitrate range for the SDK, you can configure the minimum and maximum values into the same value if you need a fixed bitrate.
* Encoding Frame Rate: "Adaption" means the SDK will adjust frame rate according to device performance and network condition. "Custom" is used to specify a desired frame rate. Frame rate is related to bitrate and definition. Inappropriately configured MinQP and MaxQP may result in a lower frame rate than expected.
* Anti-Packet Loss Redundancy: Increase redundancy by means such as FEC, to compensate for lost packet. Redundancy is usually twice as high as packet loss rate. Generally, it is recommended to disable this option.

Frame rate, bitrate and definition are related to each other to a certain extent. Inappropriately configured QP may also reduce frame rate. An easier approach is to simply choose from the preset packing modes: "Standard Definition", "High Definition" and "Ultra High Definition". If you use custom configuration, it is recommended to follow these relations:

Definition	| Bitrate	| Frame Rate
----	|----	|----
640 x 368 | 800 Kbps | 25 fps
960 x 540 | 1200 Kbps | 15 fps

### (2) Audio Parameters

![](https://mc.qcloudimg.com/static/img/28a7f98d8d139042e5c9372e998333d3/image020.png)

* Configuration Mode: You don't need to configure the other parameters in "Default" mode, while you can configure them in **Custom** mode.
* Audio Scenario: The **Broadcast** mode can be used to capture, encode and send audios, which is suitable for VJs. The **View** mode does not enable audio device or send audio data, which is suitable for viewers.
* Encoding Bitrate: Used to configure audio bitrate. Value range is 0-64.
* Anti-Packet Loss Redundancy: Increase redundancy by means such as FEC, to compensate for lost packet. It is recommended to disable this option in ILVB scenarios and enable it in instant messaging scenarios.
* aec: Acoustic echo cancellation. It is recommended to disable this option in ILVB scenarios without joint broadcasting, and enable this option when joint broadcasting is expected, and for instant messaging scenarios.
* agc: Automatic gain control. It is recommended to disable this option in ILVB scenarios without joint broadcasting, and enable this option when joint broadcasting is expected, and for instant messaging scenarios.
* ans: Automatic noise suppression. It is recommended to disable this option in ILVB scenarios without joint broadcasting, and enable this option when joint broadcasting is expected, and for instant messaging scenarios.

### (3) Differences Between Parameters

![](https://mc.qcloudimg.com/static/img/b38439c90daed4aaba9e8ae4a3b93367/image024.png)

Parameter configurations are slightly different in different platforms and scenarios. You can simply configure them according to the configurable options displayed in the page.

For example, you cannot configure audio parameters and network parameters for instant messaging scenarios.

Configurable parameters may change with version updates. The actual configuration options displayed on the configuration page shall prevail.

# Client Logic
## 1. Configuration Effective Timing
The configurations will not take effect for clients immediately after they're configured on Tencent Cloud. Clients need to pull the newest configuration from the backend when calling xxx API. The configuration is saved to local when it's successfully pulled.

## 2. Default Configuration
The SDK has a set of minimum default configuration, users can call APIs to modify this configuration. The parameters can be acquired from the cloud configuration website, parameter values are plaintext JSON strings. The SDK will use the minimum default configuration if it fails to acquire configuration from the cloud in the first attempt. In other cases, the SDK still uses the previous logic configured in the cloud.






