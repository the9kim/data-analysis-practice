import chardet
import pandas as pd
from pandas import DataFrame


class Csv:
    def check_type_of(self, path):
        with open(path, mode='rb') as f:
            d = f.readline()
            print(chardet.detect(d))

    def read(self, path):
        with open(path, encoding='EUC-KR') as f:
            for i in range(3):
                print(f.readline())

    def read_data_frame(self, path: str, encoding: str) -> DataFrame:
        df = pd.read_csv(path, encoding=encoding, low_memory=False)
        pd.set_option('display.max_columns', None)

        return df

    def read_data_frame_with_index(self, path: str, encoding: str) -> DataFrame:
        pd.read_csv(path, encoding=encoding, low_memory=False, index_col=0)

        return df

    def make_csv(self, df: DataFrame):
        df.to_csv('new.csv')

    def make_csv_without_index(self, df: DataFrame):
        df.to_csv('new_no_index.csv', index=None)



if __name__ == '__main__':
    file_path = '/Users/the9kim/PycharmProjects/data-analysis-practice/남산도서관 장서 대출목록 (2021년 04월).csv'
    csv = Csv()

    # read_csv.check_type_of(file_path)

    # read_csv.read(file_path)

    df = csv.read_data_frame(file_path, 'EUC-KR')
    print(df.head())

    df2 = csv.read_data_frame_with_index('/Users/the9kim/PycharmProjects/data-analysis-practice/data-analysis/new.csv', None)
    print(df2.head())

    csv.make_csv_without_index(df)
