    def test_aged_brie_should_not_exceed_quality_50(self):
        """
        Aged Brie should never have a quality higher than 50, even after multiple updates.
        The current implementation may allow it to exceed 50.
        """

        # Aged Brie close to max quality
        aged_brie = Item("Aged Brie", 2, 49)

        gilded_rose = GildedRose([aged_brie])

        # First update (Quality should increase by 1, but not go past 50)
        gilded_rose.update_quality()
        self.assertEqual(50, aged_brie.quality, "Aged Brie quality should not exceed 50")

        # Second update (Quality should stay at 50)
        gilded_rose.update_quality()
        self.assertEqual(50, aged_brie.quality, "Aged Brie quality should remain at 50 after reaching the limit")