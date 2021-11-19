
`TUIKit` 默认实现了文本、图片、语音、视频、文件等基本消息类型的发送和展示，如果这些消息类型满足不了您的需求，您可以新增自定义消息类型。

## 基本消息类型
<table>
     <tr>
         <th width="20%" style="text-align:center">消息类型</th>  
         <th style="text-align:center">显示效果图</th>  
     </tr>
     <tr>      
         <td style="text-align:center">文本类消息</td>   
     <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/6535b0a414d4dd51aabab464f0980ca3.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">图片类消息</td>   
     <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/1f5330a92c688b6288bbd47f97202867.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">语音类消息</td>   
     <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/5387ea2450e7fe37daa59efb163e93b6.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">视频类消息</td>   
     <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/eb50c8cefa0decf1eef1c896c44e6188.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">文件类消息</td>   
     <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/4be73ac319f7693916ee08b98f14c4c6.png" width="320"/></td>   
     </tr> 
</table>

## 自定义消息
>- 如果基本消息类型不能满足您的需求，您可以根据实际业务需求自定义消息。
>- 本文以发送一条可跳转至浏览器的超文本作为自定义消息为例，帮助您快速了解实现流程。**本文以 `5.7.1435` 版本为例，与之前版本有所不同。**

 <img src="https://main.qcloudimg.com/raw/77082a09b210baae30e41ce35e07af6b.png" width = "500"/>

上图自定义消息类型可以实现点击后跳转到指定链接地址，具体实现请参考后文。

## 实现自定义消息
自定义消息的实现大致需要以下几步：

### 步骤1: 实现自定义 cellData 类
新建  [TUILinkCellData](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/Cell/CellData/Custom/TUILinkCellData.h) 类，继承自`TUIMessageCellData` ，用于存储显示的文字和跳转的链接。

```java
@interface TUILinkCellData : TUIMessageCellData
@property NSString *text;
@property NSString *link;
@end
```

计算 `TUILinkCellData` 内容显示的大小 `contentSize`，以便 `TUIMessageController` 预留足够的位置显示此类消息。

```java
@implementation TUILinkCellData
- (CGSize)contentSize
{
    CGRect rect = [self.text boundingRectWithSize:CGSizeMake(300, MAXFLOAT) options:NSStringDrawingUsesLineFragmentOrigin | NSStringDrawingUsesFontLeading attributes:@{ NSFontAttributeName : [UIFont systemFontOfSize:15] } context:nil];
    CGSize size = CGSizeMake(ceilf(rect.size.width)+1, ceilf(rect.size.height));
    // 加上气泡边距
    size.height += 60;
    size.width += 20;
    return size;
}
@end
```

### 步骤2: 实现自定义 cell 类

新建 [TUILinkCell](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/Cell/CellUI/Custom/TUILinkCell.h) 类，继承自 `TUIMessageCell` ，用于绘制 `TUILinkCellData` 数据。

```java
@interface TUILinkCell : TUIMessageCell
@property UILabel *myTextLabel;  // 展示文本
@property UILabel *myLinkLabel;  // 链接跳转文本
- (void)fillWithData:(TUILinkCellData *)data; // 绘制
@end
```

在实现文件中，您需要创建 `myTextLabel` 和 `myLinkLabel` 对象，并添加至 `container` 容器。

```java
@implementation TUILinkCell
// 初始化控件
- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier
{
    self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];
    if (self) {
        self.myTextLabel = [[UILabel alloc] init];
        [self.container addSubview:self.myTextLabel];
        self.myLinkLabel = [[UILabel alloc] init];
        self.myLinkLabel.text = @"查看详情>>";
        [self.container addSubview:_myLinkLabel];
    }
    return self;
}
// 根据 cellData 绘制 cell
- (void)fillWithData:(TUILinkCellData *)data;
{
    [super fillWithData:data];
    self.myTextLabel.text = data.text;
}
// 设置控件坐标
- (void)layoutSubviews
{
    [super layoutSubviews];
    self.myTextLabel.frame = xxx;
    self.myLinkLabel.frame = xxx;
}
@end
```

### 步骤3: 消息列表获取自定义消息展示数据

消息列表在收到 `V2TIMMessage` 消息的时候，可以通过 [TUIMessageDataProvider](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/DataProvider/TUIMessageDataProvider.m) 的 `getCellData` 函数把 `V2TIMMessage` 转换成 UI 上可绘制的数据 `TUIMessageCellData`。

```java
@implementation TUIMessageDataProvider
+ (TUIMessageCellData *)getCellData:(V2TIMMessage *)message {
    TUIMessageCellData *data = nil;
    if (message.elemType == V2TIM_ELEM_TYPE_CUSTOM) {
        // 判断是不是自定义跳转消息
        if (!data) {
            data = [self getLinkCellData:message];
        }
    }
    return data;
}
@end

@implementation TUIMessageDataProvider (Link)
+ (TUIMessageCellData *)getLinkCellData:(V2TIMMessage *)message {
    if (message.elemType == V2TIM_ELEM_TYPE_CUSTOM) {
        NSDictionary *param = [NSJSONSerialization JSONObjectWithData:message.customElem.data options:NSJSONReadingAllowFragments error:nil];
        if (!param || ![param isKindOfClass:[NSDictionary class]]) {
            return nil;
        }
        NSString *businessID = param[@"businessID"];
        if (![businessID isKindOfClass:[NSString class]]) {
            return nil;
        }
        // 判断是不是自定义跳转消息
        if ([businessID isEqualToString:TextLink] || ([(NSString *)param[@"text"] length] > 0 && [(NSString *)param[@"link"] length] > 0)) {
            TUILinkCellData *cellData = [[TUILinkCellData alloc] initWithDirection:message.isSelf ? MsgDirectionOutgoing : MsgDirectionIncoming];
            cellData.innerMessage = message;
            cellData.msgID = message.msgID;
            cellData.text = param[@"text"];
            cellData.link = param[@"link"];
            cellData.avatarUrl = [NSURL URLWithString:message.faceURL];
            cellData.reuseId = TLinkMessageCell_ReuseId;
            return cellData;
        }
    }
    return nil;
}
@end
```

### 步骤4: 消息列表展示自定义消息

消息列表在绘制的时候，可以在 [TUIMessageController](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/UI/Chat/TUIMessageController.m) 的 `cellForRowAtIndexPath` 函数内判断是否为自定义消息，如果是的话创建 `TUILinkCell` 并且绘制 `TUILinkCellData` 数据。

```java
@implementation TUIMessageController
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    TUIMessageCell *cell = nil;
    TUIMessageCellData *data = self.messageDataProvider.uiMsgs[indexPath.row];
    // 判断是不是自定义跳转消息
    if (!cell) {
        cell = [TUIMessageDataProvider getLinkCellWithCellData:data];
    }
    return cell;
}
@end

@implementation TUIMessageDataProvider (Link)
+ (TUIMessageCell *)getLinkCellWithCellData:(TUIMessageCellData *)cellData {
    if ([cellData isKindOfClass:[TUILinkCellData class]]) {
        TUILinkCell *linkCell = [[TUILinkCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:TLinkMessageCell_ReuseId];
        [linkCell fillWithData:(TUILinkCellData *)cellData];
        return linkCell;
    }
    return nil;
}
@end
```

### 步骤5: 会话列表展示自定义消息
 <img src="https://main.qcloudimg.com/raw/428e6fab209b3cf9aae25ad504c0c4a3.jpg" width = "500" />

如果会话列表的  `lastMsg` 是您的自定义消息，您可以在 [TUIMessageDataProvider](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/DataProvider/TUIMessageDataProvider.m) 的 `getDisplayString` 函数内自定义 `lastMsg` 的展示信息。

```java
@implementation TUIMessageDataProvider
+ (NSString *)getDisplayString:(V2TIMMessage *)msg
{
    NSString *str = nil;
    switch (msg.elemType) {
        case V2TIM_ELEM_TYPE_CUSTOM:
        {
            // 判断是不是自定义跳转消息
            if (!str) {
                str = [TUIMessageDataProvider getLinkDisplayString:msg];
            }
        }
        break;
    }
    return str;
}
@end

@implementation TUIMessageDataProvider (Link)
+ (NSString *)getLinkDisplayString:(V2TIMMessage *)message {
    if (message.elemType == V2TIM_ELEM_TYPE_CUSTOM) {
        NSDictionary *param = [NSJSONSerialization JSONObjectWithData:message.customElem.data options:NSJSONReadingAllowFragments error:nil];
        if (!param || ![param isKindOfClass:[NSDictionary class]]) {
            return nil;
        }
        NSString *businessID = param[@"businessID"];
        // 判断是不是自定义跳转消息
        if ([businessID isEqualToString:@"text_link"]) {
            return @"欢迎加入即时通信 IM 大家庭！";
        }
    }
    return nil;
}
@end
```

## 发送自定义消息

您可以在 [TUIInputController](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/UI/Input/TUIInputController.m) 的输入栏里面注册自定义消息的发送按钮，当按钮被点击后发送自定义消息，详细步骤如下：
 <img src="https://main.qcloudimg.com/raw/80ff0af0e44bde79d099cd5296b3136f.jpg" width = "500"/>
 
### 步骤1: 注册自定义消息发送按钮
您可以在 [TUIChatDataProvider](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/DataProvider/TUIChatDataProvider.m) 的 `moreMenuCellDataArray` 函数里注册自定义消息发送按钮：

```java
+ (NSMutableArray<TUIInputMoreCellData *> *)moreMenuCellDataArray:(NSString *)groupID
                                                           userID:(NSString *)userID
                                                  isNeedVideoCall:(BOOL)isNeedVideoCall
                                                  isNeedAudioCall:(BOOL)isNeedAudioCall
                                                  isNeedGroupLive:(BOOL)isNeedGroupLive
                                                       isNeedLink:(BOOL)isNeedLink {
    NSMutableArray *moreMenus = [NSMutableArray array];
    TUIInputMoreCellData *linkMenusData = [TUIInputMoreCellData new];
    linkMenusData.key   = TUIInputMoreCellKey_Link; // 按钮的唯一标识
    linkMenusData.title = @"自定义";
    linkMenusData.image = [UIImage imageNamed:@"more_link"];
    [moreMenus addObject:linkMenusData];
    return moreMenus;
}
```

### 步骤2: 响应自定义消息发送按钮点击事件

单聊可以在 [TUIC2CChatViewController](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/UI/Chat/TUIC2CChatViewController.m) 的 `didSelectMoreCell` 函数中处理按钮点击事件，群聊可以在 [TUIGroupChatViewController ](https://github.com/tencentyun/TIMSDK/blob/master/iOS/TUIKit/TUIChat/UI/Chat/TUIGroupChatViewController.m) 的 `didSelectMoreCell` 函数中处理按钮点击事件。

```java
- (void)inputController:(TUIInputController *)inputController didSelectMoreCell:(TUIInputMoreCell *)cell
{
    // 判断是否为自定义消息按钮的点击事件
    if([cell.data.key isEqualToString:TUIInputMoreCellKey_Link) {  
        NSString *text = @"欢迎加入即时通信 IM 大家庭！";
        NSString *link = @"https://cloud.tencent.com/document/product/269/3794";
        TUILinkCellData *cellData = [[TUILinkCellData alloc] initWithDirection:MsgDirectionOutgoing];
        cellData.text = text;
        cellData.link = link;
        NSData *data = [NSJSONSerialization dataWithJSONObject:@{@"businessID": @"text_link",@"text":text,@"link":link} options:0 error:&error];
        cellData.innerMessage = [[V2TIMManager sharedInstance] createCustomMessage:data];
        //发送自定义消息
        [self sendMessage:cellData];
    }
}
```
