import sys
import os
from pathlib import Path
import json
import math
import GDBTools as GDBT
from openpyxl import Workbook
import re

os.chdir(os.path.dirname(__file__))
mydir = os.path.dirname(__file__) or "."


Base_Data = os.path.join(mydir, "Base_Data")
Remapped_Data = os.path.join(mydir, "Remapped_Data")
Out_Files = os.path.join(mydir, "Out_Files")
Bot_Files = os.path.join(mydir, "Bot_Files")
DB = os.path.join(mydir, "Final")
EndPath = os.path.join(Bot_Files, "Tags.json")
Stage_3 = os.path.join(mydir, "Stage_3")
Stage_4 = os.path.join(mydir, "Stage_4")
LangEN = GDBT.Stageloader("TextMapEN.json","L")
ret = { "Goblet" : "Go",
        "Feather" : "Fe",
        "Headpiece" : "He",
        "Flower" : "Fl",
        "Timepiece" : "Ti"}

demih = { "EQUIP_RING" : "Goblet",
        "EQUIP_NECKLACE" : "Feather",
        "EQUIP_DRESS" : "Headpiece",
        "EQUIP_BRACER" : "Flower",
        "EQUIP_SHOES" : "Timepiece"}

rar = {"QUALITY_BLUE" : 3,"QUALITY_PURPLE" : 4,"QUALITY_ORANGE" : 5}

cwea = { "WEAPON_SWORD_ONE_HAND" : "Sword",
        "WEAPON_CATALYST" : "Catalyst",
        "WEAPON_BOW" : "Bow",
        "WEAPON_CLAYMORE" : "Claymore",
        "WEAPON_POLE" : "Polearm"}


#QChats = Outloader("RawDiag.json")
Bantoggle = True
CharMap = GDBT.Stageloader("CharMap.json",3)
ArtifMap = GDBT.Stageloader("ArtifMap.json",3)
WeapMap = GDBT.Stageloader("WeapMap.json",3)
ItemMap = GDBT.Stageloader("ItemMap.json",3)
FurnMap = GDBT.Stageloader("FurnMap.json",3)
ShopMap = GDBT.Stageloader("ShopMap.json",3)
QuestMap = GDBT.Stageloader("QuestMap.json",3)
TagMap = GDBT.Stageloader("Tags.json",3)
ShopLink = GDBT.Stageloader("ShopLinks.json",3)
BS = GDBT.Stageloader("BulkStory.json",3)
ChapterData = GDBT.Stageloader("ChapterData.json",1)
#ChapterMap = GDBT.Stageloader("QuestCodexTrees.json",3)

ArtifEN = os.path.join(DB, "Artif_EN.json")
#CharEN = os.path.join(DB, "Char_EN.json")
WeapEN = os.path.join(DB, "Weap_EN.json")
ItemEN = os.path.join(DB, "Item_EN.json")
QuestEN = os.path.join(DB, "Quest_EN.json")
ChapEN =  os.path.join(DB, "Chap_EN.json")
ChapTEN =  os.path.join(DB, "ChapT_EN.json")
SearchEN = os.path.join(DB, "Search_EN.json")

RecipeMapData = GDBT.Stageloader("RecipeMapData.json",2)
CombineData = GDBT.Stageloader("CombineData.json",1)
AvatarHeroEntityData = GDBT.Stageloader("AvatarHeroEntityData.json",1)
ShopData = GDBT.Stageloader("ShopData.json",1)
ActivityShopOverallData = GDBT.Stageloader("ActivityShopOverallData.json",1)

EventShops = []
for item in ActivityShopOverallData:
    EventShops.append(ActivityShopOverallData[item]["ShopType"])
"""
def TexRet(TexLoc,LangPat=LangEN):
    WR = str(TexLoc)
    if WR not in LangPat:
        return(WR)
    else:
        return(LangPat[WR])
"""

def SymbolKeep(FN):
    if "CHS.json" or "CHS.json" in FN:
        return(False)
    else:
        return(True)

def TagInitializer():
    final = {}
    final.update({"Characters" : {}})
    final.update({"Artifacts" : {}})
    final.update({"Materials" : {}})
    final.update({"Weapons" : {}})
    for item in CharMap:
        Char = CharMap[item]
        temp = {}
        temp.update({"Ban" : False})
        temp.update({"Tags" : []})
        temp.update({"Helper" : Char["Helper"]})
        temp.update({"Name" : LangEN[str(CharMap[item]["Name"])]})
        final["Characters"].update({item : temp})

    for item in ArtifMap:
        ASet = ArtifMap[item]
        temp = {}
        temp.update({"Ban" : False})
        temp.update({"Tags" : []})
        temp.update({"Helper" : LangEN[ASet["Set Name"]]})
        final["Artifacts"].update({item : temp})

    for item in WeapMap:
        Weap = WeapMap[item]
        temp = {}
        temp.update({"Ban" : False})
        temp.update({"Tags" : []})
        temp.update({"Helper" : LangEN[item]})
        final["Weapons"].update({item : temp})


    for Tree in ItemMap:
        if Tree in ["Food","Ascension Materials"]:
            for item in ItemMap[Tree]:
                for tier in ItemMap[Tree][item]:
                    Mat = ItemMap[Tree][item][tier]
                    temp = {}
                    temp.update({"Ban" : False})
                    temp.update({"Tags" : []})
                    temp.update({"Helper" : Mat["Helper"]})
                    temp.update({"Type" : Tree})
                    final["Materials"].update({tier : temp})    
        else:
            for item in ItemMap[Tree]:
                Mat = ItemMap[Tree][item]
                temp = {}
                temp.update({"Ban" : False})
                temp.update({"Tags" : []})
                temp.update({"Helper" : Mat["Helper"]})
                temp.update({"Type" : Tree})
                final["Materials"].update({item : temp})    


    with open(EndPath, "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def TagRevitializer():
    final = TagMap
    for item in CharMap:

        if item in final["Characters"]:
            Char = CharMap[item]
            temp = {}
            temp.update({"Ban" : final["Characters"][item]["Ban"]})
            temp.update({"Tags" : final["Characters"][item]["Tags"]})
            temp.update({"Helper" : Char["Helper"]})
            temp.update({"Name" : GDBT.econv(str(Char["Name"]))})
            temp.update({"Element" : GDBT.conv(str(Char["Element"]))})
            temp.update({"Rarity" : GDBT.conv(str(Char["Rarity"]))})
            final["Characters"].update({item : temp})
            #continue
        else:
            Char = CharMap[item]
            temp = {}
            temp.update({"Ban" : True})
            temp.update({"Tags" : []})
            temp.update({"Helper" : Char["Helper"]})
            temp.update({"Name" : GDBT.econv(str(Char["Name"]))})
            temp.update({"Element" : GDBT.conv(str(Char["Element"]))})
            temp.update({"Rarity" : GDBT.conv(str(Char["Rarity"]))})
            final["Characters"].update({item : temp})

    for item in ArtifMap:
        if item in final["Artifacts"]:
            ASet = ArtifMap[item]
            temp = {}
            temp.update({"Ban" : final["Artifacts"][item]["Ban"]})
            temp.update({"Tags" : []})
            temp.update({"Helper" : GDBT.econv(ASet["Set Name"])})
            final["Artifacts"].update({item : temp})
            continue
        else:
            ASet = ArtifMap[item]
            temp = {}
            temp.update({"Ban" : True})
            temp.update({"Tags" : []})
            temp.update({"Helper" : GDBT.econv(ASet["Set Name"])})
            final["Artifacts"].update({item : temp})

    for item in WeapMap:
        if item in final["Weapons"]:
            Weap = WeapMap[item]
            temp = {}
            temp.update({"Ban" : final["Weapons"][item]["Ban"]})
            temp.update({"Tags" : final["Weapons"][item]["Tags"]})
            temp.update({"Helper" : Weap["Series"]})
            temp.update({"Name" : GDBT.conv(Weap["Name"])})
            temp.update({"Type" : Weap["Class"]})
            final["Weapons"].update({item : temp})
        else:
            Weap = WeapMap[item]
            temp = {}
            temp.update({"Ban" : True})
            temp.update({"Tags" : []})
            temp.update({"Helper" : Weap["Series"]})
            temp.update({"Name" : GDBT.conv(Weap["Name"])})
            temp.update({"Type" : Weap["Class"]})
            final["Weapons"].update({item : temp})

    for item in FurnMap["Pieces"]:
        if item in final["Furniture"]:
            Piece = FurnMap["Pieces"][item]
            temp = {}
            temp.update({"Ban" : final["Furniture"][item]["Ban"]})
            temp.update({"Tags" : final["Furniture"][item]["Tags"]})
            temp.update({"Helper" : Piece["Icon"]})
            temp.update({"Name" : GDBT.conv(Piece["Name"])})
            final["Furniture"].update({item : temp})
        else:
            Piece = FurnMap["Pieces"][item]
            temp = {}
            temp.update({"Ban" : True})
            temp.update({"Tags" : []})
            temp.update({"Helper" : Piece["Icon"]})
            temp.update({"Name" : GDBT.conv(Piece["Name"])})
            #temp.update({"Type" : Piece["Class"]})
            final["Furniture"].update({item : temp})

    for item in FurnMap["Sets"]:
        if item in final["FSets"]:
            Piece = FurnMap["Sets"][item]
            temp = {}
            temp.update({"Ban" : final["FSets"][item]["Ban"]})
            temp.update({"Tags" : final["FSets"][item]["Tags"]})
            temp.update({"Helper" : Piece["Icon"]})
            temp.update({"Name" : GDBT.conv(Piece["Name"])})
            final["FSets"].update({item : temp})
        else:
            Piece = FurnMap["Sets"][item]
            temp = {}
            temp.update({"Ban" : True})
            temp.update({"Tags" : []})
            temp.update({"Helper" : Piece["Icon"]})
            temp.update({"Name" : GDBT.conv(Piece["Name"])})
            #temp.update({"Type" : Piece["Class"]})
            final["FSets"].update({item : temp})


    for item in QuestMap:
        if item in final["Quests"]:
            Quest = QuestMap[item]
            temp = {}
            temp.update({"DB Dia" : final["Quests"][item]["DB Dia"]})
            temp.update({"Ban" : final["Quests"][item]["Ban"]})
            temp.update({"Name" : GDBT.conv(Quest["Title"])})
            temp.update({"Desc" : GDBT.conv(Quest["Desc"])})
            final["Quests"].update({item : temp})
        else:
            Quest = QuestMap[item]
            temp = {}
            temp.update({"DB Dia" : False})
            temp.update({"Ban" : True})
            temp.update({"Name" : GDBT.conv(Quest["Title"])})
            temp.update({"Desc" : GDBT.conv(Quest["Desc"])})
            final["Quests"].update({item : temp})


    for Tree in ItemMap:
        if Tree in ["Ascension Materials"]:
            for item in ItemMap[Tree]:
                for tier in ItemMap[Tree][item]:
                    if tier in final["Items"]:
                        Mat = ItemMap[Tree][item][tier]

                        Mat = ItemMap[Tree][item][tier]
                        temp = {}
                        temp.update({"Ban" : final["Items"][tier]["Ban"]})
                        temp.update({"Tags" : []})
                        temp.update({"Helper" : Mat["Helper"]})
                        temp.update({"Type" : Tree})
                        final["Items"].update({tier : temp})    
                    else:

                        Mat = ItemMap[Tree][item][tier]
                        temp = {}
                        temp.update({"Ban" : True})
                        temp.update({"Tags" : []})
                        temp.update({"Helper" : Mat["Helper"]})
                        temp.update({"Type" : Tree})
                        final["Items"].update({tier : temp})    
        else:
            for item in ItemMap[Tree]:
                if item in final["Items"]:
                    Mat = ItemMap[Tree][item]
                    temp = {}
                    temp.update({"Ban" : final["Items"][item]["Ban"]})
                    temp.update({"Tags" : []})
                    temp.update({"Helper" : Mat["Helper"]})
                    temp.update({"Type" : Tree})
                    final["Items"].update({item : temp})    

                else:
                    Mat = ItemMap[Tree][item]
                    temp = {}
                    temp.update({"Ban" : True})
                    temp.update({"Tags" : []})
                    temp.update({"Helper" : Mat["Helper"]})
                    temp.update({"Type" : Tree})
                    final["Items"].update({item : temp})    


    with open(os.path.join(Stage_3, "Tags.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def ArtifMapper(lan,Out):
    fin = {}
    for item in ArtifMap:
        if TagMap["Artifacts"][item]["Ban"] and Bantoggle:
            continue
        temp = {}
        bons = []
        for bon in ArtifMap[item]["Set Bonuses"]:
            bons.append([bon,GDBT.conv(ArtifMap[item]["Set Bonuses"][bon][1],lan)])
        SetPie = {}
        for Pie in ArtifMap[item]["Set Pieces"]:
            temp2 = {}
            #nam = demih[Pie]
            #sto = Tag[item][nam]
            if str(item) not in BS["Artifacts"]:
                temp2.update({Pie : [GDBT.conv(ArtifMap[item]["Set Pieces"][Pie][0],lan),GDBT.conv(ArtifMap[item]["Set Pieces"][Pie][1],lan),"",str(item)+"_"+ret[Pie]]})
            else:        
                temp2.update({Pie : [GDBT.econv(ArtifMap[item]["Set Pieces"][Pie][0],lan),GDBT.econv(ArtifMap[item]["Set Pieces"][Pie][1],lan),BS["Artifacts"][str(item)][Pie],str(item)+"_"+ret[Pie]]})

            SetPie.update(temp2)
        temp.update({"Bonuses" : bons})
        temp.update({"SID" : item})
        #temp.update({"Tags" : Tag[item]["Tags"]})
        temp.update({"Set Pieces" : SetPie})
        fin.update({GDBT.conv(ArtifMap[item]["Set Name"],lan) :  temp  })
    sort = sorted(fin.keys())
    final = {}
    for item in sort:
        final.update({item : fin[item]})
    if "CHS" in Out:
        with open(Out, "w",encoding="utf-8") as write_file:
            json.dump(fin, write_file, indent=4, ensure_ascii=False)
    else:
        with open(Out, "w") as write_file:
            json.dump(fin, write_file, indent=4)

def FurnMapper(lan,Out):
    Complete = {}
    fin = {}
    for item in FurnMap["Pieces"]:
        if TagMap["Furniture"][item]["Ban"] and Bantoggle:
            continue
        temp = {}
        Target = FurnMap["Pieces"][item]
        temp.update({"Name" : GDBT.conv(Target["Name"],lan)})
        temp.update({"FName" : GDBT.conv(Target["FName"],lan)})
        temp.update({"Desc" : GDBT.conv(Target["Desc"],lan)})
        temp.update({"Rarity" : Target["Rarity"]})
        temp.update({"Comfort" : Target["Comfort"]})
        temp.update({"Cost" : Target["Cost"]})
        if Target["Crafting"] != {}:
            CTemp = {}
            CMT = {}
            for Mat in Target["Crafting"]["Recipe"]:
                CMT.update({GDBT.conv(Mat,lan) : Target["Crafting"]["Recipe"][Mat]})
            CTemp.update({"Recipe" : CMT})
            CTemp.update({"Exp" : Target["Crafting"]["Exp Gain"]})
            CTemp.update({"Crafting Time" : GDBT.timeconv(Target["Crafting"]["Crafting Time"])})
            CTemp.update({"Friend Reduction" : GDBT.timeconv(Target["Crafting"]["Friend Reduction"])})
        #temp.update({"Tags" : Tag[item]["Tags"]})
        temp.update({"Crafting" : CTemp})
        ISets = {}
        for item in Target["Sets"]:
            if TagMap["FSets"][item]["Ban"] and Bantoggle:
                continue
            else:
                ISets.update({GDBT.conv(FurnMap["Sets"][item]["Name"],lan) : Target["Sets"][item]})
        temp.update({"Sets" : ISets})
        fin.update({GDBT.conv(Target["Name"],lan) :  temp  })
    Complete.update({"Pieces" : fin})

    fin = {}
    for item in FurnMap["Sets"]:
        if TagMap["FSets"][item]["Ban"] and Bantoggle:
            pass
        temp = {}
        Target = FurnMap["Sets"][item]
        temp.update({"Name" : GDBT.conv(Target["Name"],lan)})
        #temp.update({"Desc" : GDBT.conv(Target["Desc"],lan)})
        Faves = []
        for FChar in Target["Faves"]:
            Faves.append(GDBT.conv(CharMap[str(FChar)]["Name"]))
        temp.update({"Faves" : Faves})
        fin.update({GDBT.conv(Target["Name"],lan) :  temp  })
        IPies = {}
        for item in Target["Pieces"]:
            if TagMap["Furniture"][item]["Ban"] and Bantoggle:
                continue
            else:
                IPies.update({GDBT.conv(FurnMap["Pieces"][item]["Name"],lan) : Target["Pieces"][item]})
        temp.update({"Pieces" : IPies})

    Complete.update({"Sets" : fin})

    with open(Out, "w") as write_file:
        json.dump(Complete, write_file, indent=4)

def ShopGoodRetT0(Container,lan):
    Fin = {}
    Num = -1
    BC = ""
    TFin = {}
    for item in Container:

        temp = {}
        Target = Container[item]
        temp.update({"Name" : GDBT.conv(Target["Temp"],lan)})
        temp.update({"Count" : Target["Count"]})
        temp.update({"Limit" : Target["Limit"]})
        if Target["Cost"] != []:
            temp.update({"Cost" : {GDBT.conv(Target["Cost"][0],lan) : Target["Cost"][1]}})
        Fin.update({item : temp})


    return Fin

def ShopGoodRetT1(Container,lan):
    TFin = {}
    for Shop in Container:
        Fin = {}
        for item in Container[Shop]:

            temp = {}
            Target = Container[Shop][item]
            temp.update({"Name" : GDBT.conv(Target["Temp"],lan)})
            temp.update({"Count" : Target["Count"]})
            temp.update({"Limit" : Target["Limit"]})
            if Target["Cost"] != []:
                temp.update({"Cost" : {GDBT.conv(Target["Cost"][0],lan) : Target["Cost"][1]}})

            Fin.update({item : temp})
        TFin.update({Shop : Fin})


    return TFin

def ShopGoodRetT2(Container,lan):
    Fin = {}
    Num = -1
    BC = ""
    TFin = {}
    for item in Container:
            #if TagMap["Artifacts"][item]["Ban"] and Bantoggle:
            #continue

        temp = {}
        Target = Container[item]
        temp.update({"Name" : GDBT.conv(Target["Temp"],lan)})
        temp.update({"Count" : Target["Count"]})
        temp.update({"Limit" : Target["Limit"]})
        if Target["Cost"] != []:
            temp.update({"Cost" : {GDBT.conv(Target["Cost"][0],lan) : Target["Cost"][1]}})

        if Num > -1 and BC != Target["SortLevel"]:
            BC = Target["SortLevel"]
            TFin.update({Num : Fin})
            Fin = {}
            Num+=1
        if Num == -1:
            BC = Target["SortLevel"]
            Num+=1


        Fin.update({item : temp})



    if Num > 0:
        TFin.update({Num : Fin})
        return TFin
    else:
        return Fin

def ShopMapper(lan,Out):
    fin = {}

    for Cat in ShopMap:
        if Cat in ShopLink["Names"]:
            Nam = ShopData[ShopLink["Names"][Cat]]["ShopType"]
        elif Cat in ShopData :
            Nam = ShopData[Cat]["ShopType"]
        else:
            Nam = Cat
        fin.update({Nam : {}})

        T1 =  list(ShopMap[Cat].keys())[0]
        T0 = list(ShopMap[Cat][T1].keys())[0]

        if Nam in EventShops:
            Temp = ShopGoodRetT2(ShopMap[Cat],lan)
        elif T0 != "Temp":
            Temp = ShopGoodRetT1(ShopMap[Cat],lan)
        else:
            Temp = ShopGoodRetT0(ShopMap[Cat],lan)

        fin[Nam].update(Temp)


    with open(Out, "w") as write_file:
        json.dump(fin, write_file, indent=4)

def CharMapper(lan,out):
    fin = {}
    for item in CharMap:
        if TagMap["Characters"][item]["Ban"]:# and Bantoggle:
            continue
        Target = CharMap[item]
        temp = {
                "Name": GDBT.conv(Target["Name"],lan),
                "Title": GDBT.conv(Target["Title"],lan),
                "Element": GDBT.conv(Target["Element"],lan),
                "Affiliation": GDBT.conv(Target["Origin"],lan),
                "Rarity": rar[Target["Rarity"]],
                "Class": cwea[Target["Weapon"]],
                "Constellation": GDBT.conv(Target["Constellation"],lan),
                "Intro": GDBT.conv(Target["Intro"],lan),
            }
        if item in AvatarHeroEntityData:
            Nat = []
            for Var in Target["Normal Attack"]:
                Nat.append({"Normal Atk": [GDBT.conv(Var["Name"],lan),GDBT.conv(Var["Description"],lan),Var["Table Data"],Var["Total"],Var["Upgrade"]]})

            ESki = []
            for Var in Target["Elemental Skill"]:
                pass
                try:
                    ESki.append({"Elemental Skill": [GDBT.conv(Var["Name"],lan),GDBT.conv(Var["Description"],lan),Var["Table Data"],Var["Total"],Var["Upgrade"]]})
                except:
                    ESki.append(True)

            EBur = []
            for Var in Target["Elemental Burst"]:
                pass
                try:
                    EBur.append({"Elemental Burst": [GDBT.conv(Var["Name"],lan),GDBT.conv(Var["Description"],lan),Var["Table Data"],Var["Total"],Var["Upgrade"]]})
                except:
                    EBur.append(True)


            for Var in Nat:
                TUpgrade = []
                for Barrier in Var["Normal Atk"][4]:
                    TLev = {}
                    for Mat in Barrier[1]:
                        TLev.update({GDBT.conv(Mat["Id"],lan) : Mat["Count"]})
                    TUpgrade.append([Barrier[0],TLev])
                Var["Normal Atk"][4] = TUpgrade
            for Var in ESki:
                if Var:
                    continue
                Var["Elemental Skill"][4] = TUpgrade
            for Var in EBur:
                if Var:
                    continue
                Var["Elemental Burst"][4] = TUpgrade

            for Var in Nat:
                TUpgrade = {}
                for MatReq in  Var["Normal Atk"][3]:
                    TUpgrade.update({GDBT.conv(MatReq,lan) :  Var["Normal Atk"][3][MatReq]})
                Var["Normal Atk"][3] = TUpgrade
            for Var in ESki:
                if Var:
                    continue
                Var["Elemental Skill"][3] = TUpgrade
            for Var in EBur:
                if Var:
                    continue
                Var["Elemental Burst"][3] = TUpgrade

            Const = []
            PassTal = []
            for Var in Target["Talents"]:
                Constellations = {}
                Passives = []
                for talnum in [1,2,3,4,5,6]:
                    ntalnum = str(talnum)
                    Constellations.update({ntalnum :[GDBT.conv(Var[ntalnum]["Name"],lan),GDBT.conv(Var[ntalnum]["Description"],lan)]})
                Const.append(Constellations)
            for Var in Target["Passives"]:
                for TempPas in Var:
                    if TempPas != ["",""]:
                        Passives.append([GDBT.conv(TempPas[0],lan),GDBT.conv(TempPas[1],lan)])
                    else:
                        Passives.append(TempPas)
                PassTal.append(Passives)

            temp.update({"Normal Attack" : Nat})
            temp.update({"Elemental Skill" : ESki})
            temp.update({"Elemental Burst" : EBur})
            temp.update({"Passives" : Const})
            temp.update({"Talents" : PassTal})

        else:

            temp.update({"Normal Atk": [GDBT.conv(Target["Normal Attack"]["Name"],lan),GDBT.conv(Target["Normal Attack"]["Description"],lan),Target["Normal Attack"]["Table Data"],Target["Normal Attack"]["Total"],Target["Normal Attack"]["Upgrade"]]})

            temp.update({"Elemental Skill": [GDBT.conv(Target["Elemental Skill"]["Name"],lan),GDBT.conv(Target["Elemental Skill"]["Description"],lan),Target["Elemental Skill"]["Table Data"],Target["Elemental Skill"]["Total"],Target["Elemental Skill"]["Upgrade"]]})

            temp.update({"Elemental Burst": [GDBT.conv(Target["Elemental Burst"]["Name"],lan),GDBT.conv(Target["Elemental Burst"]["Description"],lan),Target["Elemental Burst"]["Table Data"],Target["Elemental Burst"]["Total"],Target["Elemental Burst"]["Upgrade"]]})
            TUpgrade = []
            for Barrier in temp["Normal Atk"][4]:
                TLev = {}
                for Mat in Barrier[1]:
                    TLev.update({GDBT.conv(Mat["Id"],lan) : Mat["Count"]})
                TUpgrade.append([Barrier[0],TLev])

            temp["Normal Atk"][4] = TUpgrade
            temp["Elemental Skill"][4] = TUpgrade
            temp["Elemental Burst"][4] = TUpgrade
            TUpgrade = {}
            for MatReq in  temp["Normal Atk"][3]:
                TUpgrade.update({GDBT.conv(MatReq,lan) :  temp["Normal Atk"][3][MatReq]})
            temp["Normal Atk"][3] = TUpgrade
            temp["Elemental Skill"][3] = TUpgrade
            temp["Elemental Burst"][3] = TUpgrade
            Constellations = {}
            for talnum in [1,2,3,4,5,6]:
                ntalnum = str(talnum)
                Constellations.update({ntalnum :[GDBT.conv(Target["Talents"][ntalnum]["Name"],lan),GDBT.conv(Target["Talents"][ntalnum]["Description"],lan)]})
            Passives = []
            for TempPas in Target["Passives"]:
                if TempPas != ["",""]:
                    Passives.append([GDBT.conv(TempPas[0],lan),GDBT.conv(TempPas[1],lan)])
                else:
                    Passives.append(TempPas)
            temp.update({"Talents" : Constellations})
            temp.update({"Passives" : Passives})


        History = {}
        for stonum in [0,1,2,3,4,5]:
            nstonum = str(stonum)
            History.update({nstonum :[GDBT.conv(Target["Story"][nstonum]["Name"],lan),GDBT.conv(Target["Story"][nstonum]["Description"],lan)]})
        History.update({"Fave" :[GDBT.conv(Target["Story"]["Fave"]["Name"],lan),GDBT.conv(Target["Story"]["Fave"]["Description"],lan)]})
        History.update({"Focus" :[GDBT.conv(Target["Story"]["Focus"]["Name"],lan),GDBT.conv(Target["Story"]["Focus"]["Description"],lan)]})
        Tg = TagMap["Characters"][item]["Tags"]
        Tg.append(str(rar[Target["Rarity"]]))
        Tg.append(str(cwea[Target["Weapon"]]))
        Tg.append(GDBT.conv(Target["Element"],lan))
        temp.update({"Tags" : Tg})



        temp.update({"Story" : History})
        temp.update({"Stats" : Target["Stats"]})
        TAsc = []
        for Level in Target["Ascension"]:
            TLev = {}
            for Mat in Level[1]:
                TLev.update({GDBT.conv(Mat,lan) : Level[1][Mat]})
            TAsc.append([Level[0],TLev])
        
        NTotal = {}
        for MatReq in  Target["total"]:
            NTotal.update({GDBT.conv(MatReq,lan) :  Target["total"][MatReq]})
        temp.update({"Total" : NTotal})
    
        fin.update({GDBT.conv(Target["Name"],lan) : temp})

    fin2 = {}
    for item in sorted(fin.keys()):
        fin2.update({item : fin[item]})

    with open(out, "w") as write_file:
        json.dump(fin2, write_file, indent=4)

def WeapMapper(lan,out):
    fin = {}
    for item in WeapMap:
        if TagMap["Weapons"][item]["Ban"]:
            pass
        temp = {}
        temp.update({"Rarity" : WeapMap[item]["Rarity"]})
        temp.update({"Description" : GDBT.conv(WeapMap[item]["Description"],lan)})
        if WeapMap[item]["Class"] == "Pole":
            temp.update({"Class" : "Polearm"})
        else:
            temp.update({"Class" : WeapMap[item]["Class"]})
        temp.update({"Series" : WeapMap[item]["Series"]})
        try:
            temp.update({"Story" : GDBT.repla(BS["Weapons"][str(item)])})
        except:
            print(item+" Missing ")
        subtemp = {}        
        temp.update({"Substat Type" : GDBT.conv(WeapMap[item]["Substat Type"],lan)})
        for det in WeapMap[item]["Passive"]:
            subtemp.update({det :   GDBT.conv(WeapMap[item]["Passive"][det],lan) })
        temp.update({"Passive" : subtemp})
        temp.update({"Stats" : WeapMap[item]["Stats"]})
        temp.update({"Tags" : []})
        for tagitem in TagMap["Weapons"][item]["Tags"]:
            if tagitem in lan.keys():
                temp["Tags"].append(GDBT.conv(tagitem,lan))
            else:
                temp["Tags"].append(tagitem)
        temp["Tags"].append(str(temp["Rarity"]))
        temp["Tags"].append(temp["Class"])
        temp["Tags"].append(temp["Substat Type"])
        TAsc = []
        for Level in WeapMap[item]["Ascension"]:
            TLev = {}
            for Mat in Level[1]:
                TLev.update({GDBT.conv(GDBT.ItemNamRet(Mat["Id"]),lan) : Mat["Count"]})
            TAsc.append([Level[0],TLev])
        temp.update({"Ascension" : TAsc})
        NTotal = {}
        for MatReq in  WeapMap[item]["total"]:
            NTotal.update({GDBT.conv(GDBT.ItemNamRet(MatReq),lan) :  WeapMap[item]["total"][MatReq]})
        temp.update({"Total" : NTotal})
        #print(temp["Passive"]["1"])
        ref = []
        ref2 = []
        for PNum in ["1","2","3","4","5"]:
            ref.append(re.findall("\*\*(.*?)\*\*", temp["Passive"][PNum]))
        if item == "13405":
            print()
            pass
        for div in ref[0]:
            ref2.append([])
        for div in ref:
            count = 0
            for div2 in div:
                ref2[count].append("**"+div2+"**")
                count = count+1
        Nref = temp["Passive"]["1"]
        for div in ref2:
            index = ref2.index(div)
            rep = "/".join(div)
            if "%" in rep:
                rep  = rep.replace("%","")+"%"
            Nref = Nref.replace("**"+ref[0][index]+"**",rep)
        temp["Passive"].update({"Refinement" : Nref})

        fin.update({GDBT.conv(WeapMap[item]["Name"],lan) : temp})
    sort = (fin.keys())
    final = {}
    for item in sort:
        final.update({item : fin[item]})
    if "CHS" in out:
        with open(out, "w",encoding="utf-8") as write_file:
            json.dump(fin, write_file, indent=4, ensure_ascii=False)
    else:
        with open(out, "w") as write_file:
            json.dump(fin, write_file, indent=4)

FTyp = {"UI_Buff_Item_Recovery_HpAdd" : "Burst Restorative",
        "UI_Buff_Item_Recovery_HpAddAll" : "Regenerative",
        "UI_Buff_Item_Recovery_Revive" : "Revivicative ",
        "UI_Buff_Item_Other_SPAdd" : "Stamina Restore",
        "UI_Buff_Item_Other_SPReduceConsume" : "Stamina Cost Down ",
        "UI_Buff_Item_Atk_Add" : "Base Atk Boost",
        "UI_Buff_Item_Atk_CritRate" : "Crit Rate Boost",
        "UI_Buff_Item_Climate_Heat" : "Warming",
        "UI_Buff_Item_Def_Resistance_Fire" : "Pyro Resist",
        "UI_Buff_Item_Def_Resistance_Water" : "Hydro Resist",
        "UI_Buff_Item_Def_Resistance_Wind" : "Anemo Resist",
        "UI_Buff_Item_Def_Resistance_Rock" : "Geo Resist",
        "UI_Buff_Item_Def_Resistance_Ice" : "Cryo Resist",
        "UI_Buff_Item_Def_Resistance_Elect" : "Electro Resist",
        "UI_Buff_Item_Def_Resistance_Grass" : "Dendro Resist",
        "UI_Buff_Item_Atk_ElementHurt_Fire" : "Pyro Damage",
        "UI_Buff_Item_Atk_ElementHurt_Water" : "Hydro Damage",
        "UI_Buff_Item_Atk_ElementHurt_Wind" : "Anemo Damage",
        "UI_Buff_Item_Atk_ElementHurt_Rock" : "Geo Damage",
        "UI_Buff_Item_Atk_ElementHurt_Ice" : "Cryo Damage",
        "UI_Buff_Item_Atk_ElementHurt_Elect" : "Electro Damage",
        "UI_Buff_Item_Atk_ElementHurt_Grass" : "Dendro Damage",
        "UI_Buff_Item_Climate_Heat" : "Warming",
        "UI_Buff_Item_Def_Add" : "Defensive",
        "" : "None",
        " " : "None",
        }

WoodLoc = {"101301" : "2872978728" , "101302" : "1096582992" , "101303" : "2006151536" , "101304" : "2623672824" , "101305" : "3824301888" , "101306" : "","101307" : "3876403736" ,  "101308" : "4041469080" , }
def ItemMapper(lan,out):
    fin = {}
    fin.update({"Food" : {}})
    nmap = ItemMap["Food"]
    checked = ["108000","108147"]
    for item in RecipeMapData:
        fintemp = {}
        Variants = []
        for food in RecipeMapData[item]["Variants"]:
            temp = {}

            if TagMap["Items"][food]["Ban"]:
                continue
            if food not in nmap:
                print(str(food)+" Food Missing")
                food = "108005"
            FIDS = nmap[food]
            temp.update({"Name" : GDBT.conv(FIDS["Item Name"],lan)})
            temp.update({"Description" : GDBT.conv(FIDS["Item Desc"],lan)})
            temp.update({"Effect" : GDBT.conv(FIDS["Effect Desc"],lan)})
            checked.append(food)
            Variants.append(temp)
        fintemp.update({"Variants" : Variants})
        fintemp.update({"Recipe" : RecipeMapData[item]["Materials"]})
        for mat in fintemp["Recipe"]:
            mat[0] = GDBT.conv(mat[0],lan)
            pass
        fintemp.update({"Unique" : True})
        fintemp.update({"Category" : GDBT.conv(RecipeMapData[item]["Type"],lan)})
        try:
            fintemp.update({"Type" : FTyp[nmap[RecipeMapData[item]["Variants"][0]]["IC"]]})
        except:
            fintemp.update({"Type" : "Unkw"})
        if RecipeMapData[item]["Specialty"][0]:
            fintemp.update({"Specialty" : [True,GDBT.conv(CharMap[RecipeMapData[item]["Specialty"][1]]["Name"],lan)]})
        else:
            fintemp.update({"Specialty" : [False]})

        if Variants == []:
            continue

        fin["Food"].update({GDBT.conv(RecipeMapData[item]["Name"],lan) :  fintemp  })



    fin.update({"Potion" : {}})
    for item in nmap:
        if (TagMap["Items"][item]["Ban"] or item in checked) and Bantoggle:
            continue
        temp = {}
        temp.update({"Name" : GDBT.conv(nmap[item]["Item Name"],lan)})
        temp.update({"Description" : GDBT.conv(nmap[item]["Item Desc"],lan)})
        temp.update({"Effect" : GDBT.conv(nmap[item]["Effect Desc"],lan)})
        Sou = []
        for SRC in nmap[item]["Sources"]:
            if GDBT.conv(SRC,lan) in [""]:
               continue
            Sou.append(GDBT.conv(SRC,lan))
        temp.update({"Sources" : Sou})
        temp.update({"Unique" : False})
        temp.update({"Type" : FTyp[nmap[item]["IC"]]})
        nam = GDBT.conv(nmap[item]["Item Name"],lan)

        if item == "701":
            fin["Potion"].update({item :  temp  })
        else:
            fin["Food"].update({nam :  temp  })
    

    fin.update({"Mats" : {}})
    fin.update({"Ascension" : {}})
    nmap = ItemMap["Ascension Materials"]
    ASCM = ["Brilliant Diamond","Bone Shard","Aerosiderite","Mist Veiled","from Guyun","Dandelion Gladiator","Boreal Wolf","Decarabian","Sacrificial Knife","Mist Grass","Chaos","Ley Line","Statuette","Horn","Arrowhead","Scroll","Mask","Slime","Gold","Diligence","Prosperity","Ballad","Nectar","Resistance","Freedom","Prithiva Topaz","Shivada Jade","Vayuda Turquoise","Vajrada Amethyst","Nagadus Emerald","Varunada Lazurite","Agnidus Agate"]
    for item in nmap:
        for tier in nmap[item]:
            if TagMap["Items"][tier]["Ban"] and Bantoggle:
                continue
            Cur_Tar = nmap[item][tier]
            temp = {}
            for aset in ASCM:
                if item == "111":
                    loc = "Fatui Insignia"
                elif item == "112":
                    loc = "Hoarder Insignia"
                elif aset.lower() in GDBT.conv(Cur_Tar["Item Name"],lan).lower():
                    loc = aset
                    break
                else:
                    loc = tier
            temp.update({"Description" : GDBT.conv(Cur_Tar["Item Desc"],lan)})
            temp.update({"Group" : loc})
            temp.update({"Characters" : []})
            temp.update({"Weapons" : []})
            temp.update({"Food Recipes" : []})
            temp.update({"Furnitures" : []})
            temp.update({"CharTalents" : []})
            Sou = []
            for SRC in Cur_Tar["Sources"]:
                if GDBT.conv(SRC,lan) in [""]:
                    continue
                Sou.append(GDBT.conv(SRC,lan))
            temp.update({"Sources" : Sou})
            fin["Mats"].update({GDBT.conv(Cur_Tar["Item Name"],lan) : temp})


    nmap = ItemMap["Materials"]
    for item in nmap:
        if TagMap["Items"][item]["Ban"] and Bantoggle:
            continue
        Cur_Tar = nmap[item]
        temp = {}
        temp.update({"Description" : GDBT.conv(Cur_Tar["Item Desc"],lan)})
        temp.update({"Group" : True})
        temp.update({"Characters" : []})
        temp.update({"Character Skills" : []})
        temp.update({"Food Recipes" : []})
        temp.update({"Weapons" : []})
        temp.update({"Furnitures" : []})
        temp.update({"CharTalents" : []})
        Sou = []
        for SRC in nmap[item]["Sources"]:
            if GDBT.conv(SRC,lan) in [""]:
               continue
            Sou.append(GDBT.conv(SRC,lan))
        temp.update({"Sources" : Sou})
        for rec in CombineData:
            frec = CombineData[rec]
            if int(item) == frec["ResultItemId"]:
                temp.update({"Recipe" : frec["MaterialItems"]})
                print(GDBT.conv(Cur_Tar["Item Name"]))
                break
        fin["Mats"].update({GDBT.conv(Cur_Tar["Item Name"],lan) : temp})

    nmap = ItemMap["Wood"]
    for item in nmap:
        if TagMap["Items"][item]["Ban"] and Bantoggle:
            continue
        Cur_Tar = nmap[item]
        temp = {}
        temp.update({"Description" : GDBT.conv(Cur_Tar["Item Desc"],lan)})
        temp.update({"Group" : True})
        temp.update({"Characters" : []})
        temp.update({"Character Skills" : []})
        temp.update({"Food Recipes" : []})
        temp.update({"Weapons" : []})
        temp.update({"Furnitures" : []})
        temp.update({"CharTalents" : []})
        Sou = []
        for SRC in nmap[item]["Sources"]:
            if GDBT.conv(SRC,lan) in [""]:
               continue
            Sou.append(GDBT.conv(SRC,lan))
        temp.update({"Sources" : Sou})
        temp.update({"Location" : GDBT.conv(WoodLoc[item],lan)})
        for rec in CombineData:
            frec = CombineData[rec]
            if int(item) == frec["ResultItemId"]:
                temp.update({"Recipe" : frec["MaterialItems"]})
                print(GDBT.conv(Cur_Tar["Item Name"]))
                break
        fin["Mats"].update({GDBT.conv(Cur_Tar["Item Name"],lan) : temp})

    fin.update({"Quest Items" : {}})
    nmap = ItemMap["Quest"]
    for item in nmap:
        if TagMap["Items"][item]["Ban"] and Bantoggle:
            continue
        Cur_Tar = nmap[item]
        temp = {}
        temp.update({"Description" : GDBT.conv(Cur_Tar["Item Desc"],lan)})
        temp.update({"Group" : True})
        Sou = []
        for SRC in nmap[item]["Sources"]:
            if GDBT.conv(SRC,lan) in [""]:
               continue
            Sou.append(GDBT.conv(SRC,lan))
        temp.update({"Sources" : Sou})
        fin["Quest Items"].update({GDBT.conv(Cur_Tar["Item Name"],lan) : temp})

    fin.update({"Glider" : {}})
    nmap = ItemMap["Wings"]
    for item in nmap:
        if TagMap["Items"][item]["Ban"] and Bantoggle:
            continue
        Cur_Tar = nmap[item]
        temp = {}
        temp.update({"Description" : GDBT.conv(Cur_Tar["Item Desc"],lan)})


        if str(item) not in BS["Gliders"]:
            temp.update({"Story" : GDBT.repla(BS["Gliders"][str(item)])})
        else:        
            temp.update({"Story" : GDBT.repla(BS["Gliders"][str(item)])})

        temp.update({"Group" : True})
        Sou = []
        for SRC in nmap[item]["Sources"]:
            if GDBT.conv(SRC,lan) in [""]:
               continue
            Sou.append(GDBT.conv(SRC,lan))
        temp.update({"Sources" : Sou})
        fin["Glider"].update({GDBT.conv(Cur_Tar["Item Name"],lan) : temp})

    fin.update({"Costumes" : {}})
    nmap = ItemMap["Costumes"]
    for item in nmap:
        if TagMap["Items"][item]["Ban"] and Bantoggle:
            continue
        Cur_Tar = nmap[item]
        temp = {}
        temp.update({"Description" : GDBT.conv(Cur_Tar["Item Desc"],lan)})


        if str(item) not in BS["Costume"]:
            temp.update({"Story" : GDBT.repla(BS["Costume"][str(item)])})
        else:        
            temp.update({"Story" : GDBT.repla(BS["Costume"][str(item)])})

        temp.update({"Group" : True})
        Sou = []
        for SRC in nmap[item]["Sources"]:
            if GDBT.conv(SRC,lan) in [""]:
               continue
            Sou.append(GDBT.conv(SRC,lan))
        temp.update({"Sources" : Sou})
        fin["Costumes"].update({GDBT.conv(Cur_Tar["Item Name"],lan) : temp})

    fin.update({"Gadgets" : {}})
    nmap = ItemMap["Gadgets"]
    for item in nmap:
        if TagMap["Items"][item]["Ban"] and Bantoggle:
            continue
        temp = {}
        Cur_Tar = nmap[item]
        temp.update({"Description" : GDBT.conv(Cur_Tar["Item Desc"],lan)})
        Sou = []
        for SRC in Cur_Tar["Sources"]:
            if GDBT.conv(SRC,lan) in [""]:
               continue
            Sou.append(GDBT.conv(SRC,lan))
            temp.update({"Sources" : Sou})
        fin["Gadgets"].update({GDBT.conv(Cur_Tar["Item Name"],lan) : temp})

    fin.update({"Furniture Recipes" : {}})
    nmap = ItemMap["Furniture Recipes"]
    for item in nmap:
        if TagMap["Items"][item]["Ban"] and Bantoggle:
            continue
        Cur_Tar = nmap[item]
        temp = {}
        temp.update({"Description" : GDBT.conv(Cur_Tar["Item Desc"],lan)})
        Sou = []
        for SRC in Cur_Tar["Sources"]:
            if GDBT.conv(SRC,lan) in [""]:
               continue
            Sou.append(GDBT.conv(SRC,lan))
            temp.update({"Sources" : Sou})
        for rec in CombineData:
            frec = CombineData[rec]
            if int(item) == frec["ResultItemId"]:
                temp.update({"Recipe" : frec["MaterialItems"]})
                print(GDBT.conv(Cur_Tar["Item Name"]))
                break
        fin["Furniture Recipes"].update({GDBT.conv(Cur_Tar["Item Name"],lan) : temp})

    fin.update({"Catalysts" : {}})
    nmap = ItemMap["Variable"]
    for item in nmap:
        if TagMap["Items"][item]["Ban"] and Bantoggle:
            continue
        temp = {}
        temp.update({"Description" : GDBT.conv(nmap[item]["Item Desc"],lan)})
        Sou = []
        for SRC in nmap[item]["Sources"]:
            if GDBT.conv(SRC,lan) in [""]:
               continue
            Sou.append(GDBT.conv(SRC,lan))
            temp.update({"Sources" : Sou})
        for rec in CombineData:
            frec = CombineData[rec]
            if int(item) == frec["ResultItemId"]:
                temp.update({"Recipe" : frec["MaterialItems"]})
                print(GDBT.conv(nmap[item]["Item Name"]))
                break
        fin["Catalysts"].update({GDBT.conv(nmap[item]["Item Name"],lan) : temp})

    for Weapon in WeapMap:
        for mat in WeapMap[Weapon]["total"]:
            if TagMap["Weapons"][Weapon]["Ban"] == False:
                nam = GDBT.conv(Weapon,lan)
                ItemNam = GDBT.conv(GDBT.ItemNamRet(mat),lan)
                fin["Mats"][ItemNam]["Weapons"].append([GDBT.conv(str(WeapMap[Weapon]["Name"]),lan),WeapMap[Weapon]["total"][mat]])

    for Character in CharMap:
        if Character in AvatarHeroEntityData:
            continue
        CName = GDBT.conv(CharMap[Character]["Name"],lan)
        if TagMap["Characters"][Character]["Ban"]:
            continue
        for mat in CharMap[Character]["total"]:
            Name = GDBT.conv(mat,lan)
            CName = GDBT.conv(CharMap[Character]["Name"],lan)
            Tot = CharMap[Character]["total"][mat]
            if TagMap["Characters"][Character]["Ban"] == False and Name in fin["Mats"]:
                fin["Mats"][Name]["Characters"].append([CName,Tot])

        for mat in CharMap[Character]["Normal Attack"]["Total"]:
            Name = GDBT.conv(mat,lan)
            Tot = CharMap[Character]["Normal Attack"]["Total"][mat]
            if TagMap["Characters"][Character]["Ban"] == False and Name in fin["Mats"]:
                fin["Mats"][Name]["CharTalents"].append([CName,Tot])
    """
    for Character in CharMap:
        for mat in CharMap[Character]["Normal Attack"]["Total"]:
            if TagMap["Characters"][Character]["Ban"] == False and mat in fin["Mats"]:
                fin["Mats"][mat]["CharTalents"].append([GDBT.conv(str(CharMap[Character]["Name"]),lan),CharMap[Character]["total"][mat]])
    """
    for Food in RecipeMapData:

        for mat in RecipeMapData[Food]["Materials"]:
            if RecipeMapData[Food]["Variants"][0] not in TagMap["Items"]:
                fin["Mats"][mat[0]]["Food Recipes"].append([GDBT.conv(str(RecipeMapData[Food]["Name"]),lan),mat[1]])
            elif TagMap["Items"][RecipeMapData[Food]["Variants"][0]]["Ban"] == False and mat[0] in fin["Mats"]:
                fin["Mats"][mat[0]]["Food Recipes"].append([GDBT.conv(str(RecipeMapData[Food]["Name"]),lan),mat[1]])

    for Furnishing in FurnMap["Pieces"]:

        FName = GDBT.conv(FurnMap["Pieces"][Furnishing]["Name"],lan)
        if TagMap["Furniture"][Furnishing]["Ban"]:
            continue
        Cur_Tar = FurnMap["Pieces"][Furnishing]
        if Cur_Tar["Crafting"] == {}:
            continue

        for mat in Cur_Tar["Crafting"]["Recipe"]:
            Name = GDBT.conv(mat,lan)
            Tot = Cur_Tar["Crafting"]["Recipe"][mat]
            if Name in fin["Mats"]:
                fin["Mats"][Name]["Furnitures"].append([FName,Tot])


    with open(out, "w") as write_file:
        json.dump(fin, write_file, indent=4)

#DD = GDBT.Stageloader("DialogueData.json")
#ND = GDBT.Stageloader("NPCData.json")
#BQD = GDBT.Stageloader("QuestData.json")
#QCD = GDBT.Stageloader("QuestChapterData.json")

def delver(Hole,lan):
    End = []
    #if type(Hole) == int:
        #Hole = str(Hole)
    for item in Hole:
        if type(item) == list:
            for Branch in item:
                End.append(delver(Branch,lan))
            
        else:
            DDL = DD[str(item)]
            NPCN = DDL["TalkRole"]
            if NPCN["Id"] in ["","主角","玩家","0","****"]:
                if "Type" in NPCN:
                    if NPCN["Type"] == "TALK_ROLE_MATE_AVATAR":
                        Name = "Sibling"
                    else:
                        Name = "Traveler"
                else:
#            if NPCN["Type"] in ["TALK_ROLE_PLAYER"]:
                    Name = "Traveler"
            else:
                Name = GDBT.conv(ND[NPCN["Id"]]["NameTextMapHash"],lan)
            End.append(Name+" : "+GDBT.conv(DDL["TalkContentTextMapHash"],lan))
    return(End)

def QuestMapper(lan,Out):
    fin = {}
    for MQuest in QuestMap:
        CQ = QuestMap[MQuest]
        temp = {}
        temp.update({"Name" : GDBT.conv(CQ["Title"],lan)})
        temp.update({"Desc" : GDBT.conv(CQ["Desc"],lan)})
        Steps = {}
        for Sub in CQ["Stages"]:
            Steps.update({Sub : GDBT.conv(CQ["Stages"][Sub]["Directive"],lan)})
        temp.update({"Stages" : Steps})
        Rew = []
        for gifts in CQ["Rewards"]:
            Rew.append(GDBT.RewardTrans(gifts,lan))
        temp.update({"Rewards" : Rew})
        fin.update({MQuest :  temp  })
    with open(Out, "w") as write_file:
        json.dump(fin, write_file, indent=4)

def ChapterMapper(lan,Out):
    fin = {}
    Cfin = {}
    for Quest in QuestMap:
        QC = QuestMap[Quest]
        Iden = "Null"
        if QC["Chapter"] != "Null":
            Iden = QC["Chapter"]
        elif QC["Series"] != "Null":
            Iden = QC["Series"]
        if Iden not in fin:
            fin.update({Iden : {"Contains" : []}})
        fin[Iden]["Contains"].append([Quest,GDBT.conv(QC["Title"],lan)])
        pass
        #Nam = GDBT.conv(QCD[Quest]["ChapterNumTextMapHash"],lan)
        #ChapNam = GDBT.conv(QCD[Quest]["ChapterTitleTextMapHash"],lan)
    for Series in fin:
        if str(Series) not in ChapterData:
            print(Series)
            continue
        fin[Series].update({"Name" : GDBT.conv(ChapterData[str(Series)]["ChapterNumTextMapHash"],lan)+" - "+GDBT.conv(ChapterData[str(Series)]["ChapterTitleTextMapHash"],lan)})

    """
    for Chapter in Cfin:
        Chap = Cfin[Chapter]
        for item in range(Chap["Begin"],Chap["End"]):
            if str(item) in BQD:
                Cfin[Chapter]["Contains"].update({item : ""})
    """
    if "CHS" in Out:
        with open(Out, "w",encoding="utf-8") as write_file:
            json.dump(fin, write_file, indent=4, ensure_ascii=False)
    else:
        with open(Out, "w") as write_file:
            json.dump(fin, write_file, indent=4)

def SearchMapper(CData,AData,WData,IData,FData,Out):
    CData = GDBT.Stageloader(CData,4)
    AData = GDBT.Stageloader(AData,4)
    WData = GDBT.Stageloader(WData,4)
    FuData = GDBT.Stageloader(FData,4)
    IData = GDBT.Stageloader(IData,4)
    MData = IData["Mats"]
    FData = IData["Food"]
    FPData = FuData["Pieces"]
    FSData = FuData["Sets"]
    newdata = {"Weapon" : {},
                "Character" : {},
                "Artifact" : {},
                "Piece" : {},
                "Food" : {},
                "Furniture" : {},
                "Sets" : {},
                "Mats" : {}
    }

    SWKeys = sorted(WData.keys())
    id = 0
    for item in SWKeys:
        newdata["Weapon"][item]= {
                        "NID": id,
                        "Tags" : WData[item]["Tags"]
        }
        id+=1

    SCKeys = sorted(CData.keys())
    id = 0
    for item in SCKeys:
        newdata["Character"][item]= {
                        "NID": id,
                        "Tags" : CData[item]["Tags"]
        }
        id+=1

    SAKeys = sorted(AData.keys())
    id = 0
    idp = 0
    for item in SAKeys:
        newdata["Artifact"][SAKeys[id]]= {
                        "NID": id
                        }
        for pie in AData[item]["Set Pieces"]:
            newdata["Piece"][AData[item]["Set Pieces"][pie][0]] = {"NID" : idp,
                                                                "Set" : item,
                                                                "Part" : pie}
            idp+=1

        id+=1

    SFKeys = sorted(FData.keys())
    id = 0
    for item in SFKeys:
        newdata["Food"][item]= {
                        "NID": id
        }
        id+=1

    SMKeys = list(MData.keys())
    id = 0
    for item in SMKeys:
        newdata["Mats"][item]= {
                        "NID": id
        }
        id+=1

    SFPKeys = sorted(FPData.keys())
    id = 0
    for item in SFPKeys:
        newdata["Furniture"][item]= {
                        "NID": id
        }
        id+=1

    SFSKeys = sorted(FSData.keys())
    id = 0
    for item in SFSKeys:
        newdata["Sets"][item]= {
                        "NID": id
        }
        id+=1

    with open(Out, "w") as write_file:
        json.dump(newdata, write_file,indent =4)

def main():
    TagRevitializer()
    Languages = ["EN","CHT","CHS","ES"]

    for Lang in Languages:
        GDBT.ExC(os.path.join(Stage_4, Lang))
        LangSource = GDBT.Stageloader("TextMap"+Lang+".json","L")
        ArtifOut = os.path.join(Stage_4, Lang,"Artif_"+Lang+".json")
        CharOut = os.path.join(Stage_4, Lang,"Char_"+Lang+".json")
        SearchOut = os.path.join(Stage_4, Lang,"Search_"+Lang+".json")
        WeapOut = os.path.join(Stage_4, Lang,"Weap_"+Lang+".json")
        ItemOut = os.path.join(Stage_4, Lang,"Item_"+Lang+".json")
        QuestOut = os.path.join(Stage_4, Lang,"Quest_"+Lang+".json")
        FurnOut = os.path.join(Stage_4, Lang,"Furn_"+Lang+".json")
        ChapOut = os.path.join(Stage_4, Lang,"Chapter_"+Lang+".json")
        ShopOut = os.path.join(Stage_4, Lang,"Shop_"+Lang+".json")
        CharMapper(LangSource,CharOut)
        ArtifMapper(LangSource,ArtifOut)
        WeapMapper(LangSource,WeapOut)
        ItemMapper(LangSource,ItemOut)
        FurnMapper(LangSource,FurnOut)
        ShopMapper(LangSource,ShopOut)
        ChapterMapper(LangSource,ChapOut)
        QuestMapper(LangSource,QuestOut)
        SearchMapper(CharOut,ArtifOut,WeapOut,ItemOut,FurnOut,SearchOut)

def Xia():
    fin = {}
    Dat = GDBT.Stageloader("ActivitySalesmanRewardMatchConfigData.json",1)
    for item in Dat:
        Cur = Dat[item]
        fin.update({GDBT.conv(Cur["BoxNameTextMapHash"]) : GDBT.RewardTrans(Cur["RewardID"])})
    with open("XiaBoxes.json", "w") as write_file:
        json.dump(fin, write_file,indent =4)

def Hakto():
    FurnEN = GDBT.Loader(os.path.join(Stage_4, "EN","Furn_EN.json"))
    End = []
    for item in FurnEN:
        Target = FurnEN[item]
        for mat in Target["Crafting"]["Recipe"]:
            End.append(mat)
            #print (mat)
        #pass
    End = set(End)
    End = list(End)
    print(End)

#        print(item)
if __name__ == "__main__":
    #MQD = GDBT.Stageloader("MainQuestData.json",1)
    #QD = GDBT.Stageloader("QuestData.json",1)
    #print("Main Quest Num = "+str(len(MQD)))
    #print("Sub Quest Num = "+str(len(QD)))
    
    #TagRevitializer()
    #Xia()
    main()
    #Hakto()