# Determining-Emotional-Similarity-in-Python

Python で感情の類似度判定

Python で文章と感情を表す単語との類似度を判定するプログラム

# DEMO

感情ごとのデモ。

## 怒り

「背中の傷は剣士の恥だ」という文章が**「怒り」**の感情とどれだけ読み取れるのか。

下記の通りの結果となった。

- 単語 : 恥 → 怒り類似度 : 0.5475583076477051
- 単語 : 傷 → 怒り類似度 : 0.32582271099090576
- 単語 : 背中 → 怒り類似度 : 0.28920072317123413
- 単語 : 剣士 → 怒り類似度 : 0.17064890265464783

「恥」という単語が「怒り」との類似度が約 54%という結果となった。

## 嬉しい

「背中の傷は剣士の恥だ」という文章が**「嬉しい」**の感情とどれだけ読み取れるのか。

下記の通りの結果となった。

- 単語 : 恥 → 怒り類似度 : 0.277591735124588
- 単語 : 背中 → 怒り類似度 : 0.20289340615272522
- 単語 : 傷 → 怒り類似度 : 0.06647129356861115
- 単語 : 剣士 → 怒り類似度 : -0.05935478210449219

「恥」という単語が「嬉しい」との類似度が約 27%という結果となった。
「剣士」という単語は、「嬉しい」との類似度が約-5％という結果となった。
類似度のレンジは、-1 ～ 1 となっている。

# Features

文章から感情を簡易的に判定する。
Word2VecModel を作成している。

# Requirement

## application

- Python 3.7.3
- MeCab mecab of 0.996

## Python Install package

- gensim 3.8.3
- mecab 0.996.2
- mecab-python-windows 0.996.3

# Usage

```bash
git clone https://githubcomair-flowDetermining-Emotional-Similarity-in-Python.git
python main.py
```

# Note

このプログラムの諸注意事項

## Word2Vec

Word2VecModel を作成している。
main.py の path にそのモデルのパスを指定している。

## MeCab

MeCab の辞書に、NEologd を使用してます。
