from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Тверская", "12", "34")
from_address = Address("654321", "Санкт-Петербург", "Невский", "5", "10")

mailing = Mailing(to_address, from_address, 250, "TRK123456")

print("Отправление {} из {}, {}, {}, {} - {} в {}, {}, {}, {} - {}. "
      "Стоимость {} рублей.".format(
          mailing.track,
          mailing.from_address.index,
          mailing.from_address.city,
          mailing.from_address.street,
          mailing.from_address.house,
          mailing.from_address.apartment,
          mailing.to_address.index,
          mailing.to_address.city,
          mailing.to_address.street,
          mailing.to_address.house,
          mailing.to_address.apartment,
          mailing.cost
      ))
