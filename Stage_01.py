import sys
import os
import json
import math
import time
import GDBTools as GDBT

os.chdir(os.path.dirname(__file__))
mydir = os.path.dirname(__file__) or "."
Stage_0 = os.path.join(mydir, "Stage_0")
Stage_1 = os.path.join(mydir, "Stage_1")
Stage_L = os.path.join(mydir, "Stage_L")
Out_Files = os.path.join(mydir, "Out_Files")
Itemdex = os.path.join(Out_Files, "ItemEN.json")

UIdentifiers = {}
BDN = GDBT.Loader("BaseDataNotes.json")


Unique = ["CityLevelupConfigData.json"]
Skip = ["GuideRatingExcelConfigData.json","SignInPeriodExcelConfigData.json","TowerSkipFloorExcelConfigData.json","WeatherTemplateExcelConfigData.json","WorldAreaLevelupConfigData.json"]
def AvatarPromoteData():
    APECD = GDBT.Baseloader("AvatarPromoteExcelConfigData.json")
    final = {}
    for item in APECD:
        loc = APECD.index(item)
        if APECD[loc]["AvatarPromoteId"] not in final:
            temp = item
            final.update({APECD[loc]["AvatarPromoteId"] : [temp]})

        else:
            temp = {}
            temp.update({item["PromoteLevel"] : {}})
            temp2 = ["","","",""]
            for bon in item["AddProps"]:
                if bon["PropType"]== "FIGHT_PROP_BASE_HP":
                    temp2[0] = bon
                if bon["PropType"]== "FIGHT_PROP_BASE_ATTACK":
                    temp2[1] = bon
                if bon["PropType"]== "FIGHT_PROP_BASE_DEFENSE":
                    temp2[2] = bon
                else:
                    temp2[3] = bon
            temp3 = []
            for thing in item["CostItems"]:
                try:
                    Idd = str(thing["Id"])
                    #T2 = []
                    temp3.append({
                        "Id" : Idd,
                        "Count" : thing["Count"]
                    })
                except:
                    pass
            item["CostItems"] = temp3
            item["AddProps"] = temp2
            temp = item
            final[APECD[loc]["AvatarPromoteId"]].append(temp)
    return final

def BinNoteInitializer():
    T_B = time.perf_counter() #Begin Stage Timer
    print("Stage 0 - Check For New BinData And Notify When Found")
    for BinFile in os.listdir(Stage_0):
        Source_Path = BinFile 
        if BinFile in BDN:
            Temp = BDN[BinFile] 
            UIdentifiers.update({Source_Path : {"OutPath" :Temp["OutPath"],"UID" : Temp["UID"],"Notes" : Temp["Notes"]}})
        else:
            print(BinFile+" Is New")
            Output_Path = Source_Path.replace("ExcelConfig","")
            UIdentifiers.update({Source_Path : {"OutPath" :Output_Path,"UID" : "","Notes" : ""}})

    with open("BaseDataNotes.json", "w", encoding='utf-8') as write_file:
        json.dump(UIdentifiers, write_file, indent=4, ensure_ascii=False)
    T_E = time.perf_counter() #End Stage Timer
    print(f"Stage 0 Completed in {T_E - T_B:0.4f} seconds")

def AvatarPromoteData(Data):
    final = {}
    for item in Data:
        loc = Data.index(item)
        if Data[loc]["AvatarPromoteId"] not in final:
            temp = item
            final.update({Data[loc]["AvatarPromoteId"] : [temp]})

        else:
            temp = {}
            temp.update({item["PromoteLevel"] : {}})
            temp2 = ["","","",""]
            for bon in item["AddProps"]:
                if bon["PropType"]== "FIGHT_PROP_BASE_HP":
                    temp2[0] = bon
                if bon["PropType"]== "FIGHT_PROP_BASE_ATTACK":
                    temp2[1] = bon
                if bon["PropType"]== "FIGHT_PROP_BASE_DEFENSE":
                    temp2[2] = bon
                else:
                    temp2[3] = bon
            temp3 = []
            for thing in item["CostItems"]:
                try:
                    Idd = str(thing["Id"])
                    #T2 = []
                    temp3.append({
                        "Id" : thing["Id"],
                        "Count" : thing["Count"]
                    })
                except:
                    pass
            item["CostItems"] = temp3
            item["AddProps"] = temp2
            temp = item
            final[Data[loc]["AvatarPromoteId"]].append(temp)
    return final

def AvatarCurveData(Data):
    final = {}
    temp = [[],[],[],[]]
    for item in Data:
        for itemnum in GDBT.ranger(0,4):
            temp[itemnum].append(item["CurveInfos"][itemnum]["Value"])
    for itemnum in GDBT.ranger(0,4):
        final.update({Data[0]["CurveInfos"][itemnum]["Type"] : temp[itemnum]})
    return final

def WeaponPromoteData(Data):

    final = {}
    for item in Data:
        if item["WeaponPromoteId"] not in final:
            temp = {}
            temp.update({0 : {}})
            temp[0].update({"UnlockMaxLevel" : item["UnlockMaxLevel"]})
            final.update({item["WeaponPromoteId"] : temp})

        else:
            temp = {}
            temp.update({item["PromoteLevel"] : {}})
            Evol = {"Mora" : [],"Mats" : []}
            try:
                Evol.update({"Mora" : [item["CoinCost"]] })
            except:
                Evol.update({"Mora" : [0] })
            try:
                for thing in item["CostItems"]:
                    T2 = {
                        "Id" : thing["Id"],
                        "Count" : thing["Count"]
                    }
                    Evol["Mats"].append(T2)
            except:
                Evol.update({"Mats" : [] })

            temp[item["PromoteLevel"]].update({ "Evolution" : Evol})
            temp[item["PromoteLevel"]].update({"UnlockMaxLevel" : item["UnlockMaxLevel"]})
            temp[item["PromoteLevel"]].update({"Value" : item["AddProps"][0]["Value"]})
            final[item["WeaponPromoteId"]].update(temp)
    return final

def ProudSkillData(Data):
    final = {}
    for item in Data:
        loc = Data.index(item)

        if Data[loc]["ProudSkillGroupId"] not in final:
            temp = item
            final.update({Data[loc]["ProudSkillGroupId"] : [temp]})

        else:
            temp = {}
            temp = item
            final[Data[loc]["ProudSkillGroupId"]].append(temp)
    return final

def WeaponCurveData(Data):
    final = {}
    for item in Data:
        types = {}
        for dat in item["CurveInfos"]:
            types.update({dat["Type"] : dat["Value"]})        
        
        final.update({item["Level"] : types})
    return final

def FetterStoryData(Data):
    final = {}
    for item in Data:
        FSD = item
        loc = Data.index(item)
        if FSD["AvatarId"] not in final:
            temp = {}
            temp.update({"ID" : FSD["FetterId"]})
            temp.update({"Name" : FSD["StoryTitleTextMapHash"]})
            temp.update({"Description" : FSD["StoryContextTextMapHash"]})
            final.update({FSD["AvatarId"] : [temp]})

        else:
            temp = {}
            temp.update({"ID" : FSD["FetterId"]})
            temp.update({"Name" : FSD["StoryTitleTextMapHash"]})
            temp.update({"Description" : FSD["StoryContextTextMapHash"]})
            final[FSD["AvatarId"]].append(temp)
    return final

def FetterInfoData(Data):
    final = {}
    for item in Data:
        FID = item
        temp = {}
        temp.update({"Origin" : FID["AvatarNativeTextMapHash"]})
        temp.update({"Element" : FID["AvatarVisionBeforTextMapHash"]})
        if FID["AvatarVisionBeforTextMapHash"] == 967031460:
            temp.update({"Constellation" : FID["AvatarConstellationAfterTextMapHash"]})
        else:
            temp.update({"Constellation" : FID["AvatarConstellationBeforTextMapHash"]})

        temp.update({"Title" : FID["AvatarTitleTextMapHash"]})
        temp.update({"Intro" : FID["AvatarDetailTextMapHash"]})
        final.update({FID["AvatarId"] : temp})
    return final

def MechanicusGearLevelUpData(Data):
    final = {}
    for item in Data:
        MGLUDP = item

        if item["GearID"] not in final:
            temp = {item["GearID"] : {item["GearLevel"] : item}}
            final.update(temp)
        else:
            temp = {item["GearLevel"] : item}
            final[item["GearID"]].update(temp)
    return final






def Remapper():
    T_B = time.perf_counter() #Begin Stage Timer
    print("Stage 1 - Data Remapping To Unique IDs")
    for BinFile in os.listdir(Stage_0):
        TempFinal = {}
        Source_Path = BinFile 
        Source_Data = GDBT.BinLoader(Source_Path,True)
        Output_Path = Source_Path.replace("ExcelConfig","")

        if BinFile == "AvatarPromoteExcelConfigData.json":
            TempFinal = AvatarPromoteData(Source_Data)

        elif BinFile == "AvatarCurveExcelConfigData.json":
            TempFinal = AvatarCurveData(Source_Data)

        elif BinFile == "WeaponPromoteExcelConfigData.json":
            TempFinal = WeaponPromoteData(Source_Data)

        elif BinFile == "ProudSkillExcelConfigData.json":
            TempFinal = ProudSkillData(Source_Data)

        elif BinFile == "WeaponCurveExcelConfigData.json":
            TempFinal = WeaponCurveData(Source_Data)

        elif BinFile == "FetterStoryExcelConfigData.json":
            TempFinal = FetterStoryData(Source_Data)

        elif BinFile == "FetterInfoExcelConfigData.json":
            TempFinal = FetterInfoData(Source_Data)

        elif BinFile == "MechanicusGearLevelUpExcelConfigData.json":
            TempFinal = MechanicusGearLevelUpData(Source_Data)

        elif BinFile in Unique+Skip:
            continue
        else:
            #continue
            C = 0
            for item in Source_Data:
                try:
                    temp = {item[BDN[BinFile]["UID"]] : item}
                except KeyError:
                    print(BinFile+" - Null Initial Error")
                    temp = {C : item}
                    if C > 0:
                        print("Other Error Break Point")
                    C+=1
                TempFinal.update(temp)

        with open(GDBT.ExCI(Stage_1,Output_Path), "w", encoding='utf-8') as write_file:
            json.dump(TempFinal, write_file, indent=4, ensure_ascii=False)
    T_E = time.perf_counter() #End Stage Timer
    print(f"Stage 1 Completed in {T_E - T_B:0.4f} seconds")




def main():
    RSB = time.perf_counter() #Begin Total Timer
    #BinNoteInitializer()
    Remapper()
    RSE = time.perf_counter() #End Total Timer
    print(f"Stage Remapper Completed in {RSE - RSB:0.4f} seconds")

def Temp_Deob():
    Final = {}
    Clean = []
    Dirty = []
    Names = []
    FNames = []
    CleanP = os.path.join(mydir,"Stage_T","Clean")
    DirtyP = os.path.join(mydir,"Stage_T","Dirty")
    C = 0
    for BinFile in os.listdir(CleanP):
        if BinFile not in os.listdir(DirtyP):
            continue
        TempFinal = {}
        Source_Path = BinFile 
        CleanTP = os.path.join(mydir,"Stage_T","Clean",BinFile)
        DirtyTP = os.path.join(mydir,"Stage_T","Dirty",BinFile)
        CSource_Data = GDBT.Loader(CleanTP)
        DSource_Data = GDBT.Loader(DirtyTP)
        for item in CSource_Data:
            Temp = []
            for field in item:
                TAdd = field
                if field not in Temp:
                    Temp.append(field)
        Clean.append(Temp)
        for item in DSource_Data:
            Temp = []
            for field in item:
                TAdd = field
                if field not in Temp:
                    Temp.append(field)
        Dirty.append(Temp)
        Names.append(BinFile)
        
        C+=1
    #print("Here")
    C = 0
    for item in Clean:
        C = Clean.index(item)
        TClean = Clean[C]
        TDirty = Dirty[C]
        if len(TClean) != len(TDirty):
            Point = Names[C]   
            FNames.append(Point)         
            #print("Here")
            continue
        for field in TDirty:
            Final.update({field: TClean[TDirty.index(field)]})

    print(FNames)
    #with open(GDBT.ExCI(Stage_1,"DO.json"), "w", encoding='utf-8') as write_file:
        #json.dump(Final, write_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    #Temp_Deob()
    main()

