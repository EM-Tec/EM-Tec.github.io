+++
author = "毛哥EM"
title = "滿足你的色域! color: color"
date = "2023-09-22"
series = ["不用庫 也能酷 - 玩轉 CSS & Js 特效"]
tags = ["CSS"]
categories = [""]
thumbnail = "https://em-tec.github.io/images/ironman2023.webp"
featureImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
shareImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
+++

> 今天這一篇是一個很色的冷知識分享。可以讓你調出很冷的顏色。
> 

你平常用 CSS 都在怎麼表示顏色呢？是使用 RGB 還是 HEX 碼呢？不管你是使用哪一種他們都是使用三個數字表達每種顏色通道（紅、綠、藍）要多亮。由於每個通道都可以有256種可能的值（從00到FF），所以一個Hexadecimal顏色碼可以表示的顏色總數為256 x 256 x 256 = 16,777,216 種顏色。

人類的眼睛可以分辨約700萬種顏色，~~很明顯這些顏色很不夠用對吧！~~

應該說隨著瀏覽器和螢幕的發展，螢幕的色域越來越廣，是超過 RGB 能表達的，讓我們可以看到更亮眼跟絢麗的色彩。而且每一間公司出場的螢幕顏色多少有點不一樣，而且科技一直在進步，誰知道發明新的單位什麼時候會淘汰。於是[惠普](https://zh.m.wikipedia.org/wiki/%E6%83%A0%E6%99%AE)與[微軟](https://zh.m.wikipedia.org/wiki/%E5%BE%AE%E8%BD%AF)於1996年一起開發了 **sRGB 色彩空間。**

![CIE 1931 xy色彩圖表示的sRGB色彩空間的色域以及原色的位置](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/CIExy1931_sRGB.png/800px-CIExy1931_sRGB.png)
圖片來源:維基共享資源

看我們突然多出好多顏色可以用了！但是人類對色的慾望是用無止境的，一下就發現不夠用了。尤其是藍色的部分很多印刷能夠印出來的顏色在螢幕上根本顯示不出來。於是又跑出Adobe RGB等等更多標準…

## 所以我到底要怎麼打啦？

CSS支援以下幾個色彩空間

- [sRGB](https://en.wikipedia.org/wiki/SRGB)色彩空間：[`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/hsl)[`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/hwb)[`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgb)
- [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space)色彩空間：[`lab()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/lab)[`lch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/lch)
- [Oklab](https://bottosson.github.io/posts/oklab/)色彩空間：[`oklab()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklab)[`oklch()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch)

他們都有自己的規則，而今天我要講的是不管是什麼色彩空間都可以使用的屬性：

```css
color: color
```

呃沒錯，真的是這樣…

以下是如何使用`color()` 的一些基本知識：

### 基本語法

首先，讓我們看一下`color()` 函數表示法的基本語法：

```css
color(colorspace c1 c2 c3[ / A])

```

- `colorspace`你要使用的色彩空間，例如`srgb`，`display-p3`，`rec2020`等等。
- `c1`，`c2`，`c3`：這些是數字，百分比值或關鍵字`none`，用於指定在所選色彩空間中的組件值。
- `A`（選擇性）：這是不透明度，用於指定元素的透明度，其中1對應於100％的不透明度。

### 選擇適當的色彩空間

根據您的需求，選擇適當的色彩空間非常重要。不同的色彩空間適合不同的情境。例如，`display-p3` 可以用於支援廣色域的螢幕，而 `srgb` 可能更適合一般的情況。

### 使用示例

以下是一些使用 `color()` 函數表示法的示例：

```css
/* 在sRGB色彩空間中指定紅色 */
color(srgb 1 0 0);

/* 在display-p3色彩空間中指定橙色，同時設置透明度為50% */
color(display-p3 1 0.5 0 / 0.5);

```

### 媒體特性檢測

要在您的CSS中使用`color()` 函數表示法，您還需要確保瀏覽器支援您所選擇的色彩空間。這可以通過 `color-gamut` CSS 媒體特性來檢測。這將有助於確保您的設計在不同設備上呈現一致的外觀。

```css
/* 檢測是否支援display-p3色彩空間 */
@media (color-gamut: p3) {
  /* 在此使用display-p3色彩空間中的顏色 */
  color(display-p3 1 0.5 0);
}

```

其實也不用這麼麻煩，把 HEX 碼寫在上面，這些高級的屬性寫在下面，如果瀏覽器看得懂的話他自然就會選下面的啦

總之，`color()` 函數表示法是一個強大的工具，它使網頁設計師能夠更精確地控制顏色的呈現方式，並考慮不同色彩空間的因素。讓你的網站可以~~更刺眼~~ ，**更能抓住使用者的目光**，留下深刻的印象。

以上就是我今天的分享，歡迎在 [Instagram](https://www.instagram.com/em.tec.blog) 和 [Google 新聞](https://news.google.com/publications/CAAqBwgKMKXLvgswsubVAw?ceid=TW:zh-Hant&oc=3)追蹤[毛哥EM資訊密技](https://em-tec.github.io/)，也歡迎訂閱我新開的[YouTube頻道：網棧](https://www.youtube.com/@webpallet)。

我是毛哥EM，讓我們明天再見。