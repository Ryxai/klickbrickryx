import unittest
from collections import namedtuple
from klickbrickryx import __version__
import klickbrickryx.cli as cli


def test_version():
    assert __version__ == '0.1.0'


class HelloTestCase(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(cli.dispatch_command(cli.parse_args(["hello"])), 'Hello World')

    def test_named_hello(self):
        self.assertEqual(cli.dispatch_command(cli.parse_args(['hello','--name', 'Ole'])),
                         'Hello Ole')


if __name__ == '__main__':
    unittest.main()
