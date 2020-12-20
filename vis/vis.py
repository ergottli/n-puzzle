import tkinter as tk

# window_width = 1000
# window_height = 1000

npuzzle_size = 3

tile_width = 130

window = tk.Tk()
window.configure(bg="#66B1F6")


for i in range(npuzzle_size):
    for j in range(npuzzle_size):
        tile = tk.Canvas(
            master=window,
            width=tile_width,
            height=tile_width,
            bg="#FF67B0",
            bd=0,
            highlightthickness=0,
            relief='ridge',
        )
        tile.create_text(tile_width/2, tile_width/2, font=("Purisa", 20, "bold"), text=str(i*npuzzle_size+j), fill="#5C0088")
        tile.grid(row=i, column=j, padx=3, pady=3)
        

window.mainloop()