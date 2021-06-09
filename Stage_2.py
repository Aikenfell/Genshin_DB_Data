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
Itemdex = os.path.join(Out_Files, "ItemEN.json")
langpath = os.path.join(Remapped_Data, "TextEN.json")
CharOut = os.path.join(Out_Files, "CharTables.json")
ChatOut = os.path.join(Out_Files, "RawDiag.json")

Stage_0 = os.path.join(mydir, "Stage_0")
Stage_1 = os.path.join(mydir, "Stage_1")
Stage_2 = os.path.join(mydir, "Stage_2")

AvatarData = GDBT.Stageloader("AvatarData.json",1)
AvatarPromoteData = GDBT.Stageloader("AvatarPromoteData.json",1)
AvatarCurveData = GDBT.Stageloader("AvatarCurveData.json",1)
AvatarPromoteData = GDBT.Stageloader("AvatarPromoteData.json",1)
AvatarSkillDepotData = GDBT.Stageloader("AvatarSkillDepotData.json",1)
ManualTextMap = GDBT.Stageloader("ManualTextMapConfigData.json",1)
ProudSkillData = GDBT.Stageloader("ProudSkillData.json",1)
AvatarSkillData = GDBT.Stageloader("AvatarSkillData.json",1)
WeaponData = GDBT.Stageloader("WeaponData.json",1)
WeaponPromoteData = GDBT.Stageloader("WeaponPromoteData.json",1)
WeaponCurveData = GDBT.Stageloader("WeaponCurveData.json",1)
MaterialData = GDBT.Stageloader("MaterialData.json",1)
CookRecipeData = GDBT.Stageloader("CookRecipeData.json",1)
CookBonusData = GDBT.Stageloader("CookBonusData.json",1)
DialogData = GDBT.Stageloader("DialogData.json",1)
#DD = GDBT.Stageloader("DialogData.json",1)
TalkData = GDBT.Stageloader("TalkData.json",1)
#QuestCodexData = GDBT.Stageloader("QuestCodexData.json",1)
Lang_EN = GDBT.Stageloader("TextMapEN.json","L")
#ItemEN = GDBT.Stageloader(Itemdex)
AvatarHeroEntityData = GDBT.Stageloader("AvatarHeroEntityData.json",1)

 
def AtkTableMaker(unit,SDID,GID,type=0):
    try:
        TableID = str(AvatarSkillData[GID]["ProudSkillGroupId"])
    except:
        return []
    End = [[]]
    ValT = ProudSkillData[TableID]
    for level in GDBT.ranger(0,15):
        Attrs = []
        PIDs = []
        Values = []
        Dets = []

        for Param in ValT[level]["ParamDescList"]:
            if GDBT.conv(Param) != "":
                Lang_EN[str(Param)] = Lang_EN[str(Param)].replace("#{LAYOUT_MOBILE#Tapping}{LAYOUT_PC#Press}{LAYOUT_PS#Press}","Tap")
                temp = Lang_EN[str(Param)].split("|")
                Attrs.append(temp[0])
                Values.append(temp[1])
                PIDs.append(re.findall("{(.*?)}", temp[1]))
                tloc = []
                te = re.findall("{(.*?)}", temp[1])
                for det in te:
                    tloc.append([int(det[5])-1,det.split(":")[1]])
                Dets.append(tloc)

        for param in PIDs:
            Valdex = PIDs.index(param)
            for val in param:
                Pardex = param.index(val)
                Loc = Dets[Valdex][Pardex][0]
                Typ = Dets[Valdex][Pardex][1]
                #Amber/Fischl Skill Fix


                if Typ == "P":
                    Values[Valdex] = Values[Valdex].replace("{"+PIDs[Valdex][Pardex]+"}",str(round(ValT[level]["ParamList"][Loc]*100))+"%")

                elif Typ == "F1":
                    Values[Valdex] = Values[Valdex].replace("{"+PIDs[Valdex][Pardex]+"}",str(round(ValT[level]["ParamList"][Loc],1)))
                elif Typ == "F1P":
                    Values[Valdex] = Values[Valdex].replace("{"+PIDs[Valdex][Pardex]+"}",str(round(ValT[level]["ParamList"][Loc]*100,1))+"%")
                elif Typ == "F2P":
                    Values[Valdex] = Values[Valdex].replace("{"+PIDs[Valdex][Pardex]+"}",str(round(ValT[level]["ParamList"][Loc]*100,2))+"%")
                elif Typ == "I":
                    Values[Valdex] = Values[Valdex].replace("{"+PIDs[Valdex][Pardex]+"}",str(round(ValT[level]["ParamList"][Loc])))
                elif Typ == "F":
                    Values[Valdex] = Values[Valdex].replace("{"+PIDs[Valdex][Pardex]+"}",str(round(ValT[level]["ParamList"][Loc]*100)))
                else:
                    print(Typ)
                    print(ValT[level]["ParamDescList"][Loc])
                    print(Attrs[Valdex])
                    print(Values[Valdex])
                    print("")

        End.append(Values)
    End[0] = Attrs
    FTemp = {}
    FTemp.update({"Name" : AvatarSkillData[GID]["NameTextMapHash"]})
    FTemp.update({"Description" : AvatarSkillData[GID]["DescTextMapHash"]})
    FTemp.update({"Img" : AvatarSkillData[GID]["SkillIcon"]})
    FTemp.update({"Table Data" : End})
    Evol = []
    Total = {}
    for level in ValT[1:10]:
        lv = level
        Tab = []
        for mat in lv["CostItems"]:
            if mat == {}:
                continue
            Tab.append({"Id" : GDBT.ItemNamRet(mat["Id"]),"Count" : mat["Count"]})
        Evol.append([lv["CoinCost"],Tab])

    for level in Evol:
        for mat in level[1]:
            if mat == {}:
                continue
            if mat["Id"] in Total:
                Total[mat["Id"]]+=mat["Count"]
            else:
                Total.update({mat["Id"] : mat["Count"]})
    FTemp.update({"Total" : Total})
    FTemp.update({"Upgrade" : Evol})
    return FTemp
    pass

def chartables():
    final = {}
    for item in AvatarData:
        Avatar = AvatarData[item]
        SNam = Avatar["IconName"].split("_")[-1]
        
        BaseHP = Avatar["HpBase"]
        HPCurve = Avatar["PropGrowCurves"][0]["GrowCurve"]
        
        BaseATK = Avatar["AttackBase"]
        ATKCurve = Avatar["PropGrowCurves"][1]["GrowCurve"]
        
        BaseDEF = Avatar["DefenseBase"]
        DEFCurve = Avatar["PropGrowCurves"][2]["GrowCurve"]
                
        BaseCRate = Avatar["Critical"]*100
        BaseCDmg = Avatar["CriticalHurt"]*100
        Table = AvatarPromoteData[str(Avatar["AvatarPromoteId"])]
        Maxes = []
        for items in GDBT.ranger(0,7):
            Maxes.append(Table[items]["UnlockMaxLevel"])
        
        HPBonuses = [0]
        for items in GDBT.ranger(1,7):
            HPBonuses.append(Table[items]["AddProps"][0]["Value"])

        ATKBonuses = [0]
        for items in GDBT.ranger(1,7):
            ATKBonuses.append(Table[items]["AddProps"][1]["Value"])

        DEFBonuses = [0]
        for items in GDBT.ranger(1,7):
            DEFBonuses.append(Table[items]["AddProps"][2]["Value"])
        SPEType = Lang_EN[str(ManualTextMap[Table[0]["AddProps"][3]["PropType"]]["TextMapContentTextMapHash"])]

        SPEBonuses = [0]
        for items in GDBT.ranger(1,7):
            try:
                if SPEType in ["Elemental Mastery"]:
                    SPEBonuses.append(math.trunc(Table[items]["AddProps"][3]["Value"]))
                else:
                    SPEBonuses.append(Table[items]["AddProps"][3]["Value"]*100)
            except:
                SPEBonuses.append(0)


        temp = [["Level","Base HP","Base ATK","Base DEF",SPEType]]
        Min = 0
        Bonus = 0
        HPBonus = HPBonuses[0]
        ATKBonus = ATKBonuses[0]
        DEFBonus = DEFBonuses[0]
        SPEBonus = SPEBonuses[0]
        for level in Maxes:

            index = Maxes.index(level)
            Max = level
            if index != 0:
                TempHP = math.floor(round(BaseHP,2)*round(AvatarCurveData[HPCurve][Min-1],2)+HPBonuses[index])
                TempAtk = math.floor(round(BaseATK,2)*round(AvatarCurveData[ATKCurve][Min-1],2)+ATKBonuses[index])
                TempDef = math.floor(round(BaseDEF,2)*round(AvatarCurveData[DEFCurve][Min-1],2)+DEFBonuses[index])
                if SPEType == "CRIT DMG":
                    TempSpe = round(SPEBonuses[index]+BaseCDmg,1)
                elif SPEType == "CRIT Rate":
                    TempSpe = round(SPEBonuses[index]+BaseCRate,1)
                else:
                    TempSpe = round(SPEBonuses[index],1)

                temp.append([str(Min)+"+",TempHP,TempAtk,TempDef,TempSpe])
            for intitem in GDBT.ranger(Min,Max):
                TempHP = math.trunc((BaseHP)*round(AvatarCurveData[HPCurve][intitem],2)+HPBonuses[index])
                TempAtk = math.trunc(round(BaseATK,2)*round(AvatarCurveData[ATKCurve][intitem],2)+ATKBonuses[index])
                TempDef = math.trunc(round(BaseDEF,2)*round(AvatarCurveData[DEFCurve][intitem],2)+DEFBonuses[index])
                if SPEType == "CRIT DMG":
                    TempSpe = round(SPEBonuses[index]+BaseCDmg,1)
                elif SPEType == "CRIT Rate":
                    TempSpe = round(SPEBonuses[index]+BaseCRate,1)
                else:
                    TempSpe = round(SPEBonuses[index],1)
    
                temp.append([str(intitem+1),TempHP,TempAtk,TempDef,TempSpe])
            Min = Max
        temp2 = {"Stats" : temp}
        temp2.update({"Helper" : SNam})
        temp2.update({"BonusType" : SPEType})
        temp2.update({"Name" : Avatar["NameTextMapHash"]})

        final.update({item : temp2})

    with open(GDBT.ExCI(Stage_2,"CharTables.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def normaltables():
    final = {}
    for unit in AvatarData:
        if unit in AvatarHeroEntityData:
            FTemp = []
            for element in AvatarData[unit]["CandSkillDepotIds"]:
                SDID = str(element)
                GID = str(AvatarSkillDepotData[SDID]["Skills"][0])
                FTemp.append(AtkTableMaker(unit,SDID,GID))

        else:
            SDID = str(AvatarData[unit]["SkillDepotId"])
            GID = str(AvatarSkillDepotData[SDID]["Skills"][0])
            FTemp = AtkTableMaker(unit,SDID,GID)
            #print("Here")
        final.update({unit : FTemp})

    with open(GDBT.ExCI(Stage_2,"NormalTables.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def skilltables():
    final = {}
    for unit in AvatarData:
        if unit in AvatarHeroEntityData:
            FTemp = []
            for element in AvatarData[unit]["CandSkillDepotIds"]:
                SDID = str(element)
                GID = str(AvatarSkillDepotData[SDID]["Skills"][1])
                FTemp.append(AtkTableMaker(unit,SDID,GID))

        else:
            SDID = str(AvatarData[unit]["SkillDepotId"])
            GID = str(AvatarSkillDepotData[SDID]["Skills"][1])
            FTemp = AtkTableMaker(unit,SDID,GID)
            #print("Here")
        final.update({unit : FTemp})

    with open(GDBT.ExCI(Stage_2,"SkillTables.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def bursttables():
    final = {}
    for unit in AvatarData:
        if "10000047" == unit:
            print("Here")
        if unit in AvatarHeroEntityData:
            FTemp = []
            for element in AvatarData[unit]["CandSkillDepotIds"]:
                SDID = str(element)
                try:
                    GID = str(AvatarSkillDepotData[SDID]["EnergySkill"])
                except:
                    FTemp.append([])
                    continue
                FTemp.append(AtkTableMaker(unit,SDID,GID))

        else:
            SDID = str(AvatarData[unit]["SkillDepotId"])
            try:
                GID = str(AvatarSkillDepotData[SDID]["EnergySkill"])
                FTemp = AtkTableMaker(unit,SDID,GID)
            except:
                FTemp = {}
            #print("Here")

        final.update({unit : FTemp})

    with open(GDBT.ExCI(Stage_2,"BurstTables.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def weapontables():
    final = {}
    c = []
    for item in WeaponData:
        tcheck = WeaponData[item]
        SNam = WeaponData[item]["Icon"].split("_")[-1]
        
        BaseMain = WeaponData[item]["WeaponProp"][0]["InitValue"]
        BaseCurve = WeaponData[item]["WeaponProp"][0]["Type"]
        try:
            SubMain = WeaponData[item]["WeaponProp"][1]["InitValue"]
            SubCurve = WeaponData[item]["WeaponProp"][1]["Type"]
            SubType = str(ManualTextMap[WeaponData[item]["WeaponProp"][1]["PropType"]]["TextMapContentTextMapHash"])
            RLev = WeaponData[item]["WeaponProp"][1]["PropType"]
            if RLev not in ["FIGHT_PROP_ELEMENT_MASTERY"]:
                SubMain = SubMain*100

        except:
            SubMain = 0
            SubCurve = WeaponData[item]["WeaponProp"][0]["Type"]
            SubType = "None"
            RLev = "None"
        Table = WeaponPromoteData[str(WeaponData[item]["WeaponPromoteId"])]
        Maxes = []
        for items in GDBT.ranger(0,len(Table)):
            Maxes.append(Table[str(items)]["UnlockMaxLevel"])
        
        MainBonuses = [0]
        for items in GDBT.ranger(1,len(Table)):
            MainBonuses.append(Table[str(items)]["Value"])



        temp = [["Level","Main","Sub"]]
        Min = 0
        Bonus = 0
        MainBonus = MainBonuses[0]
        for level in Maxes:

            index = Maxes.index(level)
            Max = level
            for intitem in GDBT.ranger(Min+1,Max+1):
                CurvValM = WeaponCurveData[str(intitem)][BaseCurve]
                CurvValS = WeaponCurveData[str(intitem)][SubCurve]
                TempMain = math.trunc((BaseMain*CurvValM)+MainBonuses[index])+1
                if RLev not in ["FIGHT_PROP_ELEMENT_MASTERY"]:
                    TempSub = round(SubMain*CurvValS,1)
                else:
                    TempSub = math.trunc(SubMain*CurvValS)
    
                temp.append([str(intitem),TempMain,TempSub])
            Min = Max
            if index != len(Table)-1:
                CurvValM = WeaponCurveData[str(Min)][BaseCurve]
                CurvValS = WeaponCurveData[str(Min)][SubCurve]
                TempMain = math.trunc((BaseMain*CurvValM)+MainBonuses[index+1])+1
                if RLev not in ["FIGHT_PROP_ELEMENT_MASTERY"]:
                    TempSub = round(SubMain*CurvValS,1)
                else:
                    TempSub = math.trunc(SubMain*CurvValS)

                temp.append([str(Min)+"+",TempMain,TempSub])


        FTemp = {}
        FTemp.update({"Type" : SubType})
        FTemp.update({"Stats" : temp})

        final.update({item : FTemp})

    with open(GDBT.ExCI(Stage_2,"WeaponTables.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def ilextractor():
    final = {}
    for item in MD:
        final.update({item : lang[str(MD[item]["NameTextMapHash"])]})
    with open("ItemEN.json", "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

FTyp = {"COOK_FOOD_ATTACK" : "1506899412","COOK_FOOD_DEFENSE" : "2585697844","COOK_FOOD_FUNCTION" : "526924292","COOK_FOOD_HEAL" : "339530060"}

def diver(Choi,merge):
    Poss = []
    for item in Choi:
        SubPoss = []
        SubPoss.append(["",item])
        Che = DD[str(item)]
        Nex = Che["NextDialogs"]
        while Nex != [] and Nex != [merge] and Nex != Choi:
            SubPoss.append(["",Nex[0]])
            Nex = DD[str(Nex[0])]["NextDialogs"]
        Poss.append(SubPoss)

    #print(Poss)
    return(Poss)


#I Hate Recursion So Imma Comment Here
#Nex = Next Dialog Set , Choi = Choices Passed To Reach This Point , Branch = Next Step In Flow
def Path_Flow(Nex,Choi=[],Branch=[]):
    #Base Overwrite
    #Base Case
    Amalgam = Choi+Nex#Compounds The Next Values And The Values Passed So Far To Prevent Infinite Looping
    if type(Nex) == list:
        if len(Nex) > 1:
            Paths = []
            Remerge = [ender(Nex)]
            for item in Nex:
                if str(item) not in DD:
                    continue
                StrDia = str(item)
                NextDia = DD[StrDia]["NextDialogs"]

                Paths.append(Path_Flow([item],Choi+Remerge))
            return([Paths]+Path_Flow(Remerge,Choi))
        elif len(Nex) == 1:
            if Nex[0] in Choi:
                #print(Nex[0])
                return Branch    
            if type(Nex[0]) == str:
                Nex[0] = int(Nex[0])
            StrDia = str(Nex[0])

            if StrDia not in DD:
                #print(StrDia)
                return Branch    
            NextDia = DD[StrDia]["NextDialogs"]
            return Nex+Path_Flow(NextDia,Amalgam)
        elif len(Nex) == 0:
            return []

def Path_EN(Nex,Choi=[],Branch=[]):
    #Base Overwrite
    #Base Case
    Amalgam = Choi+Nex#Compounds The Next Values And The Values Passed So Far To Prevent Infinite Looping
    if type(Nex) == list:
        if len(Nex) > 1:
            Paths = []
            Remerge = [ender(Nex)]
            for item in Nex:
                if str(item) not in DD:
                    continue
                StrDia = str(item)
                NextDia = DD[StrDia]["NextDialogs"]

                Paths.append(Path_Flow([item],Choi+Remerge))
            return([Paths]+Path_EN(Remerge,Choi))
        elif len(Nex) == 1:
            if Nex[0] in Choi:
                #print(Nex[0])
                return Branch    
            if type(Nex[0]) == str:
                Nex[0] = int(Nex[0])
            StrDia = str(Nex[0])

            if StrDia not in DD:
                #print(StrDia)
                return Branch    
            Tex = Lang_EN[str(DD[StrDia]["TalkRoleNameTextMapHash"])]+" : "+Lang_EN[str(DD[StrDia]["TalkContentTextMapHash"])]
            NextDia = DD[StrDia]["NextDialogs"]
            return [Tex]+Path_EN(NextDia,Amalgam)
        elif len(Nex) == 0:
            return []

def Full_Path(Nex,Choi=[],Branch=[]):
    #Base Overwrite
    #Base Case
    Amalgam = Choi+Nex#Compounds The Next Values And The Values Passed So Far To Prevent Infinite Looping
    if type(Nex) == list:
        if len(Nex) > 1:
            Paths = []
            Remerge = [ender(Nex)]
            #print(Choi)
            for item in Nex:
                if str(item) not in DD:
                    continue
                StrDia = str(item)
                NextDia = DD[StrDia]["NextDialogs"]

                Paths = Paths + Full_Path([item],Choi+Remerge)
            #print(Choi)
            return(Paths+Full_Path(Remerge,Choi))
        elif len(Nex) == 1:
            if Nex[0] in Choi:
                #print(Nex[0])
                return Branch    
            StrDia = str(Nex[0])

            if StrDia not in DD:
                #print(StrDia)
                return Branch    
            NextDia = DD[StrDia]["NextDialogs"]
            return Nex+Full_Path(NextDia,Amalgam)
        elif len(Nex) == 0:
            return []

def delver(Nex,Choi=[],Tree=[],PB=False,):
    #Base Overwrite
    #Base Case
    if Nex == [] or Nex in Choi or Nex in [[3760751],[10220346],[110120426],[112010209],[0]]:#Corrections [680000105->680000104]
        return Tree

    else:
        if len(Nex) == 1:
            if str(Nex[0]) not in DialogData:
                return Tree
            else:
                Tex = DialogData[str(Nex[0])]["NextDialogs"]
                return(Tree+delver(Tex,Choi+[Nex],[Nex[0]]))
        else:
            Pats = []
            for item in Nex:
                if str(item) not in DialogData:
                    continue
                Tex = DialogData[str(item)]["NextDialogs"]
                Pats.append(delver(Tex,Choi+[Nex],[item]))
            PTest = []
            NPats = []
            for line in Pats:
                for item in line:
                    PTest.append(item)        
            RM = False
            for item in PTest:
                if PTest.count(item) == len(Nex):
                    ReMerge = item
                    #print(ReMerge)
                    RM = True
                    break
            if 3960732 in Nex:
                print("Here")
            if RM:
                Pats = []
                for item in Nex:
                    Tex = DialogData[str(item)]["NextDialogs"]
                    Pats.append(delver(Tex,Choi+[Nex]+[[ReMerge]],[item]))
            if RM:    
                if type(ReMerge) == int:
                    Tex = DialogData[str(ReMerge)]["NextDialogs"]
                return (Tree+[Pats]+delver(Tex,Choi+[Nex]+[ReMerge],[ReMerge]))
            else:
                return (Tree+[Pats])
            #print(len(Nex))
            #"""
            """
            ReMerge = Nex
            Cha = False
            #print(len(NPats) == Pats)
  

            if ReMerge == "180000517":
                print(ReMerge)
            for item in Nex:
                Tex = DD[str(item)]["NextDialogs"]
                NPats.append(delver(Tex,Choi+[Nex]+[ReMerge],[item]))
            #print(NPats == Pats)
            """
            #return(delver(Tex,Choi+[Nex]+[ReMerge],Tree+Pats))

            #return Tree+NPats
            #"""    
            #return(delver(Tex,Choi+[Nex],Tree+Pats))

def ender(Choi):
    Poss = []
    for item in Choi:
        if str(item) not in DD:
            continue
        Poss.append(item)
        Che = DD[str(item)]
        Nex = Che["NextDialogs"]
        while len(Nex) == 1:
            Poss.append(Nex[0])
            if str(Nex[0]) not in DD or Nex == Choi:
                Nex = []
            else:
                if len(Nex) == 1:
                    if Nex[0] in Choi:
                        Nex = []
                    else:
                        Nex = DD[str(Nex[0])]["NextDialogs"]
                elif len(Nex) > 1:
                    #print(Nex)
                    Nex = DD[str(Nex[0])]["NextDialogs"]

    FinPoss = []
    for item in Poss:
        if Poss.count(item) == len(Choi):
            FinPoss.append(item)
    if len(FinPoss) == 0:
        for item in Poss:
            if Poss.count(item) == len(Choi)-1:
                FinPoss.append(item)
    try:
        return(FinPoss[0])
    except:
        return([])

def Mp(Choi):
    Poss = []
    for item in Choi:
        Poss.append(int(item))
        Che = DD[str(item)]
        Nex = Che["NextDialogs"]
        TPoss = []
        while len(Nex) == 1:
            Poss.append(Nex[0])
            if str(Nex[0]) not in DD or Nex == Choi:# or Nex in TPoss:
                Nex = []
            else:
                if len(Nex) == 1:
                    if Nex[0] in Choi or Nex in TPoss:
                        Nex = []
                    else:
                        Nex = DD[str(Nex[0])]["NextDialogs"]
                        TPoss.append(Nex)
                elif len(Nex) > 1:
                    #print(Nex)
                    Nex = DD[str(Nex[0])]["NextDialogs"]
                    TPoss.append(Nex)

    return Poss

def choice(Choi):
    if 3960702 in Choi:
        print("here")

    Remerge = ender(Choi)
    Branches = diver(Choi,Remerge)
    return([Remerge,Branches])

def chats():
    final = {}
    for item in TD:
        Diag = []
        BE = TD[item]
        if "InitDialog" not in BE:
            continue
        NT = [BE["InitDialog"]]
        
        if item == "34713":
            print("Here")
        if item == "1800005":
            print("Here")
        if str(NT[0]) not in DD:
            continue
        #print(item)
        Diag = delver(NT)
        final.update({item : Diag})

    with open(ChatOut, "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def RecMap():
    final = {}
    for item in CookRecipeData:
        temp = {}
        temp.update({"Helper" : GDBT.conv(str(CookRecipeData[item]["NameTextMapHash"]))})
        temp.update({"Name" : str(CookRecipeData[item]["NameTextMapHash"])})
        temp.update({"Rarity" : str(CookRecipeData[item]["RankLevel"])})
        temp.update({"Type" : FTyp[CookRecipeData[item]["FoodType"]]})

        Materials = []
        for mat in CookRecipeData[item]["InputVec"]:
            if mat != {}:
                Materials.append([GDBT.ItemNamRet(str(mat["Id"])),mat["Count"]])
        temp.update({"Materials" : Materials})
        
        Results = []
        for food in CookRecipeData[item]["QualityOutputVec"]:
            Results.append(str(food["Id"]))
        temp.update({"Variants" : Results})
        if item in CookBonusData:
            temp.update({"Specialty" : [True,str(CookBonusData[item]["AvatarId"])]})
            temp["Variants"].append(str(CookBonusData[item]["ParamVec"][0]))
        else:
            temp.update({"Specialty" : [False,""]})

        final.update({item : temp})

    with open(GDBT.ExCI(Stage_2,"RecipeMapData.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def QuestCodex():
    final = {}
    for item in QCD:
        Tree = QCD[item]
        temp = {}
        if Tree["ChapterId"] not in final:
            final.update({Tree["ChapterId"] : [Tree["ParentQuestId"]]})
        else:
            final[Tree["ChapterId"]].append(Tree["ParentQuestId"])
        

    with open("Bot_Files//QuestCodexTrees.json", "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def DialogueMapper():
    final = {}
    checked = []
    Diags = DialogData
    #Diags = [180000501,105010401,3960701,3471301,3470301,3470302]
    for item in Diags:
        if int(item) in checked:
            continue
        NT = [item]
        AllEven = Full_Path(NT)
        checked = checked+AllEven
        
        if item == "34713":
            print("Here")
        if item == "1800005":
            print("Here")
        if str(NT[0]) not in DialogueData:
            continue
        #print(item)
        #Diag = Full_Path(NT)
        Diag = Path_Flow(NT)

        final.update({item : Diag})

    with open("Bot_Files//DialogFlow.json", "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def DialogueSieve():
    final = {}
    for Field in DialogData:
        Dialog = DialogData[Field]
        temp = {}
        if "Type" in Dialog["TalkRole"]:
            temp.update({"Type" : Dialog["TalkRole"]["Type"]})
        else:
            if Dialog["TalkRole"]["Id"] == "":
                temp.update({"Type" : "Null"})
            else:
                temp.update({"Type" : "Special"})
                #print("Warp Magic Fuckery")
        temp.update({"Id" : Dialog["TalkRole"]["Id"]})
        temp.update({"Next" : Dialog["NextDialogs"]})
        temp.update({"LineSpoken" : Dialog["TalkContentTextMapHash"]})
        temp.update({"Title" : Dialog["TalkTitleTextMapHash"]})
        temp.update({"Role" : Dialog["TalkRoleNameTextMapHash"]})
        final.update({ Field : temp })
    with open(GDBT.ExCI(Stage_2,"StrainedDialog.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def TalkSieve():
    final = {}
    for Field in TalkData:
        Talk = TalkData[Field]
        temp = {}
        missing = []
        if "InitDialog" in Talk:
            temp.update({"Chain Head" : Talk["InitDialog"]})
        else:
            missing.append("Chain Head")

        if "Priority" in Talk:
            temp.update({"Priority" : Talk["Priority"]})
        else:
            missing.append("Priority")

        if "BeginWay" in Talk:
            temp.update({"BeginWay" : Talk["BeginWay"]})
        else:
            missing.append("BeginWay")

        if "ActiveMode" in Talk:
            temp.update({"ActiveMode" : Talk["ActiveMode"]})
        else:
            missing.append("ActiveMode")

        if "BeginCondComb" in Talk:
            temp.update({"BeginCondComb" : Talk["BeginCondComb"]})
        else:
            missing.append("BeginCondComb")

        if "QuestId" in Talk:
            temp.update({"QuestId" : Talk["QuestId"]})
        else:
            missing.append("QuestId")

        if "DontBlockDaily" in Talk:
            temp.update({"DontBlockDaily" : Talk["DontBlockDaily"]})
        else:
            missing.append("DontBlockDaily")
        TBegin = []
        for Conditions in Talk["BeginCond"]:
            Toss = False
            for Param in Conditions["Param"]:
                if Param != "":
                    Toss = True
                    continue

            if Toss:
                TBegin.append(Conditions)

        TFinish = []
        for Conditions in Talk["FinishExec"]:
            Toss = False
            for Param in Conditions["Param"]:
                if Param != "":
                    Toss = True
                    continue

            if Toss:
                TFinish.append(Conditions)

        temp.update({"Missing Params" : missing})
        temp.update({"BeginCond" : TBegin})
        temp.update({"FinishExec" : TFinish})
        final.update({ Field : temp })
    with open(GDBT.ExCI(Stage_2,"StrainedTalk.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def TalkCompact():
    final = {}
    StrainedDiags = GDBT.Stageloader("StrainedDialog.json",2)
    for Field in TalkData:
        Talk = TalkData[Field]
        temp = {}
        if "InitDialog" not in Talk:
            ConvoBegin = str(Talk["PerformCfg"])
        else:
            ConvoBegin = str(Talk["InitDialog"])
        if ConvoBegin in StrainedDiags:
            temp.update({"First Line" : GDBT.conv(StrainedDiags[ConvoBegin]["LineSpoken"])})
            temp.update({"First Line" : delver([ConvoBegin])})
        else:
            temp.update({"First Line" : [ConvoBegin]})
        
        final.update({ Field : temp })
    with open(GDBT.ExCI(Stage_2,"TalkCompact.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

#chats()
#print(delver([3960701]))
#End = delver([3960701])
#End = delver([3960702,3960707,3960715,3960727,3960741])
#diver([3471302, 3471303, 3471304],ender([708140706, 708140707, 708140708]))
def main():
    chartables()
    normaltables()
    skilltables()
    bursttables()
    weapontables()
    RecMap()
    DialogueSieve()
    TalkCompact()
    #DialogueMapper()
    #chats()
    #QuestCodex()
if __name__ == "__main__":
    main()
    #TalkCompact()
    #RecMap()
    #TalkSieve()
    pass