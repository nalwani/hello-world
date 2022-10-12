from datetime import datetime, timedelta


class Scheduler:

    @staticmethod
    def createEasySchedule(items):
        easySchedule = []
        interval = 0
        for item in items:
            date = datetime.today() + timedelta(days=interval)
            easySchedule.append((item, date.strftime("%B %d, %Y")
))
            interval = interval + 2

        return easySchedule
