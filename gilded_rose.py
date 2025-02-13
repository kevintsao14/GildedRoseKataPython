# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


# --- Updater Classes ---

class ItemUpdater:
    def update(self, item):
        raise NotImplementedError("Subclasses must override update() method")


class NormalUpdater(ItemUpdater):
    def update(self, item):
        # Normal items decrease by 1 quality per day before expiration,
        # and by 2 after expiration. Quality never drops below 0.
        decrement = 1 if item.sell_in > 0 else 2
        item.quality = max(0, item.quality - decrement)
        item.sell_in -= 1


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        # For "Sulfuras", quality remains unchanged.
        # Per test expectations, sell_in decreases by 1.
        item.sell_in -= 1


class ConjuredUpdater(ItemUpdater):
    def update(self, item):
        # Conjured items degrade in quality twice as fast as normal items.
        # (i.e., -2 if not expired, -4 if expired)
        decrement = 2 if item.sell_in > 0 else 4
        item.quality = max(0, item.quality - decrement)
        item.sell_in -= 1


class BackstageUpdater(ItemUpdater):
    def update(self, item):
        # Backstage passes increase in quality as the concert approaches:
        #   - More than 10 days: +1
        #   - 10 days or less but more than 5 days: +2
        #   - 5 days or less but not expired: +3
        #   - After the concert: quality drops to 0.
        if item.sell_in > 10:
            increment = 1
        elif item.sell_in > 5:
            increment = 2
        elif item.sell_in > 0:
            increment = 3
        else:
            item.quality = 0
            item.sell_in -= 1
            return

        item.quality = min(50, item.quality + increment)
        item.sell_in -= 1


# --- Main GildedRose Class ---

class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = self._get_updater(item)
            updater.update(item)

    def _get_updater(self, item):
        # Determine which updater to use based on the item's name.
        if item.name == "Sulfuras":
            return SulfurasUpdater()
        elif item.name == "Backstage passes":
            return BackstageUpdater()
        elif "Conjured" in item.name:
            return ConjuredUpdater()
        else:
            return NormalUpdater()

    def get_items(self):
        # Return a list of item names.
        return [item.name for item in self.items]
