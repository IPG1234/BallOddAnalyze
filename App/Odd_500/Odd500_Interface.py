from flask import Blueprint,request
from Base.Api_route import route
from Base.Browser import Browser
from Odd_DayPage import DayPage

bp=Blueprint('500Data',__name__,url_prefix='/500Data')

@route(bp,'/GetData',methods=['POST'])
def Get500Data():
    form_time=request.form.get('time')
    form_count=int(request.form.get('count'))
    Browser.StartBrowser("https://live.500.com/?e=" + form_time)
    # daypage = DayPage(Browser, form_time)
    # daypageData = daypage.Matchs