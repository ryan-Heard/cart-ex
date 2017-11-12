from basket import Basket
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('basket.log')
handler.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


def main():
    total = 0
    basket = {}
    codes = [True]

    basket = Basket()

    with open('prices.json') as json_data:
        prices = json.load(json_data)

    print("Please type 'total' to see current total")
    print("Please type 'checkout' to see current total and empty cart")
    print("Type 'q' to quit")

    while True:
        codes = input("Please enter your codes seperated by ',': ").split(',')
        logger.info(codes)
        if codes[0] == 'q':
            break

        elif codes[0] == 'total':
            basket.print_cart()

        elif codes[0] == 'checkout':
            basket.print_cart()
            basket.check_out()

        else:
            codes = [code.strip() for code in codes]
            for item in codes:
                if item not in prices:
                    logger.error("{} is not a code or command".format(item))
                    print("{} is not a code or command".format(item))
                else:
                    try:
                        basket.add_items(item)
                    except Exception as e:
                        logger.error(e)


if __name__ == '__main__':
    main()
