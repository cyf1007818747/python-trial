# use dynamic array in python (after seeing .cn solution)
# start to AC - 5:42
# AC
class BrowserHistory:
    def __init__(self, homepage: str):
        self.his = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.his[self.pos + 1: ] = []
        self.his.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        new_pos = max(0, self.pos - steps)
        self.pos = new_pos
        return self.his[new_pos]

    def forward(self, steps: int) -> str:
        new_pos = min(self.pos + steps, len(self.his) - 1)
        self.pos = new_pos
        return self.his[new_pos]
  