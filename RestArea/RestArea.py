from tkinter import *
from test import SearchRestArea

RestAreaList = []
checkDataButton = 0

class RestArea:
    def food(self):
        global checkDataButton
        checkDataButton = 0
        self.showData()

    def GasStation(self):
        global checkDataButton
        checkDataButton = 1
        self.showData()

    def Facility(self):
        global checkDataButton
        checkDataButton = 2
        self.showData()

    def showData(self):
        global checkDataButton
        if checkDataButton == 0:    #음식점
            pass
        elif checkDataButton == 1:  #주유소
            pass
        else:                       #편의시설
            pass

    def sendMail(self):
        pass

    def initDataPhoto(self):
        # 사진
        self.dataPhoto = PhotoImage(file='resource\_bg.png')
        dataImage = Label(self.window, image=self.dataPhoto, width=280, height=220)
        dataImage.place(x=50, y=330)

    def initDataList(self):
        # 목록
        dataList = Listbox(self.window, activestyle='none', width=35, height=18)
        dataList.place(x=333, y=330)

    def initDataInfo(self):
        # 정보
        dataInfo = Text(self.window, width=40, height=5)
        dataInfo.place(x=50, y=550)

    def initDataCategory(self):
        # 음식점
        categoryFood = Button(self.window, text="음식점", width=8, command=self.food)
        categoryFood.place(x=50, y=300)
        # 주유소
        categoryGas = Button(self.window, text='주유소', width=8, command=self.GasStation)
        categoryGas.place(x=110, y=300)
        # 편의시설
        categoryFacility = Button(self.window, text='편의시설', width=8, command=self.Facility)
        categoryFacility.place(x=170, y=300)

    def initEventData(self):
        eventList = Text(self.window, width=75, height=5)
        eventList.place(x=50, y=650)

    def intiSendGmail(self):
        # Gmail보내는 버튼
        self.mailPhoto = PhotoImage(file='resource\mail.gif')
        self.mailButton = Button(self.window, image=self.mailPhoto, command=self.sendMail)
        self.mailButton.place(x=400, y=50)

    def SearchRestAreaByName(self):
        global RestAreaList
        RestAreaList.clear()
        RestAreaList = SearchRestArea(self.searchBox.get())
        for i in range(len(RestAreaList)):
            self.searchList.insert(i,RestAreaList[i])


    def initSearchCell(self):
        # 검색창과 그 옆에 목록
        # 검색창
        self.searchBox = Entry(self.window, width=30)
        self.searchBox.place(x=50, y=220)

        Button(self.window, text='search', command=self.SearchRestAreaByName).place(x=280, y=220)
        # 검색 목록
        #self.searchList = Text(self.window, width=30, height=5)
        self.searchList = Listbox(self.window, width=30, height=5)
        self.searchList.place(x=360, y=220)


    def __init__(self):
        #global restArea
        #restArea = self

        self.window = Tk()
        self.window.title = 'ReatArea'
        self.window.geometry('600x750+100+0')

        # 우리 메인 로고
        self.RAPhoto = PhotoImage(file='resource\R.gif')
        Logo = Label(self.window, image=self.RAPhoto)
        Logo.place(x=50, y=30)

        self.initEventData()
        self.initDataPhoto()
        self.initDataList()
        self.initDataInfo()
        self.initDataCategory()
        self.intiSendGmail()
        self.initSearchCell()
        #self.window.mainloop()
