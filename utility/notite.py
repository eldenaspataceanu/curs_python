f = open("images/poze.txt")
ids = []
for line in f:
    line = line.rstrip("\n")
    ids.append(line)
f.close()
# j = 0
imgs = []
for i in range(3):
    imgs.append(ImageTk.PhotoImage(Image.open(f"images/{ids[i]}")))
    # img = Image.open(f"images/{ids[i]}")  # open image
    # resized = img.resize((70, 80), Image.ANTIALIAS)
    # self._img = ImageTk.PhotoImage(resized)
    # self._canvas.image = self._img
    Label(self._frame, image=imgs[-1], width=60, height=80).grid()
    #         # imagine.grid(row=i, column=j + 1)
    #         # images_ = tk.Label(self._frame, image=self._img, height=80, width=80)
    #         # images_.grid(row=i, column=j + 1)