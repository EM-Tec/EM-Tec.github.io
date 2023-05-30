+++
author = "毛哥EM"
title = "EP.2 5分鐘完結HTML"
date = "2023-06-05"
description = "今天我們要來聊聊什麼是網站"
tags = [
    "HTML",
    "CSS",
    "JavaScript",
]
series = ["網棧"]
thumbnail = "images/thumbnails/webpallet.webp"
featureImage = "https://em-tec.github.io/images/thumbnails/webpallet.webp"
shareImage = "https://em-tec.github.io/images/thumbnails/webpallet.webp"
+++

哈囉大家好，我是毛哥EM，歡迎來到網棧。今天我要讓你5分鐘學會所有常用的HTML語法

<!--more-->

{{< youtube lOecpIqOjjY >}}

HTML叫做超文本標記語言(Hyper Text Markup Language)。故名思義就是標記一下文字，目的是讓**瀏覽器知道這個是什麼**。比如說Google想知道網站標題會去找裡面的`<h1>`；而給盲人用的語音閱讀器在看到`<stronge>`會加重語氣。主要功能不是為了裝飾文字喔，裝飾文字是CSS的工作（下禮拜就來講）

不過讓我們先來實際寫寫看HTML再來慢慢探討這些大道理。首先請你再瀏覽器輸入`pen.new`。輸入之後你會看到三個輸入框方別讓你輸入HTML,CSS,和JavaScript，還有底下的預覽區域。這個網站叫做CodePen，是一個可以讓大家互相分享網頁作品的網站。平常做網站時可以來這裡尋找靈感，或是參考別人的作法。

首先這是一段文字。如果你想要讓它成為粗體的話請你在兩邊加入 `<b>` 和 `</b>`。就像word一樣，B代表了bold。那麼我們把隔壁幾個鄰居也搬過來吧

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d21870a3-33cd-4924-8446-eb0fcdd6bbe8/Untitled.png)

`<i>`是斜體(Italic)、 `<u>` 是底線(Underline)、而 `<s>` 是劃掉(Strike)。不過這幾個都只是好看而已，對於瀏覽器來說沒什麼意義，因此我比較建議你使用 `<strong>` 來增加重要性，而語氣轉折或想區別強調文字時使用 `<em>` (emphasis)。

今天假設你建立了一個 `<h1>` 元素，代表標題(header)，但是你還想增加一個屬性告訴瀏覽器說這是一個中文的標題，這時你可以這樣打: `<h1 lang="zh-TW">` 意思是說這是一段繁體中文的標題。前面這一串我們叫做開始標記，後面的 `</h1>`叫做結束標記。lang叫做屬性，而zh-TW是屬性質。

HTML就是這樣建立一個又一個地”元素” (element) 。因為寫HTML時你需要一直重複打大於小於符號很麻煩，你知道工程師都是很懶的，所以Сергей Чикуёнок發明了emmet。假如說你想建立一個`<h1>`元素你只需要打`h1`然後按`tab`就可以了。

為了方便操作我們把輸入框放到左邊，然後選一個好看的配色，然後讓我們一次認識所有常見HTML吧!順帶一題我也會告訴你這些HTML語法原本的英文單字，可能會讓你比較好理解。

## 文字

以下是常的文字元素。


```
<p>段落
  <b>粗體</b>
  <i>斜體</i>
  <s>刪除線</s>
  <u>底線</u>
  H<sup>+</sup>
CO<sub>2</sub>
</p>

```

`<p>`元素代表段落區塊(paragraph)。`<b>`是粗體(bold)、`<i>`是斜體(italic)、`<s>`是劃掉(strike)、`<u>`是底線(underline)。`<sup>`是上標(superscript)、`<sub>`是下標(subscript)。你可以記super在上面，而訂閱按鈕Subscribe在影片下方等你去按。

**粗體***斜體*~~刪除線~~
<u>底線</u>
H<sup>+</sup> CO<sub>2</sub>

## 空白 換行

也許你有發現，在HTML中一個以上的tab、空格、換行都視為一個空格，因此你可以自由地排版保持程式的簡潔。但是如果你想要換行的話，你可以使用`<br>`元素換行。而如果你想要插入一個空白的話，你可以使用`&nbsp;`。

```
橫線<hr />
換行<br />
```

這兩個是插入一個元素而不是指定範圍，因此習慣後面會用/>結尾，但如果你要打<br>或<hr>瀏覽器也看得懂。HTML是一種"好啦我看得懂就好"的語言，因此你就算用大寫，或著是屬性引號不加也沒關係，但是為了你和你的朋友之後維護起來不會那麼累我還是建議你遵守慣例。

## 標題

接下來是標題。標題有六種大小，分別是`<h1>`、`<h2>`、`<h3>`、`<h4>`、`<h5>`、`<h6>`。

```
<h1>H1</h1>
<h2>H2</h2>
<h3>H3</h3>
<h4>H4</h4>
<h5>H5</h5>
<h6>H6</h6>
```

建議從`<h1>`開始依序做使用，保持完整的架構。

## 無序清單

無序清單是用`<ul>`元素建立的，而清單內的每一個項目都是`<li>`元素。

```
<ul>
  <li>a</li>
  <li>b</li>
  <li>c</li>
</ul>

```

- a
- b
- c

## 有序清單

有序清單是用`<ol>`元素建立的，而清單內的每一個項目都是`<li>`元素。

```
<ol>
  <li>a</li>
  <li>b</li>
  <li>c</li>
</ol>

```

1. a
2. b
3. c

## 巢狀清單

而清單裡可以有清單，只要把清單放在`<li>`元素裡就可以了。

```
<ul>
         <li>玉米濃湯</li>
         <li>鮪魚吐司</li>
         <li>薯條
            <ul>
              <li>鹽味</li>
              <li>胡椒鹽</li>
              <li>番茄醬</li>
            </ul>
         </li>
     </ul>
```
<ul>
         <li>玉米濃湯</li>
         <li>鮪魚吐司</li>
         <li>薯條
            <ul>
              <li>鹽味</li>
              <li>胡椒鹽</li>
              <li>番茄醬</li>
            </ul>
         </li>
     </ul>

## 超連結

假設你想要連結到某個網站，你可以使用`<a>` (anchor)元素，並在`href`(hypertext reference)屬性中指定連結的網址，而在`<a>`元素中間的文字就是連結的文字。

```
<a href="連結">顯示文字</a>
```

比如說我們要連結到Google首頁，我們可以這樣寫:

```
<a href="https://www.google.com">Goolge</a>
```

[Google](https://www.google.com/)

## 圖片

如果你想要插入圖片，你可以使用`<img>` (iamge)元素，並在`src` (source)屬性中指定圖片的來源，`alt`屬性中填入圖片的敘述。如果圖片無法顯示時就會使用這個替代文字，而Google也會透過這個文字了解圖片內容。

```
<img src="來源" alt="文字敘述">

```

比如說這個是從Google首頁抓下來的圖片，我們可以這樣寫:

```
<img src="<https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png>" alt="Google">

```

![](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)



## 表格

表格是用`<table>`元素建立的，而表格內的每一排都是`<tr>`(table row)元素，而每一個格子都是`<td>`(table data)元素，而表格的標題則是`<th>`(table header)元素。

```
<table>
  <tr>
    <th>國家</th>
    <th>首都</th>
    <th>人口</th>
    <th>語言</th>
  </tr>
  <tr>
    <td>USA</td>
    <td>Washington D.C.</td>
    <td>309 million</td>
    <td>English</td>
  </tr>
  <tr>
    <td>Sweden</td>
    <td>Stockholm</td>
    <td>9 million</td>
    <td>Swedish</td>
  </tr>
</table>

```

<table>
  <tr>
    <th>國家</th>
    <th>首都</th>
    <th>人口</th>
    <th>語言</th>
  </tr>
  <tr>
    <td>USA</td>
    <td>Washington D.C.</td>
    <td>309 million</td>
    <td>English</td>
  </tr>
  <tr>
    <td>Sweden</td>
    <td>Stockholm</td>
    <td>9 million</td>
    <td>Swedish</td>
  </tr>
</table>



## 輸入

```
<input type="number"
       step="10"
       min="0"
       max="1000">

```



```
<input type="radio" name="color" value="red"> red<br>
<input type="radio" name="color" value="green"> green<br>
<input type="radio" name="color" value="blue"> blue

```



```
<input type="checkbox" checked> Subscribe to newsletter
<input type="checkbox"> Subscribe to newsletter
```



每週一早上六點，我們會在YouTube和各大Podcast平台不定時更新。如果你喜歡文字版，也歡迎在Instagram和Google新聞追蹤毛哥EM資訊密技。
我是毛哥EM，讓我們下週再見！