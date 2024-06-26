#!/usr/bin/python3
"""Unit tests for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestHBNBCommand(unittest.TestCase):
    """Test the HBNB command interpreter"""

    def setUp(self):
        """Set up test cases"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after tests"""
        storage._FileStorage__objects = {}

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        """Test quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        """Test EOF command"""
        self.assertTrue(self.console.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test empty line input"""
        self.console.onecmd("\n")
        self.assertEqual("", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """Test create command"""
        self.console.onecmd('create State name="California"')
        obj_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(obj_id) > 0)
        obj = storage.all()["State." + obj_id]
        self.assertEqual(obj.name, "California")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_invalid(self, mock_stdout):
        """Test create command with invalid class"""
        self.console.onecmd('create MyModel')
        self.assertEqual("** class doesn't exist **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Test show command"""
        self.console.onecmd('create User')
        obj_id = mock_stdout.getvalue().strip()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.console.onecmd(f'show User {obj_id}')
        self.assertIn(obj_id, mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show_invalid(self, mock_stdout):
        """Test show command with invalid input"""
        self.console.onecmd('show User')
        self.assertEqual("** instance id missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        """Test destroy command"""
        self.console.onecmd('create State')
        obj_id = mock_stdout.getvalue().strip()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.console.onecmd(f'destroy State {obj_id}')
        self.console.onecmd(f'show State {obj_id}')
        self.assertEqual("** no instance found **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """Test all command"""
        self.console.onecmd('create User')
        self.console.onecmd('create State')
        self.console.onecmd('all')
        output = mock_stdout.getvalue().strip()
        self.assertIn('User', output)
        self.assertIn('State', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all_class(self, mock_stdout):
        """Test all command with specific class"""
        self.console.onecmd('create User')
        self.console.onecmd('create State')
        self.console.onecmd('all User')
        output = mock_stdout.getvalue().strip()
        self.assertIn('User', output)
        self.assertNotIn('State', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        """Test update command"""
        self.console.onecmd('create User')
        obj_id = mock_stdout.getvalue().strip()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.console.onecmd(f'update User {obj_id} first_name "John"')
        self.console.onecmd(f'show User {obj_id}')
        self.assertIn('John', mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update_invalid(self, mock_stdout):
        """Test update command with invalid input"""
        self.console.onecmd('update User')
        self.assertEqual("** instance id missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        """Test count command"""
        self.console.onecmd('create User')
        self.console.onecmd('create User')
        self.console.onecmd('count User')
        self.assertEqual("2", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_default_method(self, mock_stdout):
        """Test default method for <class name>.<command>() syntax"""
        self.console.onecmd('create User')
        obj_id = mock_stdout.getvalue().strip()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        self.console.onecmd(f'User.show("{obj_id}")')
        self.assertIn(obj_id, mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_parameters(self, mock_stdout):
        """Test create command with parameters"""
        self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        obj_id = mock_stdout.getvalue().strip()
        self.assertTrue(len(obj_id) > 0)
        obj = storage.all()["Place." + obj_id]
        self.assertEqual(obj.city_id, "0001")
        self.assertEqual(obj.user_id, "0001")
        self.assertEqual(obj.name, "My house")
        self.assertEqual(obj.number_rooms, 4)
        self.assertEqual(obj.number_bathrooms, 2)
        self.assertEqual(obj.max_guest, 10)
        self.assertEqual(obj.price_by_night, 300)
        self.assertEqual(obj.latitude, 37.773972)
        self.assertEqual(obj.longitude, -122.431297)

if __name__ == "__main__":
    unittest.main()
