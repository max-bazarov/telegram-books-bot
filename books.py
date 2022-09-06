from sheets_service import worksheet


def get_all_books() -> list[str]:
    return worksheet.col_values(1)


def add_book(book: str) -> None:
    worksheet.append_row([book])


def delete_last_book() -> None:
    worksheet.batch_clear(["A"+str(len(get_all_books()))])
