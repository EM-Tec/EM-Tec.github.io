+++
author = “毛哥EM”
title = “【yt-dlp】Youtube-dl進化!最強Youtube下載器“
date = “2023-01-28”
description = “還在慢慢用線上工具處裡PDF問題嗎？用PDF Toolkit (pdftk)一行指令完成各種PDF處裡！”
categories = [“軟體分享”]
draft = true
tags = [“Terminal”,“Windows”,“Android”]
+++

市面上的線上Youtube下載器又慢又爛，還有一堆廣告，播放清單太長下載不了。相反的，yt-dlp可以滿足你所有的需求：畫質音質沒有限制、幾乎支援所有影音格式、可以下載整份影片清單、mp3可以加入歌曲封面和專輯資訊、支援字幕、影片縮圖。而且更猛的是，他不只可以下載Youtube的影片，甚至連Facebook、Twitter、Pornhub等地方上的影片都可以下載！

<!—more—>

youtube-dl隨著時間維護變得更少，且下載速度變得很慢。而yt-dlp是他的一個改編版(分支fork)。除了變得更快以外也有更多功能。不過這裡提供的指令都是相同的

[所有支援下載的網站清單](https://github.com/rg3/youtube-dl/blob/master/docs/supportedsites.md)在這裡

## 安裝
### mac
利用mac套件管理神器Homebrew來安裝

1
$ brew install youtube-dl
ffmpeg

如果要使用youtube-dl的轉檔、嵌入字幕、提取音頻、加入專輯封面等等Post-processing的功能的話，則必須安裝FFmpeg

1
$ brew install ffmpeg
下載影片

起手式: 指定影片檔案格式

用-f或是—format指定影片格式，像是mp4, flv, mkv, webm

Example: 下載mp4格式影片

1
$ youtube-dl -f mp4 <url>
品質

Youtube-dl預設會下載最高畫質的影片，但也可以自己選擇想要的品質

Example: 下載解析度不高於480p的影片

1
$ youtube-dl -f ‘bestvideo[height<=480][ext=mp4]+bestaudio/best[height<=480][ext=m4a]’ <url>
嵌入字幕

—list-subs列出所有可下載字幕的語言

—write-sub下載字幕
—embed-sub將字幕嵌入影片中
這兩個參數要一起合併使用

—all-subs下載所有語言字幕

—-sub-lang LANGS指定字幕語言
例如我想要下載まふまふcover的這首『Loser』

首先用—list-subs列出所有可下載字幕的語言

1
$ youtube-dl —list-subs https://www.youtube.com/watch?v=pnnsyjcFnjc

發現zh-TW(繁體中文)是可選的

下載影片並且嵌入中文字幕

1
$ youtube-dl —write-sub —embed-sub —sub-lang zh-tw -f mp4 https://www.youtube.com/watch?v=pnnsyjcFnjc
如果妳想要一次下載所有語言的字幕並且嵌入的話

1
$ youtube-dl —write-sub —embed-sub —all-subs -f mp4 https://www.youtube.com/watch?v=pnnsyjcFnjc
登登！現在下載下來的影片可以選擇字幕囉～
04.png

注意：只有mp4, mkv, webm這些影片格式可以嵌入字幕。

下載音樂

起手式: 指定音樂檔案類型

-x或—extract-audio表示提取音頻
—audio-format後面指定音頻檔案類型，像是 mp3, wav, m4a, aac
Example:

1
$ youtube-dl -x —audio-format mp3 <url>
縮圖和資料

—embed-thumbnail加入專輯封面(其實就是youtube影片上的縮圖)
—-add-metadata加入影片資訊
Example

例如說我要下載米津玄師的這首「ピースサイン」

轉檔成mp3並且加入縮圖和影片資訊

1
$ youtube-dl -x —audio-format mp3 —embed-thumbnail —add-metadata https://www.youtube.com/watch?v=9aJVr5tTTWk
成功下載後可以看到上傳者和影片縮圖

下載playlist

下載整份影片清單

1
$ youtube-dl -f mp4 <playlist-url>
PS: 除了影片網址的部分改成影片清單的網址，其他部分和下載影片一樣。

指定起點和終點

—playlist-start NUMBER: 指定起點
—-playlist-end NUMBER: 指定終點
從第三個影片開始下載到最後一個影片

1
$ youtube-dl —playlist-start 3 -f mp4 <playlist-url>
從第一個影片下載到倒數第二個影片

1
$ youtube-dl —playlist-end 2 -f mp4 <playlist-url>
從第三個影片開始下載到倒數第二個影片

1
$ youtube-dl —playlist-start 3 —playlist-end 2 -f mp4 <playlist-url>
輸出檔名

-o, —output TEMPLATE指定檔名輸出模板。預設是%(title)s-%(id)s.%(ext)s

直接指定檔名叫做test.mp4

1
$ youtube-dl -o “test.mp4” -f mp4 <url>
假如說我覺得影片id很煩很醜，我要把他去掉，只留下影片標題跟副檔名

1
$ youtube-dl 0o ‘%(title)s.%(ext)s’
以下官方範例

Download YouTube playlist videos in separate directory indexed by video order in a playlist

1
$ youtube-dl -o ‘%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s’ https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re
Download all playlists of YouTube channel/user keeping each playlist in separate directory:

1
$ youtube-dl -o ‘%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s’ https://www.youtube.com/user/TheLinuxFoundation/playlists
查詢更多模板參數:
https://github.com/rg3/youtube-dl#output-template

登入

如果有些影片要登入後才能觀看要怎麼辦呢？youtube-dl還有支援帳戶登入的功能:

-u, —username USERNAME
-p, —password PASSWORD
Example:

1
$ youtube-dl -u ‘username@gmail.com’ -p ‘password’ https://www.youtube.com/?v=<video_id>
總結

以上的筆記為超濃縮精華版，youtube-dl還有更多強大的功能和參數可供使用。如果要更詳細的參考文件，可以直接參考官方文件: https://github.com/rg3/youtube-dl