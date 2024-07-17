import sys

month = input("What month were you born?: ")
day = int(input("What date were you born?: "))
if month == 'december':
	astro_sign = 'Sagittarius the Archer' if (day < 22) else 'Capricorn the Goat'
elif month == 'january':
	astro_sign = 'Capricorn the Goat' if (day < 20) else 'Aquarius the Water Bearer'
elif month == 'february':
	astro_sign = 'Aquarius the Water Bearer' if (day < 19) else 'Pisces the Fish'
elif month == 'march':
	astro_sign = 'Pisces the Fish' if (day < 21) else 'Aries the Ram'
elif month == 'april':
	astro_sign = 'Aries the Ram' if (day < 20) else 'Taurus the Bull'
elif month == 'may':
	astro_sign = 'Taurus the Bull' if (day < 21) else 'Gemini the Twins'
elif month == 'june':
	astro_sign = 'Gemini the Twins' if (day < 21) else 'Cancer the Crab'
elif month == 'july':
	astro_sign = 'Cancer the Crab' if (day < 23) else 'Leo the Lion'
elif month == 'august':
	astro_sign = 'Leo' if (day < 23) else 'Virgo the Virgin'
elif month == 'september':
	astro_sign = 'Virgo the Virgin' if (day < 23) else 'Libra of Balance'
elif month == 'october':
	astro_sign = 'Libra of Balance' if (day < 23) else 'Scorpio the Scorpion'
elif month == 'november':
	astro_sign = 'Scorpio the Scorpion' if (day < 22) else 'Sagittarius the Archer'
print("Your Zodiac Sign is :",astro_sign)
