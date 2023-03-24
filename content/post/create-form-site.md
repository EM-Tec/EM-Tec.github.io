+++
author = "毛哥EM"
title = "【GAS】從頭到尾建立表單網站：使用GitHub Pages和Google Sheets存儲數據"
date = "2022-08-14"
description = "直接把整個試算表連結發給別人除了要載入很久且會出現一堆不需要的按鍵，整個畫面很醜很沒有質感。而且如果你把其他隱私的資料也放在裡面，都會被一次看光光。那我們就來幫試算表包個糖衣吧"
featured = true
tags = [ "自製", "HTML", "CSS", "JavaScript", "Github", "GAS" ]
series = ["複製貼上就能成為工程師"]
categories = [ "製作教學" ]
toc = true
thumbnail = "images/thumbnails/create-site-for-sheet.jpeg"
featureImage = "https://em-tec.github.io/images/thumbnails/create-site-for-sheet.jpeg"
shareImage = "https://em-tec.github.io/images/thumbnails/create-site-for-sheet.jpeg"
draft = true
+++

本文將為您提供從頭開始建立表單網站的指導，包括如何使用GitHub Pages建立靜態網站和如何使用Google Sheets存儲和管理表單數據的詳細步驟。跟隨本文的指導，您可以輕鬆地建立一個美觀實用的表單網站，並且可以方便地收集和管理您所需的數據。
<!--more-->

當您需要收集網站訪客的資料時，表單是一個非常有用的工具。GitHub Pages是一個免費且易於使用的網站建設平台，提供用戶建立靜態網站的功能。在此基礎上，使用表單收集訪客的資料是一種非常實用的方法。

在此過程中，使用Google Sheets作為數據儲存庫也是非常方便的。這樣做的好處在於，可以輕鬆地收集、存儲和管理來自不同來源的數據，並進行進一步的分析。

我們來做一個超簡單的小網頁讓它自己去表格抓你要的資料來顯示。我們會寫一些程式(HTML,CSS,Js）不過如果你不會也沒關系w只要跟著步驟複製貼上就可以了。

{{% notice info "薩波委託進度" %}}

開發者:毛哥EM(我)
類型:網站
網址:[毛哥EM的基地](https://Edit-Mr.github.io/code/sabooo) {{% /notice %}}

## 架一個網站！

你可以使用任何一個可以給你存放網站代碼的地方，比如說[Github](https://github.io)。

我從[Codepen](https://codepen.io/)上找到了一個很好看的表格模板來做修改。它在螢幕尺寸太窄的時候會用不同的版面來顯示，保持使用者體驗。你也可以找其他的模板或者是自己建立一個。


我在網站上增加了一點文字、顏色(CSS)、超連結(`<a>`)、還有圖片、縮圖。以及簡單的出場動畫(animate.css)<s>來炫技</s>。

## 後端 GAS! GAS!
好了前端做好了接下來我們來建另一個網站讓剛才那個網站來這裡讀取資料。為了方便起見我們在給資料的時候直接給一個做好的表格讓網站貼上。

我們先看一下試算表。在這裡我們可以看到每一行資料有5項，其中我希望第5項的資料可以放在付款狀態後面。現在請你先請你複製這個試算表的ID，也就是網址`https://docs.google.com/spreadsheets/d/`和`/`之間那一串(如`1fjX-prGu0hfb65LCQkrktWa-JavvjSz7tWMmYWAb7RA`)。等一下會用到。

![再看一次試算表](https://em-tec.github.io/images/gas.jpg)

我們會使用GAS(Google App Script)來建立網頁應用程式來讀取表格資料。

{{% notice info "Google App Script" %}}

開發者:Google
類型:免費網站（可付費升級）
網址:[script.google.com](https://script.google.com) {{% /notice %}}

請建立一個新的專案並貼上以下內容。記得貼上Google Sheet那段ID，並修改自己要的範圍，程式碼裡有詳細的註解。原理是讀取一行行的資料並轉成HTML表格，其中如果狀態是完成的加上一個class讓顏色變綠色。在排序方面我是把完成的和未完成的分成兩個陣列（清單）儲存，在把完成的接在未完成的後面合併。

 {{% notice notice "小叮嚀" %}} 為避免程式碼站太多空間，可能會部分隱藏。請記得展開或直接複製。 {{% /notice %}}

```js
function doGet(){
  var spreadsheet = SpreadsheetApp.openById('1U-Q2XXXXXXXRsrh-QYCXXXXXXXXXQmGQ'); // Sheet id
  var sheet = spreadsheet.getSheets()[0];
  var rowLength = sheet.getLastRow();
  var columnLength = sheet.getLastColumn();
  var data = sheet.getRange(3,1,rowLength,columnLength).getValues();
  var dataExport = ['<li class="table-header"><div class="col col-1">委託人姓名</div><div class="col col-2"++>委託項目</div><div class="col col-3">付款狀態</div><div class="col col-4">進度狀態</div></li>'];
  var stat, ed=[];
  // 一個個加入json
  for(i in data){
    if(data[i][0] != ""){
      if (data[i][3]=="完成"){
    ed.push('<li class="table-row"><div class="col col-1" data-label="委託人姓名">'+data[i][0]
+'</div><div class="col col-2" data-label="委託項目">'+data[i][1]
+'</div><div class="col col-3" data-label="付款狀態">'+data[i][2]+" "+data[i][4]
+'</div><div class="col col-4 finished" data-label="進度狀態">'+data[i][3]+'</div></li>')
      }else{
    dataExport.push('<li class="table-row"><div class="col col-1" data-label="委託人姓名">'+data[i][0]
+'</div><div class="col col-2" data-label="委託項目">'+data[i][1]
+'</div><div class="col col-3" data-label="付款狀態">'+data[i][2]+" "+data[i][4]
+'</div><div class="col col-4" data-label="進度狀態">'+data[i][3]+'</div></li>')
      }

    };
  };
  dataExport=dataExport.concat(ed);
  // 回傳JSON
  console.log(dataExport.join(""));
  return ContentService.createTextOutput(dataExport.join(""));
  }
```

 ![GAS快速教學](https://em-tec.github.io/images/gas.jpg)

做好了之後點擊執行▶️，你會需要授予你的程式讀取資料的權限。因為你寫的程式沒有被Google驗證過所以會顯示不安全，但我相信你不會把你的帳號搞爆，對吧。

接下來我們要部署它，讓它成為一個網站來讓我們抓。這裡選擇網頁應用程式，所有人都以你的身份讀取。按下部署就可以囉

這裡我們把部署的網址複製起來。如果要做修改除了按儲存之外要記得重新部署成新版本才會更新喔

接下來我們回到Github的網頁讓他來讀這個表格

{{% notice notice "等等，不是做好表格網頁了，直接讓它顯示就好了啊幹嘛那麼麻煩？" %}}
可以當然是可以，姑且不論網址有多長多醜，如果使用Google App Script建設的網站會出現橫幅很醜的一個警告，而且他超長讓你的版面整個跑掉。為了更好的使用者體驗既然都做了就做到底吧！
 {{% /notice %}}
