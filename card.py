class card:
    front = ""
    back = ""

    def __init__(self, front, back):
        self.front = str(front)
        self.back = str(back)

    def get_front(self):
        return  self.front

    def get_back(self):
        return self.back
