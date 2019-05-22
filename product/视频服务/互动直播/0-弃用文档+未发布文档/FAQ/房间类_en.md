#### Error 561 is reported for a room.  
Parameter userPhone should be a number for joining a room.
	
#### Error 10001 is reported for a room.  
Possible reasons:  
(1) startcontext of avskd is called even after a login failure.  
(2) startcontext of avskd is called during login.  
(3) startcontext of avskd is called after logout.
		
#### After a failure to join a room, error 1002 is reported for an attempt to join another room.  
You need to release the context to join another room.
	
#### What should be done in case of a network disconnection during a call to exitRoom?  
Deal with it in the same way as with network disconnection at client.

#### The option to automatically create a room when joining a room that does not exist.
![Automatically Create a Room](//mccdn.qcloud.com/static/img/f8f70026eae76d3b6415a8ea3c051932/image.jpg)

#### Rendering VJ's local view with beauty filter in SDK1.7(+) version

![Local Rendering with Beauty Filter](//mccdn.qcloud.com/static/img/c0ff897cac4a9a42ef452626e7404a61/image.png)
