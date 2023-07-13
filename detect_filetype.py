def get_file_header(header:str):
    if header=="00 00 1A 00 05 10 04":
        return "123 file","Lotus 1-2-3 spreadsheet (v9) file"
    elif header=="00 00 00 14 66 74 79 70 33 67 70":
        return "3gg;3gp;3g2 file","3rd Generation Partnership Project 3GPP multimedia files"
    elif header=="00 00 00 20 66 74 79 70 33 67 70":
        return "3gg;3gp;3g2 file","3rd Generation Partnership Project 3GPP2 multimedia files"
    elif header=="37 7A BC AF 27 1C":
        return "7z file","7-ZIP compressed file"
    elif header=="00 01 42 41":
        return "aba file","Palm Address Book Archive file"
    elif header=="41 4F 4C 49 4E 44 45 58":
        return "abi file","AOL address book index file"
    elif header=="41 4F 4C 44 42":
        return "aby;idx file","AOL database files: address book (ABY) and user configuration data (MAIN.IDX)"
    elif header=="00 01 00 00 53 74 61 6E 64 61 72 64 20 41 43 45 20 44 42":
        return "accdb file","Microsoft Access 2007 file"
    elif header=="4D 5A":
        return "acm file","MS audio compression manager driver"
    elif header=="44 4F 53":
        return "adf file","Amiga disk file"
    elif header=="03 00 00 00 41 50 50 52":
        return "adx file","Lotus Approach ADX file"
    elif header=="46 4F 52 4D 00":
        return "aiff file","Audio Interchange File"
    elif header=="21 12":
        return "ain file","AIN Compressed Archive File"
    elif header=="5B 76 65 72 5D":
        return "ami file","Lotus Ami Pro"
    elif header=="23 21 41 4D 52":
        return "amr file","Adaptive Multi-Rate ACELP (Algebraic Code Excited Linear Prediction) Codec, commonly audio format with GSM cell phones"
    elif header=="52 49 46 46":
        return "ani file","UNKNOWN"
    elif header=="4D 5A 90 00 03 00 00 00":
        return "api file","Acrobat plug-in"
    elif header=="1A 02":
        return "arc file","LH archive file, old version,type 1"
    elif header=="1A 03":
        return "arc file","LH archive file, old version,type 2"
    elif header=="1A 04":
        return "arc file","LH archive file, old version,type 3"
    elif header=="1A 08":
        return "arc file","LH archive file, old version,type 4"
    elif header=="1A 09":
        return "arc file","LH archive file, old version,type 1"
    elif header=="41 72 43 01":
        return "arc file","FreeArc compressed file"
    elif header=="60 EA":
        return "arj file","ARJ Compressed Archive"
    elif header=="4A 47 03 0E 00 00 00":
        return "art file","AOL ART file"
    elif header=="4A 47 04 0E 00 00 00":
        return "art file","AOL ART file"
    elif header=="30 26 B2 75 8E 66 CF 11":
        return "asf file","Windows Media"
    elif header=="30 26 B2 75 8E 66 CF 11 A6 D9 00 AA 00 62 CE 6C":
        return "asf;wma;wmv file","Microsoft Windows Media Audio/Video File(Advanced Streaming Format)"
    elif header=="3C":
        return "asx file","Advanced Stream redirector file"
    elif header=="2E 73 6E 64":
        return "au file","SoundMachine Audio FileNeXT/Sun Microsystems μ-Law audio file"
    elif header=="41 56 49 20":
        return "avi file","Audio Video Interleave (AVI)"
    elif header=="4D 5A":
        return "AX file","Library cache file"
    elif header=="4D 5A 90 00 03 00 00 00":
        return "AX file","DirectShow filter"
    elif header=="41 4F 4C 20 46 65 65 64 62 61 67":
        return "bag file","AOL and AIM buddy list file"
    elif header=="20 20 20":
        return "bas file","UNKNOWN"
    elif header=="42 4C 49 32 32 33 51":
        return "bin file","Thomson Speedtouch series WLAN router firmware"
    elif header=="42 4D":
        return "bmp file","Windows Bitmap"
    elif header=="42 4D 3E":
        return "bmp file","UNKNOWN"
    elif header=="42 5A 68":
        return "bz;bz2,(BZ2;TAR.BZ2;TBZ2;TB2) file","BZIP Archive(bzip2 compressed archive)"
    elif header=="49 53 63":
        return "cab file","UNKNOWN"
    elif header=="49 53 63 28":
        return "cab;hdr file","Install Shield v5.x or 6.x compressed file"
    elif header=="4D 53 43 46":
        return "cab file","Microsoft CAB File Format"
    elif header=="30":
        return "cat file","Microsoft security catalog file"
    elif header=="43 42 46 49 4C 45":
        return "cbd file","WordPerfect dictionary file (unconfirmed)"
    elif header=="5B 43 6C":
        return "ccd file","UNKNOWN"
    elif header=="45 4C 49 54 45 20 43 6F 6D 6D 61 6E 64 65 72 20":
        return "cdr file","Elite Plus Commander saved game file"
    elif header=="4D 53 5F 56 4F 49 43 45":
        return "cdr;dvf file","Sony Compressed Voice File"
    elif header=="49 54 53 46":
        return "chi;chm file","Microsoft Compiled HTML Help File"
    elif header=="49 54 53":
        return "chm file","UNKNOWN"
    elif header=="43 4D 58 31":
        return "clb file","Corel Binary metafile"
    elif header=="43 4F 4D 2B":
        return "clb file","COM+ Catalog file"
    elif header=="3A 42 61 73 65":
        return "cnt file","UNKNOWN"
    elif header=="4D 5A":
        return "com;dll;drv;exe;pif;qts;qtx;sys(cpl)","Windows/DOS executable file(Control panel application)"
    elif header=="E9 3B 03":
        return "com file","UNKNOWN"
    elif header=="46 41 58 43 4F 56 45 52 2D 56 45 52":
        return "cpe file","Microsoft Fax Cover Sheet"
    elif header=="43 50 54 37 46 49 4C 45":
        return "cpt file","Corel Photopaint file"
    elif header=="43 50 54 46 49 4C 45":
        return "cpt file","Corel Photopaint file"
    elif header=="5B 57 69":
        return "cpx file","UNKNOWN"
    elif header=="43 52 55 53 48":
        return "cru* file","CRUSH Archive File"
    elif header=="43 52 55 53 48 20 76":
        return "cru file","Crush compressed archive"
    elif header=="49 49 1A 00 00 00 48 45 41 50 43 43 44 52 02 00":
        return "crw file","Canon digital camera RAW file"
    elif header=="43 61 74 61 6C 6F 67 20 33 2E 30 30 00":
        return "ctf file","WhereIsIt Catalog file"
    elif header=="00 00 02 00 01 00 20 20":
        return "cur file","Windows cursor file"
    elif header=="03":
        return "dat file","MapInfo Native Data Format"
    elif header=="1A 52 54 53 20 43 4F 4D 50 52 45 53 53 45 44 20 49 4D 41 47 45 20 56 31 2E 30 1A":
        return "dat file","Runtime Software disk image"
    elif header=="41 56 47 36 5F 49 6E 74 65 67 72 69 74 79 5F 44 61 74 61 62 61 73 65":
        return "dat file","AVG6 Integrity database file"
    elif header=="43 52 45 47":
        return "dat file","Windows 9x registry hive"
    elif header=="43 6C 69 65 6E 74 20 55 72 6C 43 61 63 68 65 20 4D 4D 46 20 56 65 72 20":
        return "dat file","IE History DAT file"
    elif header=="45 52 46 53 53 41 56 45 44 41 54 41 46 49 4C 45":
        return "dat file","Kroll EasyRecovery Saved Recovery State file"
    elif header=="49 6E 6E 6F 20 53 65 74 75 70 20 55 6E 69 6E 73 74 61 6C 6C 20 4C 6F 67 20 28 62 29":
        return "dat file","Inno Setup Uninstall Log file"
    elif header=="00 06 15 61 00 00 00 02 00 00 04 D2 00 00 10 00":
        return "db file","Netscape Navigator (v4) database file"
    elif header=="44 42 46 48":
        return "db file","Palm Zire photo database"
    elif header=="08":
        return "db file","dBASE IV or dBFast configuration file"
    elif header=="03":
        return "db3 file","dBASE III file"
    elif header=="04":
        return "db4 file","dBASE IV data file"
    elif header=="00 01 42 44":
        return "dba file","Palm DateBook Archive file"
    elif header=="CF AD 12 FE":
        return "dbx file","UNKNOWN"
    elif header=="CF AD 12 FE C5 FD 74 6F":
        return "dbx file","Outlook Express"
    elif header=="3C 21 64 6F 63 74 79 70":
        return "dci file","AOL HTML mail file"
    elif header=="3A DE 68 B1":
        return "dcx file","DCX Graphic File"
    elif header=="00 01 00":
        return "ddb file","UNKNOWN"
    elif header=="42 4D":
        return "dib file","device-independent bitmap image"
    elif header=="4D 5A 90":
        return "dll file","UNKNOWN"
    elif header=="4D 44 4D 50 93 A7":
        return "dmp file","Windows minidump file"
    elif header=="44 4D 53 21":
        return "dms file","Amiga DiskMasher compressed archive"
    elif header=="0D 44 4F 43":
        return "doc file","DeskMate Document file"
    elif header=="12 34 56 78 90 FF":
        return "doc file","MS Word 6.0"
    elif header=="31 BE 00 00 00 AB 00 00":
        return "doc file","MS Word for DOS 6.0"
    elif header=="7F FE 34 0A":
        return "doc file","MS Word"
    elif header=="D0 CF 11 E0":
        return "dot;ppt;xla;ppa;pps;pot;msi;sdw;db file","MS Office/OLE2"
    elif header=="D0 CF 11 E0 A1 B1 1A E1":
        return "doc;dot;xls;xlt;xla;ppt;apr;ppa;pps;pot;msi;sdw;db file","MS Compound Document v1 or Lotus Approach APR file"
    elif header=="4D 5A 50":
        return "dpl file","UNKNOWN"
    elif header=="4D 5A 16":
        return "drv file","UNKNOWN"
    elif header=="07":
        return "drw file","A common signature and file extension for many drawing programs."
    elif header=="01 FF 02 04 03 02":
        return "drw file","Micrografx vector graphic file"
    elif header=="4D 47 58 20 69 74 70 64":
        return "ds4 file","Micrografix Designer 4"
    elif header=="4D 56":
        return "dsn file","CD Stomper Pro label file"
    elif header=="23 20 4D 69 63 72 6F 73 6F 66 74 20 44 65 76 6 56C 6F 70 65 72 20 53 74 75 64 69 6F":
        return "dsp file","Microsoft Developer Studio project file"
    elif header=="02 64 73 73":
        return "dss file","Digital Speech Standard (Olympus, Grundig, & Phillips)"
    elif header=="07 64 74 32 64 64 74 64":
        return "dtd file","DesignTools 2D Design file"
    elif header=="3C 21 45 4E 54 49 54 59":
        return "dtd file","XML DTD"
    elif header=="44 56 44":
        return "dvr file","DVR-Studio stream file"
    elif header=="41 43 31":
        return "dwg file","UNKNOWN"
    elif header=="41 43 31 30":
        return "dwg file","UNKNOWN"
    elif header=="45 56 46":
        return "enn file","EnCase evidence file"
    elif header=="2A 50 52":
        return "eco file","UNKNOWN"
    elif header=="7F 45 4C 46 01 01 01 00":
        return "elf file","ELF Executable"
    elif header=="01 00 00 00 58 00 00 00":
        return "emf file","Extended (Enhanced) Windows Metafile Format, printer spool file"
    elif header=="44 65 6C 69 76 65 72 79 2D 64 61 74 65 3A":
        return "eml file","email"
    elif header=="46 72 6F 6D 20 20 20":
        return "eml file","A common file extension for e-mail file"
    elif header=="46 72 6F 6D 20 3F 3F 3F":
        return "eml file", "A common file extension for e-mail file"
    elif header=="46 72 6F 6D 3A 20":
        return "eml file", "A common file extension for e-mail file"
    elif header=="52 65 63":
        return "eml file","UNKNOWM"
    elif header=="00 5C 41 B1 FF":
        return "enc file","Mujahideen Secrets 2 encrypted file"
    elif header=="25 21 50 53":
        return "eps file","Adobe EPS File"
    elif header=="25 21 50 53 2D 41 64 6F 62 65":
        return "eps file","Postscript"
    elif header=="25 21 50 53 2D 41 64 6F 62 65 2D 33 2E 30 20 45 50 53 46 2D 33 20 30":
        return "eps file","Adobe encapsulated PostScript file"
    elif header=="C5 D0 D3":
        return "eps file","UNKNOWN"
    elif header=="1A 35 01 00":
        return "eth file","GN Nettest WinPharoah capture file"
    elif header=="30 00 00 00 4C 66 4C 65":
        return "evt file","Windows Event Viewer file"
    elif header=="03 00 00 00 C4 66 C4 56":
        return "evt file","UNKNOWN"
    elif header=="45 6C 66 46 69 6C 65 00":
        return "evtx file","Windows Vista event log file"
    elif header=="4D 5A":
        return "exe;com;386;ax;acm;sys;dll;drv;flt;fon;ocx;scr;lrc;vxd;cpl;x32","Executable File"


def main():
    get_file_header("4D 5A")

if __name__=='__main__':
    main()
