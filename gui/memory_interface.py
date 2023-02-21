import customtkinter as ctk


class MemoryInterface(ctk.CTkFrame):
    def __init__(self, master):
        # Create frame and sub-widgets
        super().__init__(master)
        self.mem_loc_label = ctk.CTkLabel(master=self, text='Address')
        self.mem_val_label = ctk.CTkLabel(master=self, text='Value')
        self.memory = ScrollableMemory(master=self, width=150, height=400, corner_radius=0)
        
        # Pack sub-widgets in frame using grid
        self.mem_loc_label.grid(row=1, column=0, padx=10, pady=10, sticky='nw')
        self.mem_val_label.grid(row=1, column=1, padx=10, pady=10, sticky='nw')
        self.memory.grid(row=2, column=0, padx=10, pady=10, sticky='nw', columnspan=2)


class ScrollableMemory(ctk.CTkScrollableFrame):
    DEFAULT_MEMORY = '+0000'
    MEMORY_SIZE = 100

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.label_list = []
        self.entry_list = []
        for i in range(ScrollableMemory.MEMORY_SIZE):
            self.add_item(i, ScrollableMemory.DEFAULT_MEMORY)

    def add_item(self, item, value=None):
        label = ctk.CTkLabel(self, text=item, width=10, compound='left', padx=5, anchor='w')
        entry = ctk.CTkEntry(self, width=50, height=10)
        if value is not None:
            entry.delete(0, ctk.END)
            entry.insert(0, value)
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky='w')
        entry.grid(row=len(self.entry_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.entry_list.append(entry)

    def remove_item(self, item):
        for label, entry in zip(self.label_list, self.entry_list):
            if item == label.cget('text'):
                entry.delete(0, ctk.END)
                entry.insert(0, ScrollableMemory.DEFAULT_MEMORY)
                return