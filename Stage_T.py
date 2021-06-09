import sys
import os
from pathlib import Path
import json
import math
import shutil

os.chdir(os.path.dirname(__file__))
mydir = os.path.dirname(__file__) or "."
Remapped_Data = os.path.join(mydir, "Remapped_Data")
Stage_0 = os.path.join(mydir, "Stage_0")
Stage_1 = os.path.join(mydir, "Stage_1")
Stage_2 = os.path.join(mydir, "Stage_2")
Stage_3 = os.path.join(mydir, "Stage_3")

Bot_Files = os.path.join(mydir, "Bot_Files")
BulkStory = os.path.join(Stage_3, "BulkStory.json")
TexEN = os.path.join(Stage_3, "TextEN.json")
mydir = os.path.join(mydir, "Stage_T")
F1 = os.path.join(mydir, "1st_Circle")
S2 = os.path.join(mydir, "2nd_Circle")
T3 = os.path.join(mydir, "3rd_Circle")

os.chdir(os.path.dirname(__file__))
mydir = os.path.dirname(__file__) or "."

key = 0x92
#EN = "C:\\Users\\eikea\\Documents\\Beyond Ultra\\Text Hell\\1st_Circle\\ART\\UI\\Readable\\EN"
EN = os.path.join(T3, "EN")
ENLan = "C:\\Users\\eikea\\Documents\\Beyond Ultra\\Stage_T\\1st_Circle\\Data\\_ExcelBinOutput\\TextMap\\EN\\Hash"
def XR(fpath,opath):
    byte_array = bytearray(open(fpath, 'rb').read())
    size = len(byte_array)
    xord_byte_array = bytearray(size)
    for i in range(size):
            xord_byte_array[i] = byte_array[i] ^ key
    open(opath, 'wb').write(xord_byte_array)

def Floader(Loc):
    FOut = ""
    with open(Loc, encoding='UTF-8',errors='replace') as temp:#
        FOut = temp.read()
        temp.close()
    return(FOut)
Rep = { "1" : "Goblet",
        "2" : "Feather",
        "3" : "Headpiece",
        "4" : "Flower",
        "5" : "Timepiece"
}
def Dim():
    End = {}
    End.update({"Books" : {}})
    End.update({"Artifacts" : {}})
    End.update({"Weapons" : {}})
    End.update({"Gliders" : {}})
    End.update({"Costume" : {}})
    TexEnd = {}
    for item in os.listdir(EN):
        Work = item.split("_")
        Loc = os.path.join(EN,item)
        #XR(Loc,Out)
        if item[0:4] == "Book":
            FText = Floader(Loc)
            Nitem = item.split("Book")[1]
            Nitem = Nitem.split("_")[0]
            End["Books"].update({Nitem : FText})

        elif item[0:5] == "Relic":
            FText = Floader(Loc)
            Nitem = item.split("Relic")[1]
            NTyp = Rep[Nitem.split("_")[1]]
            Nitem = Nitem.split("_")[0]
            if Nitem not in End["Artifacts"]:
                End["Artifacts"].update({Nitem : {}})
            End["Artifacts"][Nitem].update({NTyp : FText})

        elif item[0:6] == "Weapon":
            FText = Floader(Loc)
            Nitem = item.split("Weapon")[1]
            Nitem = Nitem.split("_")[0]
            End["Weapons"].update({Nitem : FText})

        elif item[0:5] == "Wings":
            FText = Floader(Loc)
            Nitem = item.split("Wings")[1]
            Nitem = Nitem.split("_")[0]
            End["Gliders"].update({Nitem : FText})

        elif item[0:7] == "Costume":
            FText = Floader(Loc)
            Nitem = item.split("Costume")[1]
            Nitem = Nitem.split("_")[0]
            End["Costume"].update({Nitem : FText})


    with open(BulkStory, "w", encoding='utf-8') as write_file:
        json.dump(End, write_file, indent=4, ensure_ascii=False)

def Cus():
    End = {}
    for item in os.listdir(ENLan):
        Work = item.split("_")
        Loc = os.path.join(ENLan,item)
        Out = os.path.join(mydir, "2nd_Circle\\Lang",item)
        XR(Loc,Out)
        if item[0:4] == "Book":
            FText = Floader(Loc)
            Nitem = item.split("Book")[1]
            Nitem = Nitem.split("_")[0]
            End["Books"].update({Nitem : FText})



    with open(TexEN, "w", encoding='utf-8') as write_file:
        json.dump(End, write_file, indent=4, ensure_ascii=False)

        """
        if Work[0] == "UI":
            if Work[1] == "ItemIcon":
                if os.path.exists(os.path.join(mydir, "3rd_Circle",Work[0],Work[1])):
                    pass
                else:
                    os.makedirs(os.path.join(mydir, "3rd_Circle",Work[0],Work[1]))
                if len(Work) == 4:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],(Work[2]+"_"+Work[3]))
                else:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2])
                shutil.copyfile(F1N, T3N)
        """

Dim()
