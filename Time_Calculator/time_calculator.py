def add_time(start:str, duration:str, starting_weekday:str=None):
    start_time = start[:-3]
    (start_hour, start_minute) = start_time.split(':')
    (duration_hour, duration_minute) = duration.split(':')
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)
    if 'PM' in start:
        start_hour += 12
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Minute conversion
    if new_minute >= 60:
        new_minute -= 60
        new_hour += 1

    # Single minute padding
    if new_minute < 10:
        new_minute = f"0{new_minute}"

    # Day conversion
    days_later = 0
    if new_hour > 24:
        days_later = int(new_hour/24)
        new_hour = new_hour%24

    # Hour conversion
    if new_hour >=12:
        new_suffix = 'PM'
        new_hour -= 12
    else:
        new_suffix = 'AM'

    # Midnight case
    if new_hour == 0 and new_suffix == 'AM':
        new_hour += 12
    
    # Noon case
    if new_hour == 0 and new_suffix == 'PM':
        new_hour += 12

    # Days later formatting
    days_later_string = ''
    if days_later == 1:
        days_later_string = ' (next day)'
    elif days_later > 1:
        days_later_string = f' ({days_later} days later)'


    # Weekday handling
    weekday_list = ['Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    weekday_dict = {'sunday':0,'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6}
    weekday_str = ''
    if starting_weekday != None:
        weekday_num = weekday_dict[starting_weekday.lower()]
        weekday_num = (weekday_num+days_later)%7
        weekday_str = f', {weekday_list[weekday_num]}'

    new_time = f'{new_hour}:{new_minute} {new_suffix}{weekday_str}{days_later_string}'




    return new_time