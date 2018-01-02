import unittest

from language_resources import I18N


class GUIUnitTests(unittest.TestCase):
    def test_title_english(self):
        i18n = I18N('en')
        self.assertEqual(
            i18n.title,
            'Python Graphical User Interface'
        )

    def test_title_german(self):
        i18n = I18N('de')
        self.assertEqual(i18n.title,
                         'Python Grafische Benutzeroberfl\u00E4che'
                         )


if __name__ == '__main__':
    unittest.main()
