+++
author = "毛哥EM"
title = "【GAS】自製點名系統"
date = "2021-10-07"
description = "使用Google sheet 試算表表單串接api<br />介紹、使用說明與製作教學"
featured = true
tags = [
    "HTML",
    "CSS",
    "JavaScript",
    "Github",
    "GAS"
]
categories = [
    "自製",
]
series = [""]
thumbnail = "images/thumbnails/frog_check_in.jpg"
featureImage = "https://em-tec.github.io/images/thumbnails/frog_check_in.jpg"
shareImage = "https://em-tec.github.io/images/thumbnails/frog_check_in.jpg"
+++
大眼蛙教練的課程是以堂數做計算，也就是來一次算一次，而不是一段時間。因此每次學生上課都需要簽到，最後還需要人工來統計。因此我做了一個簡單的點名系統，讓電腦來做統計和計算的工作。
<!--more-->
![首頁](https://EM-Tec.github.io/images/frog_check_in-home.png)
{{% notice info "大眼蛙教練點名系統" %}}
* 開發者:毛哥EM(我)
* 類型:網站
* 網址:[EM's Base](http://edit-mr.github.io/code/frog)
{{% /notice %}}
## 功能
### 新增學生
![新增學生](https://EM-Tec.github.io/images/frog_check_in-add.png)
輸入名稱並按新增即可。<br />
電腦會自動在Google Sheet建立好欄位。教練只需要到試算表設定學生的課程數就好了。如果沒有課了會用紅色表示，而未設定會被判斷為沒有課程。
![試算表中的學生列表](https://EM-Tec.github.io/images/frog_check_in-student.PNG)
{{% notice warning "超重要提醒" %}}
* 學生姓名不可以有空格，如果有空格會自動刪除
* 要刪除學生請刪除整列，不可留一整列空白
{{% /notice %}}

### 點名
![點名畫面](https://EM-Tec.github.io/images/frog_check_in-check.png)
網站會從表單取得學生名單並顯示。只需要點擊名稱即可完成報到。<br />
![報到成功會提示你還剩下幾堂課](https://EM-Tec.github.io/images/frog_check_in-checked.png)
{{% notice notice "提醒" %}}
* 為了配合不同螢幕大小，沒有限制每行出現的學生數。盡可能多顯示一些，比較容易找到。
* 為避免重複點名，報到後學生會隱藏。重新整理頁面即可顯現
* 下方方框會顯示自開啟網頁後已完成報到的學生。
{{% /notice %}}
在試算表的「紀錄」可以看到之前學生的報到紀錄。當天的會以綠色做標記。
{{% notice warning "超重要提醒" %}}
* 如果要刪除記錄（如誤按到）請**務必**要「**刪除整列**」。不可留空
![報到紀錄](https://EM-Tec.github.io/images/frog_check_in-record.png)
{{% /notice %}}

### 查詢記錄
![查詢毛宥恩的報到紀錄](https://EM-Tec.github.io/images/frog_check_in-search.png)
如果要查詢之前報到的紀錄，請到查詢頁面並輸入姓名。
