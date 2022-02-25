import serial
bolunmus=[]

veribaglantisi=serial.Serial("COM4",9600)

print(veribaglantisi.isOpen())

# print("__________________________")
# b"data".decode("utf-8")  # seri haberleşme olarak usb byte olarak veri alıyor bu yüzden decode edilmesi gerekiyor
# decode edilen veri byte tan strye çevriliyor
gelenveri = veribaglantisi.readline()
print(gelenveri)
print("**********************")

cevilmis_veri = gelenveri.decode('UTF-8')
print("gelen veri = ",gelenveri)
print("cevrilmiş veri = ",cevilmis_veri)
print("**********************")
bolunmus = cevilmis_veri.split(" ")  # .split belitilen karaktere göre str dizisini böler
print(bolunmus)