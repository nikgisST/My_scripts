import os
from datetime import datetime


class ExposureSummary(dict):
    def __init__(self, location, size, created_date):
        super(ExposureSummary, self).__init__(
            {'location': location, 'size': size, 'created_date': created_date}
        )

    @property
    def location(self):
        return self['location']

    @property
    def size(self):
        return self['size']

    @property
    def created_date(self):
        return self['created_date']


def get_file_metadata(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    file_size = os.path.getsize(file_path)
    # datetime.now().strftime('%Y-%m-%d')
    creation_time_epoch = os.path.getctime(file_path)
    # convert to a readable date format
    created_date = datetime.fromtimestamp(creation_time_epoch).strftime('%Y-%m-%d %H:%M:%S')
    return ExposureSummary(location=file_path, size=file_size, created_date=created_date)


def main():
    file_path = r"D:\Documents\Заявление за ползване на платен годишен отпуск.docx"
    try:
        exposure_summary = get_file_metadata(file_path)
        print(f"Location: {exposure_summary.location}")          # Location: C:\Users\New\Downloads\nhess-21-393-2021.pdf
        print(f"Size: {exposure_summary.size} bytes")            # Size: 4871473 bytes
        print(f"Created Date: {exposure_summary.created_date}")  # Created Date: 2024-07-30

        with open('file_inventory.txt', 'a', encoding='utf-8') as f:
            f.write(f"{exposure_summary.location}, {exposure_summary.size}, {exposure_summary.created_date}\n")
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()