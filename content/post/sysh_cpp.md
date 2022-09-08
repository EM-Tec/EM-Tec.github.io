---
author: 毛哥EM
title: 【C++】常見題目解答
description: 西苑高一電腦課C++題目的最佳解。如果解不出來到想砸電腦或想只到更簡單的方法可以來看看
date: 2022-09-08
categories:
  - "Development"
thumbnail: "images/thumbnails/notes.png"
featureImage: "https://em-tec.github.io/images/thumbnails/notes.png"
shareImage: "https://em-tec.github.io/images/thumbnails/notes.png"
draft: true
---

我整理出C++題目常見的題目並寫出我認為的最佳解(取自西苑高一電腦課)。如果解不出來到想砸電腦或想只到更簡單的方法可以來看看
<!--more-->
{{% notice warning "警告" %}}
這裡的程式僅供參考，請不要偷懶直接複製貼上，小考你不會過的。
{{% /notice %}}

# 小提示

當然如果你只是想看解答然後像月同學一樣手機開超大聲打音遊可以點我跳到解答

## 減少程式碼的常用技巧

這裡講的是真的少打一點，不是全部縮成一排。減少程式碼可以方便閱讀且在bebug(找錯誤)比較方便

### 定義時賦予值
```c++
int a b;
a=87;
```
可以簡化成`int a=87, b;`一行

### 在輸出行內進行運算
```c++
a=x+y;
cout<<a
```
可以簡化成`cout<<x+y;`一行

### if else省去大括號

if else裡面如果只有一行指令可以省去大括號`{}`

```c++
if(a>b){
    cout<<a;
}else{
    cout<<b
}
```

可以簡化成`if(a>b) cout<<a; else cout<<b;`一行

### 數學含式庫<math.h>

列出來怕你忘記
* `M_E` 回傳自然常數 e
* `M_PI` 回傳圓周率 π
* `M_SQRT2` 回傳根號2
* `sin(x)` `cos(x)` `tan(x)` `asin(x)` `acos(x)` `atan(x)` 不解釋bj4
* `exp(x)` 回傳自然常數 e 的 `x` 次方
* `pow(x, y)` 回傳 `x` 的 `y` 次方
* `pow(x)` 回傳10的 `x` 次方
* `sqrt(x)` 回傳 `x` 的根號
* `log(x)` 回傳以 `e` 為底的對數
* `log10(x)` 回傳以10為底的對數
* `abs(x)` 回傳整數 `x` 的絕對值
* `fabs(x)` 回傳實數 `x` 的絕對值

