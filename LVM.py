import os
import getpass
os.system("tput setaf 11")
os.system("clear")
print("\n ----------------------------------------------------------------------------------------------")
os.system("tput setaf 5")
print("\t\t\t\t\t WELCOME TO MY MENU !!!")
os.system("tput setaf 11")
print("\n ----------------------------------------------------------------------------------------------")
password=getpass.getpass("\n\n Enter the password : ")

if password != "APARTH":
    print("password is incorrect, please provide correct password\n")
    exit()

while(1):
                os.system("tput setaf 20")
                os.system("clear")
                LVM=input("""
1.PHYSICAL VOLUME
2.VOLUME GROUP
3.LOGICAL VOLUME
4.EXIT

Enter your choice: """)
                if(LVM=="1"):
                    os.system("clear")
                    os.system("tput setaf 85")
                    PV=input("""
1. Create PV
2. Display PV 
3. Go back to main menu

Enter your choice: """)
                    if(PV=="1"):
                        os.system("clear")
                        CREATE_PV=input("\n Enter the path of harddisk : ")
                        os.system("pvcreate {}".format(CREATE_PV))
                        input("\n\n Press 'ENTER' to go back to main menu.... ") 

                    if(PV=="2"):
                        os.system("clear")
                        DISPLAY_PV=input("Enter 'ALL' to see all Physical Volume or give the path of specific Physical Volume : ")
                        if DISPLAY_PV == "ALL" :
                            os.system("pvdisplay")
                        if DISPLAY_PV!= "ALL" :
                            os.system("pvdisplay {}".format(DISPLAY_PV))
                        input("\n\nPress 'ENTER' to go back to main menu.... ") 

                    if(PV=="3"):
                        os.system("clear")
                        continue

                if(LVM=="2"):
                    os.system("clear")
                    os.system("tput setaf 75")
                    VG=input("""
1.Create VG
2.Extend VG
3.Display VG
4.To Go back to main menu

Enter your choice: """)

                    if(VG=="1"):
                        os.system("clear")
                        VG_NAME=input("\nEnter the name of Volume Group : ")
                        VG_CREATE=input("Enter the path of Physical Volume : ")
                        os.system("vgcreate {} {}".format(VG_NAME,VG_CREATE))
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(VG=="2"):
                        os.system("clear")
                        VG_EXNAME=input("\nEnter the name of Volume Group : ")
                        VG_EXCREATE=input("Enter the path of Physical Volume : ")
                        os.system("vgextend {} {}".format(VG_EXNAME,VG_EXCREATE))
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(VG=="3"):
                        os.system("clear")
                        VG_DISPLAY=input("Enter 'ALL' to see all Volume Group or give the name of specific Volume Group : ")
                        if VG_DISPLAY == "ALL" :
                            os.system("vgdisplay")
                        if VG_DISPLAY != "ALL" :
                            os.system("vgdisplay {}".format(VG_DISPLAY))
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(VG=="4"):
                        os.system("clear")
                        continue


                if(LVM=="3"):
                    os.system("clear")
                    os.system("tput setaf 135")
                    LV=input("""
1.Create LV
2.Extend LV
3.Display LV
4.To Go back to main menu

Enter your choice: """)
                    if(LV=="1"):
                        os.system("clear")
                        LV_NAME=input("\nEnter the name of Logical Volume : ")
                        LV_VGNAME=input("Enter the name of Volume Group : ")
                        LV_SIZE=input("Enter the size of Logical Volume : ")
                        os.system("lvcreate --size {} --name {} {}".format(LV_SIZE,LV_NAME,LV_VGNAME))
                        os.system("mkfs.ext4 /dev/{}/{}".format(LV_VGNAME,LV_NAME))
                        input("\n\n Press 'ENTER' to go back to main menu.... ")

                    if(LV=="2"):
                        os.system("clear")
                        LV_EXNAME=input("\nEnter the name of Logical Volume : ")
                        LV_EXVGNAME=input("Enter the name of Volume Group associated with this Logical Volume : ")
                        LV_EXSIZE=input("Enter the size to extend the Logical Volume : ")
                        os.system("lvextend --size +{} /dev/{}/{}".format(LV_EXSIZE,LV_EXVGNAME, LV_EXNAME))
                        os.system("resize2fs /dev/{}/{}".format(LV_EXVGNAME,LV_EXNAME))
                        input("\n\n Press 'ENTER' to go back to main menu.... ")

                    if(LV=="3"):
                        os.system("clear")
                        os.system("lvdisplay")
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(LV=="4"):
                        os.system("clear")
                        continue

                
                if(LVM=="4"):
                    os.system("clear")
                    exit()

