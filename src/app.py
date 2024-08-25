import tkinter as tk

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("中国象棋")

        # 棋盘的宽度和高度
        self.canvas_width = 500  # 增加宽度以适应边界的数字
        self.canvas_height = 550  # 增加高度以适应边界的数字

        # 创建画布
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        # 棋盘的网格尺寸
        self.grid_size = 50
        # 棋子半径
        self.piece_radius = 20

        # 初始化棋盘和棋子
        self.board = [
            ["車", "馬", "象", "士", "将", "士", "象", "馬", "車"],
            ["", "", "", "", "", "", "", "", ""],
            ["", "炮", "", "", "", "", "", "炮", ""],
            ["卒", "", "卒", "", "卒", "", "卒", "", "卒"],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["兵", "", "兵", "", "兵", "", "兵", "", "兵"],
            ["", "炮", "", "", "", "", "", "炮", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["车", "马", "相", "仕", "帅", "仕", "相", "马", "车"]
        ]
        self.create_board()

    def create_board(self):
        # 绘制棋盘网格
        for i in range(10):
            self.canvas.create_line(50, 50 + i * self.grid_size, 450, 50 + i * self.grid_size)  # 改变起点x坐标为50
        for i in range(9):
            if i == 0 or i == 8:
                self.canvas.create_line(50 + i * self.grid_size, 50, 50 + i * self.grid_size, 500)  # 改变起点y坐标为50
            else:
                self.canvas.create_line(50 + i * self.grid_size, 50, 50 + i * self.grid_size, 250)
                self.canvas.create_line(50 + i * self.grid_size, 300, 50 + i * self.grid_size, 500)

        # 绘制红方（下方）的数字标记 从右到左 1 到 9
        for i, num in enumerate("九八七六五四三二一"):
            self.canvas.create_text(50 + i * self.grid_size, 537, text=num, font=("Arial", 14))

        # 绘制黑方（上方）的数字标记 从左到右 1 到 9
        for i in range(9):
            self.canvas.create_text(50 + i * self.grid_size, 18, text=str(i + 1), font=("Arial", 14))

        # 绘制棋子
        for row in range(10):
            for col in range(9):
                piece = self.board[row][col]
                if piece:
                    x = 50 + col * self.grid_size  # 修改为从50开始
                    y = 50 + row * self.grid_size  # 修改为从50开始
                    self.canvas.create_oval(x - self.piece_radius, y - self.piece_radius,
                                            x + self.piece_radius, y + self.piece_radius, fill="white")

                    # 根据棋子的位置决定颜色
                    if row < 5:  # 黑方的棋子在前五行
                        color = "black"
                    else:  # 红方的棋子在后五行
                        color = "red"

                    self.canvas.create_text(x, y, text=piece, font=("Arial", 16), fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()