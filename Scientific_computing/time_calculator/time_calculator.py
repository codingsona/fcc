'''Here we are creating a time calculator as per our requirement.'''

''' To create time claculator we'll create a class as "time_calculator"..
Inside the class we'll iitialize the attributes in the init method.The attributes are start_time and duration ,
The day which is the optional parameter.'''
class time_calculator(object):
    def __init__(self, start_time, duration, day=None):
        self.start_time = start_time
        self.duration = duration
        self.day = None if day is None else day

    '''Here we have the "aa_time" method which acts as the time calculator '''
    #Note: Here we are not passing the attributes again as it is already initialized in the init method
    def add_time(self):
        #start_time contains both time and meridian. Hence we are spliting it.
        time, med = self.start_time.split()
        start_med = med

        #time contains both hour and minute sothat we are spliting it again. Same we are doing for duration also.
        start_hr, start_min = time.split(':')
        duration_hr, duration_minute = self.duration.split(':')

        # created a new variable new_hr which is the sum of start_hr and duration_hr.
        # created a new variable new_min which is the sum of start_minute and duration_minute.
        new_hr = int(start_hr) + int(duration_hr)
        new_min = int(start_min) + int(duration_minute)

        if new_min > 60:
            new_hr += 1
            new_min = new_min - 60

        days_later = 0
        med_later = 0

        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        result_hr = new_hr

        while new_hr > 12:
            new_hr = new_hr - 12

        while result_hr > 11:
            result_hr -= 12
            med = "PM" if med == "AM" else "AM"
            med_later += 1

        if med_later % 2 != 0:
            if start_med == "PM":
                med_later += 1
            else:
                med_later -= 1

        if result_hr == 0:
            result_hr = 12

        days_later = med_later / 2
        # new_time = ("%s:%s %s" % (result_hr, new_min, med))
        new_time = f"{result_hr}:{str(new_min).zfill(2)} {med}"
        #print(new_time)

        if self.day:
            day_index = week_days.index(self.day.title())
            new_day_index = int((day_index + days_later) % 7)
            new_time += f", {week_days[new_day_index]}"

        if days_later == 1:
            new_time += " (next day)"

        if days_later > 1:
            new_time += f" ({int(days_later)} days later)"

        return new_time

