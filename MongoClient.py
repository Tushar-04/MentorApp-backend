import pymongo

class MongoConnector:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://svtushar04:6swOd7t4gLoWvFQd@mentor-app.ssqvv2l.mongodb.net/?retryWrites=true&w=majority")
        self.db=self.client["Mentor-app"]
        self.studentData=self.db["StudentData"]
        self.mentorData=self.db["MentorData"]
    
    def get_available_students(self):
        res=list(self.studentData.find({"MentorID":None},{"_id":0}))
        return res
    def get_student(self,Uid):
        res=self.studentData.find_one({"Uid":Uid},{"_id":0})
        return res
    def get_all_students(self):
        res=list(self.studentData.find({},{"_id":0}))
        return res
    def get_my_students(self,Mid):
        l=self.mentorData.find_one({"Mid":Mid},{"StudentList":1})
        res=[]
        for i in l["StudentList"]:
            res.append(self.get_student(i))
        
        return res
    def remove_mentor(self,Uid):
        self.studentData.update_one({"Uid":Uid},{"$set":{"MentorID":None}},True)
    
    def add_mentor(self,Uid,Mid):
        self.studentData.update_one({"Uid":Uid},{"$set":{"MentorID":Mid}},True)

    def save_students(self,Mid,StudentList):
        oldList=self.mentorData.find_one({"Mid":Mid},{"StudentList":1})["StudentList"]
        
        for i in oldList:
            if i not in StudentList:
                self.remove_mentor(i)
        
        for i in StudentList:
            if i not in oldList:
                self.add_mentor(i,Mid)
        
        self.mentorData.update_one({"Mid":Mid},{"$set":{"StudentList":StudentList}},True)
    
    def save_marks(self,uid,marks):
        self.studentData.update_one({"Uid":uid},{"$set":{"Marks":marks,"MarksAssigned":True}},True)
    
    def submit_marks(self,uid,marks):
        self.studentData.update_one({"Uid":uid},{"$set":{"Marks":marks,"MarksAssigned":True,"MarksLocked":True}},True)

if __name__=="__main__":
    pass
    # dm=MongoConnector()
    # r=dm.get_all_students()
    # print(r)
