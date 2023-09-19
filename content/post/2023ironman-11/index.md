+++
author = "毛哥EM"
title = "Day11 說滾不是真的要你滾 - 背景滾動視差"
date = "2023-09-25"
series = ["不用庫 也能酷 - 玩轉 CSS & Js 特效"]
tags = ["HTML", "CSS", "JS"]
categories = [""]
thumbnail = "images/ironman2023.webp"
featureImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
shareImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
+++

你有看過這種頁面往下滾，但圖片沒有變的效果嗎？

偷偷告訴你，這個效果只需要一行 CSS就可以做到。`background-attachment` 屬性可以用來控制背景圖片的滾動方式。在這篇文章中，我們將詳細介紹這個屬性以及如何使用它來實現不同的效果。

## 什麼是 `background-attachment` ？

`background-attachment` 是 CSS 中用於控制背景圖片滾動行為的屬性。它有三個可能的值：

1. `scroll`（滾動）：這是默認值，背景圖片將隨著頁面的滾動而移動。這意味著當頁面滾動時，背景圖片會被視為固定的。
2. `fixed`（固定）：當你設置此值時，背景圖片將保持固定在視口的某個位置，不隨頁面的滾動而移動。這可以創建一種視差滾動效果，使背景圖片保持在原地，而內容文字或元素則滾動過它。
3. `local`（本地）：它會使背景圖片隨著元素的內容滾動而移動，而不是整個頁面。有點像屬於那個框框的背景。這個值在大部分情況下比較少見。

## 飯粒範例

現在讓我們來看看幾個飯粒的範例

### 創建固定背景圖片

假設你想要在網站的首頁上創建一個固定的背景圖片，以實現視差效果。你可以這樣設置 CSS：

```css
body {
    background-image: url('your-image.jpg');
    background-attachment: fixed;
    background-size: cover; /* 可選，用於調整圖片大小以填充整個視口 */
}

```

這將使背景圖片保持固定，而內容將在其上滾動，創建出一種動態的效果。

### 創建滾動效果

如果你想要一個網站上的背景圖片會隨著頁面滾動而移動…那麼你什麼都不用做，本來不就是這樣。但如果你有別的屬性蓋過去的話可以用  `scroll` 改回來。

```css
body {
    background-image: url('your-image.jpg');
    background-attachment: scroll;
}

```

這將使背景圖片與頁面的滾動同步，創建一種比較傳統的網頁設計效果。

### 使用 `local` 值

最後，如果你想要在某個元素內部創建一個背景圖片，並且希望它隨著該元素的滾動而移動，你可以使用 `local` 值。這個值通常應用於具有自己的滾動區域的元素，例如 `div` 或 `section`。

```css
.container {
    background-image: url('your-image.jpg');
    background-attachment: local;
}

```

這將使背景圖片與 `.container` 元素的內容滾動同步，而不是整個頁面。

總之，`background-attachment` 屬性是一個強大的工具，可以用來控制背景圖片的滾動方式，從而實現不同的視覺效果。雖然實際功能不大但可以給人一種出乎意料且不會那麼死板的感覺。

不過這只是最基本的滾動視差，且只能應用在圖片上面。明天我們將要討論如何讓任何你想要的東西滾起來。

希望這篇文章能幫助你更好地理解和應用這個屬性，歡迎在 [Instagram](https://www.instagram.com/em.tec.blog) 和 [Google 新聞](https://news.google.com/publications/CAAqBwgKMKXLvgswsubVAw?ceid=TW:zh-Hant&oc=3)追蹤[毛哥EM資訊密技](https://em-tec.github.io/)，也歡迎訂閱我新開的[YouTube頻道：網棧](https://www.youtube.com/@webpallet)。

我是毛哥EM，讓我們明天再見。