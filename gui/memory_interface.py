import customtkinter as ctk


class MemoryInterface(ctk.CTkFrame):
    def __init__(self, vm, master):
        # Create frame and sub-widgets
        super().__init__(master)
        self.mem_loc_label = ctk.CTkLabel(master=self, text='Address')
        self.mem_val_label = ctk.CTkLabel(master=self, text='Value')
        self.memory_list = ScrollableMemory(vm, master=self, width=150, height=300, corner_radius=0)
        
        # Pack sub-widgets in frame using grid
        self.mem_loc_label.grid(row=1, column=0, padx=10, pady=10, sticky='nw')
        self.mem_val_label.grid(row=1, column=1, padx=10, pady=10, sticky='nw')
        self.memory_list.grid(row=2, column=0, padx=10, pady=10, sticky='nw', columnspan=2)


class ScrollableMemory(ctk.CTkScrollableFrame):
    def __init__(self, vm, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.vm = vm
        self.label_list = []
        self.entry_list = []
        self.entry_vars = []

    def add_item(self, index, value):
        i = len(self.label_list)
        while index >= len(self.label_list):
            sv = ctk.StringVar()
            sv.trace_add('write', lambda name, index, mode, var=sv, i=i: self.update_vm_mem(i, sv.get()))
            self.entry_vars.append(sv)
            label = ctk.CTkLabel(self, text=i, width=10, compound='left', padx=5, anchor='w')
            entry = ctk.CTkEntry(self, width=50, height=10, textvariable=sv)
            label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky='w')
            entry.grid(row=len(self.entry_list), column=1, pady=(0, 10), padx=5)
            self.label_list.append(label)
            self.entry_list.append(entry)
            i += 1
        self.entry_list[index].delete(0, ctk.END)
        self.entry_list[index].insert(0, value)

    def remove_item(self, index):
        for label, entry in zip(self.label_list, self.entry_list):
            if index == label.cget('text'):
                entry.delete(0, ctk.END)
                entry.insert(0, self.vm.DEFAULT_MEMORY)
                self.update_vm_mem(index, self.vm.DEFAULT_MEMORY)
                return

    def update_vm_mem(self, index, val):
        try:
            self.vm.mainMemory[index] = val
        except Exception as e:
            return e
    def set_accum(self, val):
        self.vm.vmAccumulator = val