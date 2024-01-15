+++
author = "毛哥EM"
title = "【GAS】用Line Bot&Line Notify轉發群組訊息給自己"
date = "2023-02-22"
description = "你是否有群組充滿著垃圾訊息？用Line Bot&Line Notify轉發重要訊息給自己！"
tags = [
"自製", 
    "JavaScript",
    "GAS"
]
series = ["複製貼上就能成為工程師"]
categories = [
    "製作教學"
]
toc = true
+++

你是否有群組充滿著垃圾訊息？用Line Bot&Line Notify轉發重要訊息給自己！不用程式經驗，複製貼上就好了！

<!--more-->

![某群組充斥著垃圾訊息](https://emtech.cc/images/line2notify-why.webp)


<blockquote class=“instagram-media” data-instgrm-captioned data-instgrm-permalink=“https://www.instagram.com/reel/Cp9kNc9DWK1/?utm_source=ig_embed&amp;utm_campaign=loading” data-instgrm-version=“14” style=“ background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);”><div style=“padding:16px;”> <a href=“https://www.instagram.com/reel/Cp9kNc9DWK1/?utm_source=ig_embed&amp;utm_campaign=loading” style=“ background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;” target=“_blank”> <div style=“ display: flex; flex-direction: row; align-items: center;”> <div style=“background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;”></div> <div style=“display: flex; flex-direction: column; flex-grow: 1; justify-content: center;”> <div style=“ background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;”></div> <div style=“ background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;”></div></div></div><div style=“padding: 19% 0;”></div> <div style=“display:block; height:50px; margin:0 auto 12px; width:50px;”><svg width=“50px” height=“50px” viewBox=“0 0 60 60” version=“1.1” xmlns=“https://www.w3.org/2000/svg” xmlns:xlink=“https://www.w3.org/1999/xlink”><g stroke=“none” stroke-width=“1” fill=“none” fill-rule=“evenodd”><g transform=“translate(-511.000000, -20.000000)” fill=“#000000”><g><path d=“M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631”></path></g></g></g></svg></div><div style=“padding-top: 8px;”> <div style=“ color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;”>在 Instagram 查看這則貼文</div></div><div style=“padding: 12.5% 0;”></div> <div style=“display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;”><div> <div style=“background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);”></div> <div style=“background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;”></div> <div style=“background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);”></div></div><div style=“margin-left: 8px;”> <div style=“ background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;”></div> <div style=“ width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)”></div></div><div style=“margin-left: auto;”> <div style=“ width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);”></div> <div style=“ background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);”></div> <div style=“ width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);”></div></div></div> <div style=“display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;”> <div style=“ background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;”></div> <div style=“ background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;”></div></div></a><p style=“ color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;”><a href=“https://www.instagram.com/reel/Cp9kNc9DWK1/?utm_source=ig_embed&amp;utm_campaign=loading” style=“ color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;” target=“_blank”>毛哥EM資訊密技（@em.tec.blog）分享的貼文</a></p></div></blockquote> <script async src=“//www.instagram.com/embed.js”></script>


## 原理

機器人在群組收到訊息，過濾不要的，再讓Line Notfy轉傳訊息到群組或私訊給你。

### LINE bot 
  
 至[Line Developers](https://developers.line.biz/console/) => 新增或選取Provider => Create a new channel => Message API。
 > * Messaging API 底下的 Webhook 等一下我們要填入，非常重要。
  
### 生成Line Notify仗權

Line Notify是個比較冷門但是非常好用的工具。我們可以透過他來從第三方(如你的網站、或是ios捷徑)無限量的廣播訊息到指定的群組，或是單獨發給你。
  
 https://notify-bot.line.me/my/ => 發行權杖 => 把那一串複製下來，等一下要用。 
  
  要給Line看這一串他才知道要傳送信息到哪裡。使用Line Notify而不是Line機器人的原因是免費版的官方帳號一個月只能傳送500則訊息，但Line Notify則沒有限制。 
  
 > * 記得換成電腦板模式 
 > 權杖名稱是顯示在 `【 】` 中的文字，建議越短越好避免洗版
 
### 建立API(Google App Script)

{{% notice info "Google App Script" %}}

開發者:Google
類型:免費網站（可付費升級）
網址:[script.google.com](https://script.google.com) {{% /notice %}}

請建立一個新的專案並貼上以下內容。記得貼上記得貼上Line Notify Token。

```js
// 定義一個名為 'doPost' 的函數，該函數帶有一個名為 'e' 的參數。
function doPost(e) {
  
  // 從傳入的 POST 請求中解析出文本消息。只要是傳給機器人的訊息都會被解析出來。
  var message = JSON.parse(e.postData.contents).events[0].message.text;
  
  // 從傳入的 POST 請求中解析出使用者 ID。
  var id = JSON.parse(e.postData.contents).events[0].source.userId;
  
  // 如果沒有 ID，則返回。你可以在這裡加入你的過濾條件。
  if (!id) return;
  
  // 設置 Line Notify API 的權杖。
  var token = "YOUR_LINE_NOTIFY_TOKEN";
  
  // 設置 POST 請求的選項。
  var options = {
    "method": "post",
    "payload": {
      "message": id + "\n" + message // 這裡是要傳送的訊息，我們第一行放了發送者的id，第二行放了訊息本身。可以自行修改。
    },
    "headers": {
      "Authorization": "Bearer " + token
    }
  };
  
  // 發送 POST 請求到 Line Notify API。會傳給剛才設定的權杖指定的群組或私人訊息。
  UrlFetchApp.fetch("https://notify-api.line.me/api/notify", options);
}
```

我們在傳送的訊息同時添加了發送者的id。如果你想要塞選訊息的話請修改第四行if裡面的參數

* `!id  - 全部`（預設）
* `id=="某人id"` - 不要某人
* `id!="某人id"` - 只要某人
* `id!="某人id" || id!="某人id"` - 只要某一群人

 {{% notice notice "小叮嚀" %}} 為避免程式碼站太多空間，可能會部分隱藏。請記得展開或直接複製。 {{% /notice %}}
 
  ![GAS快速教學](https://emtech.cc/images/gas.jpg)

做好了之後點擊執行▶️，你會需要授予你的程式讀取資料的權限。因為你寫的程式沒有被Google驗證過所以會顯示不安全，但我相信你不會把你的帳號搞爆，對吧。執行後會看到錯誤，這是正常的，因為我們直接執行沒有給他訊息。

接下來我們要部署它，讓它成為一個網站來讓我們抓。這裡選擇網頁應用程式，所有人都以你的身份讀取。按下部署就可以囉~

這裡我們把部署的網址複製起來。如果要做修改除了按儲存之外要記得重新部署成新版本才會更新喔。

將這個部屬的網址貼到剛才Webhook的地方就完成了

