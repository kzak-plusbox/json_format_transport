import os
import glob
import json
import datetime
import traceback

from util_module import utility

logger = utility.get_logger(__name__)


def create_csv(dict_datas):
    try:
        record_create_ts = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        file_create_dt = (datetime.datetime.now()).strftime('%Y%m%d')

        flg = False
        csv_list = []
        if not os.path.exists('.\\files\\z_output_csv\\shopping_data_{0}.csv'.format(file_create_dt)):
            # ファイルなければヘッダ追加
            flg = True
            csv_list.append('店名,購入日時,作品名,作者,金額,購入数,レコード作成日時')

        for data in dict_datas:
            csv_list.append('通販本屋MAX,' + data['shopping_datetime'] + ',' + data['name'] + ',' + data['author'] + ',' \
                        + str(data['price']) + ',' + str(data['buy_num']) + ',' + record_create_ts)

        with open('.\\files\\z_output_csv\\shopping_data_{0}.csv'.format(file_create_dt), mode='a', encoding='UTF-8') as wf:
            wf.write('\n'.join(csv_list))
        
        if flg:
            logger.info('shopping_data_{0}.csv'.format(file_create_dt) + 'を新規作成しました。')
        else:
            logger.info('shopping_data_{0}.csv'.format(file_create_dt) + 'に追記しました。')
    except:
        logger.error('エラー')
        raise


def main():
    try:
        h = []
        # JSONファイル読み込み
        for f_path in glob.glob('.\\files\\json_ptn1\\*'):
            with open(f_path, mode='r', encoding='UTF-8') as f:
                h.extend(json.load(f))

        logger.info("JSON読み込み正常終了。CSVファイルを作成します。")

        # CSVファイル作成
        create_csv(h)

        return 0
    except:
        logger.error(traceback.format_exc())
        return -1



if __name__ == "__main__":
    logger.info('～～ フォーマットパターン1 処理開始 ～～')
    if main() == 0:
        logger.info('～～ 正常終了 ～～')
    else:
        logger.error('～～ 異常終了 ～～')

