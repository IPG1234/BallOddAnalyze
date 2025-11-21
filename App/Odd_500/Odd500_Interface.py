from flask import Blueprint,request
from Base.Api_route import route
from Base import browser
# from Odd_DayPage import DayPage

bp=Blueprint('500Data',__name__,url_prefix='/500Data')

@route(bp,'/GetData',methods=['POST'])
def Get500Data():
    # form_time=request.form.get('time')
    # form_count=int(request.form.get('count'))
    browser.StartBrowser("https://live.500.com/?e=2025-5-25")
    # daypage = DayPage(Browser, form_time)
    # daypageData = daypage.Matchs