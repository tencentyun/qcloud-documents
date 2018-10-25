
### Does iOS SDK use hot patching or private APIs?
XGPush SDK does not use hot patching or private APIs, so the Apple review will not be affected.

### Is the push volume/frequency limited?
No limit is set to push volume. As for push frequency, only full broadcast frequency is limited as once every 3 seconds, and other push actions are not limited.

### How many offline messages can be saved for a single device? How long will it be saved?
A maximum of 2 offline Messages can be saved for Android, and 1 for iOS, for 72 hours at most.

### Is there a tag limit?
A maximum of 100 tags can be set for a single device, and a single App can own a maximum of 10,000 different tags globally.

### Does XGPush share the same APP ID data with Tencent open platform?
When you register your App on the open platform and use XGPush, messages of the App are automatically synchronized from the open platform to XGPush platform, and you do not need to re-access the App when using only XGPush. However, the App accessed in XGPush will not be synchronized to the open platform.

### After the first successful registration, if I do not unregister, do I need to register for future use?
No, as long as you do not unregister, you do not need to register again

### Can the App receive push messages after the process is closed or ended?
XGPush sends and receives messages mainly relying on XGPush service which will be terminated after the process is closed. The App cannot receive pushes until the service is activated or the App is restarted. If any other App accessing XGPush are opened on the phone, you can use its service to receive messages. But the service channel sharing is limited by mobile ROM, so a success rate of 100% cannot be guaranteed.

### Why can't I receive the callback message when registering a device?
In the registration process, only three errors may occur at the backend:
1) No response;
2) Return a data packet in wrong format;
3) Return an error code. The terminal can detect all the three behaviors, and return a callback.

### For a successful push, why the arrival is counted while the number of click is 0?
For iOS, special codes need to be called for click statistics. For more information, please see the iOS development documentation.

### Why there is only voice but no text message in a push notification?
This mainly depends on the system. And the logcat of device is required for specific analysis.

### What is the difference between token and Account?
Token is the identifier of a device, while account is the identifier of a user. A token can only be bound with one account. If multiple accounts are bound, only the last one can be bound successfully.

### If an account logged in on both device A and B, what will happen when pushing a message to this account?
As long as the account is not logged out, both devices will receive the message.

### What is the difference between tag and account?
A tag is used to identify a token or some attributes of the user, such as Guangdong Province, male, game player. An account is the user's account. Do not use the tag as an alias.

### What does "Number of covered devices" in the App list mean?
It refers to the number of devices/terminals that are registered in the App, and also the maximum number of devices that the App can cover for pushing. If the terminal calls the unregister API, the number of covered devices will decrease.

### Why the server is busy when I push on the Web?
Check whether the token and the selected push environment are correct, and then check whether the certificate is submitted correctly. If the error persists, you can recreate a certificate without a password, and then submit it.

### In the push process, can non-scheduled push (immediate push) be undone?
No, only tasks that return push_id can be undone.

### Though a push is completed, its status in the push list is "pushing". Why?
Refresh and try again.

### How to push messages to a single user?
Refer to the development manual for guidance on "Push messages to a single device" and "Push messages to a single account or alias".

### What is the order in which users receive multiple pushes after reconnecting?
Pushes are received in ascending order based on message ID. The client also receives messages according to this rule. Therefore, the order of receiving messages depends on the order of sending messages.

### I have Android and iOS users. Then do I need to write two different APIs at php backend for pushes to Android users and iOS users?**
You need to call the push API twice, or package the two APIs as one.

### If a past time is selected for a scheduled push, will the push fail?
No, the system will push the message immediately if a past time is selected.


