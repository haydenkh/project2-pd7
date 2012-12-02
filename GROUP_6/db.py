#!usr/bin/python                                                                                                                               

from pymongo import Connection

class db:
    def __init__(self):
        """ Handles connecting to mongo.stuycs.org, authentication, and connecting to our (Group_6) database. Returns our database.    
        """
        self.connection = Connection('mongo.stuycs.org')
        self.db = self.connection.admin
        self.db.authenticate('ml7','ml7')
        self.db = self.connection['Group_6']



    def getTaglist(self):
        """ Returns a list of all of the tags used
        """
        collection = self.db.tags
        list = collection.find({"tag" : "tag"})[0]['tags']
        print list
        return list
        
        

    def getTags(self,picture):
        """ Returns a list of tags associated with a picture
        """
        collection = self.db.pictures
        tags = collection.find({"picture" : picture})[0]['tags']
        print tags
        return tags
        
    def addTag(self,picture,tag):
        """ Adds a tag to the picture
        """
        self.db.pictures.update({"picture" : picture}, {"$push": {"tags":tag}})
        self.db.tags.update({"tag":"tag"},{"$push":{"tags":tag}})

    def getComments(self,picture):
        """ Returns a list of all the comments associated with the picture
        """
        collection = self.db.pictures
        comments = collection.find({"picture" : picture})[0]['comments']
        print comments
        return comments

    def addComment(self,picture,comment):
        """ Adds a comment to the picture
        """
        self.db.pictures.update({"picture" : picture},{"$push":{"comments":comment}})

    def getPictures(self,tag):
        """ Returns a list of pictures with the tag
        """
        collection = self.db.pictures
        ans=[x["picture"] for x in collection.find({"tags":tag})]
        print ans
        return ans

    def addPicture(self,picture):
        """ Adds a picture to the database
        """
        collection = self.db.pictures
        collection.insert({"picture":picture,"comments":[],"tags":[]})

        
if __name__=="__main__":
    mydb = db()
    print mydb.db
    mydb.addPicture("http://b.vimeocdn.com/ps/101/290/1012902_300.jpg");
