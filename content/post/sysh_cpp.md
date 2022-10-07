+++
author = "毛哥EM"
title=  "【C++】常見題目解答"
description=  "西苑高一電腦課C++題目的最佳解。如果解不出來到想砸電腦或想只到更簡單的方法可以來看看"
date=  "2022-09-08"
tags = ["C++"]
categories = ["Development"]
thumbnail=  "images/thumbnails/notes.png"
featureImage = "https://em-tec.github.io/images/thumbnails/notes.png"
shareImage = "https://em-tec.github.io/images/thumbnails/notes.png"
+++

我整理出C++題目常見的題目並寫出我認為的最佳解(取自西苑高一電腦課)。也有提供一些減少程式碼的常用技巧。如果解不出來到想砸電腦或想只到更簡單的方法可以來看看
<!--more-->
{{% notice note "沒事都來西苑高中C語言程式教學營隊" %}}
快來報名西苑高中C語言程式教學營隊!完全免費！附午餐！
<https://docs.google.com/forms/d/e/1FAIpQLSdXEOR8OvjXlZVseeq5A4re5a_05a95uGBqGqI5WLzRfWSXQw/viewform?usp=sf_link>
學長姐將帶你走入真正需要用文字編輯的程式語言，

快來加入我們吧，從最基礎的c語言帶你認識

這也是真正職場上能用到的語言喔

寫得好直接畢業即就業，心動不如馬上報名，全程參加者發予證書，報名額滿為止。

課程大綱：

1.程式語言簡介
2.編程環境安裝&介紹
3.C語言基礎介紹
4.基礎教學
5.進階教學
6.編寫計算機程式
7.程式語言的運用
8.物聯網實際應用

講師:資訊志工教學組(高二，三學生)

地點:西苑高中圖書館五樓

對象:西苑國中部二三年級學生，高中部一年級學生

課程時間:10/16(日)09:00-1600(共7小時)

費用:免費，提供午餐


有任何問題均可聯絡西苑高中圖書館！

即時資訊及錄取通知都由mail發送 請隨時關注信箱！！

主辦單位:西苑高中資訊志工教學組(學生團體)

指導單位:西苑高中圖書館
{{% notice warning "警告" %}}
網站終於搶救成功啦!這兩天來更新!這裡的程式僅供參考，請不要偷懶直接複製貼上，小考你不會過的。

關於有人問我是誰，選單有各種連結。

**目前只更新到410**
{{% /notice %}}

# 小提示

當然如果你只是想看解答<s>然後像月同學一樣手機開超大聲打音遊</s>可以[點我跳到解答](#題目解答)

{{% notice note "C語言" %}}
如果你忘記C語言的語法想看看可以閱讀[這篇文章](https://em-tec.github.io/post/apcs_note/)，不過相信你學過C++就不會想要碰它了。
{{% /notice %}}

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
# 題目解答

就..雖然我很貼心還給你了複製鍵...但有問題要問...

裡面的換行空格是大家的習慣寫法，可以參考。且你會發現雖然空格多一點程式還是比標準答案少

{{% notice info "提醒" %}}
裡面有一些東西還沒有教過，有興趣可以問我或是Google。

**目前只更新到308**

{{% /notice %}}

## Ch.1

### 101.Hello C++

```C++
#include<iostream>

using namespace std;
int main() {
  cout << "Hello C++";
  return 0;
}
```

### 102.BMI

```c++
#include<iostream>

using namespace std;
int main() {
  float weight, height, BMI;
  cin >> weight >> height;
  BMI = weight / ((height / 100) * (height / 100));
  cout << "BMI為" << BMI;
  return 0;
}
```

## Ch.2

### 201.運算子

{{% notice note "提示筆記" %}}
先乘除後加減(依照優先順序)
* 有括弧的先計算
* 多個括弧皆使用小括弧。EX:((8+9)-7)
* 整數跟整數相除的結果為整數

|運算子 | 定義  | 優先順序  | 結合律
|---|---  |---  | ---
|++/--  | 後置遞增/遞減  | 2 |  左
|++/--  | 前置遞增/遞減  | 3 |  右
|+/-  | 正負號  | 3  | 右
|* |  乘法  | 5  | 左
|/ | 除法 |  5  | 左
|% |餘數(mod) | 5 |左
|+/- |加法/減法  | 6 |左

{{% /notice %}}

```c++
#include<iostream>

using namespace std;
int main() {
  int x, y;
  cin >> x >> y;
  cout << x << " 加 " << y << " 的和是 " << x + y << endl;
  cout << x << " 減 " << y << " 的差是 " << x - y << endl;
  cout << x << " 乘 " << y << " 的積是 " << x * y << endl;
  cout << x << " 除 " << y << " 的結果是 " << 1.0 * x / y << endl;
  cout << x << " 除 " << y << " 的商是 " << x / y << endl;
  cout << x << " 除 " << y << " 的餘數是 " << x % y << endl;
  return 0;
}
```

### 202.成績計算

請製作一個程式，輸入五個成績，計算總和與平均並輸出

{{% notice note "提示筆記" %}}
C++換行可以用`<<endl`，但C語言的`\n`明顯短了三倍
{{% /notice %}}

```c++
#include<iostream>

using namespace std;
int main() {
  float sum, a, b;
  for (int i = 1; i < 6; ++i) {
    cin >> b;
    a += b;
  }
  cout << "總和:" << a;
  cout << "\n平均:" << a / 5;
  return 0;
}
```

### 203.矩形周長面積

請製作一個程式，輸入長方形的長 寬，並計算周長與面積

```c++
#include<iostream>

using namespace std;
int main() {
  int x, y;
  cin >> x >> y;
  cout << "周長=" << 2 * (x + y);
  cout << "\n面積=" << x * y;
  return 0;
}
```

### 204.畢氏定理

請製作一個程式，輸入直角三角形兩邊長，利用畢氏定理求斜邊長

{{% notice note "提示筆記" %}}

`sqrt(x)` 回傳 `x` 的平方根(Square Root)

{{% /notice %}}

```c++
#include<iostream>
#include<cmath>

using namespace std;
int main() {
  float x, y;
  cin >> x >> y;
  cout << "斜邊長=" << sqrt(x * x + y * y);
  return 0;
}
```

### 205.兩點距離

請製作一個程式，輸入二維中兩點座標，計算出兩點距離

{{% notice note "提示筆記" %}}

`pow(x, y)` 回傳 `x` 的 `y` 次方

{{% /notice %}}

```c++
#include<iostream>

#include<cmath>

using namespace std;
int main() {
  float x1, x2, y1, y2;
  cin >> x1 >> y1 >> x2 >> y2;
  cout << "兩點距離=" << sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
  return 0;
}
```

### 206.兩點求一線

請製作一個程式，輸入二維中兩點座標，計算出通過兩點的直線方程式

```c++
#include<iostream>
#include<cmath>

using namespace std;
int main(){
	float x1,x2,y1,y2,m;
	cin>>x1>>y1>>x2>>y2;
	cout<<"方程式:y="<<(y1-y2)/(x1-x2)<<"x+"<<(y1*x2-y2*x1)/(x2-x1);
}
```

{{% notice info "原本想法" %}}

斜率`m`為y變化量除以x變化量。將一數代數`y=mx+b`即可求出b並寫出方程式。`b`只會用一次算出來直接輸出，不用多設一個變數。

不過浮點數是使用科學記號儲存，有一定的誤差 當斜率本身已經有誤差時，再用來算出截距，誤差將擴大。因此最後一個測資會有誤差。

```c++
#include<iostream>
#include<cmath>
using namespace std;
int main(){
	float x1,x2,y1,y2,m;
	cin>>x1>>y1>>x2>>y2;
	m=(y1-y2)/(x1-x2);
	cout << "方程式:y=" << m << "x+" << y2-x2*m;
}
```

{{% /notice %}}

## Ch.3

### 301.奇偶同籠?

請製作一個程式，可以讓使用者輸入一個整數，判斷是奇數還是偶數

{{% notice note "提示筆記" %}}

如果否則的語法是

```c++
if (條件式){
	程式區塊;
} else {
    程式區塊;
}
```

如果大括號裡面只有一行程式可以省略

{{% /notice %}}

```c++
#include<iostream>

using namespace std;
int main() {
  int a;
  cin >> a;
  if (a % 2 == 0) cout << "偶數";
  else cout << "奇數";
  return 0;
}
```

### 302.及格?

請製作一個程式，讓使用者輸入一個成績，顯示「成績及格」或「成績不及格」

```c++
#include<iostream>

using namespace std;
int main() {
  int a;
  cin >> a;
  if (a >= 60) cout << "成績及格";
  else cout << "成績不及格";
  return 0;
}
```

### 303.幾科不及格

請製作一個程式：

1. 可以輸入五個成績
2. 計算有幾科不及格
3. 
{{% notice note "提示筆記" %}}
這裡使用了`for-each`循環。 它將`y`設置為`a`的第一個元素，運行大掛號（可省略）的程式，然後它將`y`設置為`a`的第二個元素，然後...

使用它是因用`for (int i = 0; i < 2; i++ )`太長了（如果要自動判斷陣列有多長要打`for (int i = 0; i < i.length; i++ )`）。重點是要存取清單的內容要用`a[i]`而不是`i`
{{% /notice %}}

```c++
#include<iostream>

using namespace std;
int main() {
  int a[5], b = 0;
  cin >> a[0] >> a[1] >> a[2] >> a[3] >> a[4];
  for (int y: a)
    if (y < 60) b++;
  cout << "共" << b << "科不及格";
  return 0;
}
```

### 304.明年當學弟/妹?

請製作一個程式：
1. 可以輸入五個成績
2. 判斷明年是否當學弟妹(不及格科數達一半)


```c++
#include<iostream>

using namespace std;
int main() {
  int a[5], b = 0;
  cin >> a[0] >> a[1] >> a[2] >> a[3] >> a[4];
  for (int y: a)
    if (y < 60) b++;
  if (b > 2) cout << "明年當學弟妹";
  else cout << "明年當學長姊";
  return 0;
}
```

### 305.比大小

請製作一個程式，輸入兩個正整數，輸出較大者

```c++
#include<iostream>

using namespace std;
int main() {
  int a, b;
  cin >> a >> b;
  if (a > b) cout << a;
  else cout << b;
  return 0;
}
```

### 306.本丸好呷

某數字商店飯糰第二件59折，以低價者計。請製作一個程式，輸入兩個正整數，代表兩顆飯糰的定價，請計算優惠後的總價。

```c++
#include<iostream>

using namespace std;
int main() {
  int a, b, c;
  cin >> a >> b;
  if (a > b) c = 0.59 * b + a;
  else c = 0.59 * a + b;
  cout << "優惠價=" << c;
  return 0;
}
```

### 307.比仨大

請製作一個程式，輸入三個正整數，輸出最大者

**更新:最大值b如果一開始沒有給定值會被設為0。故先將b設為第一個數再進行比較。**

```c++
#include<iostream>
using namespace std;
int main(){
  int a[3];
  cin>>a[0]>>a[1]>>a[2];
    int b = a[0];
    for( int y : a ) if(y>b) b=y;
        cout<<"最大值="<<b;
    return 0;
}
```

### 308.比不完

請製作一個程式，輸入五個正整數，輸出最大者

```c++
#include<iostream>

using namespace std;
int main() {
  int a[5], b;
  cin >> a[0] >> a[1] >> a[2] >> a[3] >> a[4];
  for (int y: a)
    if (y > b) b = y;
  cout << "最大值=" << b;
  return 0;
}
```

### 309.正負?

請製作一個程式，判斷輸入的數字是正數、負數還是0

```c++
#include<iostream>

using namespace std;
int main() {
  int a;
  cin >> a;
  if (a > 0) cout << "正數";
  else if (a == 0) cout << "零";
  else cout << "負數";
  return 0;
}

```

### 310.分級

請製作一個程式，讓使用者輸入成績，並判斷等級：
* 90~100分：A
* 80~89分：B
* 70~79分：C
* 60~69分：D
* 0~59分：F
```c++
#include<iostream>
using namespace std;
int main() {
  int a;
  cin >> a;
  switch (a / 10) {
  case 10:
  case 9:
    cout << "A";
    break;
  case 8:
    cout << "B";
    break;
  case 7:
    cout << "C";
    break;
  case 6:
    cout << "D";
    break;
  default:
    cout << "F";
  }
  return 0;
}
```

### 311.電腦教室不能帶飲料進來

某項數字商店飲料定價87元，第二件8折，第三件77折
請製作一個程式可以輸入件數計算價錢

```c++
#include<iostream>

using namespace std;
int main() {
  int a,c;
  float b[4]={0,1,1.8,2.57};
  cin >> a;
  c=a/3*223.59+b[a%3]*87;
  cout << "總價=" << c;
  return 0;
}
```

### 312.一塊錢玩兩次

ax2 + bx + c = 0，請製作一個程式，輸入a、b、c，解一元二次方程式。
若a = 0則輸出ERROR<br />
令d = b2 - 4ac：<br />
若d = 0，則輸出方程式唯一解x=-b/2a<br />
若d > 0，則輸出方程式兩解x=(-b±√d)/2a<br />
若d < 0，則輸出無實數解<br />


```c++
#include<iostream>

#include<cmath>

using namespace std;
int main() {
  float a, b, c;
  cin >> a >> b >> c;
  if (a == 0) cout << "ERROR";
  else {
    float d = b * b - 4 * a * c;
    if (d < 0) cout << "無實數解";
    else {
      if (d == 0) cout << "唯一解x=" << 0 - b / (a * 2);
      else cout << "兩解:\nx1=" << (0 - b + sqrt(d)) / 2 * a << "\nx2=" << (0 - b - sqrt(d)) / 2 * a;
    }
  }
  return 0;
}
```

### 313.三角形

請製作一個程式，輸入三角形三邊長a、b、c，先判斷能否構成三角形，若無法構成三角形則輸出ERROR，然後評定三角形種類，最後計算三角形面積。
* 假如𝑎2+𝑏2>𝑐2，為銳角三角形
* 假如𝑎2+𝑏2=𝑐2，為直角三角形
* 假如𝑎2+𝑏2<𝑐2，為鈍角三角形
* 令d=(a+b+c)/2，三角形面積=√(d(d−a)(d−b)(d−c))

```c++
#include<iostream>

#include<cmath>

using namespace std;
int main() {
  float a, b, c, d;
  cin >> a >> b >> c;
  if (a > b) {
    d = a;
    a = b;
    b = d;
  }
  if (b > c) {
    d = b;
    b = c;
    c = d;
  }
  if (c >= a + b) {
    cout << "ERROR";
  } else {

    int e = b * b + a * a;
    int f = c * c;
    if (e > f) cout << "銳";
    else
    if (e == f) cout << "直";
    else cout << "鈍";
    float D = (a + b + c) / 2;
    cout << "角三角形\n面積=" << sqrt(D * (D - a) * (D - b) * (D - c));
  }
  return 0;
}
```

## Ch.4

這一段有點尷尬，沒有人叫你用`for`迴圈你幹嘛寫那麼多行跑那麼久?測資要什麼複製貼上就好了。

如果你像用正規的辦法`for`的原型在這裡相信你會的uwu

```c++
for(變數設為;如果...; 變數要...){
  指令區塊;
  [break;]    //跳出迴圈
  [continue;] //跳下一次迴圈
}
```

比如說這兩個程式都會輸出`uwu uwu uwu`

```c++
#include<iostream>

using namespace std;
int main() {
  int i;
  for (i = 0; i < a; i++) {
    cout << "uwu ";
  }
  return 0;
}
```

```c++
#include<iostream>

using namespace std;
int main() {
  for (int i = 0; i < a; i++)
    cout << "uwu ";
  return 0;
}
```

### 401


請列印出1  2  3  4  5  6  7  8 ......19
```c++
#include<iostream>

using namespace std;
int main() {
  cout << "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19";
  return 0;
}
```

### 402

請列印出1  3  5  7  9  11  13  15  17  19

```c++
#include<iostream>

using namespace std;
int main() {
  cout << "1 3 5 7 9 11 13 15 17 19 ";
  return 0;
}
```

### 403

請列印出7  6  5  4  3  2  1  0  -1  -2  -3

```c++
#include<iostream>

using namespace std;
int main() {
  cout << "7 6 5 4 3 2 1 0 -1 -2 -3 ";
  return 0;
}
```

### 405

請列印出7  5  3  1  -1  -3  -5  -7  -9  -11

不要問我404去哪。404找不到此頁面

```c++
#include<iostream>

using namespace std;
int main() {
  cout << "7 5 3 1 -1 -3 -5 -7 -9 -11 ";
  return 0;
}
```

### 406

請製作一個程式計算1~100之和

國小數學會吧...梯形公式。當然你要直接輸出5050也可以

```c++
#include<iostream>

using namespace std;
int main() {
  cout << "5050";
  return 0;
}
```

### 407

輸入兩個整數a,b，計算a到b的合(包含a、b)

例如輸入1跟100，計算1~100之合為5050
```c++
#include<iostream>

using namespace std;
int main() {
  int a, b;
  cin >> a >> b;
  cout << (a + b) * (abs(a - b) + 1) / 2;
  return 0;

}
```

### 408

請製作一個程式，輸入的第一個正整數為班級人數n，代表接下來會有n個正整數，為班上每個人的成績。請計算班級總分。

```c++
#include<iostream>

using namespace std;
int main() {
  int a, b, c = 0, i;
  cin >> a;
  for (i = 0; i < a; i++) {
    cin >> b;
    c = c + b;
  }
  cout << c;
  return 0;
}
```

### 409

請製作一個程式，輸入的第一個正整數為班級人數n，代表接下來會有n個正整數，為班上每個人的成績。請計算班級平均。


```c++
#include<iostream>

using namespace std;
int main() {
  int a, b, c = 0, i;
  cin >> a;
  for (i = 0; i < a; i++) {
    cin >> b;
    c = c + b;
  }
  cout << 1.0 * c / a;
  return 0;
}
```

### 410

請製作一個程式，輸入的第一個正整數為班級人數n，代表接下來會有n個正整數，為班上每個人的成績。請計算班級中不及格的人數。

```c++
#include<iostream>

using namespace std;
int main() {
  int n,a,b=0,i;
  cin >> n;
  for (i = 0; i < n; i++) {
    cin >> a;
    if(a<60) b++;
  }
  cout << b;
  return 0;
}
```

這些應該夠你們用幾週了，剩下的有空再繼續更新。
