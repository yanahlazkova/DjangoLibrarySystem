from django.shortcuts import render
from datetime import date, datetime, timedelta
from django.http import HttpResponse
import locale


def day_now(request):
    return HttpResponse(f'<p>{date.today()}</p>')


def time_now(request):
    return HttpResponse(f'<h1>{datetime.now().strftime('%X')}</h1>')


def programmers_day(request):
    day, day_week = get_programmers_day(datetime.now().year)
    return HttpResponse(f'<h2>День програміста цьго року:</h2><br><p>{day}, {day_week}</p>')


def get_programmers_day(year: int):
    """
    Розраховує дату та день тижня для Дня програміста (256-й день року).
    Args:
        year: Рік для розрахунку.
    Returns:
        Кортеж, що містить дату (str) та день тижня (str).
    """
    # Визначаємо дату, додавши 255 днів до першого дня року
    programmers_day_date = date(year, 1, 1) + timedelta(days=255)

    # Отримуємо дату у форматі "13 вересня"
    date_str = programmers_day_date.strftime("%d %B").replace(programmers_day_date.strftime("%B"), programmers_day_date.strftime("%B").capitalize())

    # Отримуємо повну назву дня тижня
    day_of_week = programmers_day_date.strftime("%A").capitalize()

    return date_str, day_of_week
