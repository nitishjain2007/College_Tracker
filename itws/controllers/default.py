# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
from datetime import datetime,date
import time
def faq():
    if session.login!="login":
        session.login="login1"
        session.uname=""
    return dict(check1=session.login,check2=session.uname,check3=session.photo)
def tables(): 
   return dict(tables=db().select(db.persons.ALL))
def helloa():
	return dict();

def echo():
	return request.vars
def validater():
    session.states="not"
    rows=db(db.persons.id>0).select()
    for i in rows:
	    if(i.name==session.uname):
		    if(i.password==session.passwo):
			    session.states="ok"
def hello1():
    if session.state=="logout":
	session.state="login"

#for initializing the login state
#login1 refers to logout
#login refers to logged in

    if session.login!="login":
        session.login="login1"
        session.uname=""

#part for logging out

    session.state=request.get_vars["a"]
    if session.state == "logout":
	response.flash = T("logout successfull")
	response.mess="notput"
	session.login = "login1"
	session.logout = "true"

#for logging in

    if request.vars.login1:
	session.uname = request.vars["user"]
	session.passwo = request.vars["pass"]

#for checking the credentials
	
	validater()

#redirecting user to his page

	if session.states == "ok":
		rows = db(db.persons.name == session.uname).select()
		for i in rows:
			session.photo = i.photo
			session.designation = i.designation
		rows1 = db(db[session.designation].name == session.uname).select()
		for i in rows1:
			session.sec = i.sec
		session.times = datetime.today().time()
		#print session.times
		#print session.sec
		session.days = time.strftime("%A")	
		rows2 = db(db[session.sec].dayn == session.days).select()
		rows3 = db(db.periods.id > 0).select()

#for taking the current period of user
		session.periodname = None
		for i in rows3:
			if i.T1 < session.times and i.T2 > session.times:
				session.periodname = i.pname
		if session.periodname == "labs":
			session.periodtype = "lab"
		elif session.periodname is not None:
			session.periodtype = "class"
		if session.periodname is not None:
			session.var = rows2[0][session.periodname]
			print session.var
			print type(session.var)
			if session.var is not "-":
				session.var = session.var.split()
				session.period = session.var[0]
				print session.period
				l = len(session.var)
				session.schedule = ""
				for i in range(1,l):
					session.schedule = session.schedule + session.var[i] + " "
			else:
			  	session.period = None
					
		else:
			session.period = None

#changing the profile pic
	if request.vars.changeimage:
		print "wooooooooooooooooooo"
		session.newpic = request.vars["photochange"]
		db(db.persons.name == session.uname).update(photo=session.newpic)
		response.flash = t("Image Changed")

#flash messages

	if session.states=="ok":
	   response.flash=T("login successfull")
	   session.login = "login"
	else:
	   response.flash=T("wrong username/password")
    return dict(check1=session.login,check2=session.uname,check3=session.photo,check4=session.period,check5=session.schedule,check6=session.periodtype)
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if session.login!="login":
        session.login="login1"
        session.uname=""
    response.flash = T("Welcome to IIIT tracker!")
    return dict(message=T('Hello IIIT'),check1=session.login,check2=session.uname,check3=session.photo,check4=session.period)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth(),check1=session.login,check2=session.uname)

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud(),check1=session.login,check2=session.uname)

