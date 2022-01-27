#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

duration = int(input("Введите продолжительность "))
day = duration // 86400
hours = duration // 3600
minutes = duration // 60 - hours * 60
seconds = duration % 60
print('Дней:', day, 'Часов:', hours, 'Минут:', minutes, 'Секунд:', seconds )























