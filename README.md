# 概要

## [blueqat](https://github.com/Blueqat/Blueqat)
量子コンピューターのSDK

## インストール
```
git clone https://github.com/kutakutat/blueqat_primer.git
```

## 実行ファイル
/opt/blueqat_demo.py
あらかじめ代表的な量子回路を関数として組んでいます

# 手順

## 環境構築
docker を起動した状態で
docker-compose.yml のある ディレクトリで以下を実行
```
docker-compose up -d --build
```

## コンテナへ接続
起動させたコンテナに接続 
```
docker-compose exec python3 bash
```

## pythonを対話モードで起動
blueqat_demo.py のあるディレクトリで python を対話モードで実行
```
cd ./opt
python
```

## blueqat で計算
```
>>> from blueqat_demo import *
>>> plus_2qbit(100) # 足し算 を 100回
>>> simple_grover_2qbit(10) # 2量子ビットの Grover を 10回
>>> simple_grover_3qbit(100) # 3量子ビットの Grover を 100回
```

## python を終了
```
>>> exit()
```

## コンテナから抜ける
```
exit
```

## コンテナを落とす
```
docker-compose down
```

