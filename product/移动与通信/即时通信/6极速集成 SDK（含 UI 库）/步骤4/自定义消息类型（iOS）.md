在 TUIChatController 中，每一条消息在内部都是存储为 TUIMessageCellData 或子类对象，当滑动消息列表时，再将 TUIMessageCellData 转换为 TUIMessageCell 用于显示。
您可以通过设置 TUIChatController 回调 delegate，控制具体的 TUIMessageCell 实例，从而达到定制消息的目的。
![](https://main.qcloudimg.com/raw/77082a09b210baae30e41ce35e07af6b.png)
以上图红色线框中的超链接自定义消息为例，TUIKit 内部没有实现此类效果，您只需在 TUIMessageCell 的 container 里添加两个 UILabel ，即可快速实现显示效果。本文将详细介绍实现过程：

## 自定义消息
### 步骤1: 实现一个自定义 cellData 类
自定义一个继承自`TUIMessageCellData`的`cellData`类，用于存储显示的文字和链接。

```objectivec
@inerface MyCustomCellData : TUIMessageCellData
@property NSString *text;
@property NSString *link;
@end
```

TUIMessageCellData 需要计算出显示内容的大小，以便 TUIChatController 预留足够的位置显示此类消息。

```objectivec
@implement MyCustomCellData : TMessageCellData
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


### 步骤2: 实现一个自定义 cell 类

自定义一个继承自 TUIMessageCell 的 cell 类。

```objectivec
@interface MyCustomCell : TUIMessageCell
@property UILabel *myTextLabel;
@property UILabel *myLinkLabel;
@end
```

在实现文件中，您需要创建 myTextLabel 和 myLinkLabel 对象，并添加至 container。

```objectivec
@implementation MyCustomCell

- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier
{
    self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];
    if (self) {
        _myTextLabel = [[UILabel alloc] init];
        _myTextLabel.numberOfLines = 0;
        _myTextLabel.font = [UIFont systemFontOfSize:15];
        [self.container addSubview:_myTextLabel];
        
        _myLinkLabel = [[UILabel alloc] initWithFrame:CGRectZero];
        _myLinkLabel.text = @"查看详情>>";
        _myLinkLabel.font = [UIFont systemFontOfSize:15];
        _myLinkLabel.textColor = [UIColor blueColor];
        [self.container addSubview:_myLinkLabel];
        
        self.container.backgroundColor = [UIColor whiteColor];
        [self.container.layer setMasksToBounds:YES];
        [self.container.layer setBorderColor:[UIColor lightGrayColor].CGColor];
        [self.container.layer setBorderWidth:1];
        [self.container.layer setCornerRadius:5];
    }
    return self;
}

- (void)fillWithData:(MyCustomCellData *)data;
{
    [super fillWithData:data];
    self.customData = data;
    self.myTextLabel.text = data.text;
}

- (void)layoutSubviews
{
    [super layoutSubviews];
    self.myTextLabel.mm_top(10).mm_left(10).mm_flexToRight(10).mm_flexToBottom(50);
    self.myLinkLabel.mm_sizeToFit().mm_left(10).mm_bottom(10);
}
@end
```


### 步骤3: 注册 TUIChatController 回调

注册 TUIChatController 回调是用于告知 TUIChatController 该如何显示自定义消息，注册该回调需要实现下列回调：
- 收到消息时，将 V2TIMMessage 转换为 TUIMessageCellData 对象。
- 在显示前将 TUIMessageCellData 转换为 TUIMessageCell 对象，用于最终显示。

```objectivec
@implement MyChatController
- (id)init
{
	self = [super init];
	// 初始化
	chat = [[TUIChatController alloc] initWithConversation:conversationData]; // conversationData 为当前会话数据，包括 groupID、userID 等，可以在会话列表获取
    [self addChildViewController:chat]; // 将聊天界面加到内部
    chat.delegate = self;	// 设置回调
    // 配置导航条
    ...
    
    return self;
}
// TChatController 回调函数
- (TUIMessageCellData *)chatController:(TUIChatController *)controller onNewMessage:(V2TIMMessage *)msg
{
    if (msg.elemType == V2TIM_ELEM_TYPE_CUSTOM) {
        MyCustomCellData *cellData = [[MyCustomCellData alloc] initWithDirection:msg.isSelf ? MsgDirectionOutgoing : MsgDirectionIncoming];
        cellData.text = @"查看详情>>";
        cellData.link = @"https://cloud.tencent.com/product/im";
        return cellData;
    }
    return nil;
}

- (TUIMessageCell *)chatController:(TUIChatController *)controller onShowMessageData:(TUIMessageCellData *)data
{
    if ([data isKindOfClass:[MyCustomCellData class]]) {
        MyCustomCell *myCell = [[MyCustomCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"MyCell"];
        [myCell fillWithData:(MyCustomCellData *)data];
        return myCell;
    }
    return nil;
}

@end
```


## 发送自定义消息

TUIChatController 提供了发送消息接口，用户通过代码控制消息发送操作，自定义消息的类型必须继承自 TUIMessageCellData。例如，发送文本消息可以创建一个 TUITextMessageCellData 对象。
如需发送自定义数据，需要初始化 innerMessage 属性，请参考如下代码：

```objectivec
MyCustomCellData *cellData = [[MyCustomCellData alloc] initWithDirection:MsgDirectionOutgoing];       
cellData.innerMessage = [[V2TIMManager sharedInstance] createCustomMessage:data]; // data 为自定义二进制数据
[chatController sendMessage:cellData];
```

