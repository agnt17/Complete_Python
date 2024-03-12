from Basics import fun
fun(8)

#  Everything is fine here but as we import from 1 python file to other python file we get a folder named __pychache__. What does this folder mean?

# Internal Working of Python: 
    # Basically Python also Produces ByteCode which is fed to Virtual Machine... This __pychache__ folder is written in Byte code and it is fast to execute cause it is more in LOW LEVEL LANGUAGE. Its extension is .pyc 
    
    # Python HLL is "COMPILED" to Byte Code. This .pyc is called Frozen Binaries.
    
    # FROZEN BINARIES: Frozen binaries typically refer to compiled, executable files that have been "frozen" or packaged with all their dependencies into a single, standalone binary file. 
    
    # PVM: PYTHON VIRTUAL MACHINE is an Engine similar to V8 engine of JS. This engine runs the byte code of python. It is basically a code loop that runs python 
    
    # BYTE code is not Machine Code it is upper level than Machine code 
    
    
    # PYTHON HLL -----(COMPILER)-----> BYTE CODE -----(PVM)----> MACHINE CODE 
    
    # while using shell sometimes we just import the file and then make changes their then after importing any furthur changes wont be included thus to reload the file status python provides us a reload functionality now...
    
    # from importlib import reload
    # reload("file_name_to_be_changed")