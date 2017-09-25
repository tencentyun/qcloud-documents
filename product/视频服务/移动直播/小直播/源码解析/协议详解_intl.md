
Mini LVB communicates with business server using HTTP protocol. The data in request and response packages are in JSON format. API name is specified using Action, for example, Action=RequestLVBAddr. POST method is used to send a request.

## Protocol Descriptions
### 1. Request LVB push URL
This API is used to submit LVB-related data (for example, user information and LVB data such as title, position, etc.) and return push URL. After receiving the request, the business server will store the LVB-related data in database, and return the data when it receives a request for LVB list from a viewer
Request package format:

| Parameter       | Type     | Description                      |
| -------- | ------ | ----------------------- |
| Action   | string | Action of this API is RequestLVBAddr |
| userid   | string | User id                    |
| groupid  | string | Group id                    |
| title    | string | LVB title                    |
| userinfo | object | User information                    |

userinfo is defined as follows:

| Parameter         | Type     | Description   |
| ---------- | ------ | ---- |
| nickname   | string | Nickname   |
| headpic    | string | Avatar address |
| frontcover | string | Front cover address |
| location   | string | Geographical position |

Response package format:

| Parameter          | Type     | Description               |
| ----------- | ------ | ---------------- |
| returnValue | int    | Error code. 0: Successful; other values: Failed |
| returnMsg   | string | Description of error codes           |
| returnData  | object | Returned data in JSON format     |

returnData format:

| Parameter      | Type     | Description   |
| ------- | ------ | ---- |
| pushurl | string | Push URL |
| timestamp| int| Time stamp |


### 2. Modify online status
VJ starts push, and calls this API when it receives the push event (PUSH_EVT_PUSH_BEGIN), to set the push status to online. After stopping push, VJ calls this API to set the push status to offline
Request package format:

| Parameter     | Type     | Description           |
| ------ | ------ | ------------ |
| Action | string | ChangeStatus |
| userid | string | User id         |
| status | int    | 0: Online; 1: Offline    |

Response package format:

| Parameter          | Type     | Description               |
| ----------- | ------ | ---------------- |
| returnValue | int    | Error code. 0: Successful; other values: Failed |
| returnMsg   | string | Description of error codes           |
| returnData  | object | Null                |

### 3. Modify counter
This protocol is used to modify the number of likes. When a viewer gives a like, this protocol is sent to the business server to modify the like counter
Request package format:

| Parameter     | Type     | Description                 |
| ------ | ------ | ------------------ |
| Action | string | ChangeCount        |
| userid | string | User id               |
| type   | int    | 0: Modify the number of viewers; 1: Modify the number of likes (0 is deprecated. The number of viewers is modified using EnterGroup and QuitGroup protocols)  |
| optype | int    | 0: Increase; 1: Decrease          |
| flag   | int    | 0: LVB; 1: VOD          |
| fileid | string | It is used in VOD scenarios to determine which video is played |

Response package format:

| Parameter          | Type     | Description               |
| ----------- | ------ | ---------------- |
| returnValue | int    | Error code. 0: Successful; other values: Failed |
| returnMsg   | string | Description of error codes           |
| returnData  | object | Null                |

### 4. Pull the list
Pull the list from business server. Paged pull is supported
Request package format:

| Parameter       | Type     | Description                                       |
| -------- | ------ | ---------------------------------------- |
| Action   | string | FetchList                                |
| flag     | int    | 1: Pull online LVB list; 2: Pull VOD list of last 7 days; 3: Pull online LVB list and VOD list of last 7 days with LVB list followed by VOD list |
| pageno   | int    | Page number                                      |
| pagesize | int    | Page size                                     |

Response package format:

| Parameter          | Type     | Description               |
| ----------- | ------ | ---------------- |
| returnValue | int    | Error code. 0: Successful; other values: Failed |
| returnMsg   | string | Description of error codes           |
| returnData  | object | List data             |

returnData format:

| Parameter         | Type    | Description        |
| ---------- | ----- | --------- |
| totalcount | int   | Total number of lists      |
| pusherlist | array | LVB/VOD list data |

pusherlist is the array of pusherinfo which is defined as follows:

| Parameter          | Type     | Description                      |
| ----------- | ------ | ----------------------- |
| userid      | string | User id                    |
| groupid     | string | Group id                    |
| timestamp   | int    | Time stamp where push starts                |
| type        | int    | 0: LVB; 1: Recording               |
| viewercount | int    | Number of viewers                    |
| likecount   | int    | Number of likes                    |
| title       | string | LVB title                    |
| playurl     | string | Playback URL                    |
| fileid      | string | VOD file id                 |
| status| string| 0: Offline; 1: Online |
| hls_play_url| string| HLS playback URL |
| userinfo    | object | User information, which is the same as that defined in RequstLVBAddr |

### 5. Obtain signature required to upload COS files
Cloud Object Storage (COS) is a service provided by Tencent Cloud for file storage. You need to provide a signature when uploading files. Since the signature is generated using encryption key, it is not applicable to be generated locally at the client side, but by business server according to specified rules
Request package format:

| Parameter     | Type     | Description         |
| ------ | ------ | ---------- |
| Action | string | GetCOSSign |

Response package format:

| Parameter          | Type     | Description               |
| ----------- | ------ | ---------------- |
| returnValue | int    | Error code. 0: Successful; other values: Failed |
| returnMsg   | string | Description of error codes           |
| returnData  | object | Returned data in JSON format     |

returnData format:

| Parameter   | Type     | Description   |
| ---- | ------ | ---- |
| sign | string | Upload signature |

### 6. Notify business server that a member joins the group
Since the group list of imsdk cannot be customized, for example sorting by levels, it is maintained by the business server, and you can modify the sorting rules based on your demands. When a viewer joins the group, you can call this protocol to notify the business server of a new member:
Request package format:

| Parameter     | Type     | Description         |
| ------ | ------ | ---------- |
| Action | string | EnterGroup |
| userid | string | User id |
| flag | int | 0: LVB; 1: VOD |
| liveuserid | string | VJ's user id |
| groupid | string | Enter group id if flag is 0; enter fileid if flag is 1 |
| nickname | string | Nickname |
| headpic | string | Avatar address |

Response package format:

| Parameter          | Type     | Description               |
| ----------- | ------ | ---------------- |
| returnValue | int    | Error code. 0: Successful; other values: Failed |
| returnMsg   | string | Description of error codes           |
| returnData  | object | Null                |

### 7. Notify business server that a member exits the group
Since the group list of imsdk cannot be customized, for example sorting by levels, it is maintained by the business server, and you can modify the sorting rules based on your demands. When a viewer exits the group, you can call this protocol to notify the business server of the exit of a member:
Request package format:

| Parameter     | Type     | Description         |
| ------ | ------ | ---------- |
| Action | string | QuitGroup |
| userid | string | User id |
| flag | int | 0: LVB; 1: VOD |
| liveuserid | string | VJ's user id |
| groupid | string | Enter group id if flag is 0; enter fileid if flag is 1 |

Response package format:

| Parameter          | Type     | Description               |
| ----------- | ------ | ---------------- |
| returnValue | int    | Error code. 0: Successful; other values: Failed |
| returnMsg   | string | Description of error codes           |
| returnData  | object | Null                |

### 8. Pull the list of group members
Since the group list of imsdk cannot be customized, for example sorting by levels, it is maintained by the business server, and you can modify the sorting rules based on your demands. When a viewer joins an Live room, you can call this protocol to pull the list of group members, display the list of viewer profile photos, and update the total number of members on the interface.
Request package format:

| Parameter     | Type     | Description         |
| ------ | ------ | ---------- |
| Action | string | FetchGroupMemberList |
| liveuserid | string | VJ's user id |
| groupid | string | Enter group id if flag is 0; enter fileid if flag is 1 |
| pageno | int | Page number |
| pagesize | int | Page size |

Response package format:

| Parameter          | Type     | Description               |
| ----------- | ------ | ---------------- |
| returnValue | int    | Error code. 0: Successful; other values: Failed |
| returnMsg   | string | Description of error codes           |
| returnData  | object | Returned data in JSON format                |

returnData format:

| Parameter   | Type     | Description   |
| ---- | ------ | ---- |
| totalcount | int | Total number of members |
| memberlist| array| List of members |

memberlist is a list of meminfo which is defined as follows:

| Parameter          | Type     | Description                      |
| ----------- | ------ | ----------------------- |
| userid      | string | User id                    |
| nickname     | string | Nickname                  |
| headpic     | string | Avatar address                  |

### 9. Obtain details of specified VJ
Request package format:

| Parameter     | Type     | Description                |
| ------ | ------ | ----------------- |
| Action | string | GetUserInfo       |
| userid | string | User id              |
| type   | int    | 0: LVB; 1: Recording         |
| fileid | string | VOD file id, which can be ignored if type is 0 |

Response package format:
  
| Parameter          | Type     | Description                            |
| ----------- | ------ | ----------------------------- |
| returnValue | int    | Error code. 0: Successful; other values: Failed              |
| returnMsg   | string | Description of error codes                        |
| returnData  | object | Details of VJ, which is the same as pusherinfo defined in protocol 4 (pull the list) |


