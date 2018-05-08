### Adding Watermark in Channel Mode
When editing (or creating) a channel in channel mode, select the name of the watermark to be added from **Basic Settings** -> **Watermark Settings**.
![](//mc.qcloudimg.com/static/img/4c79d7bdfe5a222d8df42dbf07e5c944/image.png)
### Adding Watermark in LVB Code Mode
For push in LVB code mode, the watermark can be added by adding watermark parameters in the push URL parameter. Watermark parameters are as follows:

| Parameter Name | Description | Value | Required |
|---------|---------|---------|
| wm | Whether to enable watermark | 0: Disabled; 1: Enabled | Y |
| wmid | Watermark ID obtained after uploading the watermark | Assigned by LVB backend | Y |
| wml | Watermark position | 1: Upper left corner <br/>2: Upper right corner <br/>3: Lower right corner <br/>4: Lower left corner<br/> If it is left empty, the watermark position is determined by the settings in the watermark management | N |

For example: Add a watermark with the ID of 14049, then the push URL is `rtmp://8888.livepush.myqcloud.com/live/8888_test?bizid=8888&txSecret=xxxxxxxxxxxxxxxxxxxxxxxxxxxxc&txTime=5A0C647F&**wm=1&wmid=14049&wml=1**`.



