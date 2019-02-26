### Does iOS support offline messages saving?
By default, Apple supports saving one message offline. No statement on the duration of messages saved offline is provided in Apple's official documentation.

### Why does the actual volume of full push fluctuate every day? 
XGPush backend clears the invalid, expired Token based on the error returned by APNS during the daily push. This cleanup is performed once a day. The actual volume of full push on the next day may be less than that of the previous day as the expired Tokens of the previous day has been removed, which is normal.

### When initializing XGPush API, the following log appears: 2017-10-26 15:13:38.888951+0800 XG-Demo [2295:1737660] [xgpush]  Server error code: 20 
Do not use macro definitions for appid and appkey in the method for initializing XGPush.

### When will push suspension occur?
A maximum of 30 full pushes can be created per hour, and pushes exceeding the limit will be suspended. Pushes with the same content created within one hour will be suspended. Suspended tasks will not be delivered. Please recreate the push as appropriate.

### Failed to upload the certificate to the console
#### For failed verification, refresh and try again
Open the certificate file using the editor, and find the friendlyname field. If it is found in the same line, change it to something else, then save and upload it again.

#### The push parameter is not included
Generate a new push certificate

#### File size is 0 Kb, so the file cannot be uploaded
Transform the pem format again by following XGPush Certificate Production Tutorial: [https://v.qq.com/x/page/u0302fjna1h.html]().

### Error "Error Domain=NSCocoaErrorDomain Code=3000" Authorization string for "aps-environment" of application not found" UserInfo=0x16545fc0 {NSLocalizedDescription=Authorization string for "aps-environment" of application not found}" appears on the terminal
This is caused by the App certificate without push permissions. Reconfigure the certificate.

### The device does not go to callback after receiving the message.
For iOS 10, it goes to the callback method of silent notification.

### The following error occurs when I set/delete a tag: exception.name= WupSerializableException exception.reason= -[XGJceOutputStream writeAnything:tag:required:], 349: assert(0) fail!
Perform setTag/delTag after registerDevice is performed. This error will occur when operating tag before registerDevice.

### Mapping relationship between Token and alias (account)
One device corresponds to one token. The token is issued by Apple when you register a device for push. A token can be bound with one account at most, and a maximum of 15 tokens can be bound with an account. When the limit is exceeded, the latest token replaces a previously bound token. iOS tokens change as you perform uninstallation, reinstallation, iOS upgrading, and resetting.

### Although a push is created successfully, there is no record of this push in the push list.
The push list only displays the records of pushes to all devices and bulk devices.

### How to play a custom notification tone?
Put the audio file under the bundle directory. When creating a push, pass the name of the audio file to the sound field.

### How to create a silent push using XGPush Server SDK?
Set the content-available parameter to be 1, and do not use setalert.

