from unittest import TestCase

from street_address_parser import StreetAddressParser


class AddressLineParserTest(TestCase):
    def _assert_parses_address_correctly(self, test_data):
        for input_line, expected_output in test_data:
            self.assertEqual(
                expected_output,
                StreetAddressParser.parse_address_string(input_line)
            )

    def test_simple_addresses(self):
        test_data = (
            ('Winterallee 3',    ('Winterallee', '3')),
            ('Musterstrasse 45', ('Musterstrasse', '45')),
            ('Blaufeldweg 123B', ('Blaufeldweg', '123B')),
            ('Blaufeldweg mit Umläuten 123ä', ('Blaufeldweg mit Umläuten', '123ä')),
        )
        self._assert_parses_address_correctly(test_data)

    def test_complicated_addresses(self):
        test_data = (
            ('Am Bächle 23',            ('Am Bächle', '23')),
            ('Auf der Vogelwiese 23 b', ('Auf der Vogelwiese', '23 b')),
        )
        self._assert_parses_address_correctly(test_data)

    def test_other_countries(self):
        test_data = (
            ('4, rue de la revolution', ('rue de la revolution', '4')),
            ('200 Broadway Av',         ('Broadway Av', '200')),
            ('Calle Aduana, 29',        ('Calle Aduana', '29')),
            ('Calle 39 No 1540',        ('Calle 39', 'No 1540')),
        )
        self._assert_parses_address_correctly(test_data)

    def test_invalid_addresses(self):
        test_data = (
            '',
            'Foobar',
            'Foobar-',
            'Foobar- 123',
            'Foobar- 123 b',
        )
        for invalid_input in test_data:
            self.assertRaises(
                SyntaxError,
                StreetAddressParser.parse_address_string,
                invalid_input
            )

