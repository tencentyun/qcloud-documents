## 1. Working with Rooms
### 1.1 Overview
**Differences between the service-end rooms and audio/video SDK-end rooms:**
Service-end rooms are maintained by the client and have a uniqueness. For example, the client can maintain by itself the room numbers, discussion group numbers, group numbers, game seat numbers, etc.
Audio/video SDK-end rooms are maintained by the audio/video SDK end and also have a uniqueness. Such a room is dynamically assigned each time a user joins the room.
You need to enter the service-end room number when joining an audio/video SDK-end room to establish a mapping between the both rooms.
In addition, the numbers of audio/video SDK-end rooms are visible to the client, so you don't need to care about them.

**Maximum number of room members:**
A maximum of 100,000 viewers are allowed at a time in a single room.

### 1.2 Create a room
Supported systems: Windows/iOS/Android
Note: Before the first member of a room joins the room, the room is automatically created at the audio/video backend. When subsequent members join the room, the creation process is eliminated.

### 1.3 Join a room
Supported systems: Windows/iOS/Android

### 1.4 Exit a Room
Supported systems: Windows/iOS/Android

### 1.5 Terminate a room
Supported systems: Windows/iOS/Android
Note: When the last member has exited the room, the room is terminated automatically at audio/video backend.

### 1.6 Obtain the list of members sending voice/video
Supported systems: Windows/iOS/Android

### 1.7 Obtain the member list of all rooms

## 2. Event Notification
### 2.1 Event notification of you joining the room
Supported systems: Windows/iOS/Android

### 2.2 Event notifications of others joining the room
Supported systems: Windows/iOS/Android
Note:
On the DC, only if the number of room members is not more than 50 is the event notification supported; if the number of members exceeds 50, only the event notifications of the first 50 members joining the room are issued.
On the OC, only the notifications of VJ and special users joining the room are issued.

### 2.3 Event notification of you exiting the room
Supported systems: Windows/iOS/Android

### 2.4 Event notifications of others exiting the room
Supported systems: Windows/iOS/Android
Note:
On DC, only if the number of room members is not more than 50 is the event notification supported; if the number of members exceeds 50, only the event notifications of the first 50 members exiting the room are issued.
On OC, only the notifications of VJ and special users exiting the room are issued.

### 2.5 Event notification of status change about whether a member has sent a voice/video
Supported systems: Windows/iOS/Android
Note:
On the DC, the notification is issued whenever a status change occurs.
On the OC, the notification is only issued when a status change of VJ or special users occurs.









