import sys
import os
from pathlib import Path
import json
import math
import shutil
import GDBTools as GDBT
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageOps

os.chdir(os.path.dirname(__file__))
mydir = os.path.dirname(__file__) or "."
Bot_Files = os.path.join(mydir, "Bot_Files")
Remapped_Data = os.path.join(mydir, "Remapped_Data")
mydir = os.path.join(mydir, "Image Hell")
F1 = os.path.join(mydir, "1st_Circle")
S2 = os.path.join(mydir, "2nd_Circle")
T3 = os.path.join(mydir, "3rd_Circle")
F4 = os.path.join(mydir, "4th_Circle")
F5 = os.path.join(mydir, "5th_Circle")
F5C = os.path.join(mydir, "5th_Circle","Characters")
Earth = os.path.join(mydir, "Earth")
#MapDir = os.path.join(mydir, "Earth","CBT3Map")
MapDir = os.path.join(mydir, "Earth","MapFiles")
DBPath = os.path.join(mydir, "DB_Images")


Stage_0 = os.path.join(mydir, "Stage_0")
Stage_1 = os.path.join(mydir, "Stage_1")
Stage_2 = os.path.join(mydir, "Stage_2")

LangEN = GDBT.Stageloader("TextMapEN.json","L")
LangCHS = GDBT.Stageloader("TextMapCHS.json","L")
TagMap = GDBT.Stageloader("Tags.json","3")

def conv(st):
    st = str(st)
    if st == "":
        return ""
    elif st in LangEN.keys():
        return LangEN[st]
    #elif st in SP.keys():
        #return SP[st]["Story"]
    else:
#        print(st)
        return("")

CharMap = GDBT.Stageloader("CharMap.json","3")
ArtifMap = GDBT.Stageloader("ArtifMap.json","3")
WeapMap = GDBT.Stageloader("WeapMap.json","3")
ItemMap = GDBT.Stageloader("ItemMap.json","3")
MonMap = GDBT.Stageloader("MonMap.json","3")
FurnMap = GDBT.Stageloader("FurnMap.json","3")
MTM = GDBT.Stageloader("ManualTextMapConfigData.json","1")

def Third():
    for item in os.listdir(F1):
        Work = item.split("_")
        F1N = os.path.join(mydir, "1st_Circle",item)
        S2N = os.path.join(mydir, "2nd_Circle",item)
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
            if Work[1] == "AvatarIcon":
                if os.path.exists(os.path.join(mydir, "3rd_Circle",Work[0],Work[1])):
                    pass
                else:
                    os.makedirs(os.path.join(mydir, "3rd_Circle",Work[0],Work[1]))
                if len(Work) == 4:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],(Work[2]+"_"+Work[3]))
                else:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2])
                shutil.copyfile(F1N, T3N)
            if Work[1] == "EquipIcon":
                if os.path.exists(os.path.join(mydir, "3rd_Circle",Work[0],Work[1])):
                    pass
                else:
                    os.makedirs(os.path.join(mydir, "3rd_Circle",Work[0],Work[1]))
                if len(Work) >= 4:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],"_".join(Work[2:]))
                else:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2])
                shutil.copyfile(F1N, T3N)
            if Work[1] == "NameCardIcon":
                if os.path.exists(os.path.join(mydir, "3rd_Circle",Work[0],Work[1])):
                    pass
                else:
                    os.makedirs(os.path.join(mydir, "3rd_Circle",Work[0],Work[1]))
                if len(Work) >= 4:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],"_".join(Work[2:]))
                else:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2])
                shutil.copyfile(F1N, T3N)
            if Work[1] == "MonsterIcon":
                if os.path.exists(os.path.join(mydir, "3rd_Circle",Work[0],Work[1])):
                    pass
                else:
                    os.makedirs(os.path.join(mydir, "3rd_Circle",Work[0],Work[1]))
                if len(Work) >= 4:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],"_".join(Work[2:]))
                else:
                    T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2])
                shutil.copyfile(F1N, T3N)
            if Work[1] == "Talent":
                if Work[2] == "C":
                    if os.path.exists(os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2])):
                        pass
                    else:
                        os.makedirs(os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2]))
                    if len(Work) >= 4:
                        T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],"_".join(Work[3:]))
                    else:
                        T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],Work[3])
                    shutil.copyfile(F1N, T3N)
            if Work[1] == "Gacha":
                if Work[2] == "AvatarImg":
                    if os.path.exists(os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2])):
                        pass
                    else:
                        os.makedirs(os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2]))
                    if len(Work) >= 4:
                        T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],"_".join(Work[3:]))
                    else:
                        T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],Work[3])
                    shutil.copyfile(F1N, T3N)
                if Work[2] == "AvatarIcon":
                    if os.path.exists(os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2])):
                        pass
                    else:
                        os.makedirs(os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2]))
                    if len(Work) >= 4:
                        T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],"_".join(Work[3:]))
                    else:
                        T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],Work[3])
                    shutil.copyfile(F1N, T3N)
                if Work[2] == "EquipIcon":
                    if os.path.exists(os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],Work[3])):
                        pass
                    else:
                        os.makedirs(os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],Work[3]))
                    if len(Work) >= 4:
                        T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],Work[3],"_".join(Work[4:]))
                    else:
                        T3N = os.path.join(mydir, "3rd_Circle",Work[0],Work[1],Work[2],Work[3],Work[4])
                    shutil.copyfile(F1N, T3N)

WO = os.path.join(F4, "Weapons")
IO = os.path.join(F4, "Items")
FO = os.path.join(F4, "Food")
for item in [WO,IO,FO]:
    if os.path.exists(item):
        pass
    else:
        os.makedirs(item)

def Fourth():
    for Weap in WeapMap:
        if TagMap["Weapons"][Weap]["Ban"]:
            pass
        item = WeapMap[Weap]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Awk = os.path.join(F1,item["AIcon"]+".png")
        Gach = os.path.join(F1,"UI_Gacha_EquipIcon_"+item["Class"]+"_"+item["Series"]+".png")
        Name = conv(item["Name"]).replace(" ","_")
        NormO = ExCI(os.path.join(F5,"Weapons",Name),"Base.png")
        AwkO = ExCI(os.path.join(F5,"Weapons",Name),"Awk.png")
        GachO = ExCI(os.path.join(F5,"Weapons",Name),"Gacha.png")
        try:
            shutil.copyfile(Norm, NormO)
            shutil.copyfile(Awk, AwkO)
            shutil.copyfile(Gach, GachO)
        except:
            print(Name+" Missing")


    for Mat in ItemMap["Materials"]:
        if TagMap["Items"][Mat]["Ban"]:
            pass
        item = ItemMap["Materials"][Mat]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Name = conv(item["Item Name"]).replace(" ","_")
        NormO = ExCI(os.path.join(F5,"Mats",Name),"Raw.png")
        try:
            shutil.copyfile(Norm, NormO)
        except:
            print(Name+" Missing")

    for Mat in ItemMap["Gadgets"]:
        if TagMap["Items"][Mat]["Ban"]:
            pass
        item = ItemMap["Gadgets"][Mat]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Name = conv(item["Item Name"]).replace(" ","_").replace(":","_")
        NormO = ExCI(os.path.join(F5,"Gadget",Name),"Raw.png")
        try:
            shutil.copyfile(Norm, NormO)
        except:
            print(Name+" Missing")

    for Mat in ItemMap["Ascension Materials"]:
        for tier in ItemMap["Ascension Materials"][Mat]:
            if TagMap["Items"][tier]["Ban"]:
                continue
            item = ItemMap["Ascension Materials"][Mat][tier]
            Norm = os.path.join(F1,item["Icon"]+".png")
            Name = conv(item["Item Name"]).replace(" ","_")
            NormO = ExCI(os.path.join(F5,"Mats",Name),"Raw.png")
            try:
                shutil.copyfile(Norm, NormO)
            except:
                print(Name+" Missing")
    
    for Mat in ItemMap["Food"]:
        if TagMap["Items"][Mat]["Ban"]:
            continue
        item = ItemMap["Food"][Mat]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Name = conv(item["Item Name"]).replace(" ","_").replace("\"","").replace("\\","")
        NormO = ExCI(os.path.join(F5,"Food",Name),"Raw.png")
        try:
            shutil.copyfile(Norm, NormO)
        except:
            print(Name+" Missing")

OO = os.path.join(F4, "Food")
XFP = os.path.join(Earth, "XF.png")
XF = Image.open(XFP).convert("RGBA")
UP = os.path.join(F4, "Test")
Charp = os.path.join(Earth, "Characters\\Side")
X1 = XF.resize((256,312))



Siz = (100,100)
BGSiz = (100,122)
Temp = os.path.join(Earth, "BGC\\5.png")
Temp = Image.open(Temp).convert("RGBA")
Star_5 = Temp.resize(Siz)

Temp = os.path.join(Earth, "BGC\\4.png")
Temp = Image.open(Temp).convert("RGBA")
Star_4 = Temp.resize(Siz)

Temp = os.path.join(Earth, "BGC\\3.png")
Temp = Image.open(Temp).convert("RGBA")
Star_3 = Temp.resize(Siz)

Temp = os.path.join(Earth, "BGC\\2.png")
Temp = Image.open(Temp).convert("RGBA")
Star_2 = Temp.resize(Siz)

Temp = os.path.join(Earth, "BGC\\1.png")
Temp = Image.open(Temp).convert("RGBA")
Star_1 = Temp.resize(Siz)


Temp = os.path.join(Earth, "BGC\\0.png")
Temp = Image.open(Temp).convert("RGBA")
Star_0 = Temp.resize(Siz)

RarBG = [Star_0,Star_1,Star_2,Star_3,Star_4,Star_5]

Temp = os.path.join(Earth, "BGC\\BG.png")
Temp = Image.open(Temp).convert("RGBA")
Item_BG = Temp.resize(BGSiz)


Temp = os.path.join(Earth, "BGC\\WBG.png")
Temp = Image.open(Temp).convert("RGBA")
Weap_BG = Temp

Temp = os.path.join(Earth, "BGC\\Curve.png")
Temp = Image.open(Temp).convert("RGBA")
Curve_M = Temp.resize(Siz)

Temp = os.path.join(Earth, "BGC\\Crest.png")
Crest = Image.open(Temp).convert("RGBA")

Norm = os.path.join(IO,"Brilliant_Diamond_Gemstone"+".png")

def ExC(Loc):
    if os.path.exists(Loc):
        pass
    else:
        os.makedirs(Loc)
    return(Loc)

def ExCI(Loc,Nam):
    if os.path.exists(Loc):
        pass
    else:
        os.makedirs(Loc)
    return(os.path.join(Loc,Nam))

def ICards():
    for Mat in ItemMap["Materials"]:

        if TagMap["Items"][Mat]["Ban"] or Mat in ["100757","100758"]:
            continue
        item = ItemMap["Materials"][Mat]
        Norm = os.path.join(F5,item["Icon"],"Raw.png")
        Name = conv(item["Item Name"]).replace(" ","_")
        #NormO = GDBT.ExCI(os.path.join(F5,"ItemCards"),Name+".png")
        NormO = ExCI(os.path.join(F5,"Mats",Name),"Raw.png")
        SID = item["Rarity"]
        Img = Image.open(NormO).convert("RGBA")
        Img = Img.resize(Siz)

        Item_BG.paste(RarBG[SID],mask = Curve_M)
        Item_BG.paste(Crest,mask = Crest)
        Item_BG.paste(Img,mask = Img)
        OP = ExCI(os.path.join(F5,"Mats",Name),"Card.png")
        Item_BG.save(OP)

    for Mat in ItemMap["Ascension Materials"]:
        for tier in ItemMap["Ascension Materials"][Mat]:
            item = ItemMap["Ascension Materials"][Mat][tier]
            if TagMap["Items"][tier]["Ban"] or tier in ["100757","100758"]:
                continue

            Norm = os.path.join(F1,item["Icon"]+".png")
            Name = conv(item["Item Name"]).replace(" ","_")
            NormO = ExCI(os.path.join(F5,"Mats",Name),"Raw.png")
            SID = item["Rarity"]

            Img = Image.open(NormO).convert("RGBA")
            Img = Img.resize(Siz)

            Item_BG.paste(RarBG[SID],mask = Curve_M)
            Item_BG.paste(Crest,mask = Crest)
            Item_BG.paste(Img,mask = Img)
            OP = ExCI(os.path.join(F5,"Mats",Name),"Card.png")
            Item_BG.save(OP)

font = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 128)
wfont = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 128)
Bfont = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 60)
Sfont = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 58)

def CharImD():
    print("Workin")
    for Char in CharMap:
        if Char == "10000051":
            print("Here")
        CM = CharMap[Char]
        CID = TagMap["Characters"][Char]["Name"]        
        #CD = os.path.join(FO,CID+".png")
        CD = os.path.join(F5C,CID)
        if TagMap["Characters"][Char]["Ban"]:
            continue
        #print(CID)
        ExC(CD)
        C = 0
        TP = ExC(os.path.join(F5C,CID,"Passives"))
        for const in CM["Passives"]:
            OP = os.path.join(F1,const[2]+".png")
            FP = os.path.join(TP,str(C)+".png")
            try:
                shutil.copyfile(OP, FP)
            except:
                print(const[2]+" Missing")
            C+=1

        C = 1
        TP = ExC(os.path.join(F5C,CID,"Talents"))
        for Tal in CM["Talents"]:
            Tal = CM["Talents"][Tal]
            OP = os.path.join(F1,Tal["Icon"]+".png")
            FP = os.path.join(TP,str(C)+".png")
            try:
                shutil.copyfile(OP, FP)
            except:
                print(Tal["Icon"]+" Missing")
            C+=1

        C = 0
        TP = ExC(os.path.join(F5C,CID,"Skills"))
        for SI in [CM["Normal Attack"]["Img"],CM["Elemental Skill"]["Img"],CM["Elemental Burst"]["Img"],]:
            OP = os.path.join(F1,SI+".png")
            if C == 2:
                OP = os.path.join(F1,SI+"_HD.png")               
            FP = os.path.join(TP,str(C)+".png")
            try:
                shutil.copyfile(OP, FP)
            except:
                print(SI+" Missing")
            C+=1
        TP = ExC(os.path.join(F5C,CID))
        OP = os.path.join(F1,"UI_Gacha_AvatarIcon_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Panel.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_Gacha_AvatarIcon_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_Gacha_AvatarImg_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Full.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_Gacha_AvatarImg_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_AvatarIcon_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Icon.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_AvatarIcon_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_LegendQuestImg_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Page.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_LegendQuestImg_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_NameCardIcon_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Card.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_NameCardIcon_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_AvatarIcon_"+CM["Icon"]+"_Card.png")
        FP = os.path.join(TP,"Raw_Item.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_AvatarIcon_"+CM["Icon"]+"_Card.png"+" Missing")
            
        OP = os.path.join(F1,"UI_NameCardPic_"+CM["Icon"]+"_Alpha.png")
        FP = os.path.join(TP,"Raw_Bar.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_NameCardPic_"+CM["Icon"]+"_Alpha.png"+" Missing")
            
def CharAscIgs():
    XOff = 350
    YOff = 100
    TXOff = XOff+45
    TYOff = 203

    Card = os.path.join(Earth, "BGC\\Card.png")
    Card = Image.open(Card).convert("RGBA").resize((327,1324))

    StarBG = os.path.join(Earth, "BGC\\AStar.png")
    StarBG = Image.open(StarBG).convert("RGBA").resize((100,122))
    print("Workin")

    for Char in CharMap:

        if TagMap["Characters"][Char]["Ban"]:
            continue
        IName = CharMap[Char]["Icon"]
        Side = os.path.join(Earth,"Characters",GDBT.conv(CharMap[Char]["Name"]).replace(" ","_"),"Fade.png")

        Side = Image.open(Side).convert("RGBA").resize((320,1024))
        Base = os.path.join(Earth, "BGC\\"+LangEN[str(CharMap[Char]["Element"])]+".png")
        if Base == "c:\\Users\\eikea\\Documents\\Post War\\Image Hell\\Earth\\BGC\\.png":
            Base = os.path.join(Earth, "BGC\\None.png")        
        Base = Image.open(Base).convert("RGBA").resize((1124,1024))
        MatNums = ImageDraw.Draw(Base)
        yCount = 0

        for rank in CharMap[Char]["Ascension"]:
            xCount = 0
            for item in rank[1]:
                ICount = rank[1][item]
                temp = os.path.join(UP,GDBT.conv(item).replace(" ","_")+".png")
                temp = Image.open(temp).convert("RGBA")
                if yCount==0:
                    Base.paste(temp,(XOff+75+(150*xCount),YOff+(150*yCount)),mask = temp)
                else:
                    Base.paste(temp,(XOff+(150*xCount),YOff+(150*yCount)),mask = temp)

                if ICount < 10:
                    if yCount==0:
                        MatNums.text((TXOff+75+(150*xCount),TYOff+(150*yCount)), str(ICount),font = font, fill=(0,0,0))
                    else:
                        MatNums.text((TXOff+(150*xCount),TYOff+(150*yCount)), str(ICount),font = font, fill=(0,0,0))
                else:
                    MatNums.text((TXOff-4+(150*xCount),TYOff+(150*yCount)), str(ICount),font = font, fill=(0,0,0))
                    
                xCount+=1

            if yCount==0:
                xCount+=1
            Base.paste(StarBG,(XOff+(150*xCount),YOff+(150*yCount)),mask = StarBG)
            if yCount==0:
                MatNums.text((TXOff-10+(150*xCount),YOff+25+(150*yCount)), str(yCount+1),font = Bfont, fill=(0,0,0))
            else:
                MatNums.text((TXOff-15+(150*xCount),YOff+25+(150*yCount)), str(yCount+1),font = Bfont, fill=(0,0,0))

            yCount+=1
        Base.paste(Card,(-5,-100),mask = Card)
        Base.paste(Side,mask = Side)
        OP = ExCI(os.path.join(F5,"Characters\\"+TagMap["Characters"][Char]["Name"]),"ASC.png")
        Base.save(OP)

        print(Char)

def CharTalAscIgs():
    XOff = 350
    YOff = 100
    TXOff = XOff+45
    TYOff = 203

    Card = os.path.join(Earth, "BGC\\Card.png")
    Card = Image.open(Card).convert("RGBA").resize((327,1324))

    StarBG = os.path.join(Earth, "BGC\\AStar.png")
    StarBG = Image.open(StarBG).convert("RGBA").resize((100,122))

    Panel = os.path.join(Earth, "BGC\\StarBG.png")
    Panel = Image.open(Panel).convert("RGBA").resize((700,244+50))
    print("Workin")

    for Char in CharMap:

        if TagMap["Characters"][Char]["Ban"]:
            continue
        Side = Base = os.path.join(Earth, "BGC\\"+LangEN[str(CharMap[Char]["Element"])]+".png")
        Side = Image.open(Side).convert("RGBA").resize((320,1024))
        Base = os.path.join(Earth, "BGC\\"+LangEN[str(CharMap[Char]["Element"])]+".png")
        Base = Image.open(Base).convert("RGBA").resize((1550,1024))
        MatNums = ImageDraw.Draw(Base)
        yCount = 0
        TalNum = 0
        P2 = 0
        if Char in ["10000005","10000007"]:
            LevMap = CharMap[Char]["Normal Attack"][0]["Upgrade"]
            TLevMap = CharMap[Char]["Normal Attack"][0]["Total"]
        else:
            LevMap = CharMap[Char]["Normal Attack"]["Upgrade"]
            TLevMap = CharMap[Char]["Normal Attack"]["Total"]
        for rank in LevMap:
            if TalNum < 5:
                xCount = 0
                for item in rank[1]:
                    ICount = item["Count"]
                    temp = os.path.join(UP,GDBT.conv(item["Id"]).replace(" ","_")+".png")
                    temp = Image.open(temp).convert("RGBA")
                    Base.paste(temp,(XOff+(150*xCount),YOff+(150*yCount)),mask = temp)

                    if ICount < 10:
                        MatNums.text((TXOff+(150*xCount),TYOff+(150*yCount)), str(ICount),font = font, fill=(0,0,0))
                    else:
                        MatNums.text((TXOff-4+(150*xCount),TYOff+(150*yCount)), str(ICount),font = font, fill=(0,0,0))
                        
                    xCount+=1

                if yCount<=4:                
                    xCount+=1
                Base.paste(StarBG,(XOff+(150*2),YOff+(150*yCount)),mask = StarBG)
                if yCount==0:
                    MatNums.text((TXOff-10+(150*2),YOff+25+(150*yCount)), str(TalNum+2),font = Bfont, fill=(0,0,0))
                else:
                    MatNums.text((TXOff-15+(150*2),YOff+25+(150*yCount)), str(TalNum+2),font = Bfont, fill=(0,0,0))

                yCount+=1
            elif TalNum < 8:
                xCount = 0
                for item in rank[1]:
                    ICount = item["Count"]
                    temp = os.path.join(F5,"Mats",GDBT.conv(item["Id"]).replace(" ","_"),"Card.png")
                    temp = Image.open(temp).convert("RGBA")
                    Base.paste(temp,(XOff+P2+(150*xCount),YOff+(150*yCount)),mask = temp)

                    if item["Count"] < 10:
                        MatNums.text((TXOff+P2+(150*xCount),TYOff+(150*yCount)), str(ICount),font = font, fill=(0,0,0))
                    else:
                        MatNums.text((TXOff+P2-4+(150*xCount),TYOff+(150*yCount)), str(ICount),font = font, fill=(0,0,0))
                        
                    xCount+=1

                if yCount<=4:                
                    xCount+=1
                Base.paste(StarBG,(XOff+P2+(150*3),YOff+(150*yCount)),mask = StarBG)
                if yCount==0:
                    MatNums.text((TXOff+P2-10+(150*3),YOff+25+(150*yCount)), str(TalNum+2),font = Bfont, fill=(0,0,0))
                else:
                    MatNums.text((TXOff+P2-15+(150*3),YOff+25+(150*yCount)), str(TalNum+2),font = Bfont, fill=(0,0,0))

                yCount+=1

            else:
                xCount = 0
                for item in rank[1]:
                    ICount = item["Count"]
                    temp = os.path.join(F5,"Mats",GDBT.conv(item["Id"]).replace(" ","_"),"Card.png")
                    temp = Image.open(temp).convert("RGBA")
                    Base.paste(temp,(XOff+P2+(150*xCount),YOff+(150*yCount)),mask = temp)

                    if ICount < 10:
                        MatNums.text((TXOff+P2+(150*xCount),TYOff+(150*yCount)), str(ICount),font = font, fill=(0,0,0))
                    else:
                        MatNums.text((TXOff+P2-4+(150*xCount),TYOff+(150*yCount)), str(ICount),font = font, fill=(0,0,0))
                        
                    xCount+=1
                Base.paste(StarBG,(XOff+P2+(150*4),YOff+(150*yCount)),mask = StarBG)
                MatNums.text((TXOff+P2-30+(150*4),YOff+25+(150*yCount)), str(TalNum+2),font = Bfont, fill=(0,0,0))

                yCount+=1

            TalNum+=1
            if TalNum == 5:
                yCount = 0
                P2 = (150*(xCount))
            if TalNum == 8:
                P2 = int((150*(xCount-1)))
        Base.paste(Panel,(XOff+P2,YOff+(150*yCount)),mask = Panel)

        Mats = list(TLevMap.keys())
        if Mats[0] in ["Teachings of Freedom","Teachings of Prosperity"]:
            Text = "Mon/Thur/Sun"
        elif Mats[0] in ["Teachings of Resistance","Teachings of Diligence"]:
            Text = "Tue/Fri/Sun"
        elif Mats[0] in ["Teachings of Ballad","Teachings of Gold"]:
            Text = "Wed/Sat/Sun"
        else:
            Text = "N/A"

        MatNums.text((TXOff+P2-30,YOff+25+(150*(yCount))), "Books : "+Text,font = Sfont, fill=(0,0,0))

        TM = GDBT.conv(Mats[6])
        if TM in ["Dvalin's Plume","Dvalin's Sigh","Dvalin's Claw"]:
            Text = "Stormterror"
        elif TM in ["Tusk of Monoceros Caeli","Shard of a Foul Legacy","Shadow of the Warrior"]:
            Text = "Childe"

        elif TM in ["Tail of Boreas","Ring of Boreas","Spirit Locket of Boreas"]:
            Text = "Andrius/Wolf"
        else:
            Text = "N/A"
        MatNums.text((TXOff+P2-30,YOff+25+(150*(yCount+1))), "Special : "+Text,font = Sfont, fill=(0,0,0))
        Base.paste(Card,(-5,-100),mask = Card)
        Base.paste(Side,mask = Side)
        OP = os.path.join(F5,"Characters\\"+TagMap["Characters"][Char]["Name"]+"\\TAL.png")
        Base.save(OP)

        print(Char)

def ranger(base,max):
    ret = []
    for item in range(base,max):
        ret.append(item)
    return ret

def StAdd(img,rar):
    SBase = Image.new(mode = "RGBA" , size = (80,80) , color = (255,204,50))
    Star = XF.resize((80,80))
    SMask = Image.open(os.path.join(Earth, "BGC\\RStar.png")).convert("RGBA")
    Star.paste(SBase,mask = SMask)
    Star = Star.resize((32,32))    
    
    for item in ranger(0,rar):
        img.paste(Star,(30+(38*item),64+205),mask = Star)

def IStAdd(img,rar):
    SBase = Image.new(mode = "RGBA" , size = (80,80) , color = (255,204,50))
    Star = XF.resize((80,80))
    SMask = Image.open(os.path.join(Earth, "BGC\\RStar.png")).convert("RGBA")
    Star.paste(SBase,mask = SMask)
    Star = Star.resize((28,28))    
    
    for item in ranger(1,2):
        img.paste(Star,(30,256),mask = Star)

class WDetails:
    def __init__(self, name, rarity , sub , typ,icon):
        self.name = name
        self.rarity = rarity
        self.Substat_Type = sub
        self.Weapon_Type = typ
        self.icon = icon
        if self.Weapon_Type == "Pole":
            self.Weapon_Type = "Polearm"

class OIDetails:
    def __init__(self, name, rarity, icon, itype):
        self.name = name
        self.rarity = rarity
        self.icon = icon
        self.itype = itype

class IDetails:
    def __init__(self, data):
        self.name = GDBT.econv(data["Item Name"])
        if self.name == "":
            self.name = GDBT.conv(data["Item Name"],LangCHS).replace("()","_")
        self.fname = self.name.replace(" ","_").replace("\"","_").replace(":","_").replace("\\","_").replace("\t","")
        self.rarity = data["Rarity"]
        self.icon = data["Icon"]
        self.itype = GDBT.conv(data["Type Designation"])

class DBIDetails:
    def __init__(self, data ,mtype="norm"):
        if mtype == "norm":
            self.name = GDBT.econv(data["Item Name"])
            if self.name == "":
                self.name = GDBT.conv(data["Item Name"],LangCHS)
            self.fname = self.name.replace(" ","").replace("\"","").replace(":","").replace("\\","").replace("\t","").replace("?","")
            self.rarity = data["Rarity"]
            self.icon = data["Icon"]
            self.itype = GDBT.conv(data["Type Designation"])
            self.fitype = self.itype.replace(" ","").replace("\"","").replace(":","").replace("\\","").replace("\t","").replace("?","")
        else:
            self.name = GDBT.conv(data["Name"])
            if self.name == "":
                self.name = GDBT.conv(data["Name"],LangCHS)
            self.fname = self.name.replace(" ","").replace("\"","").replace(":","").replace("\\","").replace("\t","").replace("?","")
            self.rarity = data["Rarity"]
            self.icon = data["Icon"]
            self.itype = GDBT.conv(MTM[data["Type"]]["TextMapContentTextMapHash"])
            if data["SurfaceType"]:
                self.fitype = "furnishing_"+data["SurfaceType"].lower().replace("objplane","")
            else:
                self.fitype = "fixture_"
                        
class PipDetails:
    def __init__(self, name, rarity, icon):
        self.name = name
        self.rarity = rarity
        self.icon = icon
        
Crest = Image.new(mode = "RGBA" , size = (337,256) , color = (0,0,0))

Fram = os.path.join(Earth, "BGC\\FinFrame.png")
Fram = Image.open(Fram).convert("RGBA")

class IFonts:
    Base_Atk_Value = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 48)
    Banner_Name = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 37)
    Banner_Name_38 = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 38)
    Banner_Name_T = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 30)
    Banner_Name_26 = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 26)
    Class_SubType = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 23)
    WCard_Value_Font = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 27)
    Base_Atk = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 25)
    Weapon_Mark = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), 27)

class Banners:
    #B# = [Banner Back,Frame Col]
    B5 = [Image.new(mode = "RGBA" , size = (555,66) , color = (188,105,50)),Image.new(mode = "RGBA" , size = (555,64) , color = (144,82,41))]
    B4 = [Image.new(mode = "RGBA" , size = (555,66) , color = (161,86,224)),Image.new(mode = "RGBA" , size = (555,64) , color = (125,69,173))]
    B3 = [Image.new(mode = "RGBA" , size = (555,66) , color = (81,128,203)),Image.new(mode = "RGBA" , size = (555,64) , color = (64,98,155))]
    B2 = [Image.new(mode = "RGBA" , size = (555,66) , color = (42,143,114)),Image.new(mode = "RGBA" , size = (555,64) , color = (35,110,89))]
    B1 = [Image.new(mode = "RGBA" , size = (555,66) , color = (114,119,138)),Image.new(mode = "RGBA" , size = (555,64) , color = (89,92,107))]
    B0 = [Image.new(mode = "RGBA" , size = (555,66) , color = (114,119,138)),Image.new(mode = "RGBA" , size = (555,64) , color = (89,92,107))]

    def Cols(self,Rar):
        #print(Rar)
        if Rar == 5:
            return self.B5
        elif Rar == 4:
            return self.B4
        elif Rar == 3:
            return self.B3
        elif Rar == 2:
            return self.B2
        elif Rar == 1:
            return self.B1
        else:
            return self.B0

WMC = [(89,92,107,128),(89,92,107,128),(35,110,89,128),(64,98,155,128),(125,69,173,128),(144,82,41,128)]
def WaterM(Rar):
    Temp = os.path.join(Earth, "XF.png")
    Temp = Image.open(Temp).convert("RGBA")
    WaterM = Temp.resize((277,64+256))
    WaterB = Temp.resize((277,64+256))
    #BGC.paste(Weap_BG,(218,64),mask = Weap_BG)
    #BGC.paste(WeapImg,(81+218,64),mask = WeapImg)
    #StAdd(BGC,Contents.rarity)
    WMT = ImageDraw.Draw(WaterM)
    WMT.text((32,64+115), "@Genshin_Intel",font = IFonts.Weapon_Mark, fill=WMC[Rar])
    WaterM = WaterM.rotate(45)
    WaterB.paste(WaterM,mask = WaterM)
    #WaterB.show()
    return(WaterB)
def WeapWM():
    Temp = os.path.join(Earth, "XF.png")
    Temp = Image.open(Temp).convert("RGBA")
    WaterM = Temp.resize((277,64+256))
    WaterB = Temp.resize((277,64+256))
    #BGC.paste(Weap_BG,(218,64),mask = Weap_BG)
    #BGC.paste(WeapImg,(81+218,64),mask = WeapImg)
    #StAdd(BGC,Contents.rarity)
    WMT = ImageDraw.Draw(WaterM)
    WMT.text((32,64+115), "@Genshin_Intel",font = IFonts.Weapon_Mark, fill=(233,211,255))
    WaterM = WaterM.rotate(45)
    WaterB.paste(WaterM,mask = WaterM)
    #WaterB.show()
    return(WaterB)

def WCCreator(Contents,ValSet,Asc):
    BannerHei = 64
    XTPixOff = 32
    if Contents.name == "Thrilling Tales of Dragon Slayers":
        print("Here")

    Lines = BannerNameSplit(Contents.name)
    BCol = Banners().Cols(Contents.rarity)

    if Asc:
        TName = Contents.icon+"_Awaken #"
    else:
        TName = Contents.icon+" #"
    WeapImg = Image.open(os.path.join(Earth, "XF.png")).convert("RGBA")
    for item in os.listdir(F1):
        if TName in item:
            WeapImg = Image.open(os.path.join(F1,item)).convert("RGBA")
    BG = Image.new('RGB', (337+218,BannerHei+256), color = 'black')
    Temp = os.path.join(Earth, "BGC\\"+str(Contents.rarity)+".png")
    Temp = Image.open(Temp).convert("RGBA")
    BGC = Temp.resize((337+218,BannerHei+256))
    BGC.paste(Weap_BG,(218,BannerHei),mask = Weap_BG)
    StAdd(BGC,Contents.rarity)
    BL = Image.new('RGBA', (337+218,6), color = (0,0,0,64))
    BGC.paste(BL,(0,BannerHei+256-6),mask = BL)
    BGC.paste(WeapImg,(81+218,BannerHei),mask = WeapImg)
    

    DatNums = ImageDraw.Draw(BGC)


    BGC.paste(BCol[0])
    BGC.paste(BCol[1],(0,1) ,mask = Fram)

    #Banner Text
    if len(Lines[0]) == 1:
        DatNums.text((32,32), Lines[0][0],font = Lines[1],anchor="lm", fill=(255,255,255))
    else:
        DatNums.text((32,4), Lines[0][0],font = Lines[1], fill=(255,255,255))
        DatNums.text((32,33), Lines[0][1],font = Lines[1], fill=(255,255,255))
    DatNums.text((32,BannerHei+14), Contents.Weapon_Type,font = IFonts.Class_SubType, fill=(255,255,255))
    DatNums.text((32,BannerHei+47), Contents.Substat_Type,font = IFonts.Class_SubType, fill=(191,191,191))
    DatNums.text((32,BannerHei+74), str(ValSet[1]),font = IFonts.WCard_Value_Font, fill=(255,255,255))
    DatNums.text((32,BannerHei+115), "Base ATK",font = IFonts.Base_Atk, fill=(191,191,191))
    DatNums.text((32,BannerHei+142), str(ValSet[0]),font = IFonts.Base_Atk_Value, fill=(255,255,255))
    BG.paste(BGC)
    return BG

#https://stackoverflow.com/questions/5920643/add-an-item-between-each-item-already-in-the-list
def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

#Pixel Point Conversion - https://www.joomlasrilanka.com/web-design-development-blog/web-design-font-size-measurements-convert-points-pixelsems-percentages-web-designing/
#Source Of Knowledge - http://vnoted.com/articles/putting-text-on-images-with-python-pil/ - 2018
#Source Of Knowledge - https://itnext.io/how-to-wrap-text-on-image-using-python-8f569860f89e - 2019
#They're Pretty Much The Same Code But Imma Credit Both And Let You Sort Em Out
def BannerNameSplit(Text):
    Lines = ["1",""]
    Size = 38
    BG = Image.new('RGB', (337+218,256), color = 'black')
    Tester = ImageDraw.Draw(BG)
    while (Size > 25) and len(Lines)>1:
        Lines = []
        Constraints = (555-64)
        Banner_Font = ImageFont.truetype(os.path.join(Earth, "Default_SC.ttf"), Size)
        Temp = Banner_Font.getsize(Text)
        Temp2 = Banner_Font.getsize(Text)
        TempSiz = Tester.textsize(Text,Banner_Font)
        if TempSiz[0]  <= Constraints:
            Lines.append(Text)
        else:
            #split the line by spaces to get words
            words = intersperse(Text.split(' '),' ')
            i = 0
            # append every word to a line while its width is shorter than the image width
            while i < len(words):
                line = ''
                while i < len(words) and Banner_Font.getsize(line + words[i])[0] <= Constraints:
                    line = line + words[i]
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                Lines.append(line)
        Size = Size-1
    #Tester = Tester.textbbox()
    #TempHeight = Tester.textbbox(Text,Banner_Font)
    return (Lines,Banner_Font)

def SubNameSplit(Text):
    Lines = []
    Constraints = (555-192)
    BG = Image.new('RGB', (337+218,256), color = 'black')
    Tester = ImageDraw.Draw(BG)
    Banner_Font = IFonts.Class_SubType
    Temp = Banner_Font.getsize(Text)
    TempSiz = Tester.textsize(Text,Banner_Font)
    if TempSiz[0]  <= Constraints:
        Lines.append(Text)
    else:
        #split the line by spaces to get words
        words = intersperse(Text.split(' '),' ')
        i = 0
        # append every word to a line while its width is shorter than the image width
        while i < len(words):
            line = ''
            while i < len(words) and Banner_Font.getsize(line + words[i])[0] <= Constraints:
                line = line + words[i]
                i += 1
            if not line:
                line = words[i]
                i += 1
            Lines.append(line)
    #Tester = Tester.textbbox()
    #TempHeight = Tester.textbbox(Text,Banner_Font)
    return (Lines,Banner_Font)

def IPCreator(Contents):
    #Get Font Size And Line Number
    Lines = BannerNameSplit(Contents.name)

    BCol = Banners().Cols(Contents.rarity)

    #Icon File Name
    TName = Contents.icon+".png"
    #WeapImg = Image.open(os.path.join(Earth, "XF.png")).convert("RGBA")
    CurveSiz = 64
    ItemImg = Image.open(os.path.join(F1,TName)).convert("RGBA")
    #BG = Image.new('RGB', (337+218,BannerHei+256), color = 'black')
    Bottom = Image.open(os.path.join(Earth, "BGC\\CurveBottom.png")).convert("RGBA").resize((256,314))
    Curve = Image.open(os.path.join(Earth, "BGC\\ImgTextBg.png")).convert("RGBA").resize((CurveSiz,CurveSiz))
    BG = Image.open(os.path.join(Earth, "BGC\\UI_QualityBg_"+str(Contents.rarity)+".png")).convert("RGBA").resize((256,314))
    BGB = BG
    TName = Contents.icon+".png"
    ItemImg = Image.open(os.path.join(F1,TName)).convert("RGBA")


    BG.paste(ItemImg,mask = ItemImg)
    #BG.paste(Curve,(256-CurveSiz,256-(CurveSiz-20)),mask = Curve)
    BG.paste(Bottom,mask = Bottom)
    BG.paste(BG,mask=BGB)
    IStAdd(BG,Contents.rarity)
    #BG = BG.resize((80,98))
    return BG

def ICCreator(Contents):
    BannerHei = 64
    XTPixOff = 32
    #Get Font Size And Line Number
    Lines = BannerNameSplit(Contents.name)
    SLines = SubNameSplit(Contents.itype)

    BCol = Banners().Cols(Contents.rarity)

    #Icon File Name
    TName = Contents.icon+".png"
    #WeapImg = Image.open(os.path.join(Earth, "XF.png")).convert("RGBA")

    ItemImg = Image.open(os.path.join(F1,TName)).convert("RGBA").resize((256,256))
    BG = Image.new('RGB', (337+218,BannerHei+256), color = 'black')
    BGC = Image.open(os.path.join(Earth, "BGC\\"+str(Contents.rarity)+".png")).convert("RGBA").resize((337+218,BannerHei+256))
    BGC.paste(Weap_BG,(218,BannerHei),mask = Weap_BG)
    BGC.paste(ItemImg,(81+218,BannerHei),mask = ItemImg)
    StAdd(BGC,Contents.rarity)
    BL = Image.new('RGBA', (337+218,6), color = (0,0,0,64))
    BGC.paste(BL,(0,BannerHei+256-6),mask = BL)
    
    DatNums = ImageDraw.Draw(BGC)


    BGC.paste(BCol[0])
    BGC.paste(BCol[1],(0,1) ,mask = Fram)
    #Banner Text
    if len(Lines[0]) == 1:
        DatNums.text((32,32), Lines[0][0],font = Lines[1],anchor="lm", fill=(255,255,255))
    else:
        DatNums.text((32,4), Lines[0][0],font = Lines[1], fill=(255,255,255))
        DatNums.text((32,33), Lines[0][1],font = Lines[1], fill=(255,255,255))

    #Descriptive Text
    if len(SLines[0]) == 1:
        DatNums.text((32,BannerHei+14), SLines[0][0],font = SLines[1], fill=(255,255,255))
    else:
        DatNums.text((32,BannerHei+14), SLines[0][0],font = SLines[1], fill=(255,255,255))
        DatNums.text((32,BannerHei+44), SLines[0][1],font = SLines[1], fill=(255,255,255))
        #print(Lines)
    BG.paste(BGC)
    return BG

def PipGen(Contents):
    """
    BG = Image.new('RGB', (100,126), color = 'black')

    Norm = os.path.join(F1,Contents.icon)
    Img = Image.open(Norm).convert("RGBA")

    Crest = Image.open(os.path.join(Earth, "BGC\\UI_ImgSign_ItemIcon.png")).convert("RGBA")


    Item_Icon = Img.resize((100,100))
    ColBG = RarBG[Contents.rarity]
    BG.paste(ColBG,mask = ColBG)
    BG.paste(Crest,mask = Crest)
    BG.paste(Item_Icon,mask = Item_Icon)
    #BG.paste(Img,mask = Img)
    """
    BG = Image.new('RGB', (2*100,2*126), color = 'black')

    Norm = os.path.join(F1,Contents.icon)
    Img = Image.open(Norm).convert("RGBA")

    Crest = Image.open(os.path.join(Earth, "BGC\\UI_ImgSign_ItemIcon.png")).convert("RGBA").resize((2*100,2*100))
    BGCrest = Image.open(os.path.join(Earth, "BGC\\UI_Img_BgColor_Item.png")).convert("RGBA").resize((2*100,2*100))


    Item_Icon = Img.resize((2*100,2*100))
    ColBG = RarBG[Contents.rarity].resize((2*100,2*100))
    BG.paste(ColBG,mask = BGCrest)
    #BG.paste(BGCrest,mask = BGCrest)
    BG.paste(Crest,mask = Crest)
    BG.paste(Item_Icon,mask = Item_Icon)
    #BG.paste(Img,mask = Img)
    return BG

def ItemPips():

    for ItemSet in [ItemMap["Materials"],ItemMap["Gadgets"],ItemMap["Recipes"],ItemMap["Wings"],ItemMap["Wood"],]:
        for Mat in ItemSet:

            #Base
            #BG = Image.new(mode = "RGBA" , size = (337+218,YTPixOff+256) , color = (0,0,0))
            #BG.paste(BGC,mask=BGC)

            if TagMap["Items"][Mat]["Ban"] or Mat in ["100757","100758"]:
                continue
            item = ItemSet[Mat]

            PName = conv(item["Item Name"]).replace(" ","_").replace(":","").replace("\'","").replace("\"","")
            PipDet = PipDetails(PName,item["Rarity"],item["Icon"]+".png")
            BGC = PipGen(PipDet)


            OP = ExCI(os.path.join(F5,"Test"),PName+".png")
            BGC.save(OP)
def Narukami():
    
    for Weapon in ["11509","12509","13509","14509","15509","14414","15414"]:

        if TagMap["Weapons"][Weapon]["Ban"]:
            pass
        Weap = WeapMap[Weapon]
        PName = GDBT.conv(Weap["Name"])
        Name = PName.replace(" ","_")
        if Name == "":
            PName = GDBT.conv(Weap["Name"],LangCHS)
            Name = PName.replace(" ","_")

        Rar = Weap["Rarity"]
        #print(Norm)
        SST = conv(Weap["Substat Type"])
        WT = Weap["Class"]
        if SST == "":
            Max = [Weap["Stats"][-1][1],"",Weap["Stats"][-1][0]]
            Min = [Weap["Stats"][1][1],"",Weap["Stats"][1][0]]
        elif SST == "Elemental Mastery":
            Max = [Weap["Stats"][-1][1],Weap["Stats"][-1][2],Weap["Stats"][-1][0]]
            Min = [Weap["Stats"][1][1],Weap["Stats"][1][2],Weap["Stats"][1][0]]
        else:
            Max = [Weap["Stats"][-1][1],str(Weap["Stats"][-1][2])+"%",Weap["Stats"][-1][0]]
            Min = [Weap["Stats"][1][1],str(Weap["Stats"][1][2])+"%",Weap["Stats"][1][0]]

        YTPixOff = 64
        #BG = XF.resize((337+218,YTPixOff+256))
        BG = Image.new('RGB', (337+218,YTPixOff+256), color = 'black')
        BGB = ImageDraw.Draw(BG)
        BGB.rectangle((0, 0,337+218,YTPixOff+256), fill=(0,0,0))
        

        WBase = WDetails(PName,Rar,conv(Weap["Substat Type"]),Weap["Class"],Weap["Icon"])
        WMax = WDetails(PName,Rar,conv(Weap["Substat Type"]),Weap["Class"],Weap["Icon"])
        #Base
        #BG = Image.new(mode = "RGBA" , size = (337+218,YTPixOff+256) , color = (0,0,0))
        #BG.paste(BGC,mask=BGC)
        BGC = WCCreator(WBase,Min,False)
        Water_Mark = WeapWM()
        BGC.paste(Water_Mark,(277,0),mask = Water_Mark)
        OP = ExCI(os.path.join(F5,"Weapons",Name),"BCard.png")
        BGC.save(OP)


        BGC = WCCreator(WMax,Max,True)
        Water_Mark = WeapWM()
        BGC.paste(Water_Mark,(277,0),mask = Water_Mark)
        OP = ExCI(os.path.join(F5,"Weapons",Name),"ACard.png")
        BGC.save(OP)


def WeapCards():
    
    for Weapon in WeapMap:

        if TagMap["Weapons"][Weapon]["Ban"]:
            pass
        Weap = WeapMap[Weapon]
        PName = GDBT.conv(Weap["Name"])
        Name = PName.replace(" ","_")
        if Name == "":
            PName = GDBT.conv(Weap["Name"],LangCHS)
            Name = PName.replace(" ","_")

        Rar = Weap["Rarity"]
        #print(Norm)
        SST = conv(Weap["Substat Type"])
        WT = Weap["Class"]
        if SST == "":
            Max = [Weap["Stats"][-1][1],"",Weap["Stats"][-1][0]]
            Min = [Weap["Stats"][1][1],"",Weap["Stats"][1][0]]
        elif SST == "Elemental Mastery":
            Max = [Weap["Stats"][-1][1],Weap["Stats"][-1][2],Weap["Stats"][-1][0]]
            Min = [Weap["Stats"][1][1],Weap["Stats"][1][2],Weap["Stats"][1][0]]
        else:
            Max = [Weap["Stats"][-1][1],str(Weap["Stats"][-1][2])+"%",Weap["Stats"][-1][0]]
            Min = [Weap["Stats"][1][1],str(Weap["Stats"][1][2])+"%",Weap["Stats"][1][0]]

        YTPixOff = 64
        #BG = XF.resize((337+218,YTPixOff+256))
        BG = Image.new('RGB', (337+218,YTPixOff+256), color = 'black')
        BGB = ImageDraw.Draw(BG)
        BGB.rectangle((0, 0,337+218,YTPixOff+256), fill=(0,0,0))
        

        WBase = WDetails(PName,Rar,conv(Weap["Substat Type"]),Weap["Class"],Weap["Icon"])
        WMax = WDetails(PName,Rar,conv(Weap["Substat Type"]),Weap["Class"],Weap["Icon"])
        #Base
        #BG = Image.new(mode = "RGBA" , size = (337+218,YTPixOff+256) , color = (0,0,0))
        #BG.paste(BGC,mask=BGC)
        BGC = WCCreator(WBase,Min,False)
        Water_Mark = WaterM(Rar)
        BGC.paste(Water_Mark,(277,0),mask = Water_Mark)
        OP = ExCI(os.path.join(F5,"Weapons",Name),"BCard.png")
        BGC.save(OP)


        BGC = WCCreator(WMax,Max,True)
        Water_Mark = WaterM(Rar)
        BGC.paste(Water_Mark,(277,0),mask = Water_Mark)
        OP = ExCI(os.path.join(F5,"Weapons",Name),"ACard.png")
        BGC.save(OP)


        #Combo


        ComboCard = Image.new(mode = "RGBA" , size = (337+218,2*(YTPixOff+256)))


        WBase.name = "Base Level - "+str(Min[2])
                
        ComboCard.paste(WCCreator(WBase,Min,False))

        WBase.name = "Max Level - "+str(Max[2])

        ComboCard.paste(WCCreator(WBase,Max,True),((0,YTPixOff+256)))

        OP = ExCI(os.path.join(F5,"Weapons",Name),"Combo.png")
        ComboCard.save(OP)

def ItemCards():
    FM = {"1100204" : FurnMap["1100204"],"600112" : FurnMap["600112"],"700510" : FurnMap["700510"],"700508" : FurnMap["700508"]}
    for Furniture in FurnMap:
        
        if not TagMap["Furniture"][Furniture]["Ban"]:
            continue
        Furn = FurnMap[Furniture]
        if Furn["Icon"] == "":
            continue
        try:
            ItemImg = Image.open(os.path.join(F1,Furn["Icon"]+".png")).convert("RGBA")
        except:
            continue
        
        PName = GDBT.conv(Furn["Name"])

        Name = PName.replace(" ","_").replace("\"","_").replace(":","_")
        if Name == "":
            PName = GDBT.conv(Furn["Name"],LangCHS)
            Name = PName.replace(" ","_")

        Rar = Furn["Rarity"]
        if Rar != 4:
            continue
        #print(Norm)

        YTPixOff = 64
        #BG = XF.resize((337+218,YTPixOff+256))
        BG = Image.new('RGB', (337+218,YTPixOff+256), color = 'black')
        BGB = ImageDraw.Draw(BG)
        BGB.rectangle((0, 0,337+218,YTPixOff+256), fill=(0,0,0))


        CarDet = IDetails(PName,Rar,Furn["Icon"],GDBT.conv(MTM[Furn["Type"]]["TextMapContentTextMapHash"]))
        #Base
        #BG = Image.new(mode = "RGBA" , size = (337+218,YTPixOff+256) , color = (0,0,0))
        #BG.paste(BGC,mask=BGC)
        BGC = ICCreator(CarDet)
        #Water_Mark = WaterM((105,154,175))#3* WaterMark
        Water_Mark = WaterM((146,119,176))#3* WaterMark
        BGC.paste(Water_Mark,(277,0),mask = Water_Mark)
        #OP = ExCI(os.path.join(F5,"Furniture",Name),"Card.png")
        OP = ExCI(os.path.join(F5,"Furniture"),Name+".png")
        BGC.save(OP)

def FrameC():
    Temp = os.path.join(Earth, "BGC\\Frame.png")
    Temp = Image.open(Temp).convert("RGBA")
    Bas = XF.resize((555,70))
    LS = Temp.crop((1,0,32,70))
    RS = Temp.crop((33,0,63,70))
    Cen = Temp.crop((32,0,33,70))
    Cen = Cen.resize((494,70))
    Bas.paste(LS,mask = LS)#.resize(64,70)
    Bas.paste(Cen,(31,0),mask = Cen)#.resize(64,70)
    Bas.paste(RS,(525,0),mask = RS)
    Bas = Bas.resize((555,64))
    OP = ExCI(os.path.join(Earth, "BGC"),"FinFrame.png")
    Bas.save(OP)

def ImageTesting():
    Coating = Image.new(mode = "RGBA" , size = (555,66) , color = (161,86,224))
    FrameCoat = Image.new(mode = "RGBA" , size = (555,64) , color = (125,69,173))

    SBase = XF.resize((80,80))
    SInt = ImageDraw.Draw(SBase)
    SInt.rectangle((0, 0,80,80), fill=(255,204,50))
    Star = XF.resize((80,80))
    SMask = Image.open(os.path.join(Earth, "BGC\\RStar.png")).convert("RGBA")
    Star.paste(SBase,mask = SMask)
    Star = Star.resize((32,32))

    Temp = os.path.join(Earth, "BGC\\4.png")
    Temp = Image.open(Temp).convert("RGBA")

    Coating = XF.resize((555,70))
    CoatFrame = ImageDraw.Draw(Coating)
    CoatFrame.rectangle((0, 0,555,70), fill=(161,86,224))

    NCrest = XF.resize((337,256))
    Crest = Image.new(mode = "RGBA" , size = (337,256) , color = (0,0,0))

    Crest.paste(Crest,(218,65),mask = Weap_BG)
    Bands = Weap_BG.split()
    NN = ImageOps.invert(Bands[3])
    #NN.show()
    NN.save("C:\\Users\\eikea\\Documents\\Beyond Ultra\\Image Hell\\Earth\\BGC\\TestInverse.png")
    NBands = Image.merge('RGBA', (NN,NN,NN,NN))
    #NBands.show()
    NBands.save("C:\\Users\\eikea\\Documents\\Beyond Ultra\\Image Hell\\Earth\\BGC\\TestCompInverse.png")
    pixeldata = list(Weap_BG.getdata())
    Max = 0
    for i,pixel in enumerate(pixeldata):
        Pixel = pixeldata[i]
        if Pixel[3] > Max:
            Max = Pixel[3]
        pixeldata[i] = (Pixel[0],Pixel[1],Pixel[2],69-Pixel[3])
    Ni = Image.new(mode = "RGBA" , size = (337,256) )
    Ni.putdata(pixeldata)
    #Ni.show()
    Ni.save("C:\\Users\\eikea\\Documents\\Beyond Ultra\\Image Hell\\Earth\\BGC\\TestyTest.png")

    BGC = Temp.resize((337+218,65+256))
    BGC.paste(Crest,(218,65),mask = Ni)
    BGC.save("C:\\Users\\eikea\\Documents\\Beyond Ultra\\Image Hell\\Earth\\BGC\\TestyTestTesty.png")

    #BGC.show()

def DBImages():
    for Char in CharMap:
        if Char == "10000051":
            print("Here")
        if Char in ["10000005","10000007"]:
            continue
        CM = CharMap[Char]
        CID = TagMap["Characters"][Char]["Name"].replace(" ","")        
        #CD = os.path.join(FO,CID+".png")
        CD = os.path.join(mydir,"DB_Images","Characters",CID)
        if TagMap["Characters"][Char]["Ban"]:
            continue
        #print(CID)
        ExC(CD)
        C = 0
        TP = ExC(CD)
        for const in CM["Passives"]:
            OP = os.path.join(F1,const[2]+".png")
            Nam = conv(const[0]).replace(" ","").replace(":","").replace("-","")
            if C == 0:
                FP = os.path.join(TP,"t04_combatPassive"+"_"+Nam+".png")
            elif C == 1:
                FP = os.path.join(TP,"t05_combatPassive"+"_"+Nam+".png")
            elif C == 2:
                FP = os.path.join(TP,"t06_systemPassive"+"_"+Nam+".png")
            try:
                shutil.copyfile(OP, FP)
            except:
                print(const[2]+" Missing")
            C+=1

        C = 1
        for Tal in CM["Talents"]:
            Tal = CM["Talents"][Tal]
            OP = os.path.join(F1,Tal["Icon"]+".png")
            Nam = conv(Tal["Name"]).replace(" ","").replace(":","").replace("-","")
            FP = os.path.join(TP,"c0"+str(C)+"_"+Nam+".png")
            try:
                shutil.copyfile(OP, FP)
            except:
                print(Tal["Icon"]+" Missing")
            C+=1

        C = 0
        for SI in [CM["Normal Attack"],CM["Elemental Skill"],CM["Elemental Burst"]]:
            #Cur = SI
            Nam = conv(SI["Name"]).replace(" ","").replace(":","").replace("-","")
            OP = os.path.join(F1,SI["Img"]+".png")
            if C == 2:
                OP = os.path.join(F1,SI["Img"]+"_HD.png")               
            if C == 0:
                FP = os.path.join(TP,"t01"+"_"+Nam.replace("NormalAttack","")+".png")
            elif C == 1:
                FP = os.path.join(TP,"t02"+"_skill_"+Nam+".png")
            elif C == 2:
                FP = os.path.join(TP,"t03"+"_burst_"+Nam+".png")
            try:
                shutil.copyfile(OP, FP)
            except:
                print(SI["Img"]+" Missing")
            C+=1
        OP = os.path.join(F1,"UI_Gacha_AvatarIcon_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"gachaIcon_"+CID+".png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_Gacha_AvatarIcon_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(Earth,"Characters",CID,"Const.png")
        FP = os.path.join(TP,"constpanel_"+CID+".png")
        try:
            CBase = Image.open(OP).convert("RGBA").crop((550,96,1920,960))
            CBase.save(FP)
        except:
            print("UI_Gacha_AvatarIcon_"+CM["Icon"]+".png"+" Missing")


        OP = os.path.join(F1,"UI_Gacha_AvatarImg_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"gachaPortrait_"+CID+".png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_Gacha_AvatarImg_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_AvatarIcon_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"charAvatar_"+CID+".png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_AvatarIcon_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_LegendQuestImg_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"storyChapter_"+CID+".png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_LegendQuestImg_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_NameCardIcon_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"namecard_friendship_"+CID+".png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_NameCardIcon_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_AvatarIcon_"+CM["Icon"]+"_Card.png")
        FP = os.path.join(TP,"shopIcon_"+CID+".png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_AvatarIcon_"+CM["Icon"]+"_Card.png"+" Missing")
            
        OP = os.path.join(F1,"UI_NameCardPic_"+CM["Icon"]+"_Alpha.png")
        FP = os.path.join(TP,"namecard_friendship_"+CID+"List.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_NameCardPic_"+CM["Icon"]+"_Alpha.png"+" Missing")

    for Weap in WeapMap:
        continue
        item = WeapMap[Weap]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Awk = os.path.join(F1,item["AIcon"]+".png")
        Gach = os.path.join(F1,"UI_Gacha_EquipIcon_"+item["Class"]+"_"+item["Series"]+".png")
        Name = conv(item["Name"]).replace(" ","_")
        NormO = ExCI(os.path.join(DBPath,"Weapons"),Name+"_Base.png")
        AwkO = ExCI(os.path.join(DBPath,"Weapons"),Name+"_Awk.png")
        GachO = ExCI(os.path.join(DBPath,"Weapons"),Name+"_Gacha.png")
        try:
            shutil.copyfile(Norm, NormO)
            shutil.copyfile(Awk, AwkO)
            shutil.copyfile(Gach, GachO)
        except:
            print(Name+" Missing")

    #TempMap = ["Materials","Quest","Tablets","Gadgets","Unsorted","Namecards","Pips","Currencies"]
    TempMap = ["Materials","Gadgets","Currencies","Variable","Quest"]
    for SubMap in TempMap:
        continue
        TargetMap = ItemMap[SubMap]


        for Item in TargetMap:            
            if TagMap["Items"][Item]["Ban"]:
                pass

                    #Furn = FurnMap[Furniture]
            Target = TargetMap[Item]
            TargetSet = DBIDetails(Target)
            if TargetSet.icon+".png" not in list(os.listdir(F1)):
                continue

            TargetCard = ICCreator(TargetSet)
            Water_Mark = WaterM(TargetSet.rarity)
            TargetCard.paste(Water_Mark,(277,0),mask = Water_Mark)
            OP = ExCI(os.path.join(DBPath,SubMap),TargetSet.fitype+"_"+TargetSet.fname+"_Card.png")
            TargetCard.save(OP)
            TargetPip = IPCreator(TargetSet)
            OP = ExCI(os.path.join(DBPath,SubMap),TargetSet.fitype+"_"+TargetSet.fname+"_Icon.png")
            TargetPip.save(OP)
            try:
                shutil.copyfile(os.path.join(F1,TargetSet.icon+".png"), ExCI(os.path.join(DBPath,SubMap),TargetSet.fitype+"_"+TargetSet.fname+"_raw.png"))
            except:
                print(Name+" Missing")
    
    for Furniture in FurnMap["Pieces"]:
        continue
        Target = FurnMap["Pieces"][Furniture]
        TargetSet = DBIDetails(Target,"Furniture Pieces")
        if TargetSet.icon+".png" not in list(os.listdir(F1)):
            continue

        TargetCard = ICCreator(TargetSet)
        OP = ExCI(os.path.join(DBPath,"Furniture"),TargetSet.fitype+"_"+TargetSet.fname+"_Card.png")
        TargetCard.save(OP)
        TargetPip = IPCreator(TargetSet)
        OP = ExCI(os.path.join(DBPath,"Furniture"),TargetSet.fitype+"_"+TargetSet.fname+"_Icon.png")
        TargetPip.save(OP)
        try:
            shutil.copyfile(os.path.join(F1,TargetSet.icon+".png"), ExCI(os.path.join(DBPath,"Furniture"),TargetSet.fitype+"_"+TargetSet.fname+"_raw.png"))
        except:
            print(Name+" Missing")
    
    for Mat in ItemMap["Food"]:
        continue
        item = ItemMap["Food"][Mat]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Name = conv(item["Item Name"]).replace(" ","_").replace("\"","").replace("\\","")
        if (Name[0:9] == "Delicious") or (Name[0:10] == "Suspicious"):
            continue
        NormO = ExCI(os.path.join(DBPath,"Food"),Name+".png")
        try:
            shutil.copyfile(Norm, NormO)
        except:
            print(Name+" Missing")

    for Mon in MonMap:
        item = MonMap[Mon]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Name = conv(item["Name"]).replace(" ","_").replace("\"","").replace("\\","").replace(":","")
        NormO = ExCI(os.path.join(DBPath,"Monsters"),Name+".png")
        try:
            shutil.copyfile(Norm, NormO)
        except:
            print(Name+" Missing")

    for Mat in ItemMap["Variable"]:
        continue
        item = ItemMap["Variable"][Mat]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Name = conv(item["Item Name"]).replace(" ","_").replace("\"","").replace("\\","")
        NormO = ExCI(os.path.join(DBPath,"Variable"),Name+".png")
        try:
            shutil.copyfile(Norm, NormO)
        except:
            print(Name+" Missing")

    for Mat in ItemMap["Unsorted"]:
        continue
        item = ItemMap["Unsorted"][Mat]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Name = conv(item["Item Name"]).replace(" ","_").replace("\"","").replace("\\","")
        NormO = ExCI(os.path.join(DBPath,"Unsorted"),Name+".png")
        try:
            shutil.copyfile(Norm, NormO)
        except:
            print(Name+" Missing")


    pass

def MapMaker():

    Cur = []
    for item in os.listdir(MapDir):
        if "UI_MapBack" in item:
            if "LP" in item:
                continue
            if "None" in item:
                continue
            Cur.append(item)
    SS = 2048
    print(8*SS)
    N = 0
    """Pure Map
    Base = Image.new("RGBA", (8*SS,8*SS))
    XOffSet = 4*SS
    YOffSet = 4*SS    
    """
    """Inazuma Only Dimensions    
    Base = Image.new("RGBA", (4*SS,4*SS))
    XOffSet = -2*SS
    YOffSet = -2*SS
    """
    Base = Image.new("RGBA", (9*SS,9*SS))
    XOffSet = 2*SS
    YOffSet = 3*SS
    while N < len(Cur):
        item = Cur[N].replace(" ",".")
        if "None" in item:
            break
        print(item)
        if " #" in item:
            N+=1
        item = item.split(".")[0].split("_")
        
        YVal = int(item[2])*SS*-1
        XVal = int(item[3])*SS*-1
        Temp = Image.open(os.path.join(MapDir, Cur[N])).convert("RGBA").resize((SS,SS))
        """
        if (int(item[2]) <= -2) and (int(item[3]) <= -2):
            im = Image.new("RGBA", (SS,SS),(0,0,0,0))
            draw = ImageDraw.Draw(im)
            draw.text((0.5*SS,0.5*SS), "@Genshin_Intel",font = font)
            im = im.rotate(45)
            Temp.paste(im,mask = im)
            #Temp.show()
        """
        if (int(item[2]),int(item[3])) in [(-5,-5),(-5,-4),(-2,-4),(-5,-3),(-5,-2),(-3,-3),(-3,-2),(-2,-3),(-2,-2)]:
            im = Image.new("RGBA", (SS,SS),(0,0,0,0))
            draw = ImageDraw.Draw(im)
            draw.text((0.5*SS,0.5*SS), "@Genshin_Intel",font = font)
            im = im.rotate(45)
            Temp.paste(im,mask = im)
        #if (int(item[2]),int(item[3])) in [(-3,-5),(-3,-4),(-4,-2),(-4,-3),(-4,-5),(-4,-4),(-3,-5),(-3,-5),]:
            #im = Image.new("RGBA", (SS,SS),(0,0,0,0))
            #draw = ImageDraw.Draw(im)
            #draw.text((0.5*SS,0.5*SS), "@Genshin_Intel",font = font)
            #im = im.rotate(45)
            #Temp.paste(im,mask = im)
            #Temp.show()
        Base.paste(Temp,(XVal+XOffSet,YVal+YOffSet),mask = Temp)
        N+=1
    print("Done - Saving Now")
    OP = ExCI(os.path.join(F5,"Maps"),"MainWorld.png")
    #OP = ExCI(os.path.join(F5,"Maps"),"MainWorld"+Cur[N].split(".")[0]+".png")
    Base.save(OP)
    pass

def InazumaMapMaker():

    Cur = []
    for item in os.listdir(MapDir):
        if "UI_MapBack" in item:
            if "LP" in item:
                continue
            if "None" in item:
                continue
            Cur.append(item)
    SS = 2048
    print(8*SS)
    N = 0
    """Pure Map
    Base = Image.new("RGBA", (8*SS,8*SS))
    XOffSet = 4*SS
    YOffSet = 4*SS    
    """
    Base = Image.new("RGBA", (4*SS,4*SS))
    XOffSet = -2*SS
    YOffSet = -2*SS
    while N < len(Cur):
        item = Cur[N].replace(" ",".")
        if "None" in item:
            break
        print(item)
        if " #" in item:
            N+=1
        item = item.split(".")[0].split("_")
        
        YVal = int(item[2])*SS*-1
        XVal = int(item[3])*SS*-1
        Temp = Image.open(os.path.join(MapDir, Cur[N])).convert("RGBA").resize((SS,SS))
        """
        if (int(item[2]) <= -2) and (int(item[3]) <= -2):
            im = Image.new("RGBA", (SS,SS),(0,0,0,0))
            draw = ImageDraw.Draw(im)
            draw.text((0.5*SS,0.5*SS), "@Genshin_Intel",font = font)
            im = im.rotate(45)
            Temp.paste(im,mask = im)
            #Temp.show()
        """
        if (int(item[2]),int(item[3])) in [(-5,-5),(-5,-4),(-2,-4),(-5,-3),(-5,-2),(-3,-3),(-3,-2),(-2,-3),(-2,-2)]:
            im = Image.new("RGBA", (SS,SS),(0,0,0,0))
            draw = ImageDraw.Draw(im)
            draw.text((0.5*SS,0.5*SS), "@Genshin_Intel",font = font)
            im = im.rotate(45)
            Temp.paste(im,mask = im)
            #Temp.show()
        Base.paste(Temp,(XVal+XOffSet,YVal+YOffSet),mask = Temp)
        N+=1
    print("Done - Saving Now")
    OP = ExCI(os.path.join(F5,"Maps"),"InazumaWorld.png")
    #OP = ExCI(os.path.join(F5,"Maps"),"MainWorld"+Cur[N].split(".")[0]+".png")
    Base.save(OP)
    pass
def WhatMapMaker():

    Cur = []
    for item in os.listdir(MapDir):
        if "UI_MapBack_LP" in item:
            if "None" in item:
                continue
            Cur.append(item)
    SS = 2048
    print(8*SS)
    N = 0
    """Pure Map
    Base = Image.new("RGBA", (8*SS,8*SS))
    XOffSet = 4*SS
    YOffSet = 4*SS    
    """
    Base = Image.new("RGBA", (2*SS,2*SS))
    XOffSet = 0*SS
    YOffSet = 0*SS
    while N < len(Cur):
        item = Cur[N].replace(" ",".")
        if "None" in item:
            break
        print(item)
        if " #" in item:
            N+=1
        item = item.split(".")[0].split("_")
        
        YVal = int(item[3])*SS*-1
        XVal = int(item[4])*SS*-1
        Temp = Image.open(os.path.join(MapDir, Cur[N])).convert("RGBA").resize((SS,SS))
        """
        if (int(item[2]) <= -2) and (int(item[3]) <= -2):
            im = Image.new("RGBA", (SS,SS),(0,0,0,0))
            draw = ImageDraw.Draw(im)
            draw.text((0.5*SS,0.5*SS), "@Genshin_Intel",font = font)
            im = im.rotate(45)
            Temp.paste(im,mask = im)
            #Temp.show()
        """
        #im = Image.new("RGBA", (SS,SS),(0,0,0,0))
        #draw = ImageDraw.Draw(im)
        #draw.text((0.5*SS,0.5*SS), "@Genshin_Intel",font = font)
        #im = im.rotate(45)
        #Temp.paste(im,mask = im)
        #Temp.show()
        Base.paste(Temp,(XVal+XOffSet,YVal+YOffSet),mask = Temp)
        N+=1
    print("Done - Saving Now")
    OP = ExCI(os.path.join(F5,"Maps"),"WhatWorld.png")
    #OP = ExCI(os.path.join(F5,"Maps"),"MainWorld"+Cur[N].split(".")[0]+".png")
    Base.save(OP)
    pass

def IslesMapMaker():

    for MapNum in ["A","B"]:
        Cur = []
        for item in os.listdir(MapDir):
            if "UI_Map_GoldenAppleIsles_"+MapNum+"_" in item:
                Cur.append(item)
        SS = 1024
        #print(8*SS)
        N = 0
        """Pure Map
        Base = Image.new("RGBA", (8*SS,8*SS))
        XOffSet = 4*SS
        YOffSet = 4*SS    
        """
        im = Image.new("RGBA", (SS,SS))
        draw = ImageDraw.Draw(im)
        draw.text((0.5*SS,0.5*SS), "Genshin Intel",font = font)
        im = im.rotate(45)
        Base = Image.new("RGBA", (2*SS,2*SS))
        XOffSet = 0*SS
        YOffSet = 0*SS
        while N < len(Cur):
            item = Cur[N].replace(" ",".")
            if "None" in item:
                break
            print(item)
            if " #" in item:
                N+=1
            item = item.split(".")[0].split("_")
            
            YVal = int(item[4])*SS*-1
            XVal = int(item[5])*SS*-1
            Temp = Image.open(os.path.join(MapDir, Cur[N])).convert("RGBA").resize((SS,SS))
            Base.paste(Temp,(XVal+XOffSet,YVal+YOffSet),mask = Temp)
            Base.paste(im,(XVal+XOffSet,YVal+YOffSet),mask = im)
            N+=1
        print("Done - Saving Now")
        OP = ExCI(os.path.join(F5,"Maps"),"IsleWorld_"+MapNum+".png")
        #OP = ExCI(os.path.join(F5,"Maps"),"MainWorld"+Cur[N].split(".")[0]+".png")
        Base.save(OP)
        pass

def BotImages():
    for Char in CharMap:
        if Char == "10000051":
            print("Here")
        CM = CharMap[Char]
        CID = TagMap["Characters"][Char]["Name"]        
        #CD = os.path.join(FO,CID+".png")
        CD = os.path.join(F5C,CID)
        if TagMap["Characters"][Char]["Ban"]:
            continue
        if Char in ["10000005","10000007"]:
            continue
        #print(CID)
        ExC(CD)
        C = 0
        TP = ExC(os.path.join(F5C,CID,"Passives"))


        for const in CM["Passives"]:
            OP = os.path.join(F1,const[2]+".png")
            FP = os.path.join(TP,str(C)+".png")
            try:
                shutil.copyfile(OP, FP)
            except:
                print(const[2]+" Missing")
            C+=1

        C = 1
        TP = ExC(os.path.join(F5C,CID,"Talents"))
        for Tal in CM["Talents"]:
            Tal = CM["Talents"][Tal]
            OP = os.path.join(F1,Tal["Icon"]+".png")
            FP = os.path.join(TP,str(C)+".png")
            try:
                shutil.copyfile(OP, FP)
            except:
                print(Tal["Icon"]+" Missing")
            C+=1

        OP = os.path.join(Earth,"Characters",CID.replace(" ",""),"Const.png")
        FP = os.path.join(TP,"0.png")
        try:
            CBase = Image.open(OP).convert("RGBA").crop((550,96,1920,960))
            CBase.save(FP)
        except:
            print("FullConst"+CM["Icon"]+".png"+" Missing")


        C = 0
        TP = ExC(os.path.join(F5C,CID,"Skills"))
        for SI in [CM["Normal Attack"]["Img"],CM["Elemental Skill"]["Img"],CM["Elemental Burst"]["Img"],]:
            OP = os.path.join(F1,SI+".png")
            if C == 2:
                OP = os.path.join(F1,SI+"_HD.png")               
            FP = os.path.join(TP,str(C)+".png")
            try:
                shutil.copyfile(OP, FP)
            except:
                print(SI+" Missing")
            C+=1
        TP = ExC(os.path.join(F5C,CID))
        OP = os.path.join(F1,"UI_Gacha_AvatarIcon_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Panel.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_Gacha_AvatarIcon_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_Gacha_AvatarImg_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Full.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_Gacha_AvatarImg_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_AvatarIcon_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Icon.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_AvatarIcon_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_LegendQuestImg_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Page.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_LegendQuestImg_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_NameCardIcon_"+CM["Icon"]+".png")
        FP = os.path.join(TP,"Raw_Card.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_NameCardIcon_"+CM["Icon"]+".png"+" Missing")

        OP = os.path.join(F1,"UI_AvatarIcon_"+CM["Icon"]+"_Card.png")
        FP = os.path.join(TP,"Raw_Item.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_AvatarIcon_"+CM["Icon"]+"_Card.png"+" Missing")
            
        OP = os.path.join(F1,"UI_NameCardPic_"+CM["Icon"]+"_Alpha.png")
        FP = os.path.join(TP,"Raw_Bar.png")
        try:
            shutil.copyfile(OP, FP)
        except:
            print("UI_NameCardPic_"+CM["Icon"]+"_Alpha.png"+" Missing")
            


    for Weap in WeapMap:
        if TagMap["Weapons"][Weap]["Ban"]:
            continue
        item = WeapMap[Weap]
        Norm = os.path.join(F1,item["Icon"]+".png")
        Awk = os.path.join(F1,item["AIcon"]+".png")
        Gach = os.path.join(F1,"UI_Gacha_EquipIcon_"+item["Class"]+"_"+item["Series"]+".png")
        Name = conv(item["Name"]).replace(" ","_")
        NormO = ExCI(os.path.join(F5,"Weapons",Name),"Base.png")
        AwkO = ExCI(os.path.join(F5,"Weapons",Name),"Awk.png")
        GachO = ExCI(os.path.join(F5,"Weapons",Name),"Gacha.png")
        try:
            shutil.copyfile(Norm, NormO)
            shutil.copyfile(Awk, AwkO)
            shutil.copyfile(Gach, GachO)
        except:
            print(Name+" Missing")

    TempMap = ["Materials","Gadgets"]
    for SubMap in TempMap:
        TargetMap = ItemMap[SubMap]


        for Item in TargetMap:            
            Target = TargetMap[Item]
            TargetSet = IDetails(Target)
            if TargetSet.icon+".png" not in list(os.listdir(F1)):
                continue

            TargetCard = ICCreator(TargetSet)
            Water_Mark = WaterM(TargetSet.rarity)
            TargetCard.paste(Water_Mark,(277,0),mask = Water_Mark)
            OP = ExCI(os.path.join(F5,SubMap),TargetSet.fname+"_Card.png")
            TargetCard.save(OP)
            TargetPip = IPCreator(TargetSet)
            OP = ExCI(os.path.join(F5,SubMap),TargetSet.fname+"_Icon.png")
            TargetPip.save(OP)
            try:
                shutil.copyfile(os.path.join(F1,TargetSet.icon+".png"), ExCI(os.path.join(F5,SubMap),TargetSet.fname+"_raw.png"))
            except:
                print(Name+" Missing")

            if not TagMap["Items"][Item]["Ban"]:
                continue
            try:
                #Furn = FurnMap[Furniture]
                Target = TargetMap[Item]
                TargetSet = IDetails(Target)
                TargetCard = ICCreator(TargetSet)
                Water_Mark = WaterM(TargetSet.rarity)
                TargetCard.paste(Water_Mark,(277,0),mask = Water_Mark)
                OP = ExCI(os.path.join(F5,SubMap),TargetSet.fname+"_Card.png")
                TargetCard.save(OP)
            except:
                continue
            try:
                #Furn = FurnMap[Furniture]
                Target = TargetMap[Item]
                TargetSet = IDetails(Target)
                TargetCard = IPCreator(TargetSet)
                #Water_Mark = WaterM(TargetSet.rarity)
                #TargetCard.paste(Water_Mark,(277,0),mask = Water_Mark)
                OP = ExCI(os.path.join(F5,SubMap),TargetSet.fname+"_Pip.png")
                TargetCard.save(OP)
            except:
                #Furn = FurnMap[Furniture]
                Target = TargetMap[Item]
                TargetSet = IDetails(Target)
                TargetCard = IPCreator(TargetSet)
                #Water_Mark = WaterM(TargetSet.rarity)
                #TargetCard.paste(Water_Mark,(277,0),mask = Water_Mark)
                OP = ExCI(os.path.join(F5,SubMap),TargetSet.fname+"_Pip.png")
                TargetCard.save(OP)
                continue
            print(Item)
    pass
def ItemComplete():
    #FM = {"1100204" : FurnMap["1100204"],"600112" : FurnMap["600112"],"700510" : FurnMap["700510"],"700508" : FurnMap["700508"]}
    #TempMap = ["Materials","Quest","Tablets","Gadgets","Unsorted","Namecards","Pips","Currencies"]
    TempMap = ["Materials"]
    for SubMap in TempMap:
        TargetMap = ItemMap[SubMap]


        for Item in TargetMap:            
            if not TagMap["Items"][Item]["Ban"]:
                pass
            try:
                #Furn = FurnMap[Furniture]
                Target = TargetMap[Item]
                TargetSet = IDetails(Target)
                TargetCard = ICCreator(TargetSet)
                #Water_Mark = WaterM(TargetSet.rarity)
                #TargetCard.paste(Water_Mark,(277,0),mask = Water_Mark)
                OP = ExCI(os.path.join(F5,SubMap),TargetSet.fname+"_Card.png")
                TargetCard.save(OP)
            except:
                continue
            try:
                #Furn = FurnMap[Furniture]
                Target = TargetMap[Item]
                TargetSet = IDetails(Target)
                TargetCard = IPCreator(TargetSet)
                #Water_Mark = WaterM(TargetSet.rarity)
                #TargetCard.paste(Water_Mark,(277,0),mask = Water_Mark)
                OP = ExCI(os.path.join(F5,SubMap),TargetSet.fname+"_Pip.png")
                TargetCard.save(OP)
            except:
                #Furn = FurnMap[Furniture]
                Target = TargetMap[Item]
                TargetSet = IDetails(Target)
                TargetCard = IPCreator(TargetSet)
                #Water_Mark = WaterM(TargetSet.rarity)
                #TargetCard.paste(Water_Mark,(277,0),mask = Water_Mark)
                OP = ExCI(os.path.join(F5,SubMap),TargetSet.fname+"_Pip.png")
                TargetCard.save(OP)
                continue
            print(Item)
    pass
"""
Side = Image.open(Norm).convert("RGBA")


X1 = XF.resize((2048,1024))
X2 = X1.copy().convert("RGBA")

Norm = os.path.join(IO,item.replace(" ","_")+".png")
R4 = Image.open(Norm).convert("RGBA")
X2.paste(R4,mask = R4)
OP = os.path.join(UP,item+".png")
X2.save(OP)
"""

if __name__ == "__main__":
    #Fourth()
    #ICards()
    #CharAscIgs()
    #CharTalAscIgs()
    #CharImD()
    #DBDirec()
    #FrameC()
    #WeapCards()
    #ImageTesting()
    #DBImages()
    BotImages()
    #ItemCards()
    #temComplete()
    #ItemPips()
    #MapMaker()
    #InazumaMapMaker()
    #DBImages()
    #Narukami()
    #WhatMapMaker()
    #IslesMapMaker()
    #WeapWM()