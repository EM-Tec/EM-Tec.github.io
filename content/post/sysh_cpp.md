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

我整理出C++題目常見的題目並寫出我認為的最佳解(取自西苑高一電腦課)。也有提供一些減少程式碼的常用技巧。如果解不出來到想砸電腦或想只到更簡單的方法可以來看看
<!--more-->
{{% notice warning "警告" %}}
這裡的程式僅供參考，請不要偷懶直接複製貼上，小考你不會過的。

**目前只更新到308**

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

###　201.運算子

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

## Ch.3

### 301.奇偶同籠?

```c++
#include<iostream>

using namespace std;
int main() {
  int a;
  cin >> a;
  if (a % 2 == 0) {
    cout << "偶數";
  } else {
    cout << "奇數";
  }
  return 0;
}
```

### 302.及格?

```c++
#include<iostream>

using namespace std;
int main() {
  int a;
  cin >> a;
  if (a >= 60) {
    cout << "成績及格";
  } else {
    cout << "成績不及格";
  }
  return 0;
}
```

### 303.幾科不及格

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

```c++
#include<iostream>

using namespace std;
int main() {
  int a[3], b;
  cin >> a[0] >> a[1] >> a[2];
  for (int y: a)
    if (y > b) b = y;
  cout << "最大值=" << b;
  return 0;
}
```

### 308.比不完

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

這些應該夠你們用了，剩下的有空再繼續更新。