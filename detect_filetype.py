def get_file_header(header:str):
    if header=="00 00 1A 00 05 10 04":
        return True, "123 file","Lotus 1-2-3 spreadsheet (v9) file"
    elif header=="00 00 00 14 66 74 79 70 33 67 70":
        return True, "3gg;3gp;3g2 file","3rd Generation Partnership Project 3GPP multimedia files"
    elif header=="00 00 00 20 66 74 79 70 33 67 70":
        return True, "3gg;3gp;3g2 file","3rd Generation Partnership Project 3GPP2 multimedia files"
    elif header=="37 7A BC AF 27 1C":
        return True, "7z file","7-ZIP compressed file"
    elif header=="00 01 42 41":
        return True, "aba file","Palm Address Book Archive file"
    elif header=="41 4F 4C 49 4E 44 45 58":
        return True, "abi file","AOL address book index file"
    elif header=="41 4F 4C 44 42":
        return True, "aby;idx file","AOL database files: address book (ABY) and user configuration data (MAIN.IDX)"
    elif header=="00 01 00 00 53 74 61 6E 64 61 72 64 20 41 43 45 20 44 42":
        return True, "accdb file","Microsoft Access 2007 file"
    elif header=="4D 5A":
        return True, "acm file","MS audio compression manager driver"
    elif header=="44 4F 53":
        return True, "adf file","Amiga disk file"
    elif header=="03 00 00 00 41 50 50 52":
        return True, "adx file","Lotus Approach ADX file"
    elif header=="46 4F 52 4D 00":
        return True, "aiff file","Audio Interchange File"
    elif header=="21 12":
        return True, "ain file","AIN Compressed Archive File"
    elif header=="5B 76 65 72 5D":
        return True, "ami file","Lotus Ami Pro"
    elif header=="23 21 41 4D 52":
        return True, "amr file","Adaptive Multi-Rate ACELP (Algebraic Code Excited Linear Prediction) Codec, commonly audio format with GSM cell phones"
    elif header=="52 49 46 46":
        return True, "ani file","UNKNOWN"
    elif header=="4D 5A 90 00 03 00 00 00":
        return True, "api file","Acrobat plug-in"
    elif header=="1A 02":
        return True, "arc file","LH archive file, old version,type 1"
    elif header=="1A 03":
        return True, "arc file","LH archive file, old version,type 2"
    elif header=="1A 04":
        return True, "arc file","LH archive file, old version,type 3"
    elif header=="1A 08":
        return True, "arc file","LH archive file, old version,type 4"
    elif header=="1A 09":
        return True, "arc file","LH archive file, old version,type 1"
    elif header=="41 72 43 01":
        return True, "arc file","FreeArc compressed file"
    elif header=="60 EA":
        return True, "arj file","ARJ Compressed Archive"
    elif header=="4A 47 03 0E 00 00 00":
        return True, "art file","AOL ART file"
    elif header=="4A 47 04 0E 00 00 00":
        return True, "art file","AOL ART file"
    elif header=="30 26 B2 75 8E 66 CF 11":
        return True, "asf file","Windows Media"
    elif header=="30 26 B2 75 8E 66 CF 11 A6 D9 00 AA 00 62 CE 6C":
        return True, "asf;wma;wmv file","Microsoft Windows Media Audio/Video File(Advanced Streaming Format)"
    elif header=="3C":
        return True, "asx file","Advanced Stream redirector file"
    elif header=="2E 73 6E 64":
        return True, "au file","SoundMachine Audio FileNeXT/Sun Microsystems μ-Law audio file"
    elif header=="41 56 49 20":
        return True, "avi file","Audio Video Interleave (AVI)"
    elif header=="4D 5A":
        return True, "AX file","Library cache file"
    elif header=="4D 5A 90 00 03 00 00 00":
        return True, "AX file","DirectShow filter"
    elif header=="41 4F 4C 20 46 65 65 64 62 61 67":
        return True, "bag file","AOL and AIM buddy list file"
    elif header=="20 20 20":
        return True, "bas file","UNKNOWN"
    elif header=="42 4C 49 32 32 33 51":
        return True, "bin file","Thomson Speedtouch series WLAN router firmware"
    elif header=="42 4D":
        return True, "bmp file","Windows Bitmap"
    elif header=="42 4D 3E":
        return True, "bmp file","UNKNOWN"
    elif header=="42 5A 68":
        return True, "bz;bz2,(BZ2;TAR.BZ2;TBZ2;TB2) file","BZIP Archive(bzip2 compressed archive)"
    elif header=="49 53 63":
        return True, "cab file","UNKNOWN"
    elif header=="49 53 63 28":
        return True, "cab;hdr file","Install Shield v5.x or 6.x compressed file"
    elif header=="4D 53 43 46":
        return True, "cab file","Microsoft CAB File Format"
    elif header=="30":
        return True, "cat file","Microsoft security catalog file"
    elif header=="43 42 46 49 4C 45":
        return True, "cbd file","WordPerfect dictionary file (unconfirmed)"
    elif header=="5B 43 6C":
        return True, "ccd file","UNKNOWN"
    elif header=="45 4C 49 54 45 20 43 6F 6D 6D 61 6E 64 65 72 20":
        return True, "cdr file","Elite Plus Commander saved game file"
    elif header=="4D 53 5F 56 4F 49 43 45":
        return True, "cdr;dvf file","Sony Compressed Voice File"
    elif header=="49 54 53 46":
        return True, "chi;chm file","Microsoft Compiled HTML Help File"
    elif header=="49 54 53":
        return True, "chm file","UNKNOWN"
    elif header=="43 4D 58 31":
        return True, "clb file","Corel Binary metafile"
    elif header=="43 4F 4D 2B":
        return True, "clb file","COM+ Catalog file"
    elif header=="3A 42 61 73 65":
        return True, "cnt file","UNKNOWN"
    elif header=="4D 5A":
        return True, "com;dll;drv;exe;pif;qts;qtx;sys(cpl)","Windows/DOS executable file(Control panel application)"
    elif header=="E9 3B 03":
        return True, "com file","UNKNOWN"
    elif header=="46 41 58 43 4F 56 45 52 2D 56 45 52":
        return True, "cpe file","Microsoft Fax Cover Sheet"
    elif header=="43 50 54 37 46 49 4C 45":
        return True, "cpt file","Corel Photopaint file"
    elif header=="43 50 54 46 49 4C 45":
        return True, "cpt file","Corel Photopaint file"
    elif header=="5B 57 69":
        return True, "cpx file","UNKNOWN"
    elif header=="43 52 55 53 48":
        return True, "cru* file","CRUSH Archive File"
    elif header=="43 52 55 53 48 20 76":
        return True, "cru file","Crush compressed archive"
    elif header=="49 49 1A 00 00 00 48 45 41 50 43 43 44 52 02 00":
        return True, "crw file","Canon digital camera RAW file"
    elif header=="43 61 74 61 6C 6F 67 20 33 2E 30 30 00":
        return True, "ctf file","WhereIsIt Catalog file"
    elif header=="00 00 02 00 01 00 20 20":
        return True, "cur file","Windows cursor file"
    elif header=="03":
        return True, "dat file","MapInfo Native Data Format"
    elif header=="1A 52 54 53 20 43 4F 4D 50 52 45 53 53 45 44 20 49 4D 41 47 45 20 56 31 2E 30 1A":
        return True, "dat file","Runtime Software disk image"
    elif header=="41 56 47 36 5F 49 6E 74 65 67 72 69 74 79 5F 44 61 74 61 62 61 73 65":
        return True, "dat file","AVG6 Integrity database file"
    elif header=="43 52 45 47":
        return True, "dat file","Windows 9x registry hive"
    elif header=="43 6C 69 65 6E 74 20 55 72 6C 43 61 63 68 65 20 4D 4D 46 20 56 65 72 20":
        return True, "dat file","IE History DAT file"
    elif header=="45 52 46 53 53 41 56 45 44 41 54 41 46 49 4C 45":
        return True, "dat file","Kroll EasyRecovery Saved Recovery State file"
    elif header=="49 6E 6E 6F 20 53 65 74 75 70 20 55 6E 69 6E 73 74 61 6C 6C 20 4C 6F 67 20 28 62 29":
        return True, "dat file","Inno Setup Uninstall Log file"
    elif header=="00 06 15 61 00 00 00 02 00 00 04 D2 00 00 10 00":
        return True, "db file","Netscape Navigator (v4) database file"
    elif header=="44 42 46 48":
        return True, "db file","Palm Zire photo database"
    elif header=="08":
        return True, "db file","dBASE IV or dBFast configuration file"
    elif header=="03":
        return True, "db3 file","dBASE III file"
    elif header=="04":
        return True, "db4 file","dBASE IV data file"
    elif header=="00 01 42 44":
        return True, "dba file","Palm DateBook Archive file"
    elif header=="CF AD 12 FE":
        return True, "dbx file","UNKNOWN"
    elif header=="CF AD 12 FE C5 FD 74 6F":
        return True, "dbx file","Outlook Express"
    elif header=="3C 21 64 6F 63 74 79 70":
        return True, "dci file","AOL HTML mail file"
    elif header=="3A DE 68 B1":
        return True, "dcx file","DCX Graphic File"
    elif header=="00 01 00":
        return True, "ddb file","UNKNOWN"
    elif header=="42 4D":
        return True, "dib file","device-independent bitmap image"
    elif header=="4D 5A 90":
        return True, "dll file","UNKNOWN"
    elif header=="4D 44 4D 50 93 A7":
        return True, "dmp file","Windows minidump file"
    elif header=="44 4D 53 21":
        return True, "dms file","Amiga DiskMasher compressed archive"
    elif header=="0D 44 4F 43":
        return True, "doc file","DeskMate Document file"
    elif header=="12 34 56 78 90 FF":
        return True, "doc file","MS Word 6.0"
    elif header=="31 BE 00 00 00 AB 00 00":
        return True, "doc file","MS Word for DOS 6.0"
    elif header=="7F FE 34 0A":
        return True, "doc file","MS Word"
    elif header=="D0 CF 11 E0":
        return True, "dot;ppt;xla;ppa;pps;pot;msi;sdw;db file","MS Office/OLE2"
    elif header=="D0 CF 11 E0 A1 B1 1A E1":
        return True, "doc;dot;xls;xlt;xla;ppt;apr;ppa;pps;pot;msi;sdw;db file","MS Compound Document v1 or Lotus Approach APR file"
    elif header=="4D 5A 50":
        return True, "dpl file","UNKNOWN"
    elif header=="4D 5A 16":
        return True, "drv file","UNKNOWN"
    elif header=="07":
        return True, "drw file","A common signature and file extension for many drawing programs."
    elif header=="01 FF 02 04 03 02":
        return True, "drw file","Micrografx vector graphic file"
    elif header=="4D 47 58 20 69 74 70 64":
        return True, "ds4 file","Micrografix Designer 4"
    elif header=="4D 56":
        return True, "dsn file","CD Stomper Pro label file"
    elif header=="23 20 4D 69 63 72 6F 73 6F 66 74 20 44 65 76 6 56C 6F 70 65 72 20 53 74 75 64 69 6F":
        return True, "dsp file","Microsoft Developer Studio project file"
    elif header=="02 64 73 73":
        return True, "dss file","Digital Speech Standard (Olympus, Grundig, & Phillips)"
    elif header=="07 64 74 32 64 64 74 64":
        return True, "dtd file","DesignTools 2D Design file"
    elif header=="3C 21 45 4E 54 49 54 59":
        return True, "dtd file","XML DTD"
    elif header=="44 56 44":
        return True, "dvr file","DVR-Studio stream file"
    elif header=="41 43 31":
        return True, "dwg file","UNKNOWN"
    elif header=="41 43 31 30":
        return True, "dwg file","UNKNOWN"
    elif header=="45 56 46":
        return True, "enn file","EnCase evidence file"
    elif header=="2A 50 52":
        return True, "eco file","UNKNOWN"
    elif header=="7F 45 4C 46 01 01 01 00":
        return True, "elf file","ELF Executable"
    elif header=="01 00 00 00 58 00 00 00":
        return True, "emf file","Extended (Enhanced) Windows Metafile Format, printer spool file"
    elif header=="44 65 6C 69 76 65 72 79 2D 64 61 74 65 3A":
        return True, "eml file","email"
    elif header=="46 72 6F 6D 20 20 20":
        return True, "eml file","A common file extension for e-mail file"
    elif header=="46 72 6F 6D 20 3F 3F 3F":
        return True, "eml file", "A common file extension for e-mail file"
    elif header=="46 72 6F 6D 3A 20":
        return True, "eml file", "A common file extension for e-mail file"
    elif header=="52 65 63":
        return True, "eml file","UNKNOWM"
    elif header=="00 5C 41 B1 FF":
        return True, "enc file","Mujahideen Secrets 2 encrypted file"
    elif header=="25 21 50 53":
        return True, "eps file","Adobe EPS File"
    elif header=="25 21 50 53 2D 41 64 6F 62 65":
        return True, "eps file","Postscript"
    elif header=="25 21 50 53 2D 41 64 6F 62 65 2D 33 2E 30 20 45 50 53 46 2D 33 20 30":
        return True, "eps file","Adobe encapsulated PostScript file"
    elif header=="C5 D0 D3":
        return True, "eps file","UNKNOWN"
    elif header=="1A 35 01 00":
        return True, "eth file","GN Nettest WinPharoah capture file"
    elif header=="30 00 00 00 4C 66 4C 65":
        return True, "evt file","Windows Event Viewer file"
    elif header=="03 00 00 00 C4 66 C4 56":
        return True, "evt file","UNKNOWN"
    elif header=="45 6C 66 46 69 6C 65 00":
        return True, "evtx file","Windows Vista event log file"
    elif header=="4D 5A":
        return True, "exe;com;386;ax;acm;sys;dll;drv;flt;fon;ocx;scr;lrc;vxd;cpl;x32","Executable File"
    elif header=="00 11 AF":
        return True, "fli file","FLIC Animation file"
    elif header=="00 01 01":
        return True, "flt file","OpenFlight 3D file"
    elif header=="4D 5A 90 00 03 00 00 00":
        return True, "flt file","Audition graphic filter file (Adobe)"
    elif header=="46 4C 56 01":
        return True, "flv file","Flash video file"
    elif header=="3C 4D 61 6B 65 72 46 69 6C 65 20":
        return True, "fm file","Adobe FrameMaker file"
    elif header=="00 00 1A 00 07 80 01 00":
        return True, "fm3 file","Lotus 123 v3 FMT file"
    elif header=="20 00 68 00 20 00":
        return True, "fmt file","Lotus 123 v4 FMT file"
    elif header=="43 48 41":
        return True, "fnt file","UNKNOWN"
    elif header=="4D 5A":
        return True, "fon file","Font file"
    elif header=="87 F5 3E":
        return True, "gbc file","UNKNOWN"
    elif header=="3F 5F 03 00":
        return True, "gid file","Windows Help Index File"
    elif header=="4C 4E 02 00":
        return True, "gid file","Windows Help Index File"
    elif header=="47 49 46 38":
        return True, "gif file","Graphics interchange format file"
    elif header=="7B 50 72":
        return True, "gtd file","UNKNOWN"
    elif header=="47 58 32":
        return True, "gx2 file","Show Partner graphics file"
    elif header=="1F 8B":
        return True, "gz;tar;tgz file","Gzip Archive File"
    elif header=="91 33 48 46":
        return True, "hap file","HAP Archive File"
    elif header=="4D 44 4D 50 93 A7":
        return True, "hdmp file","Windows heap dump file"
    elif header=="23 3F 52 41 44 49 41 4E 43 45 0A":
        return True, "hdr file","adiance High Dynamic Range image file"
    elif header=="3F 5F 03 00":
        return True, "hlp file","Windows help file"
    elif header=="4C 4E 02 00":
        return True, "hlp file","Windows help file"
    elif header=="28 54 68 69 73 20 66 69 6C 65":
        return True, "hqx file","Macintosh BinHex 4 Compressed Archive"
    elif header=="3C 21 44":
        return True, "htm* file","HyperText Markup Language"
    elif header=="68 74 6D 6C 3E":
        return True, "html file","HTML"
    elif header=="00 00 01 00 00":
        return True, "ico file","Icon File"
    elif header=="00 00 01 00 01 00 20 20":
        return True, "ico file","Icon File"
    elif header=="46 4F 52 4D":
        return True, "iff file","UNKNWON"
    elif header=="44 56 44":
        return True, "ifo file","DVD info file"
    elif header=="00 01 00 08 00 01 00 01 01":
        return True, "img file","Ventura Publisher/GEM VDI Image Format Bitmap file"
    elif header=="00 FF FF":
        return True, "img file","UNKNOWN"
    elif header=="4D 5A 90":
        return True, "imm file","UNKNOWN"
    elif header=="41 4F 4C 49 44 58":
        return True, "ind file","AOL client preferences/settings file (MAIN.IND)"
    elif header=="43 44 30 30 31":
        return True, "iso file","ISO-9660 CD Disc Image"
    elif header=="2E 52 45 43":
        return True, "ivr file","	RealPlayer video file (V11 and later)"
    elif header=="4A 41 52 43 53 00":
        return True, "jar file","JARCS compressed archive"
    elif header=="5F 27 A8 89":
        return True, "jar file","JAR Archive File"
    elif header=="FF D8 FF":
        return True, "jpg;jpeg file","JPG Graphic File"
    elif header=="4B 47 42 5F 61 72 63 68 20 2D":
        return True, "kgb file","KGB archive"
    elif header=="49 44 33 03 00 00 00":
        return True, "koz file","Sprint Music Store audio file (for mobile devices)"
    elif header=="42 49 4C":
        return True, "ldb file","UNKNOWN"
    elif header=="2D 6C 68 35 2D":
        return True, "lha file","LHA Compressed"
    elif header=="3F 5F 03":
        return True, "lhp file","Windows Help File"
    elif header=="21 3C 61 72 63 68 3E 0A":
        return True, "lib file","Unix archiver (ar) files and Microsoft Program Library Common Object File Format (COFF)"
    elif header=="2A 24 20":
        return True, "lib file","UNKNOWN"
    elif header=="49 54 4F 4C 49 54 4C 53":
        return True, "lit file","Microsoft Reader eBook file"
    elif header=="4C 00 00":
        return True, "lnk file","Windows Link File"
    elif header=="2A 2A 2A 20 20 49 6E 73 74 61 6C 6C 61 74 69 6F 6E 20 53 74 61 72 74 65 64 20":
        return True, "log file","Symantec Wise Installer log file"
    elif header=="57 6F 72 64 50 72 6F":
        return True, "lwp file","Lotus WordPro v9"
    elif header=="23 45 58":
        return True, "m3u file","UNKNOWN"
    elif header=="00 00 00 20 66 74 79 70 4D 34 41 20 00 00 00 00":
        return True, "m4a;m4v file","QuickTime M4A/M4V file"
    elif header=="3C 3F 78 6D 6C 20 76 65 72 73 69 6F 6E 3D":
        return True, "manifest file","Windows Visual Stylesheet XML file"
    elif header=="4D 41 52 31 00":
        return True, "mar file","Mozilla archive"
    elif header=="4D 41 52 43":
        return True, "mar file","Microsoft/MSN MARC archive"
    elif header=="4D 41 72 30 00":
        return True, "mar file","MAr compressed archive"
    elif header=="D0 CF 11":
        return True, "max file","UNKNOWN"
    elif header=="00 01 00 00 53 74 61 6E 64 61 72 64 20 4A 65 74 20 44 42":
        return True, "mdb file","Microsoft Access file"
    elif header=="53 74 61 6E 64 61 72 64 20 4A":
        return True, "mdb;mda;mde;mdt file","MS Access"
    elif header=="00 FF FF":
        return True, "mdf file","UNKNOWN"
    elif header=="00 FF FF FF FF FF FF FF FF FF FF 00 00 02 00 01":
        return True, "mdf file","Alcohol 120% CD image"
    elif header=="01 0F 00 00":
        return True, "mdf file","Microsoft SQL Server 2000 database"
    elif header=="45 50":
        return True, "mdi file","Microsoft Document Imaging file"
    elif header=="4D 45 44":
        return True, "mds file","UNKNOWN"
    elif header=="4D 54 68 64":
        return True, "mid;midi file","Musical Instrument Digital Interface (MIDI) sound file"
    elif header=="1A 45 DF A3 93 42 82 88 6D 61 74 72 6F 73 6B 61":
        return True, "mkv file","Matroska stream file"
    elif header=="4D 49 4C 45 53":
        return True, "mls file","Milestones v1.0 project management and scheduling software"
    elif header=="4D 4C 53 57":
        return True, "mls file","Skype localization data file"
    elif header=="4D 56 32 31 34":
        return True, "mls file","Milestones v2.1b project management and scheduling software"
    elif header=="4D 56 32 43":
        return True, "mls file","Milestones v2.1a project management and scheduling software"
    elif header=="4D 4D 4D 44 00 00":
        return True, "mmf file","Yamaha Corp. Synthetic music Mobile Application Format (SMAF) for multimedia files that can be played on hand-held devices."
    elif header=="00 01 00 00 4D 53 49 53 41 4D 20 44 61 74 61 62 61 73 65":
        return True, "mny file","Microsoft Money file"
    elif header=="00 00 0F":
        return True, "mov file","UNKNOWN"
    elif header=="00 00 77":
        return True, "mov file","UNKNOWN"
    elif header=="6D 6F 6F 76":
        return True, "mov file","Quicktime"
    elif header=="6D 64 61 74":
        return True, "mov file","QuickTime Movie"
    elif header=="0C ED":
        return True, "mp file","Monochrome Picture TIFF bitmap file"
    elif header=="49 44 33":
        return True, "mp3 file","MPEG-1 Audio Layer 3 (MP3) audio file"
    elif header=="FF FB 50":
        return True, "mp3 file","UNKNOWN"
    elif header=="00 00 00 18 66 74 79 70 33 67 70 35":
        return True, "mp4 file","MPEG-4 video files"
    elif header=="00 00 01":
        return True, "mpa file","UNKNOWN"
    elif header=="00 00 01 B3":
        return True, "mpg;mpeg file","MPEG Movie"
    elif header=="00 00 01 BA":
        return True, "mpg file","MPEG"
    elif header=="3C 3F 78":
        return True, "msc file","UNKNOWN"
    elif header=="3C 3F 78 6D 6C 20 76 65 72 73 69 6F 6E 3D 22 31 2E 30 22 3F 3E 0D 0A 3C 4D 4D 43 5F 43 6F 6E 73 6F 6C 65 46 69 6C 65 20 43 6F 6E 73 6F 6C 65 56 65 72 73 69 6F 6E 3D 22":
        return True, "msc file","Microsoft Management Console Snap-in Control file"
    elif header=="23 20":
        return True, "msi file","Cerius2 file"
    elif header=="4D 53 5F 56 4F 49 43 45":
        return True, "msv file","Sony Memory Stick Compressed Voice file"
    elif header=="4E 45 53":
        return True, "nes file","UNKNOWN"
    elif header=="C2 20 20":
        return True, "nls file","UNKNOWN"
    elif header=="0E 4E 65 72 6F 49 53 4F":
        return True, "nri file","Nero CD Compilation"
    elif header=="1A 00 00":
        return True, "nsf file","Lotus Notes database template"
    elif header=="30 31 4F 52 44 4E 41 4E 43 45 20 53 55 52 56 45 59 20 20 20 20 20 20 20":
        return True, "ntf file","National Transfer Format Map File"
    elif header=="4C 01":
        return True, "obj file","Microsoft Common Object File Format (COFF) relocatable object code file for an Intel 386 or later/compatible processors"
    elif header=="4D 5A":
        return True, "ocx;olb file","ActiveX or OLE Custom Control(OLE object library)"
    elif header=="41 4F 4C 56 4D 31 30 30":
        return True, "org;pfc file","AOL personal file cabinet (PFC) file"
    elif header=="1A 0B":
        return True, "pak file","Compressed archive file"
    elif header=="47 46 31 50 41 54 43 48":
        return True, "pat file","Advanced Gravis Ultrasound patch file"
    elif header=="47 50 41 54":
        return True, "pat file","GIMP (GNU Image Manipulation Program) pattern file"
    elif header=="5B 41 44":
        return True, "pbk file","UNKNOWN"
    elif header=="17 A1 50":
        return True, "pcb file","UNKNOWN"
    elif header=="0A 05 01":
        return True, "pcs file","UNKNOWN"
    elif header=="0A 02 01 01":
        return True, "pcx file","ZSOFT Paintbrush file"
    elif header=="0A 03 01 01":
        return True, "pcx file","ZSOFT Paintbrush file"
    elif header=="0A 05 01 01":
        return True, "pcx file","ZSOFT Paintbrush file"
    elif header=="0A 05 01 08":
        return True, "pcx file","PC Paintbrush(often associated with Quake Engine games)"
    elif header=="25 50 44":
        return True, "pdf file","Adobe Portable Document Format and Forms Document file"
    elif header=="48 48 02":
        return True, "pdg file","UNKNOWN"
    elif header=="11 00 00 00 53 43 43 41":
        return True, "pf file","Windows prefetch file"
    elif header=="01 00 00 00 01":
        return True, "pic file","Unknown type picture file"
    elif header=="00 00 07":
        return True, "pjt file","UNKNOWN"
    elif header=="24 53 6F":
        return True, "pll file","UNKNOWN"
    elif header=="89 50 4E":
        return True, "png file","PNG Image File"
    elif header=="52 65 63":
        return True, "ppc file","unknown"
    elif header=="42 4F 4F 4B 4D 4F 42 49":
        return True, "prc file","Palmpilot resource file"
    elif header=="23 44 45":
        return True, "prg file","UNKNOWN"
    elif header=="25 21 50 53 2D 41 64 6F 62 65":
        return True, "ps file","Postscript"
    elif header=="38 42 50":
        return True, "psd file","Adobe Photoshop image file"
    elif header=="7E 42 4B 00":
        return True, "psp file","PaintShop Pro Image File"
    elif header=="21 42 44 4E":
        return True, "pst file","Microsoft Outlook Personal Folder file"
    elif header=="E3 82 85 96":
        return True, "pwl file","Windows Password"
    elif header=="45 86 00 00 06 00":
        return True, "qbb file","Intuit QuickBooks Backup file"
    elif header=="AC 9E BD 8F":
        return True, "qdf file","Quicken"
    elif header=="03 00 00 00":
        return True, "qph file","Quicken price history file"
    elif header=="6D 64 61 74":
        return True, "qt file","Quicktime Movie File"
    elif header=="00 00 49 49 58 50 52":
        return True, "qxd file","Quark Express document (Intel & Motorola, respectively)"
    elif header=="00 00 4D 4D 58 50 52":
        return True, "qxd file","UNKNOWN"
    elif header=="2E 52 4D 46 00 00 00 12 00":
        return True, "ra file","Real Audio file"
    elif header=="2E 72 61 FD":
        return True, "ra;ram file","Real Audio File"
    elif header=="52 61 72":
        return True, "rar file","RAR Archive File"
    elif header=="06 05 00":
        return True, "raw file","UNKNOWN"
    elif header=="52 45 47 45 44 49 54 34":
        return True, "reg file","UNKNOWN"
    elif header=="01 DA 01 01 00 03":
        return True, "rgb file","Silicon Graphics RGB Bitmap"
    elif header=="2E 52 4D":
        return True, "rm;rmvb file","Real Media streaming media file"
    elif header=="ED AB EE DB":
        return True, "rpm file","RPM Archive File"
    elif header=="43 23 2B 44 A4 43 4D A5 48 64 72":
        return True, "rtd file","RagTime document file"
    elif header=="7B 5C 72":
        return True, "rtf file","Rich Text Format File"
    elif header=="24 46 4C 32 40 28 23 29 20 53 50 53 53 20 44 41 54 41 20 46 49 4C 45":
        return True, "sav file","SPSS Data file"
    elif header=="46 45 44 46":
        return True, "sbv file","(Unknown file type)"
    elif header=="2A 76 65":
        return True, "sch file","UNKNOWN"
    elif header=="80 53 43":
        return True, "scm file","UNKNOWN"
    elif header=="48 48 47 42 31":
        return True, "sh3 file","Harvard Graphics presentation file"
    elif header=="4B 49 00 00":
        return True, "shd file","Windows 9x printer spool file"
    elif header=="53 49 54 21":
        return True, "sit file","Stuffit v1 Archive File"
    elif header=="53 74 75 66 66 49 74":
        return True, "sit file","Stuffit v5 Archive File"
    elif header=="3A 56 45 52 53 49 4F 4E":
        return True, "sle file","Surfplan kite project file"
    elif header=="41 43 76":
        return True, "sle file","teganos Security Suite virtual secure drive"
    elif header=="53 52 01 00":
        return True, "sly;srt;slt file","Sage sly.or.srt.or.slt"
    elif header=="00 FF FF":
        return True, "smd file","UNKNOWN"
    elif header=="00 1E 84 90 00 00 00 00":
        return True, "snm file","Netscape Communicator (v4) mail folder"
    elif header=="4D 53 43 46":
        return True, "snp file","Microsoft Access Snapshot Viewer file"
    elif header=="00 BF":
        return True, "sol file","Adobe Flash shared object file (e.g., Flash cookies)"
    elif header=="00 00 01 00":
        return True, "spl file","Windows NT/2000/XP printer spool file"
    elif header=="FF FF FF":
        return True, "sub file","UNKNOWN"
    elif header=="43 57 53":
        return True, "swf file","Macromedia Shockwave Flash player file(Shockwave Flash file (v5+))"
    elif header=="41 4D 59 4F":
        return True, "syw file","Harvard Graphics symbol graphic"
    elif header=="00 00 02":
        return True, "tag file","UNKNOWN"
    elif header=="30 37 30 37 30 37":
        return True, "tar file","CPIO Archive File"
    elif header=="1F 9D 90":
        return True, "tar.z file","Compressed tape archive file"
    elif header=="49 20 49":
        return True, "tif;tiff file","Tagged Image File Format file"
    elif header=="49 49 2A":
        return True, "tif;tiff file","TIFF (Intel)"
    elif header=="49 49 2A 00":
        return True, "tif;tiff file","Tagged Image File Format file"
    elif header=="4D 4D 00 2A":
        return True, "tif;tiff file","Tagged Image File Format file"
    elif header=="4D 4D 2A":
        return True, "tif;tiff file","TIFF (Motorola)"
    elif header=="4D 4D 00 2B":
        return True, "tif;tiff file","BigTIFF files; Tagged Image File Format files >4 GB"
    elif header=="4D 53 46 54 02 00 01 00":
        return True, "tlb file","OLE, SPSS, or Visual C++ type library file"
    elif header=="01 10":
        return True, "tr1 file","Novell LANalyzer capture file"
    elif header=="00 01 00":
        return True, "tst;ttf file","UNKNOWN"
    elif header=="55 46 41":
        return True, "ufa file","UFA Archive File"
    elif header=="45 4E 54 52 59 56 43 44 02 00 00 01 02 00 18 58":
        return True, "vcd file","VideoVCD (GNU VCDImager) file"
    elif header=="42 45 47 49 4E 3A 56 43 41 52 44 0D 0A":
        return True, "vcf file","vCard file"
    elif header=="00 00 01 BA":
        return True, "vob file","DVD Video Movie File (video/dvd, video/mpeg)"
    elif header=="52 49 46":
        return True, "wav file","UNKNOWN"
    elif header=="57 41 56 45":
        return True, "wav file","wave files"
    elif header=="00 00 02 00":
        return True, "wb2 files","QuattroPro for Windows Spreadsheet file"
    elif header=="30 26 B2":
        return True, "wma files","UNKNOWN"
    elif header=="01 00 09 00":
        return True, "wmf files","Graphics Metafile,(Windows Metadata file (Win 3.x format))"
    elif header=="02 00 09 00":
        return True, "wmf files","Graphics Metafile"
    elif header=="D7 CD C6 9A":
        return True, "wmf files","Windows Meta File"
    elif header=="30 26 B2":
        return True, "wmv files","UNKNOWN"
    elif header=="FF 57 50 43":
        return True, "wp* files","WordPerfect"
    elif header=="FF 57 50 47":
        return True, "wpg files","WordPerfect Graphics"
    elif header=="31 BE":
        return True, "wri files","Microsoft Write file"
    elif header=="32 BE":
        return True, "wri files","Microsoft Write file"
    elif header=="1D 7D":
        return True, "ws files","WordStar Version 5.0/6.0 document"
    elif header=="58 42 45":
        return True, "xbe files","UNKNOWN"
    elif header=="3C":
        return True, "xdr files","BizTalk XML-Data Reduced Schema file"
    elif header=="09 02 06 00 00 00 10 00 B9 04 5C 00":
        return True, "xls files","MS Excel v2"
    elif header=="09 04 06 00 00 00 10 00 F6 05 5C 00":
        return True, "xls files","MS Excel v4"
    elif header=="D0 CF 11":
        return True, "xls files","MS Excel"
    elif header=="3C 3F 78":
        return True, "xml files","XML Document"
    elif header=="FF FE 3C 00 52 00 4F 00 4F 00 54 00 53 00 54 00 55 00 42 00":
        return True, "xml files","XML Document (ROOTSTUB)"
    elif header=="00 50 01":
        return True, "xmv files","UNKNOWN"
    elif header=="FF FE 3C":
        return True, "xsl files","UNKNOWN"
    elif header=="72 73 69 6F 6E 3D 22 31 3C 3F 78 6D 6C 20 76 65 2E 30 22 3F 3E":
        return True, "xul files","XML User Interface Language file"
    elif header=="1F 9D":
        return True, "Z files","TAR Compressed Archive File"
    elif header=="50 4B 03":
        return True, "zip files","ZIP Archive"
    elif header=="50 4B 30 30":
        return True, "zip files","ZIP Archive (outdated)"
    elif header=="5A 4F 4F 20":
        return True, "zoo files","ZOO Archive File"
    else:
        return False,"UNKNOWN","UNKNOWN"


def main():
    get_file_header("4D 5A")

if __name__=='__main__':
    main()
