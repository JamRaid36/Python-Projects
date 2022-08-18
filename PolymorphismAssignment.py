

#Parent Class
class Media:
    medium = "Film or Music"
    purpose = "Entertainment"

    def mediaInfo(self):#This method will demonstrate polymorphism throughout the script.
        msg = "\nMedium: {}\nPurpose: {}".format(self.medium,self.purpose)
        print(msg)
        
        
        

# child class instance
class Film(Media):
    medium = "Film"
    title = "Happy Gilmore"
    lead_actor = "Adam Sandler"
    length = "2 hours"
    genre = "Comedy"

    def mediaInfo(self):#utilizing same method with a few changes
        msg = "\nType: {}\nTitle: {}\nLead Actor: {}".format(self.medium,self.title,self.lead_actor)
        print(msg)
        
       
    

# another child class instance
class Music(Media):
    medium = "Music"
    album_title = "Live at the Ryman"
    artist = "Johhny Lang"
    length = "63 minutes"
    genre = "Blues"
    media_format = "MP3"
    

    def mediaInfo(self): #utilizing same method with a few changes
        msg = "\nType: {}\nAlbum Title: {}\nArtist: {}".format(self.medium,self.album_title,self.artist)
        print(msg)
    





if __name__ == "__main__":
    #calling method for parent and child classes
    media = Media()
    media.mediaInfo()

    film = Film()
    film.mediaInfo()

    music = Music()
    music.mediaInfo()



    
