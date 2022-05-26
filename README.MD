# 适用于Hoshino的screenfetch
## 注意事项
- 仅在linux系统上进行过测试，不保证windows能正常使用。
- 烂代码警告。
- 感谢插图作者Mint，源地址: https://www.pixiv.net/member_illust.php?mode=medium&illust_id=82093407
- 使用GPLv3协议
## 部署
- clone本仓库进入modules目录，在config/__bot__.py中添加sysinfo-for-hoshino
- 在系统中*安装screenfetch* 
  - 例如：`# apt update && apt install screenfetch`
- 安装PIL库：
  - `pip3 install pillow`
  - 如果使用poetry，使用 `poetry add pillow`
## 使用
- 发送screenfetch
## TODO
- 增加权限管理
## 长这样
![截图](https://github.com/PerfBleu/sysinfo-for-hoshino/raw/main/screenshot.png "截图")
