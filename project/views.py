from django.template.response import TemplateResponse

def index2(request):
    return TemplateResponse(request, 'index2.html', {
            'var1': 'This is var1',
            'var2': 'This is var2',
            'list_var': ['a','b', 'c'],
})

def weeklyCal(request):
    return TemplateResponse(request, 'weeklyCal.html',{
            'day1': 'Monday',
            'day2': 'Tuesday',
            'day3': 'Wednesday',
            'day4': 'Thursday',
            'day5': 'Friday',
            'day6': 'Saturday',
            'day7': 'Sunday',
            'list_var': ['a','b', 'c'],
            })

