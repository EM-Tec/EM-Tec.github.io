+++
author = "毛哥EM"
title = "Day24 CSS 相融黏滯效果"
date = "2023-10-16"
series = ["不用庫 也能酷 - 玩轉 CSS & Js 特效"]
tags = ["HTML", "CSS", "JS"]
categories = [""]
thumbnail = "https://em-tec.github.io/images/ironman2023.webp"
featureImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
shareImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
+++

今天我們要來做這個紓壓的效果:

https://codepen.io/edit-mr/pen/poqqoLr

然後你可以應用做出一些很酷的效果:

## 原理

原理其實很簡單。要讓兩個東西之間相連只需要模糊就會糊在一起了。


```html
<div class="box">
  <div class="circle-small"></div>
  <div class="circle-big"></div>
</div>
```

```css
.box {
  position: relative;
  height: 100vh;
  background-color: #fff;
}
.circle-big,
.circle-small {
  filter: blur(10px);
  border-radius: 50%;
  width: 80px;
  height: 80px;
  background-color: red;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
.circle-big {
  width: 100px;
  height: 100px;
  background-color: black;
    transform: translate(0, -50%);
}
```



以上就是我今天的分享，歡迎在 [Instagram](https://www.instagram.com/em.tec.blog) 和 [Google 新聞](https://news.google.com/publications/CAAqBwgKMKXLvgswsubVAw?ceid=TW:zh-Hant&oc=3)追蹤[毛哥EM資訊密技](https://em-tec.github.io/)，也歡迎訂閱我新開的[YouTube頻道：網棧](https://www.youtube.com/@webpallet)。

我是毛哥EM，讓我們明天再見。