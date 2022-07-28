class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class NoResponseException(Exception):
    """Вызывается, когда от url адреса не поступил ответ."""
    pass
