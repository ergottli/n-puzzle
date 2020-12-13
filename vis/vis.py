import tkinter

window_width = 1000
window_height = 1000

npuzzle_size = 3

tile_width = 130

window = tkinter.Tk()
window.geometry(str(window_width) + 'x' + str(window_height))
# centering the window
# window.eval('tk::PlaceWindow %s center' % window.winfo_pathname(window.winfo_id()))


# field_frame = tkinter.Frame(master=window, bg="blue")
# field_frame.place(x=(window_width-(npuzzle_size * tile_width))/2, y=(window_height-(npuzzle_size * tile_width))/2)

def round_rectangle(canvas, x1, y1, x2, y2, r, **kwargs):    
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return canvas.create_polygon(points, **kwargs, smooth=True)

# for i in range(npuzzle_size):
#     for j in range(npuzzle_size):
#         canvas = tkinter.Canvas(field_frame)
#         round_rectangle(10, 10, tile_width, tile_width, 10, fill="red")
#         # frame = tk.Frame(
#         #     master=field_frame,
#         #     width=tile_width,
#         #     height=tile_width,
#         #     bg="red"
#         # )
#         canvas.grid(row=i, column=j, padx=5, pady=5)
#         # label = tk.Label(master=frame, text=str(i*npuzzle_size+j))
#         # label.pack()

canvas = tkinter.Canvas(window)
round_rectangle(canvas, 10, 10, 10+tile_width, 10+tile_width, 10, fill="red")
canvas.pack()

# canvas1 = tkinter.Canvas(window)
# round_rectangle(canvas1, 10+tile_width, , tile_width, tile_width, 10, fill="red")
# canvas1.pack()

# canvas2 = tkinter.Canvas(field_frame)
# round_rectangle(canvas2, 30, 30, tile_width, tile_width, 10, fill="red")
# canvas2.pack()
 

# tile1 = tk.Frame(master=window, height=20, bg="red")
# tile1.pack(fill=tk.X)

# tile1.place()

window.mainloop()