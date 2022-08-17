
import sqlite3


def createDB(): #This function creates the database with column names
    conn = sqlite3.connect('dbAssign.db')

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_files TEXT \
            )")
        conn.commit()
    conn.close()

def findAddTxtFiles():
    #This function stores a tuple then uses a for loop
    #to select only the .txt files and then inert this information
    #into the proper column. It then prints the qualifying data to
    #the cosole.
    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

    conn = sqlite3.connect('dbAssign.db')
    
    
    for x in fileList:
        if x.endswith('.txt'):
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_txtFiles (col_files) VALUES (?)", (x,))
                print(x)
    conn.close()





if __name__ == "__main__":
    createDB()
    findAddTxtFiles()



