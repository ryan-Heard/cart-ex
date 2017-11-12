from math import ceil
import copy
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('basket.log')
handler.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

try:
    with open('prices.json') as json_data:
        prices = json.load(json_data)
    logger.info("Opened prices.json")
except Exception as e:
    logger.error(e)


class Basket:
    def __init__(self):
        self.items = []
        self.item_objs = []
        self.disc_cup = {'name': 'BOGO', 'disc': 11.23, 'visual': "-11.23"}
        self.disc_apple_bag = {'name': 'APPL', 'disc': 4.50, 'visual': "-4.50"}
        self.disc_oatmeal = {'name': 'APOM', 'disc': .5, 'visual': "-50%"}
        self.disc_milk = {'name': 'CHMK', 'disc': 4.75, 'visual': "-4.75"}

    def print_cart(self):
        total = self.total()

        data = "...\n\n"
        data += "{: >0} {: >10} {: >10}\n".format("Item", " ", "Price")
        data += "{: >0} {: >10} {: >10}\n".format("----", " ", "-----")

        for item in self.item_objs:
            data += "{: >0} {: >10} {: >10.2f}\n".format(item['Code'],
                                                         " ",
                                                         prices[item['Code']]['Price'])
            # If price is different than item
            if item['Price'] != prices[item['Code']]['Price']:
                tmp_disc = self.get_discount_code(item)
                data += "{: >0} {: >10} {: >12}\n".format(" ",
                                                             tmp_disc['name'],
                                                             tmp_disc['visual'])

        data += "-"*26
        data += "\n"
        data += "{: >4} {: >10} {: >8}\n".format("...", " ",  total)
        data += "\n\n"

        logger.info("printed cart")
        print(data)

    def add_items(self, items):
        items = [i.strip() for i in items.split(',')]
        self.items.extend(items)
        logger.info("Added {} to cart".format(items))

    def total(self):
        total = 0

        self.item_objs = [copy.deepcopy(prices[item]) for item in self.items]

        if self.items.count('AP1') >= 3:
            # Set all of the prices of the AP1 to 4.50
            for item in self.item_objs:
                if item['Code'] == 'AP1':
                    item['Price'] = self.disc_apple_bag['disc']

        if self.items.count('CF1') > 1:
            # Set the second price of CF1 = 0
            # This will apply to all greater that ceiing of count/2
            cup = 0
            free_cups = ceil(self.items.count('CF1') - (self.items.count('CF1')/2))

            for item in self.item_objs:
                if item['Code'] == 'CF1':
                    if cup >= free_cups:
                        item['Price'] = item['Price'] - self.disc_cup['disc']

                    cup += 1

        if self.items.count('CH1') > 0:
            # Limit to one
            # Search for the next milk and set it to 0
            for item in self.item_objs:
                if item['Code'] == 'MK1':
                    item['Price'] = item['Price'] - self.disc_milk['disc']
                    break

        if self.items.count('OM1') >= 1 and self.items.count('AP1'):
            # Apply 50% discount to apples
            for item in self.item_objs:
                if item['Code'] == 'AP1':
                    item['Price'] = item['Price']*self.disc_oatmeal['disc']
                break

        for item in self.item_objs:
            total += item['Price']

        logger.info("Got total:{}".format(total))
        return total

    def check_out(self):
        self.items = []
        self.item_objs = []
        logger.info("Emptied Cart")

    def get_discount_code(self, item):
        logger.info("Discount on {} ".format(item['Code']))
        if item['Code'] == 'AP1':
            if item['Price'] == self.disc_apple_bag['disc']:
                return self.disc_apple_bag
            else:
                return self.disc_oatmeal
        elif item['Code'] == 'CF1':
            return self.disc_cup
        elif item['Code'] == 'MK1':
            return self.disc_milk
