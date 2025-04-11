import tkinter as tk

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")
        
        # Set up the canvas
        self.canvas_width = 500
        self.canvas_height = 500
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Set up grid dimensions
        self.cell_size = 20
        self.rows = self.canvas_height // self.cell_size
        self.columns = self.canvas_width // self.cell_size

        # Draw the grid of blue cells
        self.grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                cell = self.canvas.create_rectangle(
                    j * self.cell_size, i * self.cell_size, 
                    (j + 1) * self.cell_size, (i + 1) * self.cell_size, 
                    fill="blue", outline="blue"
                )
                row.append(cell)
            self.grid.append(row)

        # Set up the eraser
        self.eraser_size = 3  # Eraser size in terms of cells
        self.eraser = self.canvas.create_rectangle(
            0, 0, self.eraser_size * self.cell_size, self.eraser_size * self.cell_size,
            fill="white", outline="black"
        )

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag_eraser)

    def start_drag(self, event):
        # Get the position where the mouse was clicked
        self.drag_data = {'x': event.x, 'y': event.y}

    def drag_eraser(self, event):
        # Calculate the distance the mouse has moved
        dx = event.x - self.drag_data['x']
        dy = event.y - self.drag_data['y']

        # Move the eraser rectangle by the mouse movement
        self.canvas.move(self.eraser, dx, dy)

        # Update the last position of the mouse
        self.drag_data['x'] = event.x
        self.drag_data['y'] = event.y

        # Get the current position of the eraser
        eraser_coords = self.canvas.bbox(self.eraser)
        eraser_x1, eraser_y1, eraser_x2, eraser_y2 = eraser_coords

        # Find the cells that the eraser is touching and erase them (set to white)
        for i in range(self.rows):
            for j in range(self.columns):
                cell_coords = self.canvas.bbox(self.grid[i][j])
                cell_x1, cell_y1, cell_x2, cell_y2 = cell_coords

                # Check if the cell is in contact with the eraser
                if (eraser_x2 > cell_x1 and eraser_x1 < cell_x2 and
                    eraser_y2 > cell_y1 and eraser_y1 < cell_y2):
                    # Erase (set cell to white)
                    self.canvas.itemconfig(self.grid[i][j], fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()
