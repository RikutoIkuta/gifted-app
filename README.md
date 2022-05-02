# gifted_app

才能と個性のプラットフォーム

## ■ 作成目的

それぞれの才能と個性の顕在化

## ■ 概要

絵・写真・俳句など様々な項目において下記のようなことをアプリ内で実施  
1.週ごとにお題を決め、「いいね」数でランキング。（ユーザーの投票など方式は要検討。）  
2.投票が終了後、 良いと思った作品は購入可能 3.人気になれば、ファンが増える
(概要についてはイメージなので、今度深掘りしましょう。)
→ フォロー数は見えるかせず、それぞれの個人プロフィールから閲覧することが可能

## このアプリを通して得られること

・各個人の個性と才能に価値を与え、自信につなげる。

## 種類

- 絵
- 写真
- 声(声優)
-

## ■ 類似サービス/独自性

大きく分けて既存のサービスモデルは２つ

- ココナラ、ミツモア ⇨ 才能を「買う」モデル
- ボケてやプレバトなど ⇨ 才能を「見る」モデル

## 環境

■ バックエンド

- Python/Django

■ フロントエンド

- Typescript/Next.js
- TailwindCSS
- https://nerdcave.com/tailwind-cheat-sheet
- Next.js の環境
- https://zenn.dev/higa/articles/d7bf3460dafb1734ef43

■ テスト

- Jest
- Cypress

■ コードフォーマッター

- Prettier
- ESlint

■ デプロイ

- Vercel(フロントエンド)
- GCP(バックエンド)

## ■ デザイン

- FigmaURL  
  https://www.figma.com/file/poUaZX1p3giIaVpLJFt1OF/gifted_app?node-id=0%3A1

- URL 設計
  /api.dio

- DB 設計
  /db.dio

## ■ 裏機能

- ログインしていなくても、投稿一覧は見ることができる
- 1 日１回まで投稿が可能
- お題に対しては、１回しか投稿できない。
- 1 度の投稿に修正は 2 回まで
- ここで生まれた、メンバーとして
- 画像は Firbase で管理する
- 問題のあるユーザーは３回警告でアカウントを停止する

## エラー内容

- ログイン失敗時
- オフライン画面
- 投稿画像のサイズが大きすぎるとき

## 違反内容

- 盗作
- お題と異なることを投稿

## ■ 機能(未完)

- ログイン
- ログアウト
- お気に入り機能
- 投稿機能
- 投稿編集機能
- 投票機能

## ■ 必要な画面

- トップページ
- 項目選択画面
- 投稿一覧画面
- マイアプロフィール画面
- ログイン画面
- 投稿編集画面
- ログアウト画面
- オフライン画面
- マイプロフィール編集画面
- ユーザー詳細画面(ユーザーの画像をタッチしたら詳細画面を見ることができる)

## 開発環境

■ 本番サーバー  
main ブランチ  
↑  
■ テストサーバー  
develop ブランチ  
↑  
■ 各自作業
feature ブランチ
(ex.feature/add_loginFunc)


## ■ 開発ルール

- キャメルケース
- 処理完了するたびに、feature ブランチから develop ブランチにプルリクを送る。

## ■ 段階

## フェーズ 1

- 絵のプラットフォーム

## フェーズ 2

- 課金システムの導入
- 週ごとにお題を変える機能
- デザイン修正
- 俳句とか違う項目のものを作成する
- 賞金制度の導入

## 初期環境構築方法

pip3 install -r requirements.txt
python3 manage.py createsuperuser
python manage.py runserver

メールアドレス:sampletest@ma.jp
password:hogehoge5656

# tailwindcss

npm i -D tailwindcss@latest postcss@latest autoprefixer@latest

# tailwind 設定ファイル

npx tailwindcss init -p

## ローカルで jwt 認証のテストをするやり方

https://qiita.com/kachuno9/items/1fa592093c0fd7074aa2


