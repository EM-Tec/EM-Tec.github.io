+++
author = "毛哥EM"
title = "Day30 三十天的血與淚 - 密技"
date = "2023-10-14"
series = ["不用庫 也能酷 - 玩轉 CSS & Js 特效"]
tags = ["HTML", "CSS", "JS"]
categories = [""]
thumbnail = "https://em-tec.github.io/images/ironman2023.webp"
featureImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
shareImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
+++

不知不覺，三十天的鐵人賽就要結束了。一開始還覺得時間很漫長，但到了二十幾天之後我開始發現時間不多了，十分珍惜每一次能夠和大家分享的機會。

## 這三十天我們做了什麼？

在前面九天的文章中，我們直擊了許多人不敢去碰，但是對於要做出許多效果又是必備的技術。我們先複習 Flex 讓我們能隨心所欲切出任何我們想要的版面，用 `@keyframes` 與 `transition` 做出動畫效果，並認識開啟顏色新世界的 `filter`、`color:color()`、以及 `mix-blend-mode` 等等屬性。

在接下來的十幾天，我們製作了許多令人驚豔的效果。每一天專案的背後都會放入一些實用的思維，語法的應用，以及一些小技巧。希望用效果的視覺包裝可以讓大家更容易理解與覺得有趣，並且能夠在未來的開發中運用。

![](https://em-tec.github.io/post/2023ironman-18/final.gif)

而到了第二十天的【[Day20 GPU! 啟動! - 淺談 CSS3 硬體加速](https://ithelp.ithome.com.tw/articles/10333947)】 我們開始探討在技術上的選擇，以及如何讓網頁的動畫更加順暢，並帶出更多較為複雜的效果。 

![](https://em-tec.github.io/post/2023ironman-22/final.gif)

>　[Day 22 JavaScript 乱薍覼釠亂碼效果](https://ithelp.ithome.com.tw/articles/10335389)

而到了最後五天，我們談到了一些網站最常見的效果，像是漢堡選單，滑動到特定位置時，會有動畫效果的 Animate On Scroll，以及網站最常見的輪播效果等。應用我們所學的語法讓這一些效果製作起來變得簡單但又十分獨一無二。

而到昨天我們回到了鐵人賽的頁面，並用我們所學的語法重現了 header 的太空效果。

![](https://em-tec.github.io/post/2023ironman-29/final.gif)

身為一個高二的普通學生，平常能寫文章的時間真的有限，但是我還是盡量讓每一天的文章可以新鮮有趣，並且能夠讓新手容易閱讀，但老手又不會覺得無聊，保留一點深度。雖然這三十天裡沒有人留言或是 Like，但希望路過的你們能夠找到點你要的東西，或至少得到些快樂。

礙於時間和篇幅，我們沒有辦法把每一天的語法都探討得很深入，如果你有任何問題都可以留言告訴我，我會盡量回答。而如果有幸這個系列出成書，我會把每一天的效果和語法都做更詳細的介紹，並且加入更多的實用技巧。

## 背後的血與淚

這三十天的內容可以說是我對於我這一年來做的大小專案的回顧。有一些最後有成功發布，有一些效果在計畫在過程中就被捨棄了。每一個特效的背後都有一個故事，可能是數天燒腦的 Debug，~~或著是我和甲方溝通的血與淚~~。比如說【[Day5 載入中… Animation-delay](https://ithelp.ithome.com.tw/articles/10322369)】的鍵盤特效是今年 DaptKey 團隊送我的快捷鍵盤，我回禮的使用心得文章加上這個載入特效。

![](https://em-tec.github.io/post/2023ironman-5/loading.gif)

### 平常寫文章的流程

在開始前其實我有先備幾篇半成的文章打在 Notion，原本想說都是 Markdown 語法，直接貼到iT邦就可以了，但是後來發現 Notion 的 Markdown 語法和iT邦的不太一樣，而且圖片也是一個很大的問題，所以最後我是用 VSCode 寫完文章，上傳到我的部落格，最後再貼到iT邦上。

因為開賽才注意到這個問題，所以重新整理文章花了我一點時間。基本上前二十天都是每天用下課、午休、和等公車的時間用學校的筆電撰寫。一天可以寫一篇左右，假日吃一點之前的庫存。但到後面基本上就是每天和12點賽跑，因為我還是希望每篇文章能夠完整的呈現，盡量把容易不懂的地方都解釋清楚。

>　在這三十天我有好幾天晚上做夢夢到忘記發文章被淘汰。

### 背後的朋友

在這三十天裡，有幾個朋友一直在背後幫助我。我一直都沒有機會提到他們，因此我希望在這裡能夠感謝他們。

第一個是剛才提到的 VSCode，我在寫文章的時候都是用 VSCode。他要插入圖片還蠻方便的，只需要複製圖片，在文中間貼上就會自動複製到資料夾並用 Markdown 插入。

截圖有的時候我會使用 Windows 內建的 Win + Shift + S，但大多數是使用 Firefox 內建的截圖工具，因為他在截圖時可以完美的擷取某個元素。

![](shot.webp)

不過還沒完，因為截圖下來都是 PNG 或著是 JPEG，而我不管是製作網頁還是寫文章都會習慣轉檔成 WebP 格式，讓你們載入更快速。因為太常轉檔了因此我用 python 寫了一個轉檔工具叫做 [NiceFormat](https://github.com/Edit-Mr/NiceFormat)
，只需要把圖片拖進去就可以轉檔，而且還可以一次轉好幾張。如果把 WebP 圖片拖進去就會轉回 PNG。

![轉檔](convert.gif)

而 GIF 我是先使用 OBS 錄製，再用線上工具 [cloudconvert](https://cloudconvert.com/mkv-to-gif) 轉檔。

最後是有好幾篇文章我有畫示意圖，大部分是使用 Adobe Illustrator 繪製，也有一些在 iPhone 上完成是使用 Procreate 以及 Curve (前 Vectornator) 繪製。

![混和模式比較](https://em-tec.github.io/post/2023ironman-9/mix.webp)

> [Day9 給你五彩斑斕的黑: mix-blend-mode](https://ithelp.ithome.com.tw/articles/10325681) - 混和模式比較

![永無止境跑馬燈原理](https://em-tec.github.io/post/2023ironman-10/marquee.svg)

> [Day10 永無止境跑馬燈 - 不同螢幕 相同速度](https://ithelp.ithome.com.tw/articles/10326819)

當然最後也要感謝這台學校借我的筆電。這台文書機真的被我操的很慘，一下跑 Blender 一下跑 Illustrator。~~早餐三明治放在底下畫完就差不多可以出爐了~~

----------------


三十天的旅程差不多到一段落，

還能走多遠就不在我能掌握。

蓋上螢幕，回到現實...

下禮拜還要段考，客戶還在等我交稿，比賽馬上就要到。

*我是毛哥EM，讓我們MWC 2023 大會再見。*