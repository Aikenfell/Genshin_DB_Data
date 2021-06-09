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
Stage_1 = os.path.join(mydir, "Stage_1")
Stage_E = os.path.join(mydir, "Stage_E")

DialogData = GDBT.Stageloader("DialogData.json",1)
NpcData = GDBT.Stageloader("NpcData.json",1)
LangEN = GDBT.Stageloader("TextMapEN.json","L")

def MTMConv():
    Out = os.path.join(Stage_E,"ManualTextMapConfigData.json")
    Target = GDBT.Stageloader("ManualTextMapConfigData.json",1)
    Final = {}
    for item in Target:
        TarDat = Target[item]
        Final.update({item : GDBT.econv(TarDat["TextMapContentTextMapHash"])})

    with open(Out, "w",encoding="utf-8") as write_file:
        json.dump(Final, write_file, indent=4, ensure_ascii=False)
def delver(Hole,lan=LangEN):
    End = []
    #if type(Hole) == int:
        #Hole = str(Hole)
    for item in Hole:
        if type(item) == list:
            for Branch in item:
                End.append(delver(Branch,lan))
            
        else:
            DDL = DialogData[str(item)]
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
                Name = GDBT.econv(NpcData[NPCN["Id"]]["NameTextMapHash"],lan)
            End.append(Name+" : "+GDBT.econv(DDL["TalkContentTextMapHash"],lan))
    return(End)


def DialogueDump():
    final = {}
    Out = os.path.join(Stage_E,"StrainedDialog.json")
    Target = GDBT.Stageloader("StrainedDialog.json",2)
    for Item in Target:
        temp = {}
        Field = Target[Item]
        temp.update({"Id" : Field["Id"]})
        temp.update({"Next" : Field["Next"]})
        temp.update({"LineSpoken" : GDBT.econv(Field["LineSpoken"])})
        temp.update({"Title" : GDBT.econv(Field["Title"])})
        temp.update({"Role" : GDBT.econv(Field["Role"])})
        final.update({ Item : temp })
    with open(Out, "w",encoding="utf-8") as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def TalkDump():
    final = {}
    Out = os.path.join(Stage_E,"TalkCompact.json")
    Target = GDBT.Stageloader("TalkCompact.json",2)
    for Item in Target:
        Field = Target[Item]
        Starter = Field["First Line"]
        try:
            temp = delver(Field["First Line"])
        except:
            temp = Field["First Line"]
        final.update({ Item : temp })
    with open(Out, "w",encoding="utf-8") as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)

def FeatureTagGroupData():
    final = {}
    IGTD = GDBT.Stageloader("IGNTags.json",3)
    Out = os.path.join(Stage_E,"FeatureTagGroupData.json")
    Target = GDBT.Stageloader("FeatureTagGroupData.json",1)
    Charmap = GDBT.Stageloader("CharMap.json",3)
    Monmap = GDBT.Stageloader("MonMap.json",3)
    for Item in Target:
        Field = Target[Item]
        Starter = Field["TagIDs"]
        temp = []
        for Tag in Starter:
            if Tag == 0:
                continue
            temp.append(IGTD[str(Tag)]["TagName"])
        if Item in Charmap:
            final.update({ Item : {"Name" : Charmap[Item]["Helper"],"Tags" : temp} })
        elif Item in Monmap:
            final.update({ Item : {"Name" : "_".join(Monmap[Item]["Icon"].split("_")[2:]),"Tags" : temp} })
        else:
            final.update({ Item : {"Name" : "Other","Tags" : temp} })
    with open(Out, "w",encoding="utf-8") as write_file:
        json.dump(final, write_file, indent=4, ensure_ascii=False)


def TutorialDetailData():
    Out = os.path.join(Stage_E,"TutorialDetailData.json")
    Target = GDBT.Stageloader("TutorialDetailData.json",1)
    Final = {}
    for item in Target:
        TarDat = Target[item]
        Temp = [GDBT.econv(TarDat["DescriptTextMapHash"])]#{}
        """
        Temp.update({"Name" : GDBT.econv(TarDat["NameTextMapHash"])})
        Temp.update({"Desc" : GDBT.econv(TarDat["DescriptTextMapHash"])})
        """

        if TarDat["ImageNameList"] != []:
            if TarDat["ImageNameList"][0] not in Final:
                Final.update({TarDat["ImageNameList"][0] : Temp})
        else:
            Final.update({item : Temp})


    with open(Out, "w",encoding="utf-8") as write_file:
        json.dump(Final, write_file, indent=4, ensure_ascii=False)

def AvatarTalentData():
    Out = os.path.join(Stage_E,"AvatarTalentData.json")
    Target = GDBT.Stageloader("AvatarTalentData.json",1)
    Final = {}
    for item in Target:
        TarDat = Target[item]
        Temp = {}
        Temp.update({"Name" : GDBT.econv(TarDat["NameTextMapHash"])})
        Temp.update({"Desc" : GDBT.econv(TarDat["DescTextMapHash"])})

        Final.update({TarDat["OpenConfig"] : Temp})


    with open(Out, "w",encoding="utf-8") as write_file:
        json.dump(Final, write_file, indent=4, ensure_ascii=False)

def RewardData():
    Out = os.path.join(Stage_E,"RewardData.json")
    Target = GDBT.Stageloader("RewardData.json",1)
    Final = {}
    for item in Target:
        TarDat = Target[item]
        Temp = GDBT.RewardTrans(item)
        Final.update({item : Temp})


    with open(Out, "w",encoding="utf-8") as write_file:
        json.dump(Final, write_file, indent=4, ensure_ascii=False)

def RewardPreviewData():
    Out = os.path.join(Stage_E,"RewardPreviewData.json")
    Target = GDBT.Stageloader("RewardPreviewData.json",1)
    Final = {}
    for item in Target:
        TarDat = Target[item]
        Temp = {"Items" : GDBT.RewardPreviewTrans(item),"Desc" : TarDat["Desc"]}
        Final.update({item : Temp})


    with open(Out, "w",encoding="utf-8") as write_file:
        json.dump(Final, write_file, indent=4, ensure_ascii=False)


def main():
    #MTMConv()
    #TutorialDetailData()
    #AvatarTalentData()
    #RewardData()
    #DialogueDump()
    #TalkDump()
    #RewardPreviewData()
    FeatureTagGroupData()

if __name__ == "__main__":
    main()
