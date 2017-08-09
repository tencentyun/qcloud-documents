

# Play Background Music Using a Third-Party App

Scenario: A VJ who is playing the background music using a third-party music App wants the viewers to listen to the music with him or her.
## iOS

Only HQ (High Quality) configuration needs to be enabled at **VJ end**. No change is needed for the configurations of viewers, including those who join the broadcasting.

```
//Enable the HQ configuration when joining a room.
ILiveRoomOption *option = [ILiveRoomOption defaultHostLiveOption];
option.avOption.autoHdAudio = YES;
```

## Android
Android supports this feature without the need of configuration.

**Notes**
> * The music App should be opened to play background music only after you join the room. Otherwise the background music will be interrupted by the room.
> * For the VJ and the viewers who join the broadcasting, aec (acoustic echo cancellation) of the background spear configuration needs to be enabled.



