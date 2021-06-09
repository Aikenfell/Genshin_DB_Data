import os
import json

os.chdir(os.path.dirname(__file__))
mydir = os.path.dirname(__file__) or "."
Base_Data = os.path.join(mydir, "Base_Data")
Remapped_Data = os.path.join(mydir, "Remapped_Data")
Out_Files = os.path.join(mydir, "Out_Files")


def ranger(base,max):
    ret = []
    for item in range(base,max):
        ret.append(item)
    return ret

def Baseloader(Loc):
    Loc = os.path.join(Base_Data , Loc)
    with open(Loc, encoding='utf-8') as temp:
        NTemp = json.load(temp)
    return(NTemp)

def Stageloader(Loc, Stage ="F"):
    Loc = os.path.join(mydir, "Stage_"+str(Stage) , Loc)
    with open(Loc, encoding='utf-8') as temp:
        NTemp = json.load(temp)
    return(NTemp)

def RMaploader(Loc):
    Loc = os.path.join(Remapped_Data , Loc)
    with open(Loc, encoding='utf-8') as temp:
        NTemp = json.load(temp)
    return(NTemp)

def Outloader(Loc):
    Loc = os.path.join(Out_Files , Loc)
    with open(Loc, encoding='utf-8') as temp:
        NTemp = json.load(temp)
    return(NTemp)

def Loader(Loc,Ob=False):
    with open(Loc, encoding='utf-8') as temp:
        NTemp = json.load(temp)
    return(NTemp)

def BinLoader(Loc,Ob=False):
    if Ob:
        with open(os.path.join("Stage_0" ,Loc),"r", encoding='utf-8') as temp:
            Base = temp.read()
            NTemp = DOB(Base)
            NTemp = json.loads(NTemp)

    else:
        with open("Stage_0" ,Loc, encoding='utf-8') as temp:
            NTemp = json.load(temp)
    return(NTemp)

def DOB(Fil):
    Pack = Stageloader("DO.json","L")
    for item in Pack:
        Fil = Fil.replace(item,Pack[item])
    return(Fil)

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

def timeconv(st):
    FT = []
    H = st//(60*60)
    st = st%(60*60)
    print(st)
    M = st//(60)
    S = st
    #st = st-S
    #M = st//(60)
    #st = st-M
    if H != 0 :
        FT.append(str(H)+" Hour(s)")

    if M != 0 :
        FT.append(str(M)+" Minute(s)")

    if S != 0 :
        FT.append(str(S)+" Second(s)")
    return(" - ".join(FT))

#print(timeconv(54001))


Lang_EN = Stageloader("TextMapEN.json","L")
Lang_CHS = Stageloader("TextMapCHS.json","L")
MaterialData = Stageloader("MaterialData.json","1")
HomeWorldFurnitureData = Stageloader("HomeWorldFurnitureData.json","1")
WeaponData = Stageloader("WeaponData.json","1")
ReliquaryData = Stageloader("ReliquaryData.json","1")
RewardData = Stageloader("RewardData.json","1")
RewardPreviewData = Stageloader("RewardPreviewData.json","1")
DisplayItemData = Stageloader("DisplayItemData.json","1")

def ItemNamRet(st,lang=Lang_EN):
    if str(st) in MaterialData:
        Nam = MaterialData[str(st)]["NameTextMapHash"]
    elif str(st) in HomeWorldFurnitureData:
        Nam = HomeWorldFurnitureData[str(st)]["NameTextMapHash"]
    elif str(st) in WeaponData:
        Nam = WeaponData[str(st)]["NameTextMapHash"]
    elif str(st) in ReliquaryData:
        Nam = ReliquaryData[str(st)]["NameTextMapHash"]
    elif str(st) in DisplayItemData:
        Nam = DisplayItemData[str(st)]["NameTextMapHash"]
    else:
        for item in HomeWorldFurnitureData:
            if str(HomeWorldFurnitureData[item]["Id"]) == str(st):
                return(HomeWorldFurnitureData[item]["NameTextMapHash"])
        Nam = "Data Error"#"1769963853"
    return Nam

def RewardTrans(st,lang=Lang_EN):
    TList = {}
    if str(st) not in RewardData:
        return(TList)
    if "PlayerExp" in RewardData[str(st)]:
        TList.update({conv(ItemNamRet(102),lang) : RewardData[str(st)]["PlayerExp"] })
    if "Scoin" in RewardData[str(st)]:
        TList.update({conv(ItemNamRet(202),lang) : RewardData[str(st)]["Scoin"] })
    for item in RewardData[str(st)]["RewardItemList"]:
        if item != {}:
            TList.update({econv(ItemNamRet(item["ItemId"]),lang) : item["ItemCount"] })
    return TList

def RewardPreviewTrans(st,lang=Lang_EN):
    TList = {}
    if str(st) not in RewardPreviewData:
        return(TList)
    for item in RewardPreviewData[str(st)]["PreviewItems"]:
        if item != {"Count": ""}:
            TList.update({econv(ItemNamRet(item["Id"]),lang) : item["Count"] })
    return TList

def conv(st,lang=Lang_EN):
    st = str(st)
    if st == "3816664530":
        st = "2329553598"
    elif st == "1533656818":
        st = "1818743358"
        
    if st in [""]:
        return ""
    elif st in ["QUALITY_BLUE"]:
        return "3"
    elif st in ["QUALITY_PURPLE"]:
        return "4"
    elif st in ["QUALITY_ORANGE"]:
        return "5"
    elif st in lang.keys():
        return repla(lang[st])
    else:
        print(st)
        return("")

def econv(st,lang=Lang_EN):
    st = str(st)
    if st == "3816664530":
        st = "2329553598"
    elif st == "1533656818":
        st = "1818743358"
        
    if st in [""]:
        return ""
    elif st in ["QUALITY_BLUE"]:
        return "3"
    elif st in ["QUALITY_PURPLE"]:
        return "4"
    elif st in ["QUALITY_ORANGE"]:
        return "5"
    elif st in lang.keys():
        Ret = repla(lang[st])
        if Ret == "":
            Ret = repla(Lang_CHS[st])
        return Ret
    elif st in Lang_CHS.keys():
        return(Lang_CHS[st])
    else:
        print(st)
        return("")

def repla(st):
    st = st.replace("<color=#FF9999FF>","**")##Pyro Replace
    st = st.replace("<color=#FFE14BFF>","**")##Null Replace
    st = st.replace("<color=#80FFD7FF>","**")##Anemo Replace
    st = st.replace("<color=#FFD780FF>","**")##Anemo Replace
    st = st.replace("<color=#99FFFFFF>","**")##Cryo Replace
    st = st.replace("<color=#80C0FFFF>","**")##Hydro Replace
    st = st.replace("<color=#FFACFFFF>","**")##Electro Replace
    st = st.replace("<color=#FFE699FF>","**")##Geo Replace
    st = st.replace("<i>","_")##Italic Replace
    st = st.replace("</i>","_")##Italic Replace
    st = st.replace("<color=#FFD780FF>","**")##Unknown Replace
    st = st.replace("\u00b7","\t-")##Bullet Point Replace
    st = st.replace("\\n","\n")##Double Tab Replace
    st = st.replace("\\\\n","\\n")##Double Tab Replace

    st = st.replace("{LAYOUT_MOBILE#Tap}{LAYOUT_PC#Press}{LAYOUT_PS#Press}","Tap")##Hold Prompt Replace
    st = st.replace("{LAYOUT_MOBILE#Tapping}{LAYOUT_PC#Press}{LAYOUT_PS#Press}","Tapping")##Hold Prompt Replace
    st = st.replace("#","")##Italic Replace
    st = st.replace("</color>","**")##Color End Replace
    return st

