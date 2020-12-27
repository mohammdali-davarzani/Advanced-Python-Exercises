yekan = ["صفر", "یک","دو","سه","چهار","پنج","شش","هفت","هشت"," نُه"] 
dah_ta_nozdah = ["ده", "یازده","دوازده","سیزده","چهارده","پانزده","شانزده","هفده","هجده","نوزده"]
dahghan = ["","ده","بیست","سی","چهل","پنجاه","شست","هفتاد","هشتاد","نود"]
sadghan = [" ","صد","دویست","سیصد","چهارصد","پانصد","ششصد","هفتصد","هشتصد","نهصد"]  

adad = int(input("لطفا عدد مورد نظر خود را وارد کنید: "))

def tak_raghami(n):
    print(yekan[adad])
    
def do_raghmami(n):
    dahghan_adad = (n // 10)
    yekan_adad = (n % 10)
    if (dahghan_adad == 1):
        print ('%s' % (dah_ta_nozdah[yekan_adad]))
    elif (dahghan_adad > 1) and (yekan_adad == 0):
        print ('%s' % (dahghan[dahghan_adad]))
    else:
        print('%s و %s' % (dahghan[dahghan_adad], yekan[yekan_adad]))

def seh_raghami(n):
    sadghan_adad = (n // 100)
    dahghan_adad = ((n % 100) // 10)
    yekan_adad = (n % 10)
    if (sadghan_adad != 0) and (dahghan_adad == 0) and (yekan_adad == 0):
        print('%s' % (sadghan[sadghan_adad]))
    elif (sadghan_adad != 0) and (yekan_adad != 0) and (dahghan_adad == 0):
        print ('%s و %s' % (sadghan[sadghan_adad], yekan[yekan_adad]))
    elif (sadghan_adad != 0) and (dahghan_adad == 1) :
        print ('%s و %s' % (sadghan[sadghan_adad], dah_ta_nozdah[yekan_adad]))
    elif (sadghan_adad != 0) and (dahghan_adad != 0) and (yekan_adad == 0):
        print ('%s و %s' % (sadghan[sadghan_adad], dahghan[dahghan_adad]))
    else :
        print ('%s و %s و %s' % (sadghan[sadghan_adad], dahghan[dahghan_adad], yekan[yekan_adad]))
 
def chahar_raghami():
    hezarghan_adad = (n // 1000)
    sadghan_adad = ((n % 1000) // 100)
    dahghan_adad = ((n % 100) // 10)
    yekan_adad = (yekan % 10)
    if (hezarghan_adad != 0) and (sadghan_adad == 0) and (dahghan_adad == 0) and ( yekan_adad == 0):
        print ('%s' % (hezarghan_adad))




if (0 <= adad < 10):
    tak_raghami(adad)

elif (10 <= adad < 100):
    do_raghmami(adad)

elif (100 <= adad < 1000):
    seh_raghami(adad)