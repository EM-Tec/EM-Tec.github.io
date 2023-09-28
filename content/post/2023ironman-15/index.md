+++
author = "毛哥EM"
title = "Day15 今天我想來點...純CSS的並排選單"
date = "2023-09-29"
series = ["不用庫 也能酷 - 玩轉 CSS & Js 特效"]
tags = ["HTML", "CSS", "JS"]
categories = [""]
thumbnail = "https://em-tec.github.io/images/ironman2023.webp"
featureImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
shareImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
+++

昨天我們做了一個開關，那麼我們今天就來做一個選單吧！

<!--more-->


![](final.gif)

這個雖然是一種 `radio` 選單，但對於選擇數字這種比較短的文字其實也是一種不錯的選擇，可以讓版面更乾淨。比下拉式選單或著是傳統的radio都更方便操作。而且不用寫一行 JS，只要純 CSS 就可以完成。

## 原理

和昨天的類似，不過今天不需要 `<label>`。點擊透明的 `<input>` 之後後面的一個圓形 `<div>` 就會跑過來。最上面用一層 `<div>` 疊上去數字即可，當然你要使用 `<label>` 也是可以的。

## 開始做吧!

照剛才原理寫出 HTML，然後加上 CSS 即可。
### HTML

```html
<div class="hope-container">
  <input type="radio" name="hope" value="0">
  <input type="radio" name="hope" value="1">
  <input type="radio" name="hope" value="2" checked="">
  <input type="radio" name="hope" value="3">
  <input type="radio" name="hope" value="4">
  <div class="hope-selected"></div>
  <div class="hope-label">
    <div>0</div>
    <div>1</div>
    <div>2</div>
    <div>3</div>
    <div>4</div>
  </div>
</div>
```

### 新擬物化設計 Neumorphism 的介面

CSS 的部分我想要製作使用新擬物化設計 Neumorphism，或是說 Soft UI 的風格。有點像 iPhone3 擬物化設計
```css
```



https://codepen.io/edit-mr/pen/LYMmQOE