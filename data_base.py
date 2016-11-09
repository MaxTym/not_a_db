class NotDataBase:


    def __init__(self, data_filename="not_a_db.db"):
        self.data_filename = data_filename
        self.data = []
        with open(self.data_filename, "r") as f:
            for line in f:
                self.data.append(line.strip())

    def __getitem__(self, index):
        return self.data[index]

    def add(self, new_item):
        self.data.append(new_item)
        self._save()

    def remove(self, index):
        try:
            index = int(index)
        except:
            pass
        if isinstance(index, int):
            self.data.pop(index)
        else:
            if index in self.data:
                self.data.pop(self.data.index(index))
        self._save()

    def clear(self):
        self.data = []
        self._save()

    def _save(self):
        with open(self.data_filename, "w") as f:
            for d in self.data:
                f.write(d)
                f.write("\n")
