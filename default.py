import math

class tmp:
        
    class settings:
            
        def __init__(self):
            self.startTime = ''
            self.endTime = ''
            self.versionNumber = 1
            
        class options:
                
            def __init__(self):
                self.procParallel = 1
                self.autoSetup = 1
                self.memSafetyMargin = 0
                self.keepFiles = 0
                self.procMemory = 0
                self.saveIntermediate = 0
                self.force = 0
                self.noCombine = 0
                    
            class kspace:
                        
                def __init__(self):
                    self.force = 0
                    self.decorrelateChannels = 0
                    self.unwrap = 0
                    self.denoise = 0
                    self.filter= 'BM4D'
                    self.tukeyWindow = 1
                    self.variableAveraging = 0
                    self.acquisitionWeighting = 0
                    self.partialFourier = 1
                    self.GRAPPA = 0
                        
            class xspace:
                        
                def __init__(self):
                    self.force = 0
                    self.combineChannels= 'SoS'
                    self.coilCompression = 0
                    self.getMaxChannel = 0
                            
                    
            class imspace:
                        
                def __init__(self):
                    self.force = 0
                            
                    
            class NIfTI:
                        
                def __init__(self):
                    self.force = 0
                            
                            
            class output:
                        
                def __init__(self):
                    self.writeNIfTI = 1
                    self.writePhase = 0
                    self.writeComplex = 0
                    self.gzip = 1
                    self.refData = 0
                    self.trueComplex = 0
                    self.writeChannelwise = 0
                    self.shortName = 0
                    self.shortFilename = 0
                            
            class post:
                        
                def __init__(self):
                    self.distortionCorrection =0 
                    self.biasfield =0
                    self.segmentation =0
                    self.mask =0 
                    self.keepSegmentation =0 
                    self.keepBiascorrection =0
                            
            kspace = kspace()
            xspace = xspace()
            imspace = imspace()
            NIfTI = NIfTI()
            output = output()
            post = post()
                    
            
        class parameters:
                
            def __init__(self):
                self.maxCPUs = math.inf
                self.preprocWorkers = math.inf
                self.combineWorkers = math.inf
                self.procWorkers = math.inf
                self.maxMemory = math.inf
                self.stepSize = 2
                self.nChunks = 32
                self.safetyMargin = 1
                self.scalefac =1000
                self.path = ''
                self.numFiles = 1
                self.nCh = 32
                self.nRO = 64
                self.nPE = 64
                self.nSlc = 40
                self.pRO = 50
                self.pPE = 64
                self.pSlc = 30
                self.uRO = 14
                self.uPE = 0
                self.uSlc = 10
                self.inPlaneRot = 0
                self.w =0
                self.availableMem = 106.9540
                self.estimatedSliceMem =0.1342
                self.estimatedChannelMem =0.0839
                self.maxchannel =1
                    
            class kspace:
                    
                def __init__(self):
                    self.scalefac = 1.0000e+11
                    self.decorrelateChannels= 'noiseScan'
                    self.tukey = 0.2000
                    self.partialFourier= 'zero'
                    self.processed= 0
                        
                
                        
            class xspace:
                def __init__(self):
                    self.combineType = 'byChunk'
                    self.processed = 0
                        
                class blockSize:
                    pass
                    
                blockSize = blockSize()
                    
            class post:
                    
                def __init__(self):
                    self.fwhm = 30
                    self.reg = 1.0000e-03
                    self.samp = 2
                    self.dilate = 10
                    self.erode =10
                    self.path = ''
                
            class pk:
                    
                def __init__(self):
                    self.names = ['gauss', 'gauss', 'gauss']
                    self.scale = 0
                    self.writephasemap =0
                        
                class width:
                    pass
                    
                class shifts:
                    pass
                    
                width = width()
                shifts = shifts()
                    
            class denoise:
                    
                def __init__(self):
                    self.distribution = 'Gauss'
                    self.sigma =0
                    self.verbose =0
                    self.shrinkcheck =0
                    self.NwLevel =4
                    self.wname ='db5'
                    self.type = 2
                    self.beta = 0.2000
                    self.patchradius =1
                    self.searchradius = 3
                    self.profile = 'lc'
                    self.do_wiener = 1
                    self.N1 = 8
                    self.Nstep= 5
                    self.N2 = 32
                    self.Ns = 11
                    self.tau_match = 0.1000
                    self.lambda_thr4D = 1
                    self.N2_wiener = 32
                    self.tau_match_wiener = 0.0500
                        
                        
            class FoV:
                pass
                
            class Resolution:
                pass
                    
            class Pos:
                pass
                
            class Quaternion:
                pass
                
            class orientation:
                    
                class RotationPhys2Pat:
                    pass
                    
                class RotationPhys2Log:
                    pass
                    
                class RotationPat2Phys:
                    pass
                    
                class RotationPat2Log:
                    pass
                    
                class RotationLog2Phys:
                    pass
                    
                class RotationLog2Pat:
                    pass
                    
                class CenterPhys:
                    pass
                    
                class CenterPat:
                    pass
                    
                class CenterLog:
                    pass
                    
                class Size:
                    pass
                    
                class Basics:
                    pass
                    
                RotationPhys2Pat = RotationPhys2Pat()
                RotationPhys2Log = RotationPhys2Log()
                RotationPat2Phys = RotationPat2Phys()
                RotationPat2Log= RotationPat2Log()
                RotationLog2Phys = RotationLog2Phys()
                RotationLog2Pat= RotationLog2Pat()
                CenterPhys= CenterPhys()
                CenterPat = CenterPat()
                CenterLog = CenterLog()
                Size = Size()
                Basics = Basics()
                
            class R:
                pass
                
            class imspace:
                    
                def __init__(self):
                    self.processed =0
                        
            kspace= kspace()
            xspace = xspace()
            post = post()
            pk = pk()
            denoise = denoise()
            Pos = Pos()
            Resolution= Resolution()
            FoV= FoV()
            Quaternion = Quaternion()
            orientation = orientation()
            R = R()
            imspace = imspace()
                
        options = options()
        parameters = parameters()
            
        
    settings = settings()

tmp = tmp()