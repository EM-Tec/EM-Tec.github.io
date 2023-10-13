+++
author = "毛哥EM"
title = "Day 29 鐵人賽粒子的例子"
date = "2023-10-13"
series = ["不用庫 也能酷 - 玩轉 CSS & Js 特效"]
tags = ["HTML", "CSS", "JS"]
categories = [""]
thumbnail = "https://em-tec.github.io/images/ironman2023.webp"
featureImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
shareImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
+++
相信大家對於這個頁面都不陌生吧。這是我們2023 iThome 鐵人賽的首頁。我覺得他的粒子特效和地球很酷，所以我們今天就來看看怎麼做吧。


以下是今天我們的目標。為了版面乾淨我省略了上面的文字，只留下熊俠、標題、粒子特效、和地球。且為了讓他不要太長我有稍微縮小了一點。


## HTML 架構

上面 header 我們放了兩張圖片，一個是熊俠，一個是標題。下面的 section 我們放了五個 div，它們分別是

* 粒子特效
* 粒子特效
* 粒子特效
* 光線
* 地球

```html
<header>
  <img src="https://ithelp.ithome.com.tw/static/2023ironman/img/event/kv_deco_front.png" alt="">
  <img src="https://ithelp.ithome.com.tw/static/2023ironman/img/event/logo-ironmankv.svg" alt="">
</header>
<section class="sec_eff">
  <div class="stars"></div>
  <div class="stars2"></div>
  <div class="stars3"></div>
  <div class="horizon">
    <div class="glow"></div>
  </div>
  <div class="earth"></div>
  </div>
</section>
```

## header 版面

裡面兩張圖片用 `flex` 置中。背景放圖片上面疊上一層漸層。大小設為 cover 確保圖片有填滿。最後再調整一下上方的 padding 讓它看起來比較好看。

>　背景圖片寫前面的會疊在上面，寫後面的會疊在下面。

> 官網在背景圖片設定 `background-size` 時因為被 `background` 屬性預設的 `auto` 值影響，所以使用了 `!important`，不過其實只需要打在後面就可以了。

```css
header {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 60vh;
  background: linear-gradient(
      to bottom,
      rgba(17, 55, 126, 0) 0%,
      rgba(17, 55, 126, 0) 35%,
      rgba(17, 55, 126, 1) 100%
    ),
    url(https://ithelp.ithome.com.tw/static/2023ironman/img/kv_bg.jpg) no-repeat
      center;
  background-size: cover;
  padding-top: 3.5rem;
}
header img {
  width: 37%;
}
```

## 宇宙

我們先弄一個宇宙

```css
  background: #11377e;
  min-height: 40vh;
  position: relative;
```

然後做一束高光，並進行定位。原理是先搞一個橢圓形

```css
.horizon {
  position: absolute;
  width: 160%;
  height: 70%;
  background: #038bff;
  left: -30%;
  bottom: -20%;
  border-radius: 100%/100%;
}
```



然後再模糊一下

```css
filter: blur(30px);
```

關於置中我們之前有提到，可以把 `left` 設為 `(寬度-100)/2`，這樣就不需要再用 `transform` 或是 `margin-left` 來調整位置了。

> 複習: [Day17 css.wav - 純 CSS 波浪進度條](https://ithelp.ithome.com.tw/articles/10332433)

再多加幾個光點

```css
.horizon:before {
  content: "";
  position: absolute;
  width: 81.25%;
  height: 70%;
  background: #51afff;
  -webkit-filter: blur(30px);
  opacity: 0.6;
  margin-left: 9.375%;
  border-radius: 100%/100%;
}

.horizon:after {
  content: " ";
  position: absolute;
  width: 32%;
  height: 20%;
  border-radius: 650px/350px;
  background: #b0daff;
  -webkit-filter: blur(30px);
  opacity: 0.5;
  margin-left: 34%;
  border-radius: 100%/100%;
}

.horizon .glow {
  position: absolute;
  width: 100%;
  height: 100%;
  background: #215496;
  -webkit-filter: blur(200px);
  opacity: 0.7;
  top: -10%;
  border-radius: 100%/100%;
}
```
## 地球

加上一點內陰影讓他看起來更有立體感。

```css
.earth {
  position: absolute;
  width: 200%;
  height: 100%;
  background: #2c4790;
  left: -50%;
  bottom: -50%;
  border-radius: 100%/100%;
  box-shadow: inset 0px 0px 62px 20px rgba(60, 105, 138, 0.85);
}
```

## 星空

星空效果 iThome 沒有使用什麼 [particles.js](https://vincentgarreau.com/particles.js/)。我們打開 FireFox Dev Tools 的動畫分頁可以看出原來這是一個長150秒的 CSS 動畫啊。

```css

以上就是我今天的分享，歡迎在 [Instagram](https://www.instagram.com/em.tec.blog) 和 [Google 新聞](https://news.google.com/publications/CAAqBwgKMKXLvgswsubVAw?ceid=TW:zh-Hant&oc=3)追蹤[毛哥EM資訊密技](https://em-tec.github.io/)，也歡迎訂閱我新開的[YouTube頻道：網棧](https://www.youtube.com/@webpallet)。

我是毛哥EM，讓我們明天再見。