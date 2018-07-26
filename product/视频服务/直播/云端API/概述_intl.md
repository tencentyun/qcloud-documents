Cloud API is designed to help you manage LVB streams. Tencent Cloud offers two modes: LVB Code mode (new) and channel mode (old).

### LVB Code access mode
The LVB Code mode is mainly designed to facilitate the direct management of LVB streams by customers in the backend. It was only open to several well-known LVB platforms in China before May 2016, and now it has become a mainstream access solution of Tencent Cloud LVB service owing to its low access cost and high reliability. This solution is designed in such a way that the URL generation and LVB streams are basically controlled by customers, which delivers higher flexibility and customizability. It is the preferred access solution for platform LVB scenarios such as Game LVB and Live Show.
![](https://main.qcloudimg.com/raw/bd3290f6ba0bd703e48ada857bf0a973.png)

### Channel (hosting) mode
The channel mode is customized for manual management of LVB channels. It is more suitable for a single event LVB:
- **Create a channel**: Before starting an event, you can create a channel, then get the push URL, and propagate the playback URL.
- **Disable a channel**: After the LVB is finished, or when something unexpected happens, you can disable or ban the LVB channel at any time.

This mode also provides server API support, but the access cost is much higher than LVB Code mode, while the stability is lower.

### The difference between the two modes
| Item | LVB Code mode | Channel mode |
|---------|---------|---------|
| Push URL | You are free to specify it without communicating with Tencent Cloud backend | You need to generate it in Tencent Cloud backend by creating a channel first |
| Hotlink protection | Supports push and playback hotlink protection (for playback hotlink protection configuration, please contact customer service) | Supports push hotlink protection, and FLV and HLS playback hotlink protection (RTMP playback hotlink protection is not supported) |
| API list | [LVB Stream Management API](https://cloud.tencent.com/document/product/267/5956) | Suitable for manual operation. [API](https://cloud.tencent.com/document/product/267/5664) is also provided |
| Message notification | When the stream status changes, you will be notified by a message in JSON format | Not supported |
| Applicable scenario | Suitable for server interfacing, such as Live Show | Suitable for manual operation, such as an LVB event |

