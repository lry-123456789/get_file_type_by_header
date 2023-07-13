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

def main():
    get_file_header("4D 5A")

if __name__=='__main__':
    main()
