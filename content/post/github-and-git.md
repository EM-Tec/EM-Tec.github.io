+++
author = "毛哥EM"
title = "【Github Git】超白話簡單入門"
date = "2022-08-22"
description = "簡單的git教學，輕鬆下載上傳檔案"
series = ["複製貼上就能成為工程師"]
tags = ["終端機","Git","Github"]
categories = [ "網站分享","軟體分享" ]
thumbnail = "images/thumbnails/github-and-git.jpeg"
featureImage = "https://em-tec.github.io/images/thumbnails/github-and-git.jpeg"
shareImage = "https://em-tec.github.io/images/thumbnails/github-and-git.jpeg"
draft  = true
toc = true
+++
這一篇文章我會用簡單好理解的方式讓你學會基本的使用Github和Git。且[複製貼上就能成為工程師]()系列所搭建的網站都可以免費架設在Github

# Github是什麼
Github可以說是程式的雲端硬碟或IG。註冊帳號就可以上傳檔案，可以自己決定要不要讓別人看到。當然也可以留言、按讚（星星）、或轉發改編。
上傳檔案除了可以像社群一樣用網頁版直接傳之外，因為通常一個專案裡面會有很多資料夾和檔案，所以通常會用一個叫做git的技術來實現同步檔案。

Github的單位是`使用者/倉庫/檔案`。我們會在電腦裡放一個資料夾裝一個專案，並透過git來同步
如果你還是有點不懂，實際操作一次就知道了。

# Git是什麼
你也可以想像Github是物流中心，而git就是物流。我們透過物流來傳資料到Github的倉庫合獲取檔案。git厲害的地方是每次上傳或下載時它會比較差異，只傳送不同的檔案。除了節省時間流量之外，因為記錄了每一次的更動，所以可以進行版本控制。包括釋出不同版本，和復原到指定版本。

# 註冊Github並建立倉庫

進入[github.com](https://github.com)點擊Sign Up註冊跟著步驟填入資訊就好了。記得用戶名會變成你的免費網域（用戶名.github.io）所以記得好好取 ಡ ͜ ʖ ಡ

成功註冊驗證完你可以編輯一下你的個人資訊（自我介紹，頭像之類的）。好了之後點擊New Repo，並命名為`用戶名.github.io`讓裡面的檔案自動變成網站。一定要一字不漏一樣喔，但如果只是要存檔案而已取什麼名字都可以。
底下的選項如下
* 
* 
* 

成功建立之後你可以看見有一個剛才系統建立的`README.md`。這個是別人進入這個專案網頁會看到的這個說明文件，可以先不用管它。每次我們上傳完檔案後它都會需要部署一下。大概等個三十秒就可以進去你的網站了。網站就是`使用者.github.io`。

接下來我們來讓這個專案同步到你的裝置裡的某個資料夾吧。

在開始之前我們來講一下Git的邏輯原理

# Git邏輯

* 如果要從網上下載下來檔案我們要`clone`（複製）下來
而要上傳檔案就像剛才說寄包裹一樣。
* 我們要先填寫寄信人（我們）的資訊，還有收件人的地址（網址）。這個只需要寫一次就可以了
* 接下來我們要`add`（選擇）要傳送的資料。通常會選擇傳送所有你編輯過的地方。
* 選好之後我們到把包裹

# 使用Github Destop（限電腦）

下載Github Destop並安裝，基原則上就是你也懂的一直下一步。安裝成功後他會叫你輸入剛才講的個人資訊，並且請你登入你的Github帳號。

git config --global user.name "<使用者名字>"
$ git config --global user.email "<電子信箱>"

git init
在要建立數據庫的目錄裡執行init命令。
git add .
git commit -m
git remote add origin git@github.com/EM-Tec/EM-Tec.github.io