import cv2,os
import numpy as np

ids = ['0','1','2','3','4','5']
pss = [0,1,2,3,4,5,6]

class player():

    def __init__(self):
        self.name = ''
        self.wcard = []
        self.rcard = []
        self.id = 0

    def showcard(self):
        pic = None
        if self.name != '目击':
            pic1 = cv2.imread(self.wcard[0])
            pic1 = np.hstack([pic1, cv2.imread(self.wcard[1])])
            pic1 = np.hstack([pic1, cv2.imread(self.wcard[2])])
            pic1 = np.hstack([pic1, cv2.imread(self.wcard[3])])

            pic2 = cv2.imread(self.rcard[0])
            pic2 = np.hstack((pic2, cv2.imread(self.rcard[1])))
            pic2 = np.hstack((pic2, cv2.imread(self.rcard[2])))
            pic2 = np.hstack((pic2, cv2.imread(self.rcard[3])))

            pic = np.vstack((pic1, pic2))
            cv2.imwrite('./cards/'+self.name+'.jpg',pic)
            #cv2.imshow(self.name,pic)
            #cv2.waitKey(0)
        return pic

class cards():
    def __init__(self):
        self.wcards_path = '../fzxc/w/'
        self.wcards = os.listdir(self.wcards_path)
        self.index_w = 0
        self.max_w = len(self.wcards)
        np.random.shuffle(self.wcards)

        self.rcards_path = '../fzxc/r/'
        self.rcards = os.listdir(self.rcards_path)
        self.index_r = 0
        self.max_r = len(self.rcards)
        np.random.shuffle(self.rcards)

        self.fcards_path = '../fzxc/f/'
        self.fcards = os.listdir(self.fcards_path)
        self.index_f = 0
        self.max_f = len(self.fcards)
        np.random.shuffle(self.fcards)

        self.ddcards_path = '../fzxc/dd/'
        self.ddcards = os.listdir(self.ddcards_path)
        self.index_dd = 0
        self.max_dd = len(self.ddcards)
        np.random.shuffle(self.ddcards)

        self.sycards_path = '../fzxc/sy/'
        self.sycards = os.listdir(self.sycards_path)

        self.xscards_path = '../fzxc/xs/'
        self.xscards = os.listdir(self.xscards_path)
        self.index_xs = 0
        self.max_xs = len(self.xscards)
        np.random.shuffle(self.xscards)

    def check(self,num):
        if self.max_w-self.index_w < 4*num:
            self.index_w = 0
            np.random.shuffle(self.wcards)

        if self.max_r-self.index_r < 4*num:
            self.index_r = 0
            np.random.shuffle(self.rcards)

        if self.max_f-self.index_f < 2:
            self.index_f = 0
            np.random.shuffle(self.fcards)

        if self.max_dd-self.index_dd < 1:
            self.index_dd = 0
            np.random.shuffle(self.ddcards)

        if self.max_xs-self.index_xs < 1:
            self.index_xs = 0
            np.random.shuffle(self.xscards)


class game():
    def __init__(self, num):
        self.num = num
        self.cards = cards()
        self.players = []
        # self.idcards_path = './id/'
        # self.idcards = os.listdir(self.idcards_path)
        # np.random.shuffle(self.idcards)

    def get_id(self):
        if self.num == 4:
            self.ids = ['目击', '凶手', '侦探', '侦探']
            np.random.shuffle(self.ids)
            return self.ids
        elif self.num == 5:
            self.ids = ['目击', '凶手', '侦探', '侦探', '侦探']
            np.random.shuffle(self.ids)
            return self.ids
        elif self.num == 6:
            self.ids = ['目击', '凶手', '第二目击', '帮凶','侦探', '侦探']
            np.random.shuffle(self.ids)
            return self.ids

    def create_player(self,ids):
        players = []
        i = 0
        for id in ids:
            players.append(player())
            players[-1].name = id
            if id == '目击':
                players[-1].id = i
            else:
                players[-1].id = i
                players[-1].wcard = self.get_wcards(4)
                players[-1].rcard = self.get_rcards(4)
            i+=1
        self.players = players

    def show_player(self):
        for p in self.players:
            #print(p.id, p.name)
            #print(p.wcard)
            #print(p.rcard)
            p.showcard()

    def get_wcards(self,num):
        wcards = []
        for x in self.cards.wcards[self.cards.index_w:self.cards.index_w + num]:
            wcards.append(os.path.join(self.cards.wcards_path,x))
        self.cards.index_w += num
        return wcards

    def get_rcards(self,num):
        rcards = []
        for x in self.cards.rcards[self.cards.index_r:self.cards.index_r + num]:
            rcards.append(os.path.join(self.cards.rcards_path,x))
        self.cards.index_r += num
        return rcards



    def run(self):
        self.ids = ids #获取身份
        #print(self.)
        self.create_player(self.ids)
        self.show_player()




g = game(6)
g.run()
print(g.get_id())






