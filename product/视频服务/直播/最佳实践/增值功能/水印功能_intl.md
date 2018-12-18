**To use the watermark feature, you need to upload a watermark image, and then add the watermark.**
## 1. Upload a Watermark
Add a watermark under the **Global Settings** -> **Watermark Management** on the console.
![](https://mc.qcloudimg.com/static/img/ae32975c9da664be4ee635e02e351e84/1222.png)

After the watermark is added successfully, you will obtain its watermark ID and name. Create a watermark with the ID of 13961 and the name of "test", as shown below.
![](https://mc.qcloudimg.com/static/img/579ec4c7b43837d95a909d9a2007cf44/1.png)

## 2. Add a Watermark

### 2.1 Add a watermark in channel mode
When editing (or creating) a channel in channel mode, select the name of the watermark to be added from **Basic Settings** -> **Watermark Settings**.
![](https://mc.qcloudimg.com/static/img/579ec4c7b43837d95a909d9a2007cf44/1.png)

### 2.2 Add a watermark in LVB code mode
For push in LVB code mode, watermarks can be added by adding watermark parameters in the push URL parameter.
The watermark parameters are as follows:

| Parameter Name | Description | Value | Required |
|---------|---------|---------|
| wm | Whether to enable watermark | 0: Disabled; 1: Enabled | Y |
| wmid | Watermark ID obtained after a watermark is uploaded | Assigned by the LVB backend | Y |
| wml | Watermark position | 1: Upper left corner<br/>2: Upper right corner<br/>3: Lower right corner<br/>4: Lower left corner<br/>If it is left empty, the watermark position is determined by Settings in the Watermark Management. | N |

For example:
Add a watermark with the ID of 13961.
The push URL is:

rtmp://8888.livepush.myqcloud.com/live/8888_test?bizid=8888&txSecret=xxxxxxxxxxxxxxxxxxxxxxxxxxxxc&txTime=5A0C647F&**wm=1&wmid=13961&wml=1**



