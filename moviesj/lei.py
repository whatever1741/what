CLASSIFIED={}
class Classified_movie:
    def __init__(self, cid, cidname):
        self.cid = cid
        self.cidname = cidname
class Movie:
    def __init__(self, id, name, redate, soldout, mrole, director, poster):
        self.id = id
        self.name = name
        self.redate = redate
        self.soldout = soldout
        self.mrole = mrole
        self.director = director
        self.cid = None
        self.poster = poster
class Manager:
    @staticmethod
    def add(movie, classifi):
        classifi.cid = movie.cid
        for issk,issv in CLASSIFIED.items():
            if classifi.cid==issk:
                issv[movie.id]=movie
                break
        else:
            slist={}
            CLASSIFIED[classifi.cid]=slist
            slist[movie.id]=movie.name
    @staticmethod
    def show(cid):
        for iss in CLASSIFIED.keys():
            if iss==cid:
                for issk,issv in CLASSIFIED.get(iss):
                    print("电影id是{}".format(issk))
                    print("电影是{}".format(issv))
        else:
            print("没有这个分类")
    @staticmethod
    def delll(id):
        for issv in CLASSIFIED.values():
            for issvv in issv.keys():
                if issvv==id:
                    issv.pop(id)
                    break
        else:
            print("没有这部电影")


