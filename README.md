# TOC-Project F74052308 許芸禎
聊天機器人: 威廉・莎士比亞William Shakespeare

## 使用方法
1. 開啟ngrok
2. 執行app.py
3. 開啟機器人並輸入訊息

## 如何和機器人互動
1. 使用者輸入莎士比亞著名的四大喜劇和四大悲劇的其中一部英文劇名，範例如下：
*  Romeo and Juliet(羅密歐與茱麗葉)
*  King Lear(李爾王)
*  Othello（奧賽羅）
*  Hamlet（哈姆雷特）
*  A Midsummer Night's Dream（仲夏夜之夢）
*  The Merchant of Venice（威尼斯商人）
*  Much Ado about Nothing（無事生非）
*  twelfth night, or what you will（第十二夜）

2. 機器人會回覆該劇中一段著名的英文台詞
3. 使用者再輸入講這句台詞的角色，和上述劇本對應的角色如下。機器人等到使用者答對後才會做出反應：good guess, you're right!
* Juliet
* King Lear
* Othello
* Hamlet
* Helena
* Jessica
* Claudio
* Orsino 

4. 使用者也可以在輸入劇名之後輸入: picture please,機器人就會回覆使用者該劇的藝術作品圖片

## FSM圖和state說明
![](https://i.imgur.com/8IOfzTA.jpg)
使用者輸入劇名->進入stateX(X = 1~8)，之後有兩種走法：
* 輸入角色名且答對->進入stateRX後回到user
* 輸入：picture please，進入statePX後回到user