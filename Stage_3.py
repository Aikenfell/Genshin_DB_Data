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

Stage_0 = os.path.join(mydir, "Stage_0")
Stage_1 = os.path.join(mydir, "Stage_1")
Stage_2 = os.path.join(mydir, "Stage_2")
Stage_3 = os.path.join(mydir, "Stage_3")


AvatarData = GDBT.Stageloader("AvatarData.json",1)
AvatarPromoteData = GDBT.Stageloader("AvatarPromoteData.json",1)
AvatarSkillDepotData = GDBT.Stageloader("AvatarSkillDepotData.json",1)
AvatarTalentData = GDBT.Stageloader("AvatarTalentData.json",1)
ProudSkillData = GDBT.Stageloader("ProudSkillData.json",1)
AvatarPromoteData = GDBT.Stageloader("AvatarPromoteData.json",1)
FetterStoryData = GDBT.Stageloader("FetterStoryData.json",1)
FetterInfoData = GDBT.Stageloader("FetterInfoData.json",1)
MaterialData = GDBT.Stageloader("MaterialData.json",1)
MaterialSourceData = GDBT.Stageloader("MaterialSourceDataData.json",1)
WeaponData = GDBT.Stageloader("WeaponData.json",1)
WeaponPromoteData = GDBT.Stageloader("WeaponPromoteData.json",1)
EquipAffixData = GDBT.Stageloader("EquipAffixData.json",1)
ReliquaryData = GDBT.Stageloader("ReliquaryData.json",1)
ReliquarySetData = GDBT.Stageloader("ReliquarySetData.json",1)
HomeWorldFurnitureData = GDBT.Stageloader("HomeWorldFurnitureData.json",1)
FurnitureSuiteData = GDBT.Stageloader("FurnitureSuiteData.json",1)
FurnitureMakeData = GDBT.Stageloader("FurnitureMakeData.json",1)
MonsterData = GDBT.Stageloader("MonsterData.json",1)
MonsterDescribeData = GDBT.Stageloader("MonsterDescribeData.json",1)
MechanicBuildingData = GDBT.Stageloader("MechanicBuildingData.json",1)
MechanicusGearLevelUpData = GDBT.Stageloader("MechanicusGearLevelUpData.json",1)
GadgetData = GDBT.Stageloader("GadgetData.json",1)
MainQuestData = GDBT.Stageloader("MainQuestData.json",1)
QuestData = GDBT.Stageloader("QuestData.json",1)
TalkData = GDBT.Stageloader("TalkData.json",1)
ShopGoodsData = GDBT.Stageloader("ShopGoodsData.json",1)
AvatarHeroEntityData = GDBT.Stageloader("AvatarHeroEntityData.json",1)
MaterialCodexData = GDBT.Stageloader("MaterialCodexData.json",1)
FeatureTagGroupData = GDBT.Stageloader("FeatureTagGroupData.json",1)
IGTD = GDBT.Stageloader("IGNTags.json",3)

CT  = GDBT.Stageloader("CharTables.json",2)
NT  = GDBT.Stageloader("NormalTables.json",2)
ST  = GDBT.Stageloader("SkillTables.json",2)
BT  = GDBT.Stageloader("BurstTables.json",2)
WT  = GDBT.Stageloader("WeaponTables.json",2)

Lang_EN = GDBT.Stageloader("TextMapEN.json","L")

Rep = { "EQUIP_BRACER" : "Flower",
        "EQUIP_NECKLACE" : "Feather",
        "EQUIP_SHOES" : "Timepiece",
        "EQUIP_RING" : "Goblet",
        "EQUIP_DRESS" : "Headpiece"
}

def TalDatRet(SDID):
    temp = {}
    Talent = {}
    try:
        for TalNum in [1,2,3,4,5,6]:
            TID = AvatarSkillDepotData[SDID]["Talents"][TalNum-1]
            temptal = {}
            ATD = AvatarTalentData[str(TID)]
            temptal.update({"Name" : ATD["NameTextMapHash"]})
            temptal.update({"Description" : ATD["DescTextMapHash"]})
            temptal.update({"Icon" : ATD["Icon"]})
            Talent.update({str(TalNum) : temptal})

    except:
        for TalNum in [1,2,3,4,5,6]:
            temptal = {}
            temptal.update({"Name" : ""})
            temptal.update({"Description" : ""})
            temptal.update({"Icon" : ""})
            Talent.update({str(TalNum) : temptal})
    temp.update({"Talents" : Talent})
    passives = []

    for pas in AvatarSkillDepotData[SDID]["InherentProudSkillOpens"]:
        try:
            passives.append(pas["ProudSkillGroupId"])
        except:
            passives.append("")
    cpass = []
    for GID in passives:
        try:
            cpass.append([str(ProudSkillData[str(GID)][0]["NameTextMapHash"]),str(ProudSkillData[str(GID)][0]["DescTextMapHash"]),str(ProudSkillData[str(GID)][0]["Icon"])])
        except:
            cpass.append(["","",""])
    temp.update({"Passives" : cpass})
    return temp

    pass
def Char_Mapper():
    final = {}
    for item in AvatarData:
        Char = AvatarData[item]
        temp = {}
        SNam = Char["IconName"].split("_")[-1]
        temp.update({"Helper" : SNam})
        temp.update({"Name" : Char["NameTextMapHash"]})
        temp.update({"Weapon" : Char["WeaponType"]})
        temp.update({"Rarity" : Char["QualityType"]})
        temp.update({"Short" : Char["DescTextMapHash"]})
        temp.update({"Icon" : SNam})
        Tags = []
        if item in FeatureTagGroupData:
            
            for Tag in FeatureTagGroupData[item]["TagIDs"]:
                if Tag == 0:
                    continue
                Tags.append(IGTD[str(Tag)]["TagName"])
        temp.update({"Tags" : Tags})
        if item in AvatarHeroEntityData:
            FTemp = []
            for element in AvatarData[item]["CandSkillDepotIds"]:
                SDID = str(AvatarData[item]["SkillDepotId"])
                try:
                    GID = str(AvatarSkillDepotData[SDID]["EnergySkill"])
                except:
                    FTemp.append([])
                    continue
                FTemp.append(TalDatRet(item,SDID,GID))
        SDID = str(Char["SkillDepotId"])
        EDID = str(Char["AvatarPromoteId"])
        Evol = []
        LEvol = []
        Total = {}
        for level in AvatarPromoteData[EDID][1:]:
            lv = level
            Cost = {}
            for MatReq in lv["CostItems"]:
                Cost.update({MaterialData[str(MatReq["Id"])]["NameTextMapHash"] : MatReq["Count"]})
            Evol.append([lv["ScoinCost"],lv["CostItems"]])
            LEvol.append([lv["ScoinCost"],Cost])

        for level in Evol:
            for mat in level[1]:
                if mat["Id"] in Total:
                    Total[mat["Id"]]+=mat["Count"]
                else:
                    Total.update({mat["Id"] : mat["Count"]})

        TKeys = sorted(list(Total.keys()))
        NTotal = {}
        for MatReq in TKeys:
            try:
                Nam = MaterialData[str(MatReq)]["NameTextMapHash"]
            except:
                Nam = MatReq
            NTotal.update({Nam : Total[MatReq]})

        temp.update({"Ascension" : LEvol})
        temp.update({"total" : NTotal})
        temp.update({"Normal Attack" : NT[item]})
        temp.update({"Elemental Skill" : ST[item]})
        temp.update({"Elemental Burst" : BT[item]})

        if item in AvatarHeroEntityData:
            FTemp = []
            for element in AvatarData[item]["CandSkillDepotIds"]:
                SDID = str(element)
                FTemp.append(TalDatRet(SDID)["Talents"])
        else:
            FTemp = TalDatRet(SDID)["Talents"]        
        temp.update({"Talents" : FTemp})

        if item in AvatarHeroEntityData:
            FTemp = []
            for element in AvatarData[item]["CandSkillDepotIds"]:
                SDID = str(element)
                FTemp.append(TalDatRet(SDID)["Passives"])
        else:
            FTemp = TalDatRet(SDID)["Passives"]
        temp.update({"Passives" : FTemp})

        story = {}
        emp = {"ID" : "","Name" : "","Description" : ""}
        try:
            story.update({"0" : FetterStoryData[str(item)][0]})
        except:
            story.update({"0" : emp})
        try:
            story.update({"1" : FetterStoryData[str(item)][1]})
        except:
            story.update({"1" : emp})
        try:
            story.update({"2" : FetterStoryData[str(item)][2]})
        except:
            story.update({"2" : emp})
        try:
            story.update({"3" : FetterStoryData[str(item)][3]})
        except:
            story.update({"3" : emp})
        try:
            story.update({"4" : FetterStoryData[str(item)][4]})
        except:
            story.update({"4" : emp})
        try:
            story.update({"5" : FetterStoryData[str(item)][5]})
        except:
            story.update({"5" : emp})
        try:
            story.update({"Fave" : FetterStoryData[str(item)][6]})
        except:
            story.update({"Fave" : emp})
        try:
            story.update({"Focus" : FetterStoryData[str(item)][7]})
        except:
            story.update({"Focus" : emp})

        temp.update({"Story" : story})
        
        try:
            FID = FetterInfoData[str(item)]
            temp.update({"Origin" : FID["Origin"]})
            temp.update({"Element" : FID["Element"]})
            temp.update({"Constellation" : FID["Constellation"]})
            temp.update({"Title" : FID["Title"]})
            temp.update({"Intro" : FID["Intro"]})
        except:
            temp.update({"Origin" : ""})
            temp.update({"Element" : ""})
            temp.update({"Constellation" : ""})
            temp.update({"Title" : ""})
            temp.update({"Intro" : ""})
        stats = []
        for level in [0,1,20,21,41,42,52,53,63,64,74,75,85,86,96]:
            stats.append(CT[item]["Stats"][level])
        temp.update({"Stats" : stats})
    
        final.update({item : temp})
    with open(GDBT.ExCI(Stage_3,"CharMap.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def TexRet(TexLoc,LangPat=Lang_EN):
    WR = str(TexLoc)
    if WR not in LangPat:
        return(WR)
    else:
        return(LangPat[WR])

def Item_Mapper():
    final = {}
    food = {}
    quest = {}
    mats = {}
    rest = {}
    pips = {}
    chests = {}
    cards = {}
    fortuna = {}
    asc = {}
    wid = {}
    wing = {}
    FurForms = {}
    Cats = {}
    Tabs = {}
    NCS = {}
    Costumes = {}
    NFTs = {}
    Recipes = {}
    Wood = {}
    for item in MaterialData:
        Target = MaterialData[item]
        temp = {}
        temp.update({"Item Type" : Target["ItemType"]})
        try:
            temp.update({"Material Type" : Target["MaterialType"]})
        except:
            temp.update({"Material Type" : "None"})
        INam = str(Target["NameTextMapHash"])
        temp.update({"Helper" : TexRet(INam)})
        temp.update({"Item Name" : INam})
        try:
            temp.update({"Rarity" : Target["RankLevel"]})
        except:
            temp.update({"Rarity" : 0})
        temp.update({"Icon" : Target["Icon"]})
        INde = str(Target["DescTextMapHash"]) 
        temp.update({"Helper2" : TexRet(INde)})
        temp.update({"Type Designation" : Target["TypeDescTextMapHash"]})
        temp.update({"Type Helper" : TexRet(Target["TypeDescTextMapHash"])})
        Sou = []
        try:
            for SRC in MaterialSourceData[item]["TextList"]:
                if SRC in [""]:
                    continue
                Sou.append(str(SRC))
        except:
            print(item)
        temp.update({"Sources" : Sou})
        temp.update({"Item Desc" : INde})
        if temp["Material Type"] in ["MATERIAL_FOOD","MATERIAL_NOTICE_ADD_HP"]:
            temp.update({"Ban" : False})
            temp.update({"Effect Desc" : str(Target["EffectDescTextMapHash"])})
            temp.update({"Type" : str(Target["TypeDescTextMapHash"])})
            temp.update({"IC" : str(Target["EffectIcon"])})
            try:
                temp.update({"Quality" : str(Target["FoodQuality"])})
            except:
                temp.update({"Quality" : "Specialty"})
            food.update({item : temp})

        elif temp["Material Type"] in ["MATERIAL_FURNITURE_FORMULA","MATERIAL_FURNITURE_SUITE_FORMULA"]:
            FurForms.update({item : temp})

        elif temp["Material Type"] == "MATERIAL_CHANNELLER_SLAB_BUFF":
            Tabs.update({item : temp})

        elif temp["Material Type"] == "MATERIAL_CONSUME" and temp["Type Helper"] == "Recipe":
            Recipes.update({item : temp})

        elif temp["Material Type"] == "MATERIAL_CONSUME":
            Cats.update({item : temp})

        elif temp["Material Type"] == "MATERIAL_WIDGET":
            wid.update({item : temp})
        elif temp["Material Type"] in ["MATERIAL_EXCHANGE","MATERIAL_EXP_FRUIT","MATERIAL_WEAPON_EXP_STONE"]:
            mats.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_ADSORBATE":
            pips.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_CHEST":
            chests.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_AVATAR":
            cards.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_FLYCLOAK":
            wing.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_WOOD":
            Wood.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_COSTUME":
            Costumes.update({item : temp})
        elif temp["Item Type"] == "ITEM_VIRTUAL":
            NFTs.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_QUEST":
            quest.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_TALENT":
            fortuna.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_NAMECARD":
            NCS.update({item : temp})
        elif temp["Material Type"] == "MATERIAL_AVATAR_MATERIAL":
            if Target["Rank"] not in asc:
                asc.update({Target["Rank"] : {item : temp}})
            else:
                asc[Target["Rank"]].update({item : temp})
        else:
            rest.update({item : temp})
    
    final.update({"Materials" : mats})
    final.update({"Food" : food})
    final.update({"Quest" : quest})
    final.update({"Gadgets" : wid})
    final.update({"Pips" : pips})
    final.update({"Ascension Materials" : asc})
    final.update({"Furniture Recipes" : FurForms})
    final.update({"Recipes" : Recipes})
    final.update({"Chests" : chests})
    final.update({"Character Cards" : cards})
    final.update({"Tablets" : Tabs})
    final.update({"Wings" : wing})
    final.update({"Wood" : Wood})
    final.update({"Variable" : Cats})
    final.update({"Currencies" : NFTs})
    final.update({"Namecards" : NCS})
    final.update({"Costumes" : Costumes})
    final.update({"Character Talents" : cards})
    final.update({"Unsorted" : rest})
    with open(GDBT.ExCI(Stage_3,"ItemMap.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def War_Trophies():

    final = {}
    for item in MaterialCodexData:
        WT = MaterialCodexData[item]
        temp = {}
        temp.update({"Id" : WT["Id"]})
        if "Type" in WT:
            temp.update({"Type" : WT["Type"]})
        else:
            temp.update({"Type" : "None"})
        temp.update({"MaterialId" : WT["MaterialId"]})
        temp.update({"MaterialName" : GDBT.conv(GDBT.ItemNamRet(WT["MaterialId"]))})
        temp.update({"SortOrder" : WT["SortOrder"]})
        temp.update({"NameTextMapHash" : GDBT.conv(WT["NameTextMapHash"])})
        temp.update({"DescTextMapHash" : GDBT.conv(WT["DescTextMapHash"])})
        if WT["Icon"] == "":
            temp.update({"Icon" : True})
        else:
            temp.update({"Icon" : [False,WT["TIconype"]]})
        final.update({item : temp})
    with open(GDBT.ExCI(Stage_3,"WTEN.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)
    pass

def Weapon_Mapper():
    final = {}
    NEAD = {}
        
    for wep in WeaponData:
        item = WeaponData[wep]
        temp = {}
        temp.update({"Name" : str(item["NameTextMapHash"])})
        temp.update({"Description" : str(item["DescTextMapHash"])})
        temp.update({"Story" : ""})
        temp.update({"Rarity" : item["RankLevel"]})
        IC = item["Icon"].split("_")
        temp.update({"Class" : IC[2]})
        temp.update({"Series" : IC[3]})
        temp.update({"Icon" : item["Icon"]})
        temp.update({"AIcon" : item["AwakenIcon"]})
        temp.update({"Sid" : item["Id"]})
        affix = str(item["SkillAffix"][0])
        Evol = []
        Total = {}
        TID = item["Id"]
        if str(TID) not in WeaponPromoteData:
            TID = 11101
        for level in WeaponPromoteData[str(TID)]:
            lv = WeaponPromoteData[str(TID)][level]
            if "Evolution" in lv:
                Evol.append([lv["Evolution"]["Mora"],lv["Evolution"]["Mats"]])
        for level in Evol:
            for mat in level[1]:
                if mat["Id"] in Total:
                    Total[mat["Id"]]+=mat["Count"]
                else:
                    Total.update({mat["Id"] : mat["Count"]})
        TKeys = list(Total.keys())
        if len(TKeys) == 7:
            Total = {  TKeys[0] : Total[TKeys[0]],
                        TKeys[3] : Total[TKeys[3]],
                        TKeys[6] : Total[TKeys[6]],
                        TKeys[1] : Total[TKeys[1]],
                        TKeys[4] : Total[TKeys[4]],
                        TKeys[2] : Total[TKeys[2]],
                        TKeys[5] : Total[TKeys[5]]
            }
        else:
            Total = {  TKeys[0] : Total[TKeys[0]],
                        TKeys[3] : Total[TKeys[3]],
                        TKeys[6] : Total[TKeys[6]],
                        TKeys[9] : Total[TKeys[9]],
                        TKeys[1] : Total[TKeys[1]],
                        TKeys[4] : Total[TKeys[4]],
                        TKeys[7] : Total[TKeys[7]],
                        TKeys[2] : Total[TKeys[2]],
                        TKeys[5] : Total[TKeys[5]],
                        TKeys[8] : Total[TKeys[8]]
            }


        temp.update({"Ascension" : Evol})
        temp.update({"total" : Total})
        try:
            passive = { "Name" : str(EquipAffixData[affix+"0"]["NameTextMapHash"]),
                        "1" : str(EquipAffixData[affix+"0"]["DescTextMapHash"]),
                        "2" : str(EquipAffixData[affix+"1"]["DescTextMapHash"]),
                        "3" : str(EquipAffixData[affix+"2"]["DescTextMapHash"]),
                        "4" : str(EquipAffixData[affix+"3"]["DescTextMapHash"]),
                        "5" : str(EquipAffixData[affix+"4"]["DescTextMapHash"])
            }
        except:
            passive = { "Name" : "None",
                        "1" : "N/A",
                        "2" : "N/A",
                        "3" : "N/A",
                        "4" : "N/A",
                        "5" : "N/A"
            }
        if affix == "111412":
            passive["Name"] = "613846163"
            passive["1"] = "2090107097"

        temp.update({"Passive" : passive})
        temp.update({"Substat Type" : WT[str(item["Id"])]["Type"]})
        temp.update({"Affix" : affix})

        stats = []
        Tabl = WT[str(item["Id"])]["Stats"]
        try:
            for level in [0,1,20,21,41,42,52,53,63,64,74,75,85,86,96]:
                stats.append(Tabl[level])
        except:
            for level in [0,1,20,21,41,42,52,53,63,64,74]:
                stats.append(Tabl[level])
        temp.update({"Stats" : stats})


        final.update({wep : temp})

    with open(GDBT.ExCI(Stage_3,"WeapMap.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def Artif_Mapper():
    final = {}
    for item in ReliquarySetData:
        temp = {}
        if item != "15000":
            setbon = {}
            count = 0
            for setstat in ReliquarySetData[item]["SetNeedNum"]:
                AffixID = str(ReliquarySetData[item]["EquipAffixId"])
                setbon.update({setstat : [str(EquipAffixData[AffixID+str(count)]["NameTextMapHash"]),str(EquipAffixData[AffixID+str(count)]["DescTextMapHash"])]})
                temp.update({"Set Name" : str(EquipAffixData[AffixID+str(count)]["NameTextMapHash"])})
                count+=1
            setpiece = {}
            for setpie in ReliquarySetData[item]["ContainsList"]:
                setpiece.update({Rep[ReliquaryData[str(setpie)]["EquipType"]] : [str(ReliquaryData[str(setpie)]["NameTextMapHash"]),str(ReliquaryData[str(setpie)]["DescTextMapHash"]),""]})
            temp.update({ "Set Bonuses" : setbon})
            temp.update({ "Set Pieces" : setpiece})





            final.update({item : temp})
    with open(GDBT.ExCI(Stage_3,"ArtifMap.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def Furn_Mapper():
    Complete = {}
    final = {}
    for item in HomeWorldFurnitureData:
        Furn = HomeWorldFurnitureData[item]
        temp = {}
        temp.update({ "FName" :Furn["FurnitureNameTextMapHash"]})
        temp.update({ "IID" :Furn["Id"]})
        temp.update({ "Name" : Furn["NameTextMapHash"]})
        temp.update({ "Desc" : Furn["DescTextMapHash"]})
        temp.update({ "Icon" : Furn["ItemIcon"]})
        temp.update({ "Rarity" : Furn["RankLevel"]})
        temp.update({ "Type" : Furn["ItemType"]})
        temp.update({ "Sets" : {}})

        if "Comfort" in Furn:
            temp.update({ "Comfort" : Furn["Comfort"]})
        else:
            temp.update({ "Comfort" : 0})
        if "Cost" in Furn:
            temp.update({ "Cost" : Furn["Cost"]})
        else:
            temp.update({ "Cost" : 0})
        if "SurfaceType" in Furn:
            temp.update({ "SurfaceType" : Furn["SurfaceType"]})
        else:
            temp.update({ "SurfaceType" : False})
        RecipeDat = {}
        for Rec in FurnitureMakeData:
            Recipe = FurnitureMakeData[Rec]
            if Recipe["FurnitureItemID"] == Furn["Id"]:
                TReqs = {}
                for Mat in Recipe["MaterialItems"]:
                    if Mat!= {}:
                        TReqs.update({GDBT.ItemNamRet(Mat["Id"]) : Mat["Count"]})

                RecipeDat.update({"Recipe" : TReqs})
                RecipeDat.update({"Exp Gain" : Recipe["Exp"]})
                RecipeDat.update({"Crafting Time" : Recipe["MakeTime"]})
                RecipeDat.update({"Friend Reduction" : Recipe["MaxAccelerateTime"]})
        temp.update({ "Crafting" : RecipeDat})

        """EN Testing
        temp.update({ "FName" :GDBT.conv(Furn["FurnitureNameTextMapHash"])})
        temp.update({ "Name" : GDBT.conv(Furn["NameTextMapHash"])})
        temp.update({ "Desc" : GDBT.conv(Furn["DescTextMapHash"])})
        """


        final.update({item : temp})
    Complete.update({"Pieces" : final})
    final = {}
    for item in FurnitureSuiteData:
        Furn = FurnitureSuiteData[item]
        temp = {}
        temp.update({ "IID" :Furn["SuiteID"]})
        temp.update({ "Name" : Furn["SuiteNameTextMapHash"]})
        #temp.update({ "Desc" : Furn["SuiteDescTextMapHash"]})
        temp.update({ "Icon" : Furn["ItemIcon"]})
        temp.update({ "Faves" : Furn["FavoriteNpcExcelIdVec"]})
        temp.update({ "Pieces" : {}})
        try:
            SetData = GDBT.Stageloader("HomeworldFurnitureSuit//"+Furn["JsonName"]+".json","B")
            for Piece in SetData["furnitureUnits"]:

                for FPiece in Complete["Pieces"]:
                    if Complete["Pieces"][FPiece]["IID"] == Piece["furnitureID"]:
                        Tar = FPiece
                try:
                    if Piece["furnitureID"] not in temp["Pieces"]:
                        temp["Pieces"].update({Tar : 1})
                        Complete["Pieces"][Tar]["Sets"].update({str(Furn["SuiteID"]) : 1})
                    else:
                        temp["Pieces"][Tar]+=1
                        Complete["Pieces"][Tar]["Sets"][str(Furn["SuiteID"])]+=1
                except:
                    pass
        except:
            pass

        final.update({item : temp})
    Complete.update({"Sets" : final})

    
    with open(GDBT.ExCI(Stage_3,"FurnMap.json"), "w", encoding='utf-8') as write_file:
        json.dump(Complete, write_file, indent=4, ensure_ascii=False)

def Mon_Mapper():
    final = {}
    for item in MonsterData:
        Mon = MonsterData[item]
        temp = {}
        rewards = []
        try:
            DeID = str(Mon["DescribeId"])
            PureMon = True
            Tem = MonsterDescribeData[DeID]
        except:
            DeID = str(0)
            PureMon = False
        if PureMon:
            temp.update({"Name" :MonsterDescribeData[DeID]["NameTextMapHash"]})
            temp.update({"DescID" :Mon["DescribeId"]})
            temp.update({"Icon" :MonsterDescribeData[DeID]["Icon"]})
            temp.update({"Type" :"Monster"})
            #temp.update({"MonName" :Mon["MonsterName"]})
        else:
            temp.update({"Name" :Mon["NameTextMapHash"]})
            temp.update({"DescID" :DeID})
            temp.update({"Icon" :"UI_AnimalIcon_"+Mon["MonsterName"]})
            temp.update({"Type" :"Animal"})
            #temp.update({"MonName" :Mon["MonsterName"]})
        #temp.update({"Tier" :Mon["MonsterCategory"]})
        final.update({item : temp})

    with open(GDBT.ExCI(Stage_3,"MonMap.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)
  
def Mech_Mapper():
    final = {}
    for item in MechanicBuildingData:
        Tower = MechanicBuildingData[item]
        temp = {}
        rewards = []
        for level in MechanicusGearLevelUpData[item]:
            Tier = MechanicusGearLevelUpData[item][level]
            lev = {}
            lev.update({"Long" : GDBT.conv(Tier["GearNameTextMapHash"])})
            lev.update({"Short" : GDBT.conv(Tier["GearShortNameTextMapHash"])})
            if level == "1":
                lev.update({"Upgrade Cost" : 0})
            else:
                lev.update({"Upgrade Cost" : Tier["GearLevelUpMoney"]})
            try:
                lev.update({"Attack" : Tier["Attack"]})
            except:
                lev.update({"Attack" : 0})

            try:
                lev.update({"Speed" : Tier["AttackSpeed"]})
            except:
                lev.update({"Speed" : 0})

            try:
                lev.update({"Range" : Tier["AttackRange"]})
            except:
                lev.update({"Range" : 0})
            lev.update({"Ability Desc" : GDBT.conv(Tier["DescTextMapHash"])})
            lev.update({"Build Cost" : Tier["BuildCost"]})
            lev.update({"Refund" : Tier["DemolitionRefund"]})

            temp.update({level :lev})


        try:
            temp.update({"Bonus 1" :[MechanicBuildingData[item]["SpecialEffectLevel1"],GDBT.conv(MechanicBuildingData[item]["SpecialEffectDesc1TextMapHash"])]})
            temp.update({"Bonus 2" :[MechanicBuildingData[item]["SpecialEffectLevel2"],GDBT.conv(MechanicBuildingData[item]["SpecialEffectDesc2TextMapHash"])]})
        except:
            temp.update({"Bonus 1" :[0,GDBT.conv(MechanicBuildingData[item]["SpecialEffectDesc1TextMapHash"])]})
            temp.update({"Bonus 2" :[0,GDBT.conv(MechanicBuildingData[item]["SpecialEffectDesc2TextMapHash"])]})

        #temp.update({"Name" :GD[str(MechanicBuildingData["GadgetId"])]})
        #final.update({GDBT.conv(MechanicusGearLevelUpData[item]["1"]["DILJPPJOLNA"]) : temp})
        final.update({GDBT.conv(MechanicusGearLevelUpData[item]["1"]["GearNameTextMapHash"]) : temp})

    with open(GDBT.ExCI(Stage_3,"MechMap.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def Quest_Mapper():
    final = {}
    for item in MainQuestData:
        Que = MainQuestData[item]
        temp = {"Title" : Que["TitleTextMapHash"],
                "Desc" : Que["DescTextMapHash"],
                "Rewards" : Que["RewardIdList"],
                "Stages" : {},
        }
        if "Type" in Que:
            temp.update({"Type" : Que["Type"]})
        else:
            temp.update({"Type" : "Null"})
        if "Series" in Que:
            temp.update({"Series" : Que["Series"]})
        else:
            temp.update({"Series" : "Null"})
        if "ChapterId" in Que:
            temp.update({"Chapter" : Que["ChapterId"]})
        else:
            temp.update({"Chapter" : "Null"})
        final.update({Que["Id"] : temp})
    for item in QuestData:
        Que = QuestData[item]
        #if Que["MainId"] not in final:
        #    final.update({Que["MainId"] : {}})
        temp = {"Directive" : Que["DescTextMapHash"]}
        if item in TalkData:
            temp.update({"DiD" : item})
        else:
            temp.update({"DiD" : True})
        temp.update({"Diag" : item})
        final[Que["MainId"]]["Stages"].update({Que["Order"] : temp})

    with open(GDBT.ExCI(Stage_3,"QuestMap.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def Shop_Mapper():
    final = {}
    for item in ShopGoodsData:

        temp = {}        
        ShopGood = ShopGoodsData[item]
        if ShopGood == {}:
            continue
        if ShopGood["ShopType"] not in final:
            final.update({ShopGood["ShopType"] : {}})

        if "RotateId" in ShopGood:
            temp.update({"Temp" : 1769963853})
        else:
            temp.update({"Temp" : GDBT.ItemNamRet(ShopGood["ItemId"])})
        temp.update({"Count" : ShopGood["ItemCount"]})
        temp.update({"SortLevel" : ShopGood["SortLevel"]})
        if "BuyLimit" in ShopGood:
            temp.update({"Limit" : ShopGood["BuyLimit"]})
        else:
            temp.update({"Limit" : "Null"})
        Cost = []
        if "CostScoin" in ShopGood:
            #Cost.append([3578052980,ShopGood["CostScoin"]])
            Cost = [3578052980,ShopGood["CostScoin"]]
        if "CostHcoin" in ShopGood:
            #Cost.append([1255754588,ShopGood["CostHcoin"]])
            Cost = [2696654964,ShopGood["CostHcoin"]]
        for CI in ShopGood["CostItems"]:
            if CI != {}:
                #Cost.append([GDBT.ItemNamRet(CI["Id"]),CI["Count"]])
                Cost = [GDBT.ItemNamRet(CI["Id"]),CI["Count"]]

        #if len(Cost)>1:
            #print("Here")
        temp.update({"Cost" : Cost})
        temp.update({"Cost" : Cost})
        temp.update({"Item" : GDBT.conv(ShopGood["SubTagNameTextMapHash"])})

        if "SubTabId" in ShopGood:

            if GDBT.conv(ShopGood["SubTagNameTextMapHash"]) != "":
                SubID = GDBT.conv(ShopGood["SubTagNameTextMapHash"])
            else:
                SubID = ShopGood["SubTabId"]
            
            if SubID not in final[ShopGood["ShopType"]]:
                final[ShopGood["ShopType"]].update({ SubID : {}})

            final[ShopGood["ShopType"]][SubID].update({item : temp})

        else:

            final[ShopGood["ShopType"]].update({item : temp})
    with open(GDBT.ExCI(Stage_3,"ShopMap.json"), "w", encoding='utf-8') as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def main():
    Char_Mapper()
    Item_Mapper()
    Weapon_Mapper()
    Artif_Mapper()
    Furn_Mapper()
    Mon_Mapper()
    Mech_Mapper()
    Quest_Mapper()
    Shop_Mapper()

if __name__ == "__main__":
    main()

