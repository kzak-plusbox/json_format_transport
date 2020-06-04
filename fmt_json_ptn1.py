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

        new_create_flg = False
        csv_list = []
        if not os.path.exists('C:\\workspace\\会社\\研修\\json_format_transport.git\\files\\z_output_csv\\shopping_data_{0}.csv'.format(file_create_dt)):
            # ファイルなければヘッダ追加
            new_create_flg = True
            csv_list.append('店名,購入日時,作品名,作者,金額,購入数,レコード作成日時')

        for data in dict_datas:
            csv_list.append('通販本屋MAX,' + data['shopping_datetime'] + ',' + data['name'] + ',' + data['author'] + ',' \
                        + str(data['price']) + ',' + str(data['buy_num']) + ',' + record_create_ts)

        with open('C:\\workspace\\会社\\研修\\json_format_transport.git\\files\\z_output_csv\\shopping_data_{0}.csv'.format(file_create_dt), mode='a', encoding='UTF-8') as wf:
            wf.write('\n'.join(csv_list) + '\n')
        
        if new_create_flg:
            logger.info('shopping_data_{0}.csv'.format(file_create_dt) + 'を新規作成しました。')
        else:
            logger.info('shopping_data_{0}.csv'.format(file_create_dt) + 'に追記しました。')
    except:
        logger.error('エラー')
        raise


def main():
    try:
        dict_datas = []
        # JSONファイル読み込み
        for f_path in glob.glob('C:\\workspace\\会社\\研修\\json_format_transport.git\\files\\json_ptn1\\*'):
            with open(f_path, mode='r', encoding='UTF-8') as f:
                dict_datas.extend(json.load(f))

        logger.info("JSON読み込み正常終了。CSVファイルを作成します。")

        # CSVファイル作成
        create_csv(dict_datas)

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
