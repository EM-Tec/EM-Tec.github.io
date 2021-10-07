+++
author = "毛哥EM"
title = "【VB-CABLE】虛擬麥克風。無法分享聲音?不存在的"
date = "2021-08-13"
description = "讓電腦聲音輸出成麥克風"
featured = true
tags = [
    "軟體",
    "Windows"
]
categories = [
]
series = ["線上教學"]
thumbnail = ""
+++
VB-Cable讓電腦聲音輸出成麥克風

<!--more-->
使用 Google Meet 的“全屏”或“單窗口”共享電腦屏幕時，音效無法傳輸到其他參與者的設備，因為 Google Meet 使用瀏覽器，不需要像 Zoom 那樣需要安裝軟件，所以 Google Meet 在會議中可以播放的聲音只有：

* 瀏覽器聲音（例如 YouTube 或其他網站中的視頻和音頻）
* 瀏覽器支持播放視頻和音頻文件（如MP4、MP3...），且不支持外掛字幕
*  電腦麥克風
無法在電腦上播放音效，如影音播放軟件（如Media Player、DVD播放器）、教學軟件、應用程序（如PowerPoint）產生的音效。 如果您需要在 Google Meet 會議中播放電腦音效，則需要安裝額外的軟件。
所以今天要介紹一款名為“VB-Cable”的免費軟體，它可以通過虛擬麥克風將電腦的聲音傳送到Google Meet。 它同時支持 Windows 和 Mac OS X
原理：讓電腦以為它在獲取的是麥克風的聲音，其實是你電腦的
{{% notice info "VB-CABLE Virtual Audio Device" %}}
* 開發者:V.Burel
* 軟體類型:免費軟體
* 下載位置:[官網](https://vb-audio.com/Cable/)
{{% /notice %}}
## 安裝步驟
### 下載
首先，先進入到官網並下載你的作業系統

### 安裝
解壓縮壓檔，並跟據你的電腦對VBCABLE_Setup_x64.exe (64位元) 或 VBCABLE_Setup.exe (32位元)按右鍵。這時，你可以看到有一個叫做「以管理員身分執行」。點擊後會跳出一個小視窗，點選確定即可。

進入後點擊Instill Driver

## 設定

當你想要啟用虛擬麥克風時只需要將撥放裝置改成Cable Input就好了。（對螢幕右下角聲音符號後點右鍵，並點選音效即可進入此畫面。）

{{% notice tip "Google Meet設定" %}}
如果還是沒有聲音，請到Google Meet的設定確定麥克風是CABLE Outputs。
{{% /notice %}}
