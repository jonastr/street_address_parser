import argparse
import re
import sys

if sys.version_info < (3, 6, 0):
    sys.stderr.write('You need python 3.6 or later to run this script\n')
    exit(1)


class StreetAddressParser(object):
    """
    This class parses street addresses in the following country schemes:
    - DE (<street name> <house number> <suffix>)
    - ES (<street name plus number> No <house number>)
    - FR (<house number>, <street name>)
    - US (<house number> <street name>)
    """
    _STREET_GROUP = 'street'
    _NUMBER_GROUP = 'number'

    _RE_ADDRESS_DE_ES = (
        fr'(?P<{_STREET_GROUP}>[\w\s]+),?\s+'  # match street name 
        fr'(?P<{_NUMBER_GROUP}>(?:'  # match number in either DE or ES format at end of string
        r'(?<!No\s)\d+\s?\w?$)|'  # DE format (number and optional suffix)
        r'(?:No\s+\d+$)'  # ES format (required prefix and number)
        r')'
    )
    _RE_ADDRESS_FR_US = (
        fr'(?:^(?P<{_NUMBER_GROUP}>\d+)'  # match digits for the number at beginning of the string
        r',?\s+'  # separator
        fr'(?P<{_STREET_GROUP}>[\w\s]+))'  # match street name
    )
    _RX_PATTERNS = [re.compile(pattern) for pattern in (_RE_ADDRESS_DE_ES, _RE_ADDRESS_FR_US)]

    @classmethod
    def parse_address_string(cls, address_text):
        """
        This function parses an address string into street name and house number. Raises SyntaxError
        in case the address does not conform to any of the supported address patterns.

        :param address_text: A text string containing a (partial)
                             address (street name, house number)
        :return: A tuple consisting of street name and house number
        """
        match = cls._match_address_pattern(address_text)

        street = match.group(cls._STREET_GROUP)
        number = match.group(cls._NUMBER_GROUP)
        return street, number

    @classmethod
    def _match_address_pattern(cls, address_text):
        address_text = address_text.strip()  # remove any leading or trailing whitespace

        for rx in cls._RX_PATTERNS:
            match = rx.match(address_text)
            if match:
                return match

        # no match found -> unsupported syntax
        raise SyntaxError(f'Could not parse address. Invalid input in line: "{address_text}"')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'address',
        help='The address to be parsed (supported country schemes: DE, ES, FR, US)',
        type=str
    )
    args = parser.parse_args()

    try:
        street, number = StreetAddressParser.parse_address_string(args.address)
        print(f'{{"{street}", "{number}"}}')
    except SyntaxError as e:
        sys.stderr.write(f'{e}\n')
