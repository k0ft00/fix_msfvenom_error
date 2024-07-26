import os

print(
    """

`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
                                     .$"
                                     "
1. apktool
2. zipalign
3. apksigner
"""
)
print("tele: @Cif_3")
w = input("Enter a number your problem : ")

if w == "1":
    os.system("bash bash_file/apktool.sh")
    print("apktool is solved")
elif w == "2":
    os.system("bash bash_file/zipalign.sh")
    print("zipalign is solved")
elif w == "3":
    os.system("bash bash_file/apksigner.sh")
    print("apksigner is solved")
else:
    print("not found")
