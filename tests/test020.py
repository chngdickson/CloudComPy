#!/usr/bin/env python3

##########################################################################
#                                                                        #
#                                PYCC                                    #
#                                                                        #
#  This program is free software; you can redistribute it and/or modify  #
#  it under the terms of the GNU Library General Public License as       #
#  published by the Free Software Foundation; version 2 or later of the  #
#  License.                                                              #
#                                                                        #
#  This program is distributed in the hope that it will be useful,       #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          #
#  GNU General Public License for more details.                          #
#                                                                        #
#          Copyright 2020 Paul RASCLE www.openfields.fr                  #
#                                                                        #
##########################################################################

import os
import sys
import math
from gendata import getSampleCloud, getSampleCloud2, dataDir, isCoordEqual, createSymbolicLinks
import cloudComPy as cc
createSymbolicLinks() # required for tests on build, before cc.initCC

cc.initCC()  # to do once before using plugins or dealing with numpy

cloud = cc.loadPointCloud(getSampleCloud2(3.0, 0, 0.1))
cloud.setName("cloud")
if cloud.size() != 10000:
    raise RuntimeError

mesh = cc.ccMesh.triangulate(cloud, cc.TRIANGULATION_TYPES.DELAUNAY_2D_AXIS_ALIGNED)
mesh.setName("mesh")
if not math.isclose(mesh.size(), 19602, rel_tol=5e-02):
    raise RuntimeError

meshSize = mesh.size()

cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.asc")) # OK
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.xyz")) # OK (idem .asc)
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.las")) # OK
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.E57")) # OK  FileIO::setWriterInfo has not been called
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.sbf")) # OK
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.ply")) # OK  FileIO::setWriterInfo has not been called
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.vtk")) # OK
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.dxf")) # OK
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.pcd")) # OK
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.shp")) # OK
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.pn"))  # NOK cloudComPy.CC_FILE_ERROR.CC_FERR_BAD_ENTITY_TYPE
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.pv"))  # OK
cc.SavePointCloud(cloud, os.path.join(dataDir, "cloud.bin")) # OK

cloudasc = cc.loadPointCloud(os.path.join(dataDir, "cloud.asc"))
if cloudasc.size() != 10000:
    raise RuntimeError

cloudxyz = cc.loadPointCloud(os.path.join(dataDir, "cloud.xyz"))
if cloudxyz.size() != 10000:
    raise RuntimeError

cloudlas = cc.loadPointCloud(os.path.join(dataDir, "cloud.las"))
if cloudlas.size() != 10000:
    raise RuntimeError

cloudE57 = cc.loadPointCloud(os.path.join(dataDir, "cloud.E57"))
if cloudE57.size() != 10000:
    raise RuntimeError

cloudsbf = cc.loadPointCloud(os.path.join(dataDir, "cloud.sbf"))
if cloudsbf.size() != 10000:
    raise RuntimeError

cloudply = cc.loadPointCloud(os.path.join(dataDir, "cloud.ply"))
if cloudply.size() != 10000:
    raise RuntimeError

cloudvtk = cc.loadPointCloud(os.path.join(dataDir, "cloud.vtk"))
if cloudvtk.size() != 10000:
    raise RuntimeError

clouddxf = cc.loadPointCloud(os.path.join(dataDir, "cloud.dxf"))
if clouddxf.size() != 10000:
    raise RuntimeError

cloudpcd = cc.loadPointCloud(os.path.join(dataDir, "cloud.pcd"))
if cloudpcd.size() != 10000:
    raise RuntimeError

cloudshp = cc.loadPointCloud(os.path.join(dataDir, "cloud.shp"))
if cloudshp.size() != 10000:
    raise RuntimeError

cloudpv = cc.loadPointCloud(os.path.join(dataDir, "cloud.pv"))
if cloudpv.size() != 10000:
    raise RuntimeError

cloudbin = cc.loadPointCloud(os.path.join(dataDir, "cloud.bin"))
if cloudbin.size() != 10000:
    raise RuntimeError

cc.SaveMesh(mesh, os.path.join(dataDir, "mesh.ma"))  # NOK cloudComPy.CC_FILE_ERROR.CC_FERR_BAD_ENTITY_TYPE
cc.SaveMesh(mesh, os.path.join(dataDir, "mesh.dxf")) # OK  FileIO::setWriterInfo has not been called
cc.SaveMesh(mesh, os.path.join(dataDir, "mesh.off")) # OK
cc.SaveMesh(mesh, os.path.join(dataDir, "mesh.stl")) # OK
cc.SaveMesh(mesh, os.path.join(dataDir, "mesh.vtk")) # OK
cc.SaveMesh(mesh, os.path.join(dataDir, "mesh.obj")) # OK  FileIO::setWriterInfo has not been called
cc.SaveMesh(mesh, os.path.join(dataDir, "mesh.ply")) # OK  FileIO::setWriterInfo has not been called
cc.SaveMesh(mesh, os.path.join(dataDir, "mesh.bin")) # NOK cloudComPy.CC_FILE_ERROR.CC_FERR_BROKEN_DEPENDENCY_ERROR
cc.SaveMesh(mesh, os.path.join(dataDir, "mesh.fbx")) # OK

meshdxf = cc.loadMesh(os.path.join(dataDir, "mesh.dxf"))
if meshdxf.size() != meshSize:
    raise RuntimeError

meshoff = cc.loadMesh(os.path.join(dataDir, "mesh.off"))
if meshoff.size() != meshSize:
    raise RuntimeError

meshstl = cc.loadMesh(os.path.join(dataDir, "mesh.stl"))
if meshstl.size() != meshSize:
    raise RuntimeError

meshvtk = cc.loadMesh(os.path.join(dataDir, "mesh.vtk"))
if meshvtk.size() != meshSize:
    raise RuntimeError

meshobj = cc.loadMesh(os.path.join(dataDir, "mesh.obj"))
if meshobj.size() != meshSize:
    raise RuntimeError

meshply = cc.loadMesh(os.path.join(dataDir, "mesh.ply"))
if meshply.size() != meshSize:
    raise RuntimeError

meshfbx = cc.loadMesh(os.path.join(dataDir, "mesh.fbx"))
if meshfbx.size() != meshSize:
    raise RuntimeError

cc.SaveEntities([cloud,mesh], os.path.join(dataDir, "meshCloud.bin"))
res = cc.importFile(os.path.join(dataDir, "meshCloud.bin"))
aMesh=res[0][0]
if aMesh.size() != meshSize:
    raise RuntimeError
aCloud=aMesh.getAssociatedCloud()
if aCloud.size() != 10000:
    raise RuntimeError


