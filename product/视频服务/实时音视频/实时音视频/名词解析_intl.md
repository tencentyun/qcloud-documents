### Project
A project is created by a developer in the TRTC console to be distinguished from other development projects.
You can create more than one TRTC projects under a single Tencent Cloud account.
### sdkAppId
SDKAppId is used to uniquely identify a project at Tencent Cloud backend, and is automatically generated after the TRTC service is activated on the TRTC console and a TRTC project is created.
### accountType
AccountType is the account type used to log in to a TRTC project and is automatically assigned for user authentication after the creation of the TRTC project.
### userId
UserId is used to uniquely identify a user in a TRTC project.
It represents the mapping of the user's account ID for logging in to developer system to the Tencent Cloud. A developer usually uses the user name as UserId directly.
The recommended length is not more than 32 bytes. It should be a combination of numbers, letters, and underscores (case insensitive).
### userSig
UserSig is used to authenticate a user to verify whether the user identity is true.
### Room
A room represents a space for users to interact with each other. A user can watch the real-time videos of any other users in the same room. Each room is identified by a room ID. This means that the rooms with the same room ID in the same TRTC project can be considered as a single room.
In TRTC, room is a virtual concept used to separate a group of users from another.
Room ID is maintained and assigned by the developer, with a value ranging from 1 to 10000000.
A user's video is only accessible to the other users in the same room.
A user can only enter one room at a time. To enter another room, a user must exit the current room or call the API used for switching room.
Note:
The room creator is the room owner, but cannot delete the room.
A room is deleted automatically 30 seconds after all members exit the room.
When a user wants to enter a room that does not exist, the TRTC backend creates the room first, and then adds the user to the room.
### privateMapKey
PrivateMapKey is the key for entering the specified room (roomId) and is issued by the business server.
### Role
A role in TRTC represents a fixed set of audio/video parameter configurations, including resolution, capture frame rate, etc. You can create and configure a role in the TRTC console.
### Role Name
After creating a set of parameter configurations for the specified terminal platform in the TRTC console, you can set a name for the set of configurations, which is the role name.
To send upstream audio/video data from camera/microphone in a room, a user can specify the role name when entering the room to set the parameters for sending upstream data.
Note:
When entering a room, if a user uses a role name that has not been configured in the console, he/she can still enter the room with the default role.
After entering the room, the user can change the role by calling the API used for switching role.
Switching to a non-existent role using the API will cause a failure callback.
After the role configuration is modified, logging in to the client again is required to make the new configuration take effect (the SDK will fetch the configuration from the backend when login is successful. The failure to fetch the configuration can cause the failure to find the role).
### Group
Group system is essentially an IM system that supports multi-user chat, and a group is a space where multiple users can chat with each other. Tencent Cloud supports five types of groups: private group, public group, chat room, TRTC chat room, and broadcasting group.
Note:
Group and room are two completely different concepts that should not be confused with each other.

| Type       | Name             | Maximum Number of Members | When to Reclaim  | Scenarios                                                     |
| ---------- | ---------------- | ---------------- | -------- | ------------------------------------------------------------ |
| Private    | Private group           | 200            | 30 days    | Suitable for more private chat scenarios, where the group information is not made public and a user can join the group only by being invited by a group member. |
| Public     | Public group           | 2000           | N/A       | Suitable for public chat scenarios and has a strict management and admission mechanism.             |
| ChatRoom   | Chat room           | 10000          | N/A       | Has a less stringent management mechanism and allows room members to join and exit the room freely.                             |
| AVChatRoom | TRTC chat room | Unlimited           | N/A       | Suitable for TRTC scenarios. Similar to an ordinary chat room, it allows room members to join and exit a room freely, but does not impose a limit on the number of room members. It supports receiving messages as a guest (non-logged in user). |
| BChatRoom  |Broadcasting group | Unlimited            | N/A        | Suitable for the scenarios where messages need to be pushed to all the online members.                       |
### Message
A message is a discrete unit of communication sent from the source to some recipient or group of recipients. Messages in the iLiveSDK are described by the ILiveMessage class, and are divided into text, custom, and other messages.
## Email
If you have any questions, contact us by emailing to trtcfb@qq.com.

