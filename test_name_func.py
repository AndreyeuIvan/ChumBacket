import unittest
from test_pcc import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for func"""

    def test_first_last_name(self):
        """Do names like 'Janis Jophin' work"""
        formatted_name = get_formatted_name('janis', 'jophin')
        self.assertEqual(formatted_name, "Janis Jophin")

unittest.main()