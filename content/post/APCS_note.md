+++
author = "毛哥EM"
title = "【重點整理】APCS筆記(新手請右轉)
date = "2022-07-17"
description = "這是我自己學習的筆記，紀錄一些準備考試的重點，不適合新手閱讀"

categories = [
    "筆記",
]
thumbnail = "images/thumbnails/notes.png"
featureImage = "https://em-tec.github.io/images/thumbnails/notes.png"
shareImage = "https://em-tec.github.io/images/thumbnails/notes.png"
+++
這是我自己學習的筆記，紀錄一些準備考試的重點，不適合新手閱讀
<!--more-->
{{%/* notice note "好久不見!" */%}}
因為要準備會考已經非常久沒有發文了，不過這一篇是我自己寫的一些重點整理筆記，且會持續更新。適合已經對程式有概念的人閱讀。如果你對C語言有興趣可以參考[這篇文章](https://ithelp.ithome.com.tw/users/20119869/ironman/4724)，我覺得寫得不錯w
{{%/* /notice */%}}

## C規則

### 輸出

```c
printf("字串");
printf("字串或格式代碼",變數1,變數2,變數3);
puts("ABC");//自動換行，但沒有格式化字串的功能
```

* `\n`:換行
* `\t`:自動對齊
* `\a`: 鈴聲
* `\b`: 游標(下個文字開始顯示的位置)倒退一格
* `\r`: 游標倒退到這行的開頭

### 變數
型態 | 說明 | 範圍
-----| ---- | -----
long int|長整數|±21億
int|整數|±21億
short int|短整數|±32768
char|字元|0~255
float|浮點數|1.2~3.4e±38
double|倍精度浮點數|1.2~1.8e±308

#### 快速宣告

雖然沒有硬性規定，但C語言中可以用 `f`, `F` 標示數值是浮點數，整數時可以用 `.` 標示

```c
int x=1, y=10, z=100;
int x=y=z=100;
```

### 關鍵字

auto, do, goto, signed, break, double, if, sizeof, case, else, int, static, char, enum, long, struct, const, extern, register, switch, continue, float, return, typedef, default, for, short, union

### 科學記號

* 123=1.23E+2
* 0.00041=4.1e-4