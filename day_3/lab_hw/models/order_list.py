from models.order import Order
import datetime

date1 = datetime.date(2022, 10, 31)
date2 = datetime.date(2022, 11, 3)
date3 = datetime.date(2022, 11, 11)

order1 = Order("Jean Grey", date1, 2, "Dungeons and Dragons Starter Pack")
order2 = Order("Gene Vincent", date2, 1, "Fallout")
order3 = Order("Jean Paul Gaultier", date3, 3, "Final Fantasy X-2")

orders = [order1, order2, order3]