import re
from re import findall

class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass

class HasNonEnglishSymbols(Exception):
    pass

VALID_DOMAINS = ('com', 'bg', "net", 'org')
MIN_NAME_SYMBOLS_COUNT = 4

pattern_name = r'\w+'
english_pattern = r'[^\x00-\x7F]+'

email = input()

while email != 'End':

    if email.count("@") > 1:
        raise MoreThanOneAtSymbol('The e-mail contains more than one symbol "@"')

    elif "@" not in email:
        raise MustContainAtSymbolError('Email must contain @')

    elif len(email.split('@')[0]) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError('Name must be more than 4 characters')

    elif email.split('.')[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join("." + d for d in VALID_DOMAINS)}')

    elif findall(pattern_name, email.split('@')[0])[0] != email.split('@')[0]:
        raise InvalidNameError('Name must have only letters, underscores and digits')

    elif findall(english_pattern, email):
        raise HasNonEnglishSymbols('Name must not contain any non english letters')

    print('Email is valid')

    email = input()



