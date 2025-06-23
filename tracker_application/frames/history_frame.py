from pathlib import Path
from tkinter import Tk, Frame, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_FRAME1 = OUTPUT_PATH / "assets" / "frame1"

def relative_to_assets_history_frame(path: str) -> str:
    return str(ASSETS_PATH_FRAME1 / path)


class HistoryFrame(Frame):
    def __init__(self, master, return_callback):
        super().__init__(master, bg="#2E2E2E")
        self.configure(bg="#2E2E2E")
        self.canvas = Canvas(
            self,
            bg = "#2E2E2E",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.pack(fill="both", expand=True)

        # Header Text -----------------------------------------------------------------
        self.canvas.create_text(
            248.0,
            36.0,
            anchor="nw",
            text="History",
            fill="#FFFFFF",
            font=("JosefinSans Medium", 50 * -1)
        )


        # Back button
        self.back = PhotoImage(
            file=relative_to_assets_history_frame("back_button.png"))
        self.back_button = Button(
            self,
            image=self.back,
            borderwidth=0,
            highlightthickness=0,
            command=return_callback,
            relief="flat",
            bg="#2E2E2E",
            activebackground="#2E2E2E"
        )
        self.back_button.place(
            x=30.0,
            y=30.0,
        )