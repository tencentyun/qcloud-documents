嵌入到xml文件中的python脚本，可使用的接口模块共有3部分：
1、engine：与引擎操作相关，例如，查找元素、单击、滑动、按压等动作；
2、device：与手机相关，例如，获取当前顶层包名、和手机的分辩率；
3、report：上报平台，例如，打标签 。

### engine模块支持的嵌入式python接口

#获取SDK的版本信息
engine.get_sdk_version()

#通过GameObject.Find查找对应的GameObject
find_element(name)

#获取与表达式匹配的所有节点
find_elements_path(path)

#获取GameObject在屏幕上的位置和长宽高
engine.get_element_bound(element)

#获取当前界面的可点击节点的列表
engine.get_touchable_elements()

#点击
engine.click(locator)

#在屏幕的某个位置进行点击
engine.click_position(x,y)

#长按
engine.press(locator, press_time)

#长按屏幕上某个位置
engine.press_position(x, y, press_time)

#在屏幕布上滑动
engine.swipe_position(start_x, start_y, end_x, end_y, steps)

#从一个元素位置滑到另一个元素位置
engine.swipe(start_element, end_element, steps)

#对引擎控件进行内容输入
engine.input(element, text)

### device模块支持的嵌入式python接口

#获取当前手机的顶层的Activity名称和package名称
device.get_top_package_activity()

#返回手机屏幕分辩率
device.get_display_size()

### report模块支持的嵌入式python接口

#打开始标签
report.add_start_scene_tag(scene)

#打结束标签
report.add_end_scene_tag(scene)
