import Tkinter as tk

class MovieDBInterface:
    flagtest = False
    movie_con = None
    fields = 'Movie Title', 'Year', 'Producers', 'Country'
    def __init__(self, master, con):
        self.master = master
        self.movie_con = con
        self.frame = tk.Frame(self.master)
        self.flagtest = True
        self.movie_db_ui()
        
        
        '''cur = self.movie_con.cursor()
        cur.execute("select version()")
        
        ver = cur.fetchone()
        
        print "database version AJ from querywin: %s " % ver'''
        
    def get_db_connection(self):
        return self.movie_con
        
    def movie_db_ui(self):
        
        ents = self.makeform()
        self.frame.bind('<Return>', (lambda event, e=ents: self.fetch_movie_data_from_db(e)))
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 10, command = self.close_windows)
        self.quitButton.pack(side=tk.RIGHT)
        
        self.submitButton = tk.Button(self.frame, text = 'Submit', width = 10, command = (lambda e=ents: self.sumbit_movie_data_to_db(e)))
        self.submitButton.pack(side=tk.LEFT)
        
        self.fetchButton = tk.Button(self.frame, text = 'Fetch', width = 10, command = (lambda e=ents: self.fetch_movie_data_from_db(e)))
        self.fetchButton.pack(side=tk.RIGHT)
        

        
        self.frame.pack()
        
        '''cur = self.movie_con.cursor()
        cur.execute("select version()")        
        ver = cur.fetchone()        
        print "database version fetch from querywin: %s " % ver'''
    
    def makeform(self):
        entries = []
        for field in self.fields:
            row = tk.Frame(self.frame)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
        return entries
    
    def close_windows(self):
        self.master.destroy()
    
    def preprocessing(self):
        pass
    
    def fetch_movie_data_from_db(self, entries):
        cur = self.movie_con.cursor()
        cur.execute("SELECT * FROM Movies")
        movieRows = cur.fetchone()
        
        #use generic for loop
        movieTitle = movieRows[1]
        movieYear = movieRows[2]
        movieProducers = movieRows[3]
        movieCountry = movieRows[4]
        
        print "preprocessing..."
        self.preprocessing()
        
        
        entries[0][1].insert(tk.END, movieTitle)
        entries[1][1].insert(tk.END, movieYear)
        entries[2][1].insert(tk.END, movieProducers)
        entries[3][1].insert(tk.END, movieCountry)
        
        #print('%s: "%s"' % (field, entries[0][1].get))
        '''for entry in entries:
            field = entry[0]
            text  = entry[1].set()
            print('%s: "%s"' % (field, text))'''
            
        '''cur = self.movie_con.cursor()
        cur.execute("select version()")        
        ver = cur.fetchone() 
        cur.close()       
        print "database version fetch from querywin: %s " % ver'''
    
    def sumbit_movie_data_to_db(self, entries):
        cur = self.movie_con.cursor()

        #use generic for loop
        movieTitle = entries[0][1].get()
        movieYear = entries[1][1].get()
        movieProducers = entries[2][1].get()
        movieCountry = entries[3][1].get()        
        
        cur.execute("INSERT INTO Movies(Title, Year, Producers, Country) VALUES(%s, %s, %s, %s )", (movieTitle, movieYear, movieProducers, movieCountry))
        
        
        self.postprocessing()
        
        
        
        print "postprocessing... "
        
        
    def postprocessing(self):
        pass