+++
author = "毛哥EM"
title = "【重點整理】APCS筆記"
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
{{% notice note "好久不見!" %}}
因為要準備會考已經非常久沒有發文了，不過這一篇是我自己寫的一些重點整理筆記，且會持續更新。程式語言教學只會寫C與其他語言不同的語法，適合已經對程式有概念的人閱讀。如果你對C語言有興趣可以參考[這個系列文章](https://ithelp.ithome.com.tw/users/20119869/ironman/4724)，我覺得寫得不錯w
{{% /notice %}}

# C規則

只寫和javascript不同的地方，或我自己覺得重要或會忘記的部分

## 輸出

```c
printf("字串");
printf("字串或格式代碼",var1,var2,var3);
puts("ABC");//自動換行，但沒有格式化字串的功能
```

* `\n`:換行
* `\t`:自動對齊
* `\a`: 鈴聲
* `\b`: 游標(下個文字開始顯示的位置)倒退一格
* `\r`: 游標倒退到這行的開頭

## 變數

### 型態

加上 `unsigned`，會變成只能表示正數和0，但範圍 **大小** 不變。如`unsigned char`的範圍是0~2^8

型態 | 說明 | 範圍
---- | ---- | ----
long int | 長整數 | ±21億
int | 整數 | ±21億
short int | 短整數 | ±32768
char | 字元 | 0~255
float | 浮點數 | 1.2~3.4e±38
double | 倍精度浮點數 | 1.2~1.8e±308

### 宣告

以下4種方式都可以

```c
int x
int x=1
//一次多個
int x=1, y=10, z=100;
int x=y=z=100;
```
雖然沒有硬性規定，但C語言中可以用 `f`, `F` 標示數值是浮點數，整數時可以用 `.` 標示

### 指派/指定 運算子(Assignment Operator)

前面用過的 = 就是其中一種，執行時會先將等號右邊的值算出來，再指派給左邊的變數
`a=a+1`等效`a+=1`等效`a++`
`a=a-1`等效`a-=1`等效`a--`
`a=a*2`等效`a*=2`
`a=a/2`等效`a/=2`
`a=a%2`等效`a%=2`

### 輸入
```
//輸入整數、字元、浮點到變數x、y、z
scanf("%d%c%d", &x, &y, &z);
```
## 邏輯判斷
### if、switch、while、for
和js大同小異
```c
//if
if(ture){
	printf("yes");
}
else{
	printf("no");
}
//大括號內只有一行可省略大括號
if(x>100)
	printf("x is greater than 100.");

//switch
switch(x){
	case 0: case 7:
		printf("A\n");
		//x=0或是7都會印出A
		break;
	case 2: case 5:
		printf("B\n");
		break;
	case 4: case 3:
		printf("C\n");
		break;
	case 6: case 1:
		printf("D\n");
		break;
}

//while
while(ture){
	printf("forever printing");
}

//for 大括號內只有一行一樣可省略大括號
int i;
for(i=0; i!=5; i++)
	printf("%d", i);//輸出12345
	
```
{{% notice note "程式碼縮排" %}}
和js一樣沒有規定，不縮也可以  
通常以一個 Tab 鍵(在鍵盤左邊) 為單位，每多一個大括號，就多空一個單位。如果大括號被省略還是要縮排
{{% /notice %}}

### break & continue

* break: 強制結束迴圈
* continue: 跳過這次的區塊，但迴圈不會結束

## 預留位置(Format placehold)

整數用 `%d`，浮點數用 `%f`，字元用 `%c`

%hd, %d, %lld 都是將資料轉換成整數  
能處理的位數 %hd < %d < %lld

## 關鍵字

auto, do, goto, signed, break, double, if, sizeof, case, else, int, static, char, enum, long, struct, const, extern, register, switch, continue, float, return, typedef, default, for, short, union

## 科學記號

* 123=1.23E+2
* 0.00041=4.1e-4
