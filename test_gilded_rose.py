# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)
        
    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    def test_conjured_items_degrade_twice_as_fast(self):
        item = Item("Conjured Mana Cake", 3, 6)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        # Expected: Quality should drop by 2 (from 6 to 4) and SellIn decreases by 1.
        self.assertEqual(4, item.quality, "Conjured items should degrade in quality twice as fast")
        self.assertEqual(2, item.sell_in, "SellIn should decrease by 1")
        
    def test_conjured_items_degrade_twice_as_fast_after_expiration(self):
        # When the sell-by date has passed, normal items degrade by 2.
        # Conjured items are expected to degrade twice as fast, so by 4.
        item = Item("Conjured Mana Cake", 0, 10)
        gr = GildedRose([item])
        gr.update_quality()
        self.assertEqual(6, item.quality,
                         "Expired conjured items should degrade in quality by 4 points (from 10 to 6)")
        self.assertEqual(-1, item.sell_in, "SellIn should decrease by 1")

    def test_backstage_passes_increase_in_quality(self):
        item = Item("Backstage passes", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        # Expected: Increase in Quality by 3 (10 -> 13) and SellIn decreases by 1 (5 -> 4)
        self.assertEqual(13, item.quality, "Backstage passes should increase quality by 3 when 5 days or less remain")
        self.assertEqual(4, item.sell_in, "SellIn should decrease by 1")

        
    # def test_add_item_method_should_exist(self):
    #     gilded_rose = GildedRose([])
    #     new_item = Item("Elixir of the Mongoose", 5, 7)
    #     gilded_rose.add_item(new_item)  # This should raise an AttributeError.
        
    def test_update_quality_no_exception(self):
        items = [
            Item("Normal Item", 10, 20),
            Item("Sulfuras", 5, 80)
        ]
        gilded_rose = GildedRose(items)
        try:
            gilded_rose.update_quality()
        except Exception as e:
            self.fail("update_quality raised an exception: " + str(e))
    
    


if __name__ == '__main__':
    unittest.main()
