# CSVファイル作成
## 全体概要
2つのフォーマットのjsonファイルがある。  
それぞれを同じ形式のCSVにしてファイルに出力する。  
プログラムは2つ。  
- fmt_json_ptn1.py
  - JSONフォーマットパターン1をCSVに変換、ファイル出力する。
- fmt_json_ptn2.py
  - JSONフォーマットパターン2をCSVに変換、ファイル出力する。

## 仕様
出力するCSVファイル名は「shopping_data_[yyyyMMdd].csv」  
※[yyyyMMdd]は現在日。  
既に存在する場合は追記する。  
CSVに出力する項目は以下の通り

店名,購入日時,作品名,作者,金額,購入数,レコード作成日時  
・店名はプログラムで保持  
・レコード作成日時は処理実行日時  
・上記以外の項目はJSONファイルが保持

## フォルダ構造
以下の通り
```
-fmt_json_ptn1.py
-fmt_json_ptn2.py
-util_module
  -__init__.py
  -utility.py
-files
  -json_ptn1
    -jsonfile.txt   -> フォーマットパターン1のJSONファイル
  -json_ptn2
    -jsonfile.txt   -> フォーマットパターン2のJSONファイル
  -z_output_csv
    -shopping_data_[yyyyMMdd].csv
```

## 注意事項
pythonファイルがいるディレクトリを**カレントディレクトリ**にして実行しないとちゃんと動きませぬ・・・。