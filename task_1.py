time_values = '1h 45m,360s,25m,30m 120s,2h 60s'

# Разбиваем строку по запятым на отдельные временные значения
time_parts = time_values.split(',')

total_minutes = 0

# Проходим по каждому временному значению
for part in time_parts:
    minutes_in_part = 0
    
    # Разбиваем каждую часть по пробелам
    elements = part.split()
    
    for elem in elements:
        if 'h' in elem:
            # Часы переводим в минуты
            hours = int(elem.replace('h', ''))
            minutes_in_part += hours * 60
        elif 'm' in elem:
            # Минуты просто добавляем
            minutes = int(elem.replace('m', ''))
            minutes_in_part += minutes
        elif 's' in elem:
            # Секунды переводим в минуты
            seconds = int(elem.replace('s', ''))
            minutes_in_part += seconds // 60
    
    total_minutes += minutes_in_part

# Округляем до 2 знаков после запятой для красоты
total_minutes = round(total_minutes, 2)

print(f"Общее количество минут: {total_minutes}")