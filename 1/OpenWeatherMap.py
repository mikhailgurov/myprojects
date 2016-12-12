import pyowm
import datetime
print('OpenWeatherMap')
owm = pyowm.OWM('ef076c90647b8a07629bcb63b62dc4c5')
observation = owm.weather_at_place('Moscow')
weather = observation.get_weather()
location = observation.get_location()
translate = { 'Moscow': 'Москва'}

def WhatIsCloudness():
    if 0 <=  weather.get_clouds() <= 10:
      return 'ясная'
    if 10 < weather.get_clouds() <= 30:
     return 'немного облочная'
    if 30 < weather.get_clouds() <= 70:
        return 'пасмурная'
    if 70 < weather.get_clouds() <= 100:
        return 'мрачная'

print('Погода в городе  ' + translate[location.get_name()] +
      '(' + location.get_country() + ')'+ 'сегодня ' + str(weather.get_reference_time(timeformat='date')) +
      ' '+ WhatIsCloudness() +
      ',облачность составляет ' + str(weather.get_clouds()) +
      '%' + ', давление ' + str(round(weather.get_pressure()['press']*0.75,1)) + ' мм.рт.ст.'+
      ', температура ' + str(weather.get_temperature('celsius').get('temp')) +
      ' , ночью ' + str(weather.get_temperature('celsius')['temp_min']) +
      ' , днем ' + str(weather.get_temperature('celsius')['temp_max']) +
      ' градусов цельсия ' + ',скорость ветра ' + str(weather.get_wind()['speed']) + 'м/c.')