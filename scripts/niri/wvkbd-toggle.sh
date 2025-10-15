#!/bin/bash

# 定义 wvkbd 的可执行文件名称。请根据您的实际安装情况选择正确的名称。
WVKBD_EXEC="wvkbd-mobintl"  # 例如，使用移动国际布局

# 使用 pgrep 检查 wvkbd 进程是否正在运行
if pgrep -x "$WVKBD_EXEC" > /dev/null
then
    # 进程正在运行，发送 SIGTERM 信号来杀死它
    pkill -x "$WVKBD_EXEC"
else
    # 进程没有运行，启动它
    # 使用 & 让它在后台运行，不会阻塞脚本
    "$WVKBD_EXEC" &
fi