import csv

from models.exceptions import FileCorruptedException


def read_csv(path, requires_cols):
    with open(path, newline="", encoding="utf-8") as _f:
        reader = csv.DictReader(_f)
        if any(c not in reader.fieldnames for c in requires_cols):
            raise FileCorruptedException(path)

        return list(reader)


def write_csv(path, headers, rows):
    with open(path, "w", newline="", encoding="utf-8") as _f:
        writer = csv.writer(_f)
        writer.writerow(headers)
        writer.writerows(rows)
