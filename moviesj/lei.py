CLASSIFIED={}
LIST={ 1: '最新影片',
          2: '经典影片',
          3: '国内电影',
          4: '欧美电影',
          5: '日韩电影',
          6: '华语电视',
          7: '日韩电视',
          8: '欧美电视',
          9: '最新综艺' }
#定义一个分类菜单,里面有将电影加入分类id的方法,但是通过Manager调用
class Classified_menu:
    @staticmethod
    def addd(movie):
        if movie.cid in CLASSIFIED.keys():
            # 如果有这个分类,就找到了,往里面加
            CLASSIFIED[movie.cid][movie.id]=movie
            return LIST[movie.cid]
        else:
            list={}
            CLASSIFIED[movie.cid]=list
            CLASSIFIED[movie.cid][movie.id]=movie
#             如果没有这个分类就创建了往里面加

class Movie:
    def __init__(self,id,name,redate, soldout, mrole, director,cid, poster):
        self.id = id
        self.name = name
        self.redate = redate
        self.soldout = soldout
        self.mrole = mrole
        self.director = director
        self.cid = cid
        self.poster = poster
class Manager:
    @staticmethod
    def add(*args):
        for i in args:
            Classified_menu.addd(i)
    @staticmethod
    def show_mo(id):
        for issv in CLASSIFIED.values():
            for issvv,zui in issv.items():
                if issvv==id:
                    print("电影id为{}\n电影名为{}\n上映日期为{}\n是否下架为{}\n主演为{}\n导演为{}\n分类为{}\n电影海报为{}\n"
                          .format(zui.id, zui.name, zui.redate, zui.soldout, zui.mrole,zui.director ,Classified_menu.addd(zui),
                          zui.poster))
                    break
    @staticmethod
    def show(cid):
        for iss in CLASSIFIED.keys():
            if iss==cid:
                for issk,issv in CLASSIFIED.get(iss).items():
                    Manager.show_mo(issv.id)
                else:
                    break
        else:
            print("没有这个分类")
    @staticmethod
    def delll(id):
        for issv in CLASSIFIED.values():
            for issvv in issv.keys():
                if issvv==id:
                    issv.pop(id)
                    break
def test():
    aa=Movie(11, '<<蝙蝠侠>>', '7-1', "是", 'CC','DD' ,1,'FF' )
    cc=Movie(13, '<<闪电侠>>', '8-1', '否', 'CC','DD' ,1,'FF' )
    bb=Movie(12, '<<键盘侠>>', '9-1', '否', 'CC','DD' ,2,'FF' )
    Manager.add(aa,bb,cc)
    print(CLASSIFIED)
    Manager.show(1)
    Manager.delll(12)
    Manager.show_mo(11)
    print(CLASSIFIED)
if __name__ == '__main__':
    test()

