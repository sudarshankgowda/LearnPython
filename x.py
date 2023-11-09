"""
###############################################################################################
# Copyright (c) SanDisk Corp.2023 - All rights reserved.This code, and all
# derivative work, is the exclusive property of SanDisk and may not be used
# without SanDisk's authorization.
#
# FILE:GETSET028_HMB.py: Test to Verify Get Set for HMB feature and New HMB Allocate API
# AUTHOR: Sudarshan K
###############################################################################################
"""
import os
import sys
import unittest
import random
import CTFServiceWrapper as ServiceWrap
import NVMeCMDWrapper as NVMeWrap
import Protocol.NVMe.Basic.TestCase as TestCase
import Validation.TestFixture as TestFixture
import Validation.TestParams as TP
import Validation.RWCLib as RWCLib
import Validation.CMDUtil as CMDUtil
import Core.ValidationError as ValidationError


class GETSET028_HMB(TestCase.TestCase):

    def setUp(self):
        self.TF = TestFixture.TestFixture()
        self.commandHistory = self.TF.testSession.GetCmdHistory()
        self.errorManager = self.TF.testSession.GetErrorManager()
        self.startLBA = self.currCfg.variation.startlba
        self.WRLib = RWCLib.RWCLib()
        self.CMDUtil = CMDUtil.CMDUtil()
        self.startLba = self.currCfg.variation.startlba
        self.writeTimeout = self.currCfg.variation.writetimeout
        self.readTimeout = self.currCfg.variation.readtimeout
        self.CmdTimeout = 2000000
        self.commandsPerCycle = self.currCfg.variation.commandspercycle
        self.txLenMin = self.currCfg.variation.transferlengthmin
        self.txLenMax = self.currCfg.variation.transferlengthmax
        self.nameSpaceID = self.currCfg.variation.namespaceid
        self.bufferManager = self.TF.testSession.GetDTBufferManager()
        self.maxPatternID = self.bufferManager.GetMaxPatternID()
        self.MPS = 0
        self.MPSMAX = 0
        self.MPSMIN = 0
        self.Size = 0
        self.listOfHMBFragments1 = []
        self.RdWrCNTVal = 2

    def HBM(self):
        bitFlip = 1
        if(self.TF.HMPRE > 0):
            self.TF.logger.Message("%-35s: %s" % ('HMPRE: ', self.TF.HMPRE))
            self.TF.logger.Message("%-35s: %s" % ('HMMIN:', self.TF.HMMIN))
            self.TF.logger.Message("%-35s: %s" % ('MPSMAX: ', self.MPSMAX))
            self.TF.logger.Message("%-35s: %s" % ('MPSMIN:', self.MPSMIN))
            NS_ID = 0xFFFFFFFF
            RespStatus1 = 0xFF
            RespStatus2 = 0xFF
            RespStatus3 = 0xFF
            # Issue Get Feature command : FID= 0x0D
            self.__ControllerCCReg()
            sendType = ServiceWrap.SEND_IMMEDIATE
            # Issue Read & Writes-----------------------------------------------------------------------------
            RDWRCnt = self.RdWrCNTVal
            self.__IOs(RDWRCnt)
            self.TF.logger.Message("----- Issue Power-Cycle-------------------------------\n")
            self.__PwrCycle()
            self.TF.logger.Message("------------------------------------------------------\n")
            # Read Supported Cap HMB---------------------------------------------------------------------------
            Dis_HMB = 1
            if(Dis_HMB):
                try:
                    GetFeatureCapObj = NVMeWrap.GetFeatures(
                        NVMeWrap.FID_HOST_MEM_BUF, NVMeWrap.SUPPORTED_CAP, NS_ID, self.CmdTimeout, sendType = sendType, dwTimeOut = 0xFFFFFFFF)
                except ValidationError.CVFExceptionTypes as ex:
                    self.TF.logger.Fatal(
                        "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                    raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                RespStatus1 = GetFeatureCapObj.objNVMeComIOEntry.completionEntry.DW3.SF.SC
                self.TF.logger.Message("%-35s: %s" % ('Get SupportedCap CMD status', RespStatus1))
                self.TF.logger.Message("%-35s: %s" % ('Get Capbility DW0:  ',
                                                      GetFeatureCapObj.objNVMeComIOEntry.completionEntry.DW0))
                # Read Current HMB---------------------------------------------------------------------------------------
                try:
                    ObjGetFeature = NVMeWrap.GetFeatures(
                        NVMeWrap.FID_HOST_MEM_BUF, NVMeWrap.CURRENT, NS_ID, self.CmdTimeout, sendType = sendType, dwTimeOut = 0xFFFFFFFF)
                except ValidationError.CVFExceptionTypes as ex:
                    self.TF.logger.Fatal(
                        "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                    raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                RespStatus2 = ObjGetFeature.objNVMeComIOEntry.completionEntry.DW3.SF.SC
                self.TF.logger.Message("%-35s: %s" % ('HMB CMD status', RespStatus2))
                self.TF.logger.Message("%-35s: %s" %
                                       ('Current HMB ', ObjGetFeature.objNVMeComIOEntry.completionEntry.DW0))
                outputDW0 = ObjGetFeature.objNVMeComIOEntry.completionEntry.DW0
                self.TF.logger.Message("%-35s: %s" %
                                       ('HMB DW11: ', ObjGetFeature.objNVMeComIOEntry.completionEntry.DW0))
                # ObjGetFeature.outputDataBuffer.PrintToLog()
                # Issue Set Feature: HMB-----------------------------------------------------------------------
                if(outputDW0 == 1):
                    try:
                        ObjSetFeature = NVMeWrap.SetFeatures(
                            NVMeWrap.FID_HOST_MEM_BUF, False, 0, NS_ID, sendType = ServiceWrap.SEND_IMMEDIATE)
                        # UpdateEHM and MR  in DW-11--------------------------------------------------------------------
                        MR = 0
                        EHM = 0

                        # Issue Set HMBFeature----------------------------------------------------------------------
                    except ValidationError.CVFExceptionTypes as ex:
                        self.TF.logger.Fatal(
                            "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                        raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    RespStatus3 = ObjSetFeature.objNVMeComIOEntry.completionEntry.DW3.SF.SC
                    Res_DW0 = ObjSetFeature.objNVMeComIOEntry.completionEntry.DW0
                    self.TF.logger.Message("%-35s: %s" % ('DW0 After Enable HMB', Res_DW0))
                    # self.TF.logger.Message("%-35s: %s"%('Set HMB CMD status', RespStatus3))
                # Issue Read & Writes-----------------------------------------------------------------------------
            cnt = 1
            loopLmt = 10
            while(cnt < loopLmt):
                InLoop = cnt
                # Allocate memory
                isContiguous = random.randint(0, 1)
                self.TF.logger.Message("%-35s: %s" % ('isContiguous', isContiguous))
                if(cnt % 2 == 0):
                    self.MPS = 10
                    self.TF.logger.Message("%-35s: %s" % ('self.MPS', self.MPS))
                else:
                    self.MPS = 12
                    self.TF.logger.Message("%-35s: %s" % ('self.MPS', self.MPS))
                # Allocate HOst Memory Buffer----------------------------------------------------------------------------
                while(InLoop > 0):
                    chunkSize = (self.TF.HMMIN * 4096)
                    Low_Address_starts_at_16GB = 17179869184
                    High_Address_ends_at_17GB = 18253611008

                    obj = NVMeWrap.ALLOC_MEMORY_PAGES_PARAMS_SPECIFIED_RANGE()
                    obj.AllocSize = chunkSize
                    obj.StartAddress = Low_Address_starts_at_16GB
                    obj.EndAddress = High_Address_ends_at_17GB
                    self.listOfHMBFragments1.append(obj)
                    Low_Address_starts_at_16GB = 17179869184
                    High_Address_ends_at_17GB = 18253611008

                    obj1 = NVMeWrap.ALLOC_MEMORY_PAGES_PARAMS_SPECIFIED_RANGE()
                    obj1.AllocSize = chunkSize
                    obj1.StartAddress = 0
                    obj1.EndAddress = 0

                    obj2 = obj1
                    self.listOfHMBFragments1.append(obj1)
                    self.listOfHMBFragments1.append(obj2)

                    InLoop = InLoop - 1
                # ----------------------------------------------------------------------------------------------------
                HMBSETS = 1
                if(HMBSETS):
                    # Issue Read & Writes-----------------------------------------------------------------------------
                    RDWRCnt = self.RdWrCNTVal
                    self.__IOs(RDWRCnt)
                    # ------------------------------------------------------------------------------------------------
                    try:
                        hmbMemObj = NVMeWrap.AllocateHostMemoryBuffer(
                            self.listOfHMBFragments1, self.MPS, 0, True, isContiguous, sendType)
                    except ValidationError.CVFExceptionTypes as ex:
                        self.TF.logger.Fatal(
                            "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                        raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    self.TF.logger.Message("----- Issue Power-Cycle-------------------------------\n")
                    self.__PwrCycle()
                    self.TF.logger.Message("------------------------------------------------------\n")
                    # Issue Get HMBFeature----------------------------------------------------------------------
                    try:
                        ObjGetFeature = NVMeWrap.GetFeatures(
                            NVMeWrap.FID_HOST_MEM_BUF, NVMeWrap.CURRENT, NS_ID, self.CmdTimeout, sendType = sendType, dwTimeOut = 0xFFFFFFFF)

                        self.TF.logger.Message("%-35s: %s" %
                                               ('HMB DW11: ', ObjGetFeature.objNVMeComIOEntry.completionEntry.DW0))
                        self.TF.logger.Message(
                            "%-35s: %s" % ('HMDLLA', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.DESCRIPTOR_LIST_LOWER_ADDR.DescriptorListLowerAddr))
                        self.TF.logger.Message("%-35s: %s" %
                                               ('HMDLUA', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HMDLUA))
                        self.TF.logger.Message("%-35s: %s" %
                                               ('HMDLEC', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HMDLEC))
                        self.TF.logger.Message("%-35s: %s" %
                                               ('HSIZE', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HSIZE))
                    except ValidationError.CVFExceptionTypes as ex:
                        self.TF.logger.Fatal(
                            "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                        raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    # Issue Read & Writes-----------------------------------------------------------------------------
                    RDWRCnt = self.RdWrCNTVal
                    self.__IOs(RDWRCnt)
                    # ------------------------------------------------------------------------------------------------
                    if(bitFlip):
                        self.TF.logger.Message("----- Read HMB Buffer --------------------------------\n")
                        self.Size = chunkSize  # ?????????
                        buff = ServiceWrap.Buffer.CreateBuffer(
                            self.Size, patternType = ServiceWrap.ALL_0, isSector = False)
                        # buff.PrintToLog()
                        try:
                            hmbMemObj.ReadHMBMemory(hmbMemObj.DescriptorEntryListWithUserAddr[0].USER_MAPPED_ADDR, buff)
                        except ValidationError.CVFExceptionTypes as ex:
                            self.TF.logger.Fatal(
                                "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                            raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                        self.TF.logger.Message("------------------------------------------------------\n")
                        self.TF.logger.Message("----- Write HMB Buffer --------------------------------\n")
                        buff.Fill(0xAA)
                        try:
                            hmbMemObj.WritetoHMBMemory(
                                hmbMemObj.DescriptorEntryListWithUserAddr[0].USER_MAPPED_ADDR, buff)
                            hmbMemObj.ReadHMBMemory(hmbMemObj.DescriptorEntryListWithUserAddr[0].USER_MAPPED_ADDR, buff)
                        except self.TF.CVFExceptions as ex:
                            self.TF.logger.Fatal(
                                "Failed to Post Get Feature-HMB Exception Message is ->\n %s " % ex.GetFailureDescription())
                            self.TF.logger.FlushAllMsg()
                            assert(True == False), ex.GetFailureDescription()
                        buff.PrintToLog()
                        self.TF.logger.Message("------------------------------------------------------\n")
                    # Issue Read & Writes-----------------------------------------------------------------------------
                    RDWRCnt = self.RdWrCNTVal
                    self.__IOs(RDWRCnt)
                    # ------------------------------------------------------------------------------------------------
                    status = self.TF.threadPool.WaitForThreadCompletion()
                    # Issue Set Feature: HMB-----------------------------------------------------------------------
                    try:
                        ObjSetFeature = NVMeWrap.SetFeatures(
                            NVMeWrap.FID_HOST_MEM_BUF, False, 0, NS_ID, sendType = ServiceWrap.SEND_NONE)
                        # UpdateEHM and MR  in DW-11--------------------------------------------------------------------
                        MR = 0
                        EHM = 1
                        # Issue Set HMBFeature----------------------------------------------------------------------
                        ObjSetFeature.SetHMBFeature(EHM, MR, hmbMemObj)
                        self.TF.threadPool.PostRequestToWorkerThread(ObjSetFeature, sendType)
                        status = self.TF.threadPool.WaitForThreadCompletion()
                    except ValidationError.CVFExceptionTypes as ex:
                        self.TF.logger.Fatal(
                            "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                        raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    RespStatus3 = ObjSetFeature.objNVMeComIOEntry.completionEntry.DW3.SF.SC
                    Res_DW0 = ObjSetFeature.objNVMeComIOEntry.completionEntry.DW0
                    self.TF.logger.Message("%-35s: %s" % ('DW0 After Enable HMB', Res_DW0))
                    # Issue Read & Writes-----------------------------------------------------------------------------
                    self.TF.logger.Message("----- Issue Power-Cycle-------------------------------\n")
                    self.__PwrCycle()
                    self.TF.logger.Message("------------------------------------------------------\n")
                    RDWRCnt = self.RdWrCNTVal
                    self.__IOs(RDWRCnt)
                    # ------------------------------------------------------------------------------------------------
                    # Issue Get HMBFeature----------------------------------------------------------------------
                    try:
                        ObjGetFeature = NVMeWrap.GetFeatures(
                            NVMeWrap.FID_HOST_MEM_BUF, NVMeWrap.CURRENT, NS_ID, self.CmdTimeout, sendType = sendType, dwTimeOut = 0xFFFFFFFF)
                        # ObjGetFeature.outputDataBuffer.PrintToLog()#??
                        self.TF.logger.Message("%-35s: %s" %
                                               ('HMB DW11: ', ObjGetFeature.objNVMeComIOEntry.completionEntry.DW0))
                        self.TF.logger.Message(
                            "%-35s: %s" % ('HMDLLA', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.DESCRIPTOR_LIST_LOWER_ADDR.DescriptorListLowerAddr))
                        self.TF.logger.Message("%-35s: %s" %
                                               ('HMDLUA', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HMDLUA))
                        self.TF.logger.Message("%-35s: %s" %
                                               ('HMDLEC', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HMDLEC))
                        self.TF.logger.Message("%-35s: %s" %
                                               ('HSIZE', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HSIZE))
                    except ValidationError.CVFExceptionTypes as ex:
                        self.TF.logger.Fatal(
                            "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                        raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    if(bitFlip):
                        # Read HMB Buffer when HBM is Disable---------------------------------------------------------
                        try:
                            hmbMemObj.ReadHMBMemory(hmbMemObj.DescriptorEntryListWithUserAddr[0].USER_MAPPED_ADDR, buff)
                        except ValidationError.CVFExceptionTypes as ex:
                            self.TF.logger.Fatal(
                                "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                            raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                        buff.PrintToLog()
                    # ------------------------------------------------------------------------------------------------
                    # Issue Set Feature: HMB-----------------------------------------------------------------------
                    try:
                        ObjSetFeature = NVMeWrap.SetFeatures(
                            NVMeWrap.FID_HOST_MEM_BUF, False, 0, NS_ID, sendType = ServiceWrap.SEND_NONE)
                    except ValidationError.CVFExceptionTypes as ex:
                        self.TF.logger.Fatal(
                            "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                        raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    # Read HMB Buffer when HBM is Enable---------------------------------------------------------
                    if(bitFlip):
                        try:
                            hmbMemObj.ReadHMBMemory(hmbMemObj.DescriptorEntryListWithUserAddr[0].USER_MAPPED_ADDR, buff)
                        except ValidationError.CVFExceptionTypes as ex:
                            self.TF.logger.Fatal(
                                "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                            raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                        buff.PrintToLog()
                    # Disable-EHM and MR  in DW-11----------------------------------------------------------------
                    MR = 0
                    EHM = 0
                    try:
                        ObjSetFeature.SetHMBFeature(EHM, MR, hmbMemObj)
                        self.TF.threadPool.PostRequestToWorkerThread(ObjSetFeature, sendType)
                        status = self.TF.threadPool.WaitForThreadCompletion()
                    except ValidationError.CVFExceptionTypes as ex:
                        self.TF.logger.Fatal(
                            "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                        raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    RespStatus3 = ObjSetFeature.objNVMeComIOEntry.completionEntry.DW3.SF.SC
                    Res_DW0 = ObjSetFeature.objNVMeComIOEntry.completionEntry.DW0
                    self.TF.logger.Message("%-35s: %s" % ('DW0 After Enable HMB', Res_DW0))
                    self.TF.logger.Message("----- Issue Power-Cycle-------------------------------\n")
                    self.__PwrCycle()
                    self.TF.logger.Message("------------------------------------------------------\n")
                    # Issue Get HMBFeature----------------------------------------------------------------------
                    ObjGetFeature = NVMeWrap.GetFeatures(
                        NVMeWrap.FID_HOST_MEM_BUF, NVMeWrap.CURRENT, NS_ID, self.CmdTimeout, sendType = sendType, dwTimeOut = 0xFFFFFFFF)
                    self.TF.logger.Message("%-35s: %s" %
                                           ('HMB DW11: ', ObjGetFeature.objNVMeComIOEntry.completionEntry.DW0))
                    # ObjGetFeature.outputDataBuffer.PrintToLog()    #??
                    self.TF.logger.Message("%-35s: %s" % ('Allocation Type- isContiguous : ', isContiguous))
                    self.TF.logger.Message(
                        "%-35s: %s" % ('HMDLLA', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.DESCRIPTOR_LIST_LOWER_ADDR.DescriptorListLowerAddr))
                    self.TF.logger.Message("%-35s: %s" % ('HMDLUA', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HMDLUA))
                    self.TF.logger.Message("%-35s: %s" % ('HMDLEC', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HMDLEC))
                    self.TF.logger.Message("%-35s: %s" % ('HSIZE', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HSIZE))
                    # Deallocate Host Memory Buffer-------------------------------------------------------------------
                    if(bitFlip):
                        # Read HMB Buffer when HBM is Disable---------------------------------------------------------
                        try:
                            hmbMemObj.ReadHMBMemory(hmbMemObj.DescriptorEntryListWithUserAddr[0].USER_MAPPED_ADDR, buff)
                        except ValidationError.CVFExceptionTypes as ex:
                            self.TF.logger.Fatal(
                                "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                            raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                        buff.PrintToLog()
                    # ------------------------------------------------------------------------------------------------
                    doDeallocate = 0
                    if(doDeallocate):
                        try:
                            hmbMemObj.DeAllocateHostMemoryBuffer()
                        except ValidationError.CVFExceptionTypes as ex:
                            self.TF.logger.Fatal(
                                "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                            raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    # ------------------------------------------------------------------------------------------------
                    self.TF.logger.Message("----- Issue Power-Cycle-------------------------------\n")
                    self.__PwrCycle()
                    self.TF.logger.Message("------------------------------------------------------\n")
                    # Disable-EHM and MR  in DW-11--------------------------------------------------------------------
                    MR = 1
                    EHM = 0
                    dw11 = 2  # 3
                    try:
                        ObjSetFeature = NVMeWrap.SetFeatures(
                            NVMeWrap.FID_HOST_MEM_BUF, False, dw11, NS_ID, None, self.CmdTimeout, sendType)
                    except ValidationError.CVFExceptionTypes as ex:
                        self.TF.logger.Fatal(
                            "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                        raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    RespStatus3 = ObjSetFeature.objNVMeComIOEntry.completionEntry.DW3.SF.SC
                    Res_DW0 = ObjSetFeature.objNVMeComIOEntry.completionEntry.DW0
                    self.TF.logger.Message("%-35s: %s" % ('DW0 After Enable HMB', Res_DW0))
                    # -----------------------------------------------------------------------------------------
                    self.TF.logger.Message("----- Issue Power-Cycle-------------------------------\n")
                    self.__PwrCycle()
                    self.TF.logger.Message("------------------------------------------------------\n")
                    # Issue Get HMBFeature----------------------------------------------------------------------
                    ObjGetFeature = NVMeWrap.GetFeatures(
                        NVMeWrap.FID_HOST_MEM_BUF, NVMeWrap.CURRENT, NS_ID, self.CmdTimeout, sendType = sendType, dwTimeOut = 0xFFFFFFFF)
                    self.TF.logger.Message("%-35s: %s" %
                                           ('HMB DW11: ', ObjGetFeature.objNVMeComIOEntry.completionEntry.DW0))
                    self.TF.logger.Message(
                        "%-35s: %s" % ('HMDLLA', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.DESCRIPTOR_LIST_LOWER_ADDR.DescriptorListLowerAddr))
                    self.TF.logger.Message("%-35s: %s" % ('HMDLUA', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HMDLUA))
                    self.TF.logger.Message("%-35s: %s" % ('HMDLEC', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HMDLEC))
                    self.TF.logger.Message("%-35s: %s" % ('HSIZE', hmbMemObj.HOST_MEMORY_DESCRIPTOR_ENTRY_LIST.HSIZE))
                    # Deallocate Host Memory Buffer-------------------------------------------------------------------
                    if(bitFlip):
                        # Read HMB Buffer when HBM is Disable---------------------------------------------------------
                        try:
                            hmbMemObj.ReadHMBMemory(hmbMemObj.DescriptorEntryListWithUserAddr[0].USER_MAPPED_ADDR, buff)
                        except ValidationError.CVFExceptionTypes as ex:
                            self.TF.logger.Fatal(
                                "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                            raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                        buff.PrintToLog()
                    # ------------------------------------------------------------------------------------------------
                    # Issue Read & Writes-----------------------------------------------------------------------------
                    RDWRCnt = self.RdWrCNTVal
                    self.__IOs(RDWRCnt)
                    # ------------------------------------------------------------------------------------------------
                    try:
                        hmbMemObj.DeAllocateHostMemoryBuffer()
                    except ValidationError.CVFExceptionTypes as ex:
                        self.TF.logger.Fatal(
                            "Failed to Post the Get/Set Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                        raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
                    # ------------------------------------------------------------------------------------------------
                    cnt = cnt + 1
                    del self.listOfHMBFragments1[:]
                # ------------------------------------------------------------------------------------------------
        else:
            self.TF.logger.Message("HMB Feature is not supported")
        self.TF.logger.Message("******************************************************************\n")

    def __IOs(self, RDWRCnt):
        # Issue Read & Writes-----------------------------------------------------------------------------
        LBAFromLast = self.TF.nsCap - 1
        cntREWR = RDWRCnt
        len = random.randint(1, 50)
        self.start = 0
        while((self.start >= 0) and (self.start <= LBAFromLast) and (cntREWR > 0)):
            self.__Read(len)
            self.__Write(len)
            self.start = self.start + len
            cntREWR = cntREWR - 1
        # -------------------------------------------------------------------------------------------------

    def __ControllerCCReg(self, Translen = 1):

        sendType = ServiceWrap.SEND_IMMEDIATE
        ReadCC = NVMeWrap.GetNVMeConfigReg(NVMeWrap.ControllerReg.CC, sendType = sendType, dwTimeOut = 0xFFFFFFFF)
        Rerg = ReadCC.Output
        self.TF.logger.Message("\n**************Read Controller- CC ***************************\n")
        self.TF.logger.Message("%-35s: %s" % ('MPS', Rerg.CC.MPS))
        self.TF.logger.Message("\n*************************************************************\n")
        self.MPS = Rerg.CC.MPS
        self.TF.logger.Message("\n*************************************************************\n")
        ReadCAP = NVMeWrap.GetNVMeConfigReg(NVMeWrap.ControllerReg.CAP, sendType = sendType, dwTimeOut = 0xFFFFFFFF)
        self.TF.logger.Message("%-35s: %s" % ('MPSMAX', Rerg.CAP.MPSMAX))
        self.MPSMAX = Rerg.CAP.MPSMAX
        self.TF.logger.Message("%-35s: %s" % ('MPSMIN', Rerg.CAP.MPSMIN))
        self.MPSMIN = Rerg.CAP.MPSMIN
        self.TF.logger.Message("\n*************************************************************\n")

    def __CalBuffSize(self):

        cnt = 0
        self.Size = 0
        while cnt < 3:
            self.Size = self.Size + self.listOfHMBFragments1[cnt]
            cnt = cnt + 1

    def __PwrCycle(self):
        try:
            self.CMDUtil.PostPowerCycle(ServiceWrap.GRACEFUL)
        except ValidationError.CVFExceptionTypes as ex:
            self.TF.logger.Fatal(
                "Failed to Post the Power Cycle Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
            raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
        status = False
        status = self.TF.threadPool.WaitForThreadCompletion()
        if False == status:
            self.__CheckForErrors()
        self.TF.logger.Message("------------------------------------------------------\n")

    def __CheckForErrors(self):

        self.TF.logger.Fatal("Test Execution Failed. Exception Message ")
        if self.errorManager.IsExceptionPendingForHandling():
            self.TF.logger.Fatal(self.errorManager.GetAllFailureDescription())
            # Flush all the pending log messages.
            self.TF.logger.FlushAllMsg()

    def __Read(self, Translen = 1):
        commandCount = 0
        startLba = self.start
        nameSpace = self.nameSpaceID
        submissionQID = random.randint(1, self.TF.nrOfsubmissionQ)
        while (commandCount < 1):
            transferLength = Translen
            self.TF.logger.Message("%-35s: %s" % ('RD - Start LBAs: ', startLba))
            self.TF.logger.Message("%-35s: %s" % ('RD - TransferLength: ', transferLength))
            pattern = random.randint(1, 0xAA)
            try:
                self.CMDUtil.PostReadLba(startLba, transferLength, submissionQID, nameSpace)
            except ValidationError.CVFExceptionTypes as ex:
                self.TF.logger.Fatal(
                    "Failed to Post the Read Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
            startLba = startLba + transferLength
            commandCount = commandCount + 1

        status = False
        status = self.TF.threadPool.WaitForThreadCompletion()
        if False == status:
            self.__CheckForErrors()
            raise ValidationError.CVFGenericExceptions(
                "Wait For Thread Completion Failed", self.errorManager.GetAllFailureDescription())

    def __Write(self, Translen = 1):
        commandCount = 0
        startLba = self.start
        nameSpace = self.nameSpaceID
        submissionQID = random.randint(1, self.TF.nrOfsubmissionQ)
        while (commandCount < 1):
            transferLength = Translen
            self.TF.logger.Message("%-35s: %s" % ('WR - Start LBAs: ', startLba))
            self.TF.logger.Message("%-35s: %s" % ('WR - TransferLength: ', transferLength))
            pattern = random.randint(1, 0xAA)
            pattern = 0
            try:
                self.CMDUtil.PostWriteLba(startLba, transferLength, submissionQID, nameSpace,
                                          0, pattern, writeTimeout = self.writeTimeout)
            except ValidationError.CVFExceptionTypes as ex:
                self.TF.logger.Fatal(
                    "Failed to Post the Write Command to Threadpool. Exception Message is ->\n %s " % ex.GetFailureDescription())
                raise ValidationError.CVFGenericExceptions("", "Failed in Posting Command\n")
            startLba = startLba + transferLength
            commandCount = commandCount + 1
        status = False
        status = self.TF.threadPool.WaitForThreadCompletion()
        if False == status:
            self.__CheckForErrors()
            raise ValidationError.CVFGenericExceptions(
                "Wait For Thread Completion Failed", self.errorManager.GetAllFailureDescription())

    def test_GetSetHMB028(self):
        self.HBM()