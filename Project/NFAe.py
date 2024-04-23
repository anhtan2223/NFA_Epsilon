class NFAe :
    def __init__(self,Var , Sigma , MoveMap , Start , End ) -> None:
        self.var = Var
        self.sigma = Sigma
        self.map = MoveMap
        self.start = Start
        self.end = End
        self.current = set([Start])
        
    def MoveE(self):
        result = set()
        for currentItem in self.current :
            result.add(currentItem)
            try :
                # print(currentItem)
                listItem = [self.map[currentItem]['e'] ]
                # print(listItem)
                while len(listItem) != 0 :
                    item = listItem.pop(0)
                    # print(item)
                    for i in item :
                        result.add(i)
                        try :
                            listItem.append(self.map[i]['e'])
                        except KeyError:
                            continue
            except KeyError :
                pass
        self.current = result

    def Move(self,input):
        # print("Start State :" , self.current)
        self.MoveE()
        # print("Move Epsilon : " , self.current)
        result = set()
        for currentItem in self.current :
            try :
                listValue = self.map[currentItem][input]
                for value in listValue :
                    result.add(value)
            except KeyError:
                continue
        
        self.current = result
        # print("Move with Input : " , self.current )
        self.MoveE()
        # print("Result State : " , self.current )
    
    def MoveWithString(self , string):
        path = [self.current]
        for i in string :
            # print(self.current , f"\n\n\nMove with {i} ")
            self.Move(i)
            path.append(self.current)
        return path

    def IsAccept(self):
        for e in self.end :
            if e in self.current :
                return True 
        return False

    def ResetCurrent(self):
        self.current = set([self.start])


