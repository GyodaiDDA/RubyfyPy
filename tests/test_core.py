import unittest
from RubyfyPy.core import Array, Hash, String, rubyfy

class TestRubyfyPy(unittest.TestCase):
    def test_array_methods(self):
        arr = Array([1, 2, 3, 4, 5])
        self.assertEqual(arr.len(), 5)
        self.assertEqual(arr.first(), 1)
        self.assertEqual(arr.last(), 5)
        
        result = []
        arr.each(lambda x: result.append(x * 2))
        self.assertEqual(result, [2, 4, 6, 8, 10])
        
        mapped = arr.map(lambda x: x * 3)
        self.assertEqual(mapped, Array([3, 6, 9, 12, 15]))
        
        selected = arr.select(lambda x: x % 2 == 0)
        self.assertEqual(selected, Array([2, 4]))

    def test_array_edge_cases(self):
        empty_arr = Array([])
        self.assertEqual(empty_arr.len(), 0)
        self.assertIsNone(empty_arr.first())
        self.assertIsNone(empty_arr.last())
        
        single_arr = Array([1])
        self.assertEqual(single_arr.first(), 1)
        self.assertEqual(single_arr.last(), 1)

    def test_hash_methods(self):
        h = Hash({'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(sorted(h.keys()), ['a', 'b', 'c'])
        self.assertEqual(sorted(h.values()), [1, 2, 3])
        self.assertEqual(h.get('a'), 1)
        self.assertEqual(h.get('d', 'default'), 'default')

    def test_string_methods(self):
        s = String("Hello World")
        self.assertEqual(s.upcase(), "HELLO WORLD")
        self.assertEqual(s.downcase(), "hello world")
        self.assertEqual(s.reverse(), "dlroW olleH")

    def test_rubyfy_conversion(self):
        lst = [1, 2, "test", {"a": 1}]
        rubyfied = rubyfy(lst)
        self.assertIsInstance(rubyfied, Array)
        self.assertIsInstance(rubyfied[2], str)
        self.assertIsInstance(rubyfied[3], dict)

        dct = {"key": "value", "nested": [1, 2, 3]}
        rubyfied_dict = rubyfy(dct)
        self.assertIsInstance(rubyfied_dict, Hash)
        self.assertIsInstance(rubyfied_dict["key"], str)
        self.assertIsInstance(rubyfied_dict["nested"], list)

    def test_rubyfy_shallow(self):
        nested = [1, [2, 3], {"a": "b"}]
        rubyfied_shallow = rubyfy(nested, shallow=True)
        self.assertIsInstance(rubyfied_shallow, Array)
        self.assertNotIsInstance(rubyfied_shallow[1][1], Array)
        self.assertNotIsInstance(rubyfied_shallow[2]['a'], Hash)
    
    def test_string_chaining(self):
        ruby_string = String("hello world")
        self.assertEqual(ruby_string.upcase().reverse(), "DLROW OLLEH")
        self.assertIsInstance(ruby_string.upcase(), String)
        self.assertIsInstance(ruby_string.reverse(), String)


if __name__ == '__main__':
    unittest.main()
