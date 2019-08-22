## 1. Key Concepts
- DC (Data Center): Core node accessed by the user roles who need to send upstream audio/video data or need real-time interactions in ILVB business (such as VJ, lecturer, or roles participating in real-time interaction).
- OC (Outer Center): Outer nodes accessed by the user roles who need not to send upstream audio/video data and only need to receive such data (such as ordinary viewers and students who need not to interact with their teachers).

The two features are priced differently. For more information, please see (https://cloud.tencent.com/doc/product/268/5128#2..E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C.E8.B4.B9.E7.94.A8.E8.AE.A1.E7.AE.97.E5.85.AC.E5.BC.8F).

## 2. Assignment to DC and OC
When to access DC or OC for the terminal instance of an App? To put it simply: An instance with permission to send upstream audio/video data is assigned to DC, while an instance without such permission is assigned to OC. Specifically, when you call the SDK API EnterRoom() for joining a room, its parameters EnterRoomParam.auth_bits and 
EnterRoomParam.auth_buffer set the permissions of this instance in the room, as shown below:

![User Permission Bit Description](//mccdn.qcloud.com/img56cdd6a958dff.png)

EnterRoomParam.auth_bits is the plaintext form of the permission bit, and EnterRoomParam.auth_buffer is the ciphertext form of the permission bit. You can only use the plaintext form of the permission bit. Once the encryption keys have been enabled after application, the cipertext of permission bit is required, and the background will verify whether the contents of plaintext correspond to the contents of ciphertext as well as the validity of cipertext. The logic background of business also needs to timely update the cipertext in App to avoid expiration. Please note that the cipertext form is not available for public use currently due to few application scenarios, so try to use the plaintext form.

The instance is assigned to DC if EnterRoomParam.auth_bits/EnterRoomParam.auth_buffer sets any of AUTH_BITS_SEND_AUDIO/AUTH_BITS_SEND_VEDIO/AUTH_BITS_SEND_SUB to 1; otherwise, the instance is assigned to OC.

PS: At background, an upper limit is imposed on the number of users accessing DC in a single room. For example, if every user in a business is granted the permission to send upstream data, then at background, the first 1000 users in each room is assigned to DC and the remaining ones to OC. This restriction is a background protection policy, which can be adjusted as needed.

## 3. Switching Between DC and OC
When a user is assigned to DC/OC through the EnterRoom process (for joining a room), he or she may need to switch between DC and OC occasionally. For example, in an education scenario, a student who has no permission to send upstream data and is assigned to OC needs to switch from OC (which does not allow sending upstream audio/video data) to DC when selected by a teacher to answer a question. The switching between DC and OC is also based on changes of permissions, with the relevant API being tencent::av::AVRoomMuti::ChangeAuthority(string auth_buffer). Where auth_buffer is the ciphertext form of the permission bit (currently not enabled). This involves the following several cases:
- To revoke the permission of a user assigned to DC (set AUTH_BITS_SEND_AUDIO/AUTH_BITS_SEND_VEDIO/AUTH_BITS_SEND_SUB to 0)
In this case, a redirection instruction is issued at the audio/video background to redirect the terminal instance to OC. A typical scenario is: A teacher asks a student to answer a question. After that, the student's permission for sending upstream audio/video is revoked and the student is redirected to OC (the redirection is transparent to the App and the user, and the switching is usually very fast)

	![Figure showing a switching caused by permission revocation](//mccdn.qcloud.com/img56cdd763b0628.png)

- To grant permission to a user assigned to DC: no such case exists
- To revoke the permission of a user assigned to OC: SDK does not perform any action
- To grant permission to a user assigned to OC (set one of AUTH_BITS_SEND_AUDIO/AUTH_BITS_SEND_VEDIO/AUTH_BITS_SEND_SUB to a non-zero value). In this case, a redirection instruction is issued at the audio/video background to redirect the terminal instance to DC

	![Figure showing a switching caused by permission granting](//mccdn.qcloud.com/img56cdd789c7ee8.png)

