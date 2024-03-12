#!/usr/bin/python3
"""
Test Console Modulee
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def test_do_create(self):
        """Test Create"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create"
            expected = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected, output.getvalue().strip())

    def test_do_show(self):
        """Test Show"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create"
            expected = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected, output.getvalue().strip())

    def test_do_all(self):
        """Test all"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "all"
            HBNBCommand().onecmd(input)
            self.assertIsNotNone(output.getvalue().strip())

    def test_do_destroy(self):
        """Test Destroy"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "destroy"
            expected = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected, output.getvalue().strip())

    def test_do_update(self):
        """Test update"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "update"
            expected = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected, output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
