# Forex Example

from forex_python.converter import CurrencyRates

c = CurrencyRates()
c.get_rates('USD')
c.get_rate('USD', 'THB')
print(c.get_rates('USD'))
print(c.get_rate('USD', 'THB'))
