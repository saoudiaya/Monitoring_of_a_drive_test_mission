import tkinter as tk
from tkinter import ttk
import customtkinter
from tkintermapview import TkinterMapView

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

w = tk.Tk()
w.title(" SFMTechnologies-Drive Test")
w.geometry("862x519")
w.configure(bg="#ffffff")     

def search_event(event=None):
    map_widget.set_address(entry.get())
    slider_1.set(map_widget.zoom)
def slider_event(value):
    map_widget.set_zoom(value)
def set_marker_event():
    current_position = map_widget.get_position()

# ============ create two CTkFrames ===========
frame_left = customtkinter.CTkFrame(master=w, width=150, corner_radius=0)
frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
frame_right = customtkinter.CTkFrame(master=w, corner_radius=0)
frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
# ============ frame_left ===========
button_1 = customtkinter.CTkButton(master=frame_left,
                                        text="Set Marker",
                                        command=set_marker_event,
                                        width=120, height=30,
                                        border_width=0,
                                        corner_radius=8)
button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)
button_2 = customtkinter.CTkButton(master=frame_left,
                                        text="Clear Markers",
                                        width=120, height=30,
                                        border_width=0,
                                        corner_radius=8)
button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)
# ============ frame_right ===========
map_widget=TkinterMapView(w,width=800,height=600,corner_radius=0)

map_widget.set_zoom(20)
    # set current widget position by address
marker_1 = map_widget.set_address("81 Av. Hédi Chaker, Tunis 1002", marker=True)
print(marker_1.position, marker_1.text)  # get position and tex
marker_1.set_text("Votre trajet")  # set new text
    # marker_1.set_position(48.860381, 2.338594)  # change position
    # marker_1.delete(
entry = customtkinter.CTkEntry(master=frame_right,
                                    placeholder_text="type address",
                                    width=140,
                                    height=30,
                                    corner_radius=8)
entry.grid(row=1, column=0, sticky="we", padx=(20, 0), pady=20)
entry.entry.bind("<Return>", search_event)
button_5 = customtkinter.CTkButton(master=frame_right,
                                        height=30,
                                        text="Search",
                                        command=search_event,
                                        border_width=0,
                                        corner_radius=8)
button_5.grid(row=1, column=1, sticky="w", padx=(20, 0), pady=20)
slider_1 = customtkinter.CTkSlider(master=frame_right,
                                        width=200,
                                        height=16,
                                        from_=0, to=19,
                                        border_width=5,
                                        command=slider_event)
slider_1.set(map_widget.zoom)
slider_1.grid(row=1, column=2, sticky="e", padx=20, pady=20)




w.tk.mainloop()




""" 
f2=Frame(w,width=900,height=455,bg='white')
            f2.place(x=0,y=45)
            l2=Label(f2,text=' Votre trajet',fg='#323335',bg='white')
            l2.config(font=('Comic Sans MS',20))
            l2.place(x=500,y=10)
            my_lablel=LabelFrame(w)
            my_lablel.pack(pady=20)
            map_widget=tkintermapview.TkinterMapView(my_lablel,width=800,height=600,corner_radius=0)
            map_widget.pack()
            #set coordinates
            #map_widget.set_position(36.8063666,10.1813795)
            #map_widget.set_address("81 Av. Hédi Chaker, Tunis 1002")
            #set a zoom lavel
            map_widget.set_zoom(20)
            # set current widget position by address
            marker_1 = map_widget.set_address(res['trajet'][0], marker=True)

            print(marker_1.position, marker_1.text)  # get position and text

            marker_1.set_text("Votre trajet")  # set new text
            # marker_1.set_position(48.860381, 2.338594)  # change position
            # marker_1.delete()















class App(customtkinter.CTk):
                
                APP_NAME = "Map View"
                WIDTH = 100
                HEIGHT = 100

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)

                    self.title(App.APP_NAME)
                    self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
                    self.minsize(App.WIDTH, App.HEIGHT)

                    self.protocol("WM_DELETE_WINDOW", self.on_closing)
                    self.bind("<Command-q>", self.on_closing)
                    self.bind("<Command-w>", self.on_closing)
                    self.createcommand('tk::mac::Quit', self.on_closing)

                    self.marker_list = []

                    # ============ create two CTkFrames ============

                    self.grid_columnconfigure(0, weight=0)
                    self.grid_columnconfigure(1, weight=1)
                    self.grid_rowconfigure(0, weight=1)

                    self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0)
                    self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

                    self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=self.fg_color)
                    self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

                    # ============ frame_left ============

                    self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                            text="Set Marker",
                                                            command=self.set_marker_event,
                                                            width=120, height=30,
                                                            border_width=0,
                                                            corner_radius=8)
                    self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

                    self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                            text="Clear Markers",
                                                            command=self.clear_marker_event,
                                                            width=120, height=30,
                                                            border_width=0,
                                                            corner_radius=8)
                    self.button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)

                    # ============ frame_right ============

                    self.frame_right.grid_rowconfigure(0, weight=1)
                    self.frame_right.grid_rowconfigure(1, weight=0)
                    self.frame_right.grid_columnconfigure(0, weight=1)
                    self.frame_right.grid_columnconfigure(1, weight=0)
                    self.frame_right.grid_columnconfigure(2, weight=1)

                    self.map_widget = TkinterMapView(self.frame_right, corner_radius=11)
                    self.map_widget.grid(row=0, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(20, 20), pady=(20, 0))
                    self.map_widget.set_address(res['trajet'][i-1])

                    self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                                        placeholder_text="type address",
                                                        width=140,
                                                        height=30,
                                                        corner_radius=8)
                    self.entry.grid(row=1, column=0, sticky="we", padx=(20, 0), pady=20)
                    self.entry.entry.bind("<Return>", self.search_event)

                    self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                            height=30,
                                                            text="Search",
                                                            command=self.search_event,
                                                            border_width=0,
                                                            corner_radius=8)
                    self.button_5.grid(row=1, column=1, sticky="w", padx=(20, 0), pady=20)

                    self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
                                                            width=200,
                                                            height=16,
                                                            from_=0, to=19,
                                                            border_width=5,
                                                            command=self.slider_event)
                    self.slider_1.grid(row=1, column=2, sticky="e", padx=20, pady=20)
                    self.slider_1.set(self.map_widget.zoom)

                def search_event(self, event=None):
                    self.map_widget.set_address(self.entry.get())
                    self.slider_1.set(self.map_widget.zoom)

                def slider_event(self, value):
                    self.map_widget.set_zoom(value)

                def set_marker_event(self):
                    current_position = self.map_widget.get_position()
                    self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

                def clear_marker_event(self):
                    for marker in self.marker_list:
                        marker.delete()

                def on_closing(self, event=0):
                    self.destroy()

                def start(self):
                    self.mainloop()


            if __name__ == "__main__":
                app = App()
                app.start()
"""