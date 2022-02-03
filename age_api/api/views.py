from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import date, timedelta
import datetime as dt


@api_view(['POST'])
def age(request):
    day = request.data['day']
    mon = request.data['month']
    year = request.data['year']
    birthday = dt.datetime(year, mon, day).date()
    today = dt.date.today()
    print(today, birthday)
    age = (today - birthday) // dt.timedelta(days=365.2425)
    per = {
        "age": age,
    }
    return Response(per)
