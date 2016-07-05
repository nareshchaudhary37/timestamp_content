from datetime import datetime
import time

class DateTimeUserFriendly(object):
    """
    call get_message_display method and pass your message/else created date.
    """
    def __init__(self, created_at):
        self.CALL_MESSAGE_CHOICE = {
            1439: 'get_in_hour_message',
            10079: 'get_in_day_message',
            43200: 'get_in_week_message',
            518399: 'get_in_month_message',
            518400: 'get_date'
        }
        self.repr = self.get_message_display(created_at)

    def set_today(self):
        self.today_at = datetime.utcnow()

    def get_total_minutes(self):
        timestamp_today = time.mktime(self.today_at.timetuple())
        timestamp_created = time.mktime(self.created_at.timetuple())
        diff_seconds =  timestamp_today - timestamp_created
        return int(diff_seconds/60)

    def get_in_hour_message(self, minutes):
        hours = minutes / 60
        if minutes < 1:
            return "Just now."
        elif minutes < 60:
            return "{0} minute(s) ago".format(minutes)
        else:
            return "{0} hour(s) ago".format(hours)

    def get_in_day_message(self, minutes):
        days = (minutes/60)/24
        if days <= 1:
            return "Yesterday."
        else:
            return "{0} day(s) ago.".format(int(days))

    def get_in_week_message(self, minutes):
        return "{0} week(s) ago".format((minutes/60)/168)

    def get_in_month_message(self, minutes):
        return "{0} month(s) ago.".format((minutes/60)/720)

    def get_date(self, hours):
        return self.created_at.strftime("%d %b, %Y")

    def check_for_call(self, hours):
        for key in sorted(self.CALL_MESSAGE_CHOICE.keys()):
            if hours <= key:
                return eval("self."+self.CALL_MESSAGE_CHOICE.get(key))
        return eval("self."+self.CALL_MESSAGE_CHOICE.get(max(self.CALL_MESSAGE_CHOICE.keys())))

    def get_message_display(self, created_at):
        self.created_at = created_at
        self.set_today()
        total_minutes = self.get_total_minutes()
        call_method = self.check_for_call(total_minutes)
        return call_method(total_minutes)

    @property
    def repr(self):
        return self._res

    @repr.setter
    def repr(self, value):
        self._res = value
    









