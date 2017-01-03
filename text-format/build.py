# -*- coding: utf-8 -*-


from distutils.core import setup  
import py2exe  
  
includes = ["encodings", "encodings.*"]  
  
options = {"py2exe":    
            {"compressed": 1,      # 压缩    
             "optimize": 2,        # 优化级别  
             "ascii": 1,           #   
             "includes":includes,  # 编码方式  
             "bundle_files": 1     # 所有文件打包成一个zipfile或exe文件，有效级别1，2，3  
            }}  
setup(  
    options=options,               # 是否需要可选项，默认为None  
    zipfile=None,                  # 是否需要压缩像，默认为None  
    console=[{"script": "HelloCmd.py", "icon_resources": [(1, "pc.ico")]}], # 针对CMD控制端口   
    windows=[{"script": "HelloWin.py", "icon_resources": [(1, "pc.ico")]}], # 针对GUI图形窗口  
    data_files=[("magic",["App_x86.exe",]),],  
    version = "v1.01",             # 版本信息  
    description = "py2exe testing",# 描述信息   
    name = "rw, Py2exe",        # 名字信息  
)  