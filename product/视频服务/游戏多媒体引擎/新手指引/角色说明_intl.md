Welcome to Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes voice chat roles for Tencent Cloud GME so that developers can easily access Tencent Cloud GME.
## Role Introduction
Different roles correspond to different speech quality levels. After accessing the SDK, you need to configure roles to use the real-time voice chat feature. When you enter a real-time voice chat room, you need to use the role name as a parameter to obtain the corresponding speech quality and effects, and accordingly get better user experience.
After entering a room, you can also call the relevant function to reconfigure your role.

## Role Features
![](https://main.qcloudimg.com/raw/8f50ebc5e0e8cec403e1df3cad5c0bbe.png)

The following table lists the speech quality corresponding to each role.

|Role Name     | Applicable Scenario         |Key Features|
| ------------- |:-------------: |-------------|
| esports     				|MOBA, competitive, and shooting games.      								|Ordinary sound quality and ultra-low latency.	|
| Rhost     	|Commander mode of MMORPGs, in which only a commander can join broadcasting.      		|High fluency and low latency.		|
| Raudience     		|Commander mode of MMORPGs, in which only a commander can join broadcasting.      		|High fluency and low latency.		|
| Werewolf     			|Werewolf and casual games. 										|Good sound quality and high anti packet loss rate.	|
| host     			|VJ mode of MMORPGs, in which a VJ can interact with players via voice and video. 	|Good sound quality and high anti packet loss rate.	|
| audience     			|VJ mode of MMORPGs, in which a VJ can interact with players via voice and video. 	|Good sound quality and high anti packet loss rate.	|

## Application Scenario Description
#### For fighting game applications, select a role based on the business type:
- esports
- Rhost or Raudience with the commander mode 

#### For casual game applications, select a role based on the business type:
- Werewolf
- host or audience with the LVB mode 

## Role Setting
### 1. Log in to Tencent Cloud Console.
Open [Tencent Cloud Console](https://console.cloud.tencent.com/gme). On the application list, select the application to be edited. Click **Change Application Scenario** under **SPEAR Engine Configuration**, and select **Game Real-Time Voice Chat**.

![](https://main.qcloudimg.com/raw/6ccd89f31b9489e7395e36c50b11b1de.png)
### 2. Configure information.
Select the platform to be configured.  
![](https://main.qcloudimg.com/raw/9d72ea27a068a6ff607a3d79a68c5d85.png)

Some default roles are displayed on the page.  
![](https://main.qcloudimg.com/raw/e63dbaeffcb6cd539d8be10cd26f65c2.png)

You can click **Edit** to edit the corresponding role, for example, change the name and effects.
![](https://main.qcloudimg.com/raw/64d67a101f1c135dba73661e6773efc2.png)

### 3. Add and configure a role.
To add a custom role, you can click **Add and Configure User Role** at the bottom of the page.
![](https://main.qcloudimg.com/raw/d7eed9d877bff9d23f7d7b99c11a306c.png)

Add and configure a role, enter relevant information, and click **Save**.

![](https://main.qcloudimg.com/raw/47796a9344efc37dd350e44fa8835868.png)

## Use of Roles
Each role has a name, which is entered as a parameter in the relevant function.
- Unity sample code:
```
IQAVContext.GetInstance().GetRoom().ChangeRole(“Player”, authBuffer);
```
- Android sample code:
```
ITMGContext.GetInstance(this).GetRoom().ChangeRole("Player",bytes);
```
- iOS sample code:
```
[[[ITMGContext GetInstance]GetRoom ]ChangeRole:@"Playre"authBuffer:authBuffer];
```
