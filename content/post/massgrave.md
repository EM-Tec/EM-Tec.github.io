+++
author = "毛哥EM"
title = "【開源】快速免費啟用Office及Windows"
date = "2023-01-19"
description = "無須安裝軟體，使用PowerShell快速免費啟用Office及Windows"
tags = [ "windows" ,"Github"]
thumbnail = "images/thumbnails/massgrave.webp"
featureImage = "https://em-tec.github.io/images/thumbnails/massgrave.webp"
shareImage = "https://em-tec.github.io/images/thumbnails/massgrave.webp"
+++

Office雖然目前有提供免費線上版，且學校都有提供Office365，但是都一定要使用線上版。除了十分不方便以外許多操作也都受到限制。因此這一篇文章我要來和大家分享一個可以安全啟動Office的工具，同時也可以啟用Windows。適用於所有版本，包括最新的Office 2022及Office 365。

<!--more-->

首先請先下載並安裝Office（聽起來很廢話但你很難找到下載鏈接，這裡提供官方載點。）

下載之後直接點擊`setup.exe`安裝。

安裝完之後會提示你可以免費試用或提供金鑰。當然如果你有的話就不會讀這篇文章了，因此我們先關閉軟體，並以**使用者管理員身分**打開PowerShell。

接著輸入這一串指令並按enter來打開這個軟體:

```bat
irm https://massgrave.dev/get | iex
```

這樣就進到軟體介面了。我們要啟用office所以請按鍵盤上的3

接著按下數字等幾秒就啟動完成了。可以點擊0回到主選單並離開軟體（當然也可以按x）

再次打開 Office 軟體你就會發現驗證畫面不見了！到關於介面會看到已經成功啟動了。

如果授權到期了只需要再次執行指令就可以囉。