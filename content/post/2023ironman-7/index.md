+++
author = "毛哥EM"
title = "Day7 幫我開濾鏡 filter"
date = "2023-09-21"
series = ["不用庫 也能酷 - 玩轉 CSS & Js 特效"]
tags = ["HTML", "CSS", "JS"]
categories = [""]
thumbnail = "https://em-tec.github.io/images/ironman2023.webp"
featureImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
shareImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
+++

CSS 的濾鏡屬性是一個非常實用且可以瞬間讓一個網頁看起來很厲害的功能。讓你可以以各種方式修改和調整圖像和元素的呈現方式，也可以讓元素模糊，或者是直接改變圖示顏色等等。今天我們將深入探討CSS filter 屬性，解釋其各種功能以及如何使用它來創建引人注目的效果。
<!--more-->
現在，讓我們來看一些CSS filter 屬性的常見用法：

### 1. 模糊（Blur）

模糊效果可以用來模糊圖像或元素，創建出柔和的背景效果或是陰影效果。你可以通過調整模糊半徑的值來控制模糊的程度，例如：

```css
/* 模糊半徑為5像素 */
filter: blur(5px);

```

> 冷知識：正方形 blur 可以變圓形

![Blur](https://em-tec.github.io/post/2023ironman-7/blur.webp)

### 2. 亮度（Brightness）

這不用解釋吧，讓它變更明亮或更暗。值為100%時保持原樣，大於100%將增加亮度，小於100%則減少亮度，例如：

```css
/* 增加亮度至150% */
filter: brightness(150%);

```

### 3. 對比度（Contrast）

對比度效果可以增加或減少圖像的對比度，使畫面更鮮明或柔和。值為100%時保持原樣，大於100%將增加對比度，小於100%則減少對比度，例如：

```css
/* 增加對比度至200% */
filter: contrast(200%);

```

### 4. 灰度（Grayscale）

灰度效果將圖像轉換為灰階，使其變成黑白圖像。值為100%時完全灰階，0%時保持原色，例如：

```css
/* 轉換為完全灰階 */
filter: grayscale(100%);

```

### 5. 反轉顏色（Invert）

反轉顏色效果可以將圖像的顏色反轉，使白色變為黑色，黑色變為白色。值為100%時完全反轉，0%時保持原色，例如：

```css
/* 完全反轉顏色 */
filter: invert(100%);

```

### 6. 飽和度（Saturate）

飽和度效果可以讓畫面更加鮮豔或更加淡化。值為100%時保持原飽和度，大於100%增加飽和度，小於100%減少飽和度，例如：

```css
/* 增加飽和度至200% */
filter: saturate(200%);

```

### 7. 色彩轉換（Hue-rotate）

旋轉圖像的色相。它的值以度數表示，例如：

```css
/* 旋轉色相90度 */
filter: hue-rotate(90deg);

```

### 8. 透明度（Opacity）

透明度效果控制圖像或元素的不透明度。值為0時完全透明，1時完全不透明，例如：

```css
/* 使元素變得半透明 */
filter: opacity(0.5);

```

### 為什麼不直接使用 opacity 屬性?

我自己的想法是如果你已經要使用 filter 屬性屬性的話寫在一起可以更明確的表達在為了達成同一個效果，否則直接使用 opacity 就好了。

### 9. 遮罩（Drop-shadow）

這個效果可以在圖像或元素周圍添加陰影，以使其看起來浮在其他元素之上。你可以指定陰影的偏移、模糊半徑、顏色等，例如：

```css
/* 添加陰影效果 */
filter: drop-shadow(5px 5px 10px rgba(0, 0, 0, 0.5));

```

### 10. 多重效果

您可以將多個 filter 屬性組合在一個規則中，以同時應用多個效果，例如：

```css
/* 同時應用多個效果 */
filter: grayscale(50%) brightness(150%) blur(3px);

```

這樣，你可以根據具體需求混合和匹配這些效果，創建出獨特的視覺效果，使網頁更具創意和吸引力。

### 11. 自定義濾鏡

除了上述內置的濾鏡效果，您還可以使用自定義的 SVG 濾鏡效果。這需要定義一個 SVG 濾鏡元素，然後將其引用到 filter 屬性中。這個就有一點複雜了，不在本文的討論範圍，但提供了更高度可定制性，有興趣的話可以自己研究看看。

### 用一個顏色製作漸層
finter 在製作漸層很實用，可以讓你只需要選擇一個顏色就能生成不錯看的漸層。

https://codepen.io/edit-mr/pen/GRPyNYY

![相疊](https://em-tec.github.io/post/2023ironman-7/gradient.webp)


```css
:root {
  --color: blue;
}

body {
  background: var(--color);
  min-height: 100svh;
  margin: 0;
}
body::after {
  display: block;
  width: 100%;
  height: 100svh;
  content: "";
  background: linear-gradient(var(--color), transparent);
  filter: hue-rotate(-60deg) brightness(3);
}
```

你可以看到我先設定了背景顏色，接著建立一個偽元素，並且設定他的背景為漸層。一半是設定的顏色，一半是透明。接著使用 filter 來調整顏色，我讓亮度高一點然後色相旋轉一下讓顏色淺一點。這樣就能夠做出漸層的效果囉。

這些都是 CSS filter 屬性的一些常見和進階功能。通過組合這些效果，你可以為網站的元素創建出各種視覺效果，無論是圖像處理還是動畫，都能夠實現。我們會在之後的文章繼續講你可以怎麼玩 filter 屬性。

歡迎在 [Instagram](https://www.instagram.com/em.tec.blog) 和 [Google 新聞](https://news.google.com/publications/CAAqBwgKMKXLvgswsubVAw?ceid=TW:zh-Hant&oc=3)追蹤[毛哥EM資訊密技](https://em-tec.github.io/)，也歡迎訂閱我新開的[YouTube頻道：網棧](https://www.youtube.com/@webpallet)。

我是毛哥EM，讓我們明天再見。