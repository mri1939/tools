kendaraan = ['trukmuatan', 'bustingkat', 'minibus', 'truktanki', 'trukgandeng', 'bus', 'tanki', 'ban', 'truk', 'motor', 'sedan', 'mobilpickup', 'mobil', 'mobilbox']

for i in kendaraan:
    print "item {"
    print "  id: "+str(kendaraan.index(i)+1)
    print "  name: '"+i+"'"
    print "}"
    print ""
    print
