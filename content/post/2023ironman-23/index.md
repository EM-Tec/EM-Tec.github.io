+++
author = "毛哥EM"
title = "Day23 優雅的漸層動畫 - 隨機而有秩序"
date = "2023-10-16"
series = ["不用庫 也能酷 - 玩轉 CSS & Js 特效"]
tags = ["HTML", "CSS", "JS"]
categories = [""]
thumbnail = "https://em-tec.github.io/images/ironman2023.webp"
featureImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
shareImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
+++

今天我們會提到幾個不同的原理。你可以像生菜沙拉一樣自己條配。

漸層動畫有甚麼難的? 我阿嬤...不會 CSS

```css
body {
  background: linear-gradient(90deg, red, yellow);
  animation: gradientChange 1s infinite;
}

@keyframes gradientChange {
  to {
    background: linear-gradient(90deg, yellow, green);
  }
}

```

![bruh](bruh.gif)

額，只有層，沒有漸。這是因為漸層是屬於 `background-image`，你要他怎麼漸圖片?

## 自己動

我們今天要用到的第一個方式是放大縮小，以及移動一個漸層，這樣就能做出類似於漸層的動畫。

### `background-position`

我們先把圖片拉長到兩倍，然後移動 `background-position` 來做出動畫。

```css
body {
  background: linear-gradient(90deg, red, yellow);
  background-size: 200% 100%;
  background-position: 0 0;
  animation: gradientChange 2s infinite linear alternate;
}

@keyframes gradientChange {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 100% 0;
  }
}
```

![gradient](gradient.gif)

### `background-size`

 `background-size` 如果不搭配 `background-position` 的會可以做出這種左邊維持不動，右邊比例不同漸層的效果。

```css
body {
  background: linear-gradient(90deg, red, yellow);
  animation: gradientChange 2s infinite linear alternate;
}

@keyframes gradientChange {
  from {
    background-size: 300% 300%;
  }
  to {
    background-size: 100% 100%;
  }
}
```


以上就是我今天的分享，歡迎在 [Instagram](https://www.instagram.com/em.tec.blog) 和 [Google 新聞](https://news.google.com/publications/CAAqBwgKMKXLvgswsubVAw?ceid=TW:zh-Hant&oc=3)追蹤[毛哥EM資訊密技](https://em-tec.github.io/)，也歡迎訂閱我新開的[YouTube頻道：網棧](https://www.youtube.com/@webpallet)。

我是毛哥EM，讓我們明天再見。