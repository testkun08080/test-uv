import os


def main():
    # 環境変数の取得
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    print(PROJECT_NAME)


if __name__ == "__main__":
    main()

