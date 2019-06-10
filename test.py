import unittest
from InventoryAllocator import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase):
    def test_emptyOrder(self):
        self.assertEqual(InventoryAllocator({ }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]),[])
    def test_emptyWarehouses(self):
        self.assertEqual(InventoryAllocator({ 'apple': 1 }, []),[])
    def test_emptyInput(self):
        self.assertEqual(InventoryAllocator({ }, []),[])
    def test_exactAllocation(self):
        self.assertEqual(InventoryAllocator({ 'apple': 1 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]),[{ 'owd': { 'apple': 1 } }])
    def test_splitAllocation(self):
        self.assertEqual(InventoryAllocator({ 'apple': 10 }, [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]),[{ 'owd': { 'apple': 5 }}, { 'dm': { 'apple': 5 } }])
    def test_notenoughInventory(self):
        self.assertEqual(InventoryAllocator({ 'apple': 5 }, [{ 'name': 'owd', 'inventory': { 'apple': 1 } }]),[])
    def test_oneLessItem(self):
        self.assertEqual(InventoryAllocator({ 'apple': 5, 'orange': 3 }, [{ 'name': 'owd', 'inventory': { 'apple': 2,'orange': 1 } }, { 'name': 'dm', 'inventory': { 'apple': 5,'orange': 1 }}]),[])
    def test_multipleItems_multipleWarehouses(self):
        self.assertEqual(InventoryAllocator({ 'apple': 5, 'orange': 3 }, [{ 'name': 'owd', 'inventory': { 'apple': 2,'orange': 1 } }, { 'name': 'dm', 'inventory': { 'apple': 5,'orange': 4 }}]),[{'owd': {'apple': 2,'orange': 1}},{'dm': {'apple': 3,'orange': 2}}])

if __name__ == '__main__':
    unittest.main()
