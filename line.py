class Line:
    def __init__(self, pointa, pointb):
        self.pointa = pointa
        self.pointb = pointb
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.pointa.x, self.pointa.y, self.pointb.x, self.pointb.y, fill = fill_color, width = 2
        )