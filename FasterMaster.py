import os

#zawiera dwa elementy krotkii 1. to komenda , 2.opis
MAINDIC={"number>0":"odpowiadaja katalogowi",
          "f":"pokazuja wszystkie pliki w katalogu",
          "enter":"konczy program i wyswietla ostatni katalog",
          "0||zero":"cofa biezacy katolog o jeden",
          "help":"wyswietla wszystkie komendy",
        }

def whileDecisionIntInPut(lenght,dirbase,dicList):
    while True:
        number = intInPut(lenght,dirbase,dicList)
        if number != -1:
            break

def back(base,how_many=1):
    back_path = ""
    list = base.split("\\")[:-how_many]

    for d in list:
        back_path += d + "\\"

    return back_path[:-1]

def getFileList(base):
    fileList=[]
    for f in os.listdir(base):
        if os.path.isfile(os.path.join(base, f)):
            fileList.append(f)
    return fileList

def intInPut(lenght,base,dicList):
    print(base)
    number = input("give me number\t")

    if number.isdigit():
        number = int(number)

        if number == 0:
            d = back(base,1)
            return underMain(d)

        if number > lenght:
            return -1

        if number < 0:
            return -1

        return underMain(os.path.join(base, dicList[number - 1]))

    else:
        if number == "" or number=="enter":
            end(base)
        elif number=="f":
            listFile = getFileList(base)
            printList(listFile, False)
            return -1
        elif number=="help":
            for help in sorted(MAINDIC.keys()):
                print(help.rjust(10)+"\t-->\t"+MAINDIC[help])
            return -1
        elif "0" in number and len(number)-number.count("0")-number.count(" ")==0:
            d = back(base,number.count("0"))
            return underMain(d)
        elif number.lower()==base[0].lower():
            return underMain(base[:3])
        else:
            return -1

def current_directory():
    return os.getcwd()

def end(dirEnd):
    print(dirEnd)
    print("cd " + dirEnd)
    os.system("cd " + dirEnd)
    exit()

def getListDic(dirbase):
    dicList=[]
    try:
        for f in os.listdir(dirbase):
            if os.path.isdir(os.path.join(dirbase, f)):
                dicList.append(f)
        return dicList
    except PermissionError:
        print("Odmowa dostepu do "+dirbase)
        b=back(dirbase,1)
        return underMain(b)
    except FileNotFoundError:
        print("Odmowa dostepu do "+dirbase)
        b=back(dirbase,1)
        return underMain(b)
    except:
        print("cos nie tak nie rob tego ponownie")
        return underMain(current_directory())


def printList(list,boolen=True):
    os.system("cls")
    if boolen:
        for i, element in enumerate(list):
            print("%d: %s" % (1 + i, element))
    elif not boolen:
        for element in list:
            print(element)

def underMain(path):
    if len(path)==2:
        path+="\\"
    dicList = getListDic(path)
    lenght = len(dicList)

    if lenght > 0:
        printList(dicList)
        whileDecisionIntInPut(lenght,path,dicList)

    else:
        print("it is last dir")
        whileDecisionIntInPut(0,path,dicList)

def main():
    print("jezeli czegos nie wiesz wpisz help")
    path = current_directory()
    path=back(path)
    print(path)
    underMain(path)

if __name__=="__main__":
    main()
