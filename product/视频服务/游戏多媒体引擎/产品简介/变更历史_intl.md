## GME_SDK2.2 2018-10-29

### New features:
1. Supports a variety of karaoke sound effects.
2. Optimizes the user experience in super-large rooms with lower latency and higher fluency.
3. Supports streaming voice-to-text converting for voice message.
4. Supports accompaniment on Windows.

### Optimizations
1. Optimizes voice bandwidth, saving your traffic.
2. Optimizes CPU and memory performance.

## GME_SDK2.1.5 2018-09-13

### API Changes:

1. Changes the type of parameter roomId in GenAuthBuffer from int32 to string.
2. Changes the type of parameter roomId in EnterRoom from int32 to string.
3. Changes the function of SetMicVolume from setting the microphone device volume to setting the microphone software volume.
4. Changes the function of GetMicVolume from getting the microphone device volume to getting the microphone software volume.

### Optimizations:

1. Upgrades the type of room number from int32 to string.
2. Changes the functions of the APIs for setting/getting device volume to setting/getting software volume.
3. Fixes bugs to improve stability.


## GME_SDK2.1 2018-08-21

### New features:

1. Supports voice changing on Windows.
2. Supports voice message on Windows.
3. Supports 3D sound effect on Windows.
4. Supports x86 architecture in Android SDK.
5. iOS and Mac SDKs are adapted to XCode10.

### Optimizations:

1. Optimizes authentication for voice message.
2. Supports turning on/off audio input and output devices separately on mobile devices.
3. Optimizes the standard sound quality's immunity to bad network condition.

## GME_SDK2.0 2018-06-22

### New features:

1. PC Native and PC Unity versions of GME are made available.
2. GME supports Unreal engine.
3. Offline voice-to-text converting is supported in up to 120 languages in GME.
4. GME supports 3D voice chat on PC.

### Optimizations:

1. Improves the sound quality of voice chats.
2. Lowers the bar for integration, and provides multiple sound quality options - Fluent, Standard, and HD.
3. Improves stability.

## GME_SDK1.2    2018-04-02

### New features

1. GME supports Cocos engine.
2. Provides the API for adjusting microphone volume.
3. Supports team chatting on mobile devices to better support battle royale games.
4. Supports accompaniment playback in various formats on PC.
5. Supports accompaniment playback in various formats on Android devices.

### Optimizations

1. Optimizes the audio pre-processing effect for Werewolf scenarios to deliver a more clear sound quality in multi-person chatting.
2. Optimizes the sound quality in online Karaoke and other scenarios and supports configuring higher sound quality.
3. Reduces the voice delay in Moba scenarios to achieve lower delay in team chatting.
4. Optimizes the noise cancellation algorithm to deliver a more clear sound.

## GME_SDK1.1    2017-10-18

### New features

1. Game SDK supports accompaniments and sound effects in various formats.
2. Adds voice message and voice-to-text converting in game scenarios.

### Optimizations

1. Provides the module for authentication of user entering room on client and lowers the bar for integrating SDK.
2. Optimizes the howling suppressing effect on iOS/Android.
3. Optimizes the sound quality consistency, immunity to bad network condition and other metrics in Werewolf scenario.

### Fixes

Fixes the system crash issue on Android 4.2 and below.






