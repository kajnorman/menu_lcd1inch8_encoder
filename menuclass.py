from LCD_1_8_file import LCD_1inch8

import UI


class Menu():
    def __init__(self):
        self.selected_item_index = 0
        self.menuItemList=[]
        self.back_item = menuItem('Back',None)
        self.menuItemList.append(self.back_item)
        self.LCD = LCD_1inch8()
        # color BRG
        self.LCD.fill(self.LCD.WHITE)
        self.LCD.show()



    def show(self):
        y=5
        for obj in self.menuItemList:
            self.LCD.text(obj.ItemLine, 2, y, self.LCD.BLACK)
#            print(obj.ItemLine)
            y = y + 20
        self.LCD.show()
    def highlight(self):
        self.LCD.fill(self.LCD.WHITE)
        self.show()
        self.LCD.rect(1, 3+(self.selected_item_index)*20, 150, 20, 0X0000)
        self.LCD.show()

    def AddMenuItem(self, MI):
        self.menuItemList.append(MI)

    def up(self):
        self.selected_item_index = (self.selected_item_index + 1)%len(self.menuItemList)
        self.highlight()

    def down(self):
        self.selected_item_index = (self.selected_item_index - 1)
        if (self.selected_item_index < 0):
            self.selected_item_index = len(self.menuItemList) -1
        self.highlight()

    def select(self):
         self.menuItemList[self.selected_item_index].execute()

    def execute(self):
        self.highlight()
        Flag = True
        while Flag:
            [u, d, s] = UI.UserInput()
            print([u,d,s])
            if u:
                self.up()
            if d:
                self.down()
            if s:
                if self.menuItemList[self.selected_item_index].function != None:
                    self.select()
                    self.highlight()
                else:
                    return



class menuItem():
    def __init__(self,line,f):
        self.ItemLine = line
        self.function = f

    def execute(self):
        self.function()

