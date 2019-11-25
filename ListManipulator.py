import unittest


class ListManipulator:
    def __init__(self, list):
        self.list = list

    def min(self):
        if len(self.list) == 0:
            return None

        min = self.list[0]
        for item in self.list:
            if item < min:
                min = item
        return min

    def max(self):
        if len(self.list) == 0:
            return None

        max = self.list[0]
        for item in self.list:
            if item > max:
                max = item
        return max

    def remove(self, value):
        to_remove = []
        for i, item in enumerate(self.list):
            if item == value:
                to_remove.append(i)

        removed_count = 0
        for index in to_remove:
            self.list.pop(index - removed_count)
            removed_count += 1


class ListManipulatorTest(unittest.TestCase):
    def testMax(self):
        # Create a list and check the max of the list (will max() return 4?  It should)
        _list = [1, 2, 3, 4]
        manipulator = ListManipulator(_list)
        self.assertEqual(manipulator.max(), 4)

        # Create another list and manipulator, this time with unordered integers and floats mixed in
        _list = [2, 1.4, -5, 12.7, -135.9845]
        manipulator = ListManipulator(_list)
        self.assertEqual(manipulator.max(), 12.7)

        # Create a list, including strings as well, see if it'll work
        _list = [3, 84.2, -25, "Hello", 55.1, 10]
        manipulator = ListManipulator(_list)
        self.assertEqual(manipulator.max(), 84.2)

    def testMin(self):
        # Create a list and check the min of the list (will min() return 1?  It should)
        _list = [1, 2, 3, 4]
        manipulator = ListManipulator(_list)
        self.assertEqual(manipulator.min(), 1)

        # Create a new list of unordered integers and floats
        _list = [-2, 2.784, 8952.5, 1, -10.1]
        manipulator = ListManipulator(_list)
        self.assertEqual(manipulator.min(), -10.1)

        # Add strings into the mix
        _list = [-10, 5.3, "Code test", 33, -156]
        manipulator = ListManipulator(_list)
        self.assertEqual(manipulator.min(), -156)

    def testRemove(self):
        # Create a list and check to see if the index was removed correctly
        _list = [1, 2, 3, 4]
        manipulator = ListManipulator(_list)
        manipulator.remove(2)
        self.assertEqual(2 in manipulator.list, False)

        # Create a list, and try to remove something that isn't in the list at all
        _list = [1, 3, 4]
        manipulator = ListManipulator(_list)
        manipulator.remove(2)
        self.assertEqual(2 in manipulator.list, False)

        # Include other value types in the list
        _list = [1, 2, 3, 4, "Hello!", -10, 2.54, "Hi!!", -25.29846]
        manipulator = ListManipulator(_list)
        manipulator.remove("Hi!!")
        self.assertEqual("Hi!!" in manipulator.list, False)


# Time to test everything
unittest.main()
