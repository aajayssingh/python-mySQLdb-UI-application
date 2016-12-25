#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import Tkinter as tk
from movieDBinterface import MovieDBInterface

class DbAuth(tk.Frame):
    succDB = False
    con = None
    username = None
    password = None
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent=parent
        succDB = False
        self.init_dbAuth_UI()

    def init_dbAuth_UI(self):
        """Draw a user interface allowing the user to type
        MySQL server credentials
        """
        self.parent.title("DB Authentication")       
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")

        self.label_user=tk.Label(self.parent, text="DB User: ", anchor=tk.W ,background="dark slate gray", foreground="white", font="Helvetica 8  bold")
        self.label_password=tk.Label(self.parent,text="DB Pwd:", anchor=tk.W,background="dark slate gray", foreground="white", font="Helvetica 8  bold")
        self.label_con_status=tk.Label(self.parent, text="Not connected to DB ", anchor=tk.W ,background="dark slate gray", foreground="white", font="Helvetica 8  bold")

        self.label_user.grid(row=0,column=0, sticky = tk.E+ tk.W)
        self.label_password.grid(row=1,column=0, sticky = tk.E + tk.W)
        self.label_con_status.grid(row=2,column=1, sticky = tk.E+ tk.W)

        self.dbuser = tk.Entry(self.parent)
        self.dbpassword = tk.Entry(self.parent, show="*")

        self.dbuser.grid(row=0,column=1,sticky=tk.E+tk.W)
        self.dbpassword.grid(row=1,column=1,sticky=tk.E+tk.W)

        self.connectb = tk.Button(self.parent, text="Log in", font="Helvetica 10 bold", command=self.connectDB)
        self.cancelb = tk.Button(self.parent, text="Cancel", command=self.parent.quit, font="Helvetica 10 bold")

        self.connectb.grid(row=3,column=0,sticky=tk.W)
        self.cancelb.grid(row=3,column=2)
        
    def connectDB(self):
        #if self.dbuser.get() == "root" and self.dbpassword.get() == "root":
            try:
                self.username = self.dbuser.get()
                self.password = self.dbpassword.get()
                self.con = mdb.connect('localhost', self.dbuser.get(), self.dbpassword.get(), 'testdb');#root-root or testuser- test623

                cur = self.con.cursor()
                cur.execute("SELECT VERSION()")

                ver = cur.fetchone()

                self.succDB = True
                self.con.autocommit(True)
                print "Database version : %s " % ver
                self.label_con_status['text'] = "Database version : %s " % ver
                self.movieDBInterfacewindow()
                
            except mdb.Error, e:

                print "Error %d: %s" % (e.args[0],e.args[1])
                self.label_con_status['text'] = 'DB connection error'
                sys.exit(1)

            finally:

                if self.con:
                    #self.con.close()
                    self.succDB = False
    
    def movieDBInterfacewindow(self):
        self.movieDBIntfWin = tk.Toplevel(self)
        self.app = MovieDBInterface(self.movieDBIntfWin, self.con)
        print "flagtest %s " % self.app.flagtest
        
        '''self.new_window.wm_title("process DB")
        self.new_window.grid_rowconfigure(0, weight=1)
        self.new_window.grid_columnconfigure(0, weight=1)
        
        cur = self.con.cursor()
        cur.execute("select version()")
        
        ver = cur.fetchone()
        
        print "database version from querywin: %s " % ver
        print "db user name: %s" % self.dbuser
        self.label_con_status['text'] = "database version : %s " % ver
        
        self.exitb=tk.button(self.new_window,text="exit",command=self.new_window.quit)
        self.submitb=tk.button(self.new_window,text="submit",command=self.new_window.quit)
        
        self.exitb.pack()
        self.submitb.pack()'''
        

