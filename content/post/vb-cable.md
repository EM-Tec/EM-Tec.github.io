+++
author = "毛哥EM"
title = "【Zoom】是個超讚綠幕!輕鬆去背到OBS"
date = "2021-08-14"
description = "使用OBS攝取Zoom的視窗。"
tags = [
    "OBS",  "Windows"
]
categories = [
"軟體分享",
]
thumbnail = "https://em-tec.github.io/images/thumbnails/vb-cable.jpg"
featureImage = "https://em-tec.github.io/images/thumbnails/vb-cable.jpg"
shareImage = "https://em-tec.github.io/images/thumbnails/vb-cable.jpg"
+++
綠幕是拍片直播或視訊常用到的好幫手，因為它可以讓你輕鬆地去除掉背景。只需要在軟體中選擇綠幕顏色，並調整各種數據即可。但是如果沒有綠幕怎麼辦?這時可以使用電腦免費的視訊會議軟體Zoom達到一樣的效果。
toc = true
<!--more-->

## 步驟

### 製作背景

我們需要一張只有一個顏色的圖片來作為Zoom的背景。以和人物最不相關為原則(通常使用綠色)。你可以使用小畫家來繪製。

用油漆塗滿你選的顏色

### 設定Zoom

請先到到官網下載並安裝。安裝方式和其他軟體差不多
{{% notice info "Zoom" %}}

* 開發者:Zoom Video Communications
* 軟體類型:商業軟體
* 下載位置:[官網](https://zoom.us/download)
{{% /notice %}}

#### 登入Zoom

根據你的習慣選擇登入方式，我是使用Google登入，其他也都可以。

#### 開啟一個新的視訊會議

在應用程式點選新會議

#### 不用讓程式獲取音訊

點X就好了

#### 設定

點擊左上方的會議資訊，並進入設定。我們需要改兩個項目：

取消勾選視訊下的一律在視訊上顯示參與者名稱(需要下滾)

更改背景成剛才製作的圖片。

#### 縮小畫面

回到視訊，點選最小化。視窗會小到你只能看到自己。
{{% notice tip "小提醒" %}}
如果縮小畫面還是有名字的話，可以把視窗放大再縮小一次。
{{% /notice %}}

### OBS設定

進入OBS並攝取這個Zoom小視窗。我個人是使用Streamlabs OBS，因為介面好看。這裡提供我的作法。

#### 打開OBS，新增Scene

#### 增加Window Capture

#### 命名

可依你自己喜好。記得選擇新來源再按Add Source

#### 設定攝取來源

圖片內為推薦設定，不同可能造成攝取失敗。

#### 放到最大

可視情況調整
{{% notice tip "小提醒" %}}
要放到最大記得選「Fit to screen」而不是「Stretch to screen」，否則你的臉會變形。
{{% /notice %}}

6.新增色鍵
色鍵(Color Key)可以去除指定的顏色。你可以根據情況調整參數，自己試試看

最後你也可以根據需求增加其他畫面。
