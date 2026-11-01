previous = int(input("Введите предыдущее показание: "))
current = int(input("Введите текущее показание: "))

# Расчёт использованного газа
if current >= previous:
    used = current - previous
else:
    used = 10000 - previous + current

# Расчёт стоимости газа
if used <= 300:
    payment = 21
elif used <= 600:
    payment = 21 + (used - 300) * 0.06
elif used <= 800:
    payment = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    payment = (21 + 300 * 0.06
               + 200 * 0.04
               + (used - 800) * 0.025)

# Расчёт средней стоимости одного кубометра
if used > 0:
    average = payment / used
else:
    average = 0

# Вывод результатов
print()
print(f"{'Предыдущее':>12}{'Текущее':>12}"
      f"{'Использовано':>15}{'К оплате':>12}"
      f"{'Ср. цена m^3':>15}")

print(f"{previous:12}{current:12}{used:15}"
      f"{payment:12.2f}{average:15.2f}")
