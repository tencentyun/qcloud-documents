Welcome to Tencent Cloud Game Multimedia Engine (GME) SDK. This document describes voice chat roles for Tencent Cloud GME so that developers can easily access Tencent Cloud GME.
## Role Introduction
Different roles correspond to different speech quality levels. After accessing the SDK, you need to configure roles to use the real-time voice chat feature. When you enter a real-time voice chat room, you need to use the role name as a parameter to obtain the corresponding speech quality and effects, and accordingly get better user experience.
After entering a room, you can also call the relevant function to reconfigure your role.

## Role Features
![](https://main.qcloudimg.com/raw/844f9a4c6d778076598ee6654192e1f1.png)

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
Open [Tencent Cloud Console](https://console.cloud.tencent.com/gme). On the application list, select the application to be edited.

### 2. Configure information.
Select the platform to be configured.  
![](https://main.qcloudimg.com/raw/6906de49cb428da5cbea801b352aae8d.png)

Some default roles are displayed on the page.  
![](https://main.qcloudimg.com/raw/98cf41df11743e2ab5234a668aeb9a3b.png)

You can click **Edit** to edit the corresponding role, for example, change the name and effects.
![](https://main.qcloudimg.com/raw/3768738f7621335239c252d7f6947a36.png)

### 3. Add and configure a role.
To add a custom role, you can click **Add and Configure User Role** at the bottom of the page.
![](https://main.qcloudimg.com/raw/644d41bc0ab1e7392235c4f319962946.png)

Add and configure a role, enter relevant information, and click **Save**.

![](https://main.qcloudimg.com/raw/2cd225126270b29027e49ac0b8a59acb.png)

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
