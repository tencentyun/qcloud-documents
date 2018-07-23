Log in to [Tencent Cloud Console](https://console.cloud.tencent.com/). Choose **Cloud Products** -> **Video Services** -> **LVB** to enter LVB management page. On this page, you can view the information of your current LVB channels, including LVB name, ID, status, creation time and operations. You can search for LVB by name/ID, and start, close or delete LVB channels in batches. After an LVB channel is created, it is displayed in the list. The relevant status is as follows:
- No input stream: The current LVB channel has started, but no input stream is found. The LVB channel can be closed or tested under this status.
- During LVB: The current LVB channel has started, and an input stream is found. The LVB channel can be closed or tested under this status.
- Closed: The current LVB channel is closed. The system does not receive the input stream nor distribute the output stream.

![](https://main.qcloudimg.com/raw/d518d9afe855e4af752937ab7c74561c.png)

**View and modify LVB channel settings**
When an LVB channel is closed, you can click on its name to check the LVB configuration and output address, or modify the configuration of the LVB channel.
LVB configurations are shown as follows. You can make modifications by clicking the Edit button next to Settings.

![](https://main.qcloudimg.com/raw/5bff1f46b16b979d78b870fbfa0772f6.png)

>**Note:**
> The configurations of an LVB channel can be modified only when it is closed.

**View and edit the player code for LVB publishing**
You can view the player code for LVB publishing, so as to easily integrate the LVB display capability with Web Apps. This code supports playback on PC and in mobile device.

![](https://main.qcloudimg.com/raw/a9ddabe014401eaae9909607ed710104.png)

Click **Edit** to modify the following code, and the updated player code shows after you save the edited content.
**Player size:** The size of the player border. Commonly used size and custom size are supported.
**Player password:** Basic security features are provided. You can set an 8-digit (case-sensitive) numeric password. Viewers need to enter the correct password to watch LVB.
>**Note:**
This feature does not take effect if viewers do not use the player.

![](https://main.qcloudimg.com/raw/2f3e0a1c4acf4ba632875a239ee7ac47.png)
