class Color:
    colordict = {
            "black" :"0",
            "red"   :"1",
            "green" :"2",
            "yellow":"3",
            "blue"  :"4",
            "purple":"5",
            "cian"  :"6",
            "white" :"7"
            }

    def __init__(self, bg, fg):
        self.bg = Color.colordict[bg]
        self.fg = Color.colordict[fg]

    def base(self, string, reverse=False):
        if reverse == True:
            return f"\033[4{self.fg};3{self.bg}m" + string + "\033[0m"
        else:
            return f"\033[4{self.bg};3{self.fg}m" + string + "\033[0m"

    def bright(self, string, reverse=False):
        if reverse == True:
            return f"\033[10{self.fg};9{self.bg}m" + string + "\033[0m"
        else:
            return f"\033[10{self.bg};9{self.fg}m" + string + "\033[0m"
