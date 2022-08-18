#RUBIKK NFT GENERATOR V 1.0
#  ______ _______ ______ _______ __  __ __  __ 
# |   __ \   |   |   __ \_     _|  |/  |  |/  |
# |      <   |   |   __ <_|   |_|     <|     < 
# |___|__|_______|______/_______|__|\__|__|\__|
#                                        __   __  _       __  
#                                        \ \ / / / |     /  \ 
#                                         \ V /  | |    | () |
#                                          \_/   |_| (_) \__/ 
                                                        

import os
from random import randint
from libraries import Image
import time
import json
import hashlib



#Collection size and block-chain
Number_Of_NFTS_To_Generate = 50
BlockChain = "ETH"        #REPLACE THIS WITH "SOL" FOR SOLANA METADATA 


#General Metadata for Eth and Sol
CollectionName = "The MineCraft Steve "
description = "Enter you NFT description here" 

#Base Uri
Uri = "ipfs://Replace New Uri Here" 

#Order your layers here:
LayerS_Order = [
    'Background',
    'pants',
    'shirt',
    'shoes',
    'head',
    'access_maskss',
    'accesories_blocks'
]

#General Metadata for solana
symbol = "SYC"
seller_fee_basis_points = 1000 #Secondary market sales 1000 = 10%
external_url = "https://en.wikipedia.org/wiki/Solana_(blockchain_platform)"
creators = [
    {
        "address": "Add your wallet address here!",
        "share": 100, 
    }
]


#Extra Metadata for ETH and SOL
ExtraMetadata = { 
    "compiler": "Rubik v 1.0"
}




CustomMetadata = { #Will be implemented in v 2.0
    
}

#Duplicate tolerance is used as a delimiter for ending the program if there too many duplicates are generated.
DuplicateTolerancee = 1000   # Our Program will end if duplicates are more than 1000


#Global declarations - Configuration can be done here by changing variables
OutputFolderName = "outfile"
InputLayerFolder = "layers"
jsonFolderName = "JSON METADATA"
startTime = int(time.time() * 1000)
EndTime = 0
#Dictionary for storing directory/folder/file tree
dh = None


#This list will store all the IDs for different images. IDs will be combined and then converted into md5 hash
layerIdList = list()


#This set will store image hash/Dna
hashlisst = set()

#THIS WILL MAKE OUR OUTPUT FOLDER
def MakeOutputFolder():
    try:
        os.mkdir(OutputFolderName)
        os.mkdir(os.path.join(OutputFolderName,jsonFolderName))

    except:
        print(f"Output File already exists!")


#MERGE OR LAYER IMAGES
def merge(ListOfimgesToLayer):
    #print(ListOfimgesToLayer, len(ListOfimgesToLayer))
    i = 0
    lengthOfList = len(ListOfimgesToLayer)
    RootImage = Image.open(ListOfimgesToLayer[0])
    while(i < lengthOfList-1):
        newlayer = Image.open(ListOfimgesToLayer[i+1])
        RootImage.paste(newlayer, (0, 0), newlayer)
        #print(i+1, lengthOfList)
        newlayer.close()
        i+=1

    return RootImage



#SAVE GENERATED IMAGE   
def saveimg(img, n):
    if BlockChain == "SOL":
        n-=1
    fnamee =  CollectionName + str(n) + ".png"
    try:
        SaveFileLocation = os.path.join(OutputFolderName, fnamee)
        img.save(SaveFileLocation)
        print(f"Image {n} saved successfully!")
        return SaveFileLocation 
    except:
        print(f"ERROR SAVING IMG!")
        quit()

def deleteimg(imgpathh):
    if os.path.exists(imgpathh):
        os.remove(imgpathh)
        print(f"Duplicate removed successfully!")
    else:
        print(f"Error removed file!")
        quit()

def GetDictionaryOfFolderAndFiles():
    local_dh = dict()
    foldersInLayers = os.listdir('./' + InputLayerFolder)
    for folder in foldersInLayers:
        local_dh[folder] = os.listdir(os.path.join(InputLayerFolder, folder))
    return local_dh
    #print(foldersInLayers)

def SetLayerOrder(dh): #This function will be implemented in V 2.0
    print("")


def generateMetadata(attributeList, nftnum, hashDNA):
    if BlockChain == "ETH":
        nftnum+=1
        x = {
            "name": CollectionName + "#" + str(nftnum),
            "description": description,
            "image": Uri,
            "dna": hashDNA,
            "date": int(time.time() * 1000),
            "attributes": attributeList,
            "compiler": "Rubik v 1.0"

        }
        x.update(ExtraMetadata)        

    elif BlockChain == "SOL":
        nftnum+=1
        x = {
            "symbol": symbol,
            "name": CollectionName + "#" + str(nftnum-1),
            "description": description,
            "seller_fee_basis_points": seller_fee_basis_points,
            "image": str(nftnum-1) + ".png",
            "edition": nftnum-1,
            "external_url": external_url,
            "attributes": attributeList,
            "properties": {
                "files": [
                {
                    "uri": str(nftnum-1) + ".png",
                    "type": "image/png"
                }
                ],
                "category": "image",
                "creators": creators
            },
            "compiler": "Rubik v 1.0"
        }
        x.update(ExtraMetadata)

    else:
        quit()

    
    if BlockChain == "SOL":
        jsonFilename = CollectionName + str(nftnum-1) + ".json"
    else:
        jsonFilename = CollectionName + str(nftnum) + ".json"
    JoinedjsonFPath = os.path.join(OutputFolderName, jsonFolderName, jsonFilename)
    with open(JoinedjsonFPath, 'w') as outfile:
        json.dump(x, outfile)
        return JoinedjsonFPath

def deleteMetaData(Metapathh):
    if os.path.exists(Metapathh):
        os.remove(Metapathh)
        print(f"Metadata removed successfully!")
    else:
        print(f"Error removed file!")
        quit()


    
def get_hash(img_path):
    # This function will return the `md5` checksum for any input image.
    with open(img_path, "rb") as f:
        img_hash = hashlib.md5()
        while chunk := f.read(8192):
           img_hash.update(chunk)
    return img_hash.hexdigest()
        
def saveHashValue(hashstr):
    hashlisst.add(hashstr)

def deleteHashValue(hashstring):
    hashlisst.discard(hashstring)

def HashAlreadyExists(newHash):
    if newHash in hashlisst:
        return True
    else:
        return False


def generateImages(to_generate, newDH, DUPLICATEtolerance):
    generatedd = 0 
    randNum = 0
    randSelectedImg = None
    imgsToLayer = list()
    while(generatedd < to_generate):
        attributess = list() 
        for traitType in LayerS_Order:
            imglist = newDH[traitType]
            randNum = randint(0,len(imglist)-1)
            randSelectedImg = imglist[randNum]
            selectedImg = randSelectedImg.replace(".png", "")
            attributess.append({"trait_type": traitType, "value": selectedImg})
            imgsToLayer.append(os.path.join(InputLayerFolder, traitType, randSelectedImg))
            #print(randSelectedImg)
        #print("--------------")
        GenrtdImg = merge(imgsToLayer)
        #print(attributess)
        savedImgpath = saveimg(GenrtdImg, generatedd+1)
        hashhValue = get_hash(savedImgpath)
        SavedMetaDataPATH = generateMetadata(attributeList=attributess, nftnum=generatedd, hashDNA=hashhValue)
        if HashAlreadyExists(hashhValue):
            DUPLICATEtolerance -= 1
            print(DUPLICATEtolerance)
            if DUPLICATEtolerance == -1:
                print(f"Too many duplicates detected! Please add more layers.")
                quit()
            print(f"Duplicate found!")
            #DuplicateTolerance-=1
            deleteimg(savedImgpath)
            deleteMetaData(SavedMetaDataPATH)
        else:
            saveHashValue(hashhValue)
            generatedd+=1
        print(hashhValue)
        #print(f"SAVED IMAGE PATH: {savedImgpath}")
        imgsToLayer.clear()
        attributess.clear()
    imgsToLayer.clear()


def main():
    dh = GetDictionaryOfFolderAndFiles()
    MakeOutputFolder()
    generateImages(Number_Of_NFTS_To_Generate, dh, DuplicateTolerancee)
    EndTime = int(time.time() * 1000)
    print(f"Total time taken: {(EndTime - startTime)/(1000*60)} minutes")

main()# RUBIK-NFT-Generator
