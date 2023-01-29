import os

class DataPack:

    def __init__(self, DPname):
        self.DPname = DPname

    def create(self):
        #Tworzenie folderów:
        self.path1 = f"{self.DPname}/data/minecraft/tags/functions"
        self.path2 = f"{self.DPname}/data/yourDatapack/functions"
        
        os.makedirs(self.path1)
        os.makedirs(self.path2)

        #Tworzenie plików:
        self.pack = open(f"{self.DPname}/pack.mcmeta", "w")

        #Tworzenie funcji mc:
        self.load = open(f"{self.DPname}/data/minecraft/tags/functions/load.json", "w")
        self.tick = open(f"{self.DPname}/data/minecraft/tags/functions/tick.json", "w")

        #Tworzenie funcjii:
        self.init_y = open(f"{self.DPname}/data/yourDatapack/functions/init.mcfunction", "w")
        self.tick_y = open(f"{self.DPname}/data/yourDatapack/functions/tick.mcfunction", "w")

        #Pisanie funcji mc:
        self.data_tick = open("data/tick.txt", "r")
        self.data_load = open("data/load.txt", "r")

        self.tick.write(self.data_tick.read())
        self.load.write(self.data_load.read())

        #Pisanie plików:
        self.data_pack = """{
    "pack": {
        "pack_format": 6,
        "description": "To jest datapack"
    }
}
"""
        self.pack.write(self.data_pack)

        print(f"Utworzono folder {self.DPname}!")
        
