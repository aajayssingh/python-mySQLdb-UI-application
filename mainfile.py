#!/usr/bin/python
# -*- coding: utf-8 -*-

from pydebtest27 import DbAuth
import Tkinter as tk
import MySQLdb as mdb
import sys

def main():
    root = tk.Tk()
    dba = DbAuth(root)
        
    root.mainloop()
    
    

if __name__=="__main__":
    main()