+++
author = "毛哥EM"
title = "Day20 GPU! 啟動! - 淺談 CSS3 硬體加速"
date = "2023-10-04"
series = ["不用庫 也能酷 - 玩轉 CSS & Js 特效"]
tags = ["HTML", "CSS", "JS"]
categories = [""]
thumbnail = "https://em-tec.github.io/images/ironman2023.webp"
featureImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
shareImage = "https://em-tec.github.io/images/ironman2023-banner.webp"
+++

今天我們要來探討如何善用使用者的 GPU 資源，讓網頁的動畫更加順暢。我盡量讓內容簡單易懂，可以當一篇科普文章閱讀。

## 瀏覽器的渲染流程

在我們討論之前，我們先來看看瀏覽器的渲染流程。這裡我畫了一張可愛的小圖

![瀏覽器渲染流程](https://em-tec.github.io/post/2023ironman-20/css3_gpu_speedup.svg)

* **JavaScript**: JavaScript 實現動畫效果，DOM 元素操作等。
* **Style（計算樣式）**: 決定每個 DOM 元素應該套用什麼 CSS 規則。
* **Layout（佈局）**: 計算每個 DOM 元素在最終畫面上顯示的大小和位置。 由於 web 頁面的元素佈局是相對的，所以其中任一個元素的位置發生變化，都會聯動的引起其他元素發生變化，這個過程叫做 reflow。
* **Paint（繪製）**: 在多個圖層上繪製 DOM 元素的文字、顏色、圖像、邊框和陰影等。
* **Composite（渲染圖層合併）**: 依照合理的順序合併圖層然後顯示到螢幕上。

在這裡你可以看到每次你的動畫在跑， CPU 都會需要重新計算一次佈局，然後重新繪製，最後再合併圖層。這個過程會造成 CPU 的負擔，導致電腦發熱，耗電量增加，~~然後全台停電等等~~。這時候 CSS3 硬體加速就派上用場了。

## 啊 GPU 買你那麼貴你在那裡爽啊

其實 GPU 也不是一直在爽，它有時候也有在做事情。我們先來談談 GPU 厲害的點在哪裡。

GPU 厲害的是他會把在改變的元素獨立抽出來一個圖層，修改完再插回去。這樣就不用每次都重新繪製整個畫面，只需要繪製這個塗層就好了。這樣就可以大大減少 CPU 的負擔，讓動畫更加順暢。


### 如何使用 CSS3 硬體加速

但由此你也可以看出，一定要瀏覽器建立獨立圖層才能使用 GPU 加速。

#### 自動建立條件

以下這些情況瀏覽器會自動幫你建立獨立圖層：

1. 使用某些特定的3D或透視效果的CSS屬性。
2. 在顯示視頻時，使用支援硬體加速的video元素。
3. 在畫布上繪製圖像時，使用3D(WebGL)技術或硬體加速的2D畫布(canvas)元素。
4. 如果你的網頁使用了Flash等外掛程式。
5. 當改變元素的透明度（opacity）時，使用CSS動畫，或者對元素應用webkit
6. 畫變換。
7. 使用支援硬體加速的CSS濾鏡效果的元素。
8. 當一個元素包含其他子元素，這些子元素在自己的圖層中。
9. 當一個元素有一個兄弟元素，並且這個兄弟元素在一個特別的圖層中，同時這個兄弟元素的顯示順序比較低（z-index較小）。


#### GPU! 啟動!

這幾個 CSS 屬性會觸發建立獨立圖層：
* transform
* opacity
* filter
* will-change

但如果你沒有想要使用這些屬性但是你還是想要使用 GPU 加速，你可以用一些小手段來誘導瀏覽器開啟 GPU 加速。

```css
.element {
    transform: translateZ(0); 
    /**或著**/
    transform: rotateZ(360deg);
    transform: translate3d(0, 0, 0);
}
```

## 注意事項

1. 當使用3D硬體加速來提升動畫性能時，最好為元素添加一個z-index屬性，手動調整複合層的排序。這樣可以有效減少Chrome創建不必要的複合層，提高渲染性能，特別是在安卓手機上，優化效果很明顯。

2. 過多地開啟硬體加速可能會消耗較多的內存，因此在什麼情況下啟用硬體加速，以及為多少元素啟用硬體加速，需要根據測試結果來決定。

3. GPU 渲染會影響字體的抗鋸齒效果。這是因為 GPU 和 CPU 具有不同的渲染機制，即使最終停用硬體加速，文字在動畫期間仍可能顯示得模糊不清。

## 結論

今天我們講了一下 GPU 的運作原理，以及如何使用 CSS3 硬體加速。希望你們可以在開發網頁時，能夠善用 GPU 資源，讓網頁的動畫更加順暢。

或著是冬天快要到了，知道怎麼用安卓手機以及學校電腦製作暖暖包了吧w

沒有在開玩笑，[這個](https://web.basemark.com/)就是一個不錯的暖暖包網頁。以上就是我今天的分享，歡迎在 [Instagram](https://www.instagram.com/em.tec.blog) 和 [Google 新聞](https://news.google.com/publications/CAAqBwgKMKXLvgswsubVAw?ceid=TW:zh-Hant&oc=3)追蹤[毛哥EM資訊密技](https://em-tec.github.io/)，也歡迎訂閱我新開的[YouTube頻道:網棧](https://www.youtube.com/@webpallet)。

我是毛哥EM，讓我們明天再見。