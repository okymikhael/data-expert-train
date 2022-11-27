import os
import csv
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

count_record = 631
host = 'https://shopee.co.id'
DRIVER_PATH = '/driver/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# go to login page and scan qr
driver.get('https://shopee.co.id/buyer/login')
WebDriverWait(driver, 100).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

time.sleep(10)
driver.get('https://shopee.co.id/mall/brands/11042849')

WebDriverWait(driver, 100).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
total_alphabet_toko = 3 # skip for unexpected problem
# total_alphabet_toko = len(driver.find_elements(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[3]/div'))
print(total_alphabet_toko)

while total_alphabet_toko >= 1:
    link = []

    chat_outside = []
    follower_outside = []
    rating_outside = []
    bergabung_outside = []
    nama_toko_outside = []
    jml_produk_outside = []
    diskon_inside = []
    product_href = []
    nama_produk_outside = []
    diskon_outside = []
    murah_outside = []
    harga_awal_outside = []
    harga_akhir_outside = []
    terjual_inside = []
    lokasi_inside = []
    gratis_ongkir_inside = []
    favorit_inside = []
    total_sub_toko = len(driver.find_elements(By.XPATH, f'//*[@id="main"]/div/div[2]/div/div/div/div[3]/div[{total_alphabet_toko}]/div/div[2]/div'))

    while total_sub_toko >= 1:
        link.append(driver.find_element(by=By.XPATH, value=f'//*[@id="main"]/div/div[2]/div/div/div/div[3]/div[{total_alphabet_toko}]/div/div[2]/div[{total_sub_toko}]/a').get_attribute('href'))
        total_sub_toko -= 1

    for i, toko in enumerate(link):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i+1])
        driver.get(toko)

    skip_tab = []
    for i, toko in enumerate(link):
        driver.switch_to.window(driver.window_handles[i+1])

        # link_produk field
        WebDriverWait(driver, 100).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        
        try:
            nama_toko_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div/h1').get_attribute("innerText"))
        except NoSuchElementException:
            nama_toko_outside.append('')
        
        try:
            jml_produk_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]').get_attribute("innerText"))
        except NoSuchElementException:
            jml_produk_outside.append('')
        
        try:
            chat_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[2]').get_attribute("innerText"))
        except NoSuchElementException:
            chat_outside.append('')
        
        try:
            follower_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[4]/div[2]/div[2]').get_attribute("innerText"))
        except NoSuchElementException:
            follower_outside.append('')
        
        try:
            rating_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[5]/div[2]/div[2]').get_attribute("innerText"))
        except NoSuchElementException:
            rating_outside.append('')
        
        try:
            bergabung_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div[2]').get_attribute("innerText"))
        except NoSuchElementException:
            bergabung_outside.append('')
        
        try:
            nama_produk_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/a/div/div/div[2]/div[1]/div[1]/div').get_attribute("innerText"))
        except NoSuchElementException:
            nama_produk_outside.append('')
        
        try:
            diskon_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/a/div/div/div[2]/div[1]/div[2]/div[1]/div').get_attribute("innerText"))
        except NoSuchElementException:
            diskon_outside.append('')
        
        try:
            murah_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/a/div/div/div[2]/div[1]/div[2]/div[2]').get_attribute("innerText"))
        except NoSuchElementException:
            murah_outside.append('')
        
        try:
            harga_awal_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/a/div/div/div[2]/div[2]/div[1]').get_attribute("innerText"))
        except NoSuchElementException:
            harga_awal_outside.append('')
        
        try:
            harga_akhir_outside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/a/div/div/div[2]/div[2]/div[2]').get_attribute("innerText"))
        except NoSuchElementException:
            harga_akhir_outside.append('')

        # click product
        not_found = True
        while not_found:
            try:
                # check if all product sold
                if driver.find_elements(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[1]/a/div/div/div[1]/div/div[1]/div/div'):
                    skip_tab.append(i)
                    not_found = False
                    break

                harga_akhir_outside.append('')
                product = driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/a').get_attribute('href')
                product_href.append(product)
                driver.get(product)
                not_found = False

            except NoSuchElementException:
                not_found = True

    for i, toko in enumerate(link):
        if i in skip_tab:
            break

        driver.switch_to.window(driver.window_handles[1])

        # check if page need login refresh
        # timer_login = 2
        # login_page = True
        # while login_page:
        #     try:
        #         WebDriverWait(driver, 100).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        #         if driver.find_elements(By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input'):
        #             driver.get(product_href[i])
        #             time.sleep(timer_login)
        #             timer_login += 1
        #         else:
        #             login_page = False
        #     except NoSuchElementException:
        #         print('false element')


        WebDriverWait(driver, 100).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        try:
            diskon_inside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div[2]').get_attribute("innerText"))
        except NoSuchElementException:
            diskon_inside.append('')

        try:
            terjual_inside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div[1]').get_attribute("innerText"))
        except NoSuchElementException:
            terjual_inside.append('')

        try:
            lokasi_inside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[5]/div').get_attribute("innerText"))
        except NoSuchElementException:
            lokasi_inside.append('')

        try:
            gratis_ongkir_inside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div[3]/div/div[4]/div/div[3]/div/div[1]/div[2]').get_attribute("innerText"))
        except NoSuchElementException:
            gratis_ongkir_inside.append('')

        try:
            favorit_inside.append(driver.find_element(by=By.XPATH, value=f'/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/div[2]/button/div').get_attribute("innerText"))
        except NoSuchElementException:
            favorit_inside.append('')

        ## mapping csv
        count_record += 1
        cur_time = time.time()
        order = '{0}-{1}'.format(str(cur_time).split('.')[0], count_record)
        start_url = 'https://shopee.co.id/mall/brands/11042849'
        link_toko = toko.replace('https://shopee.co.id/','')
        link_toko_href = toko
        nama_toko = nama_toko_outside[i]
        jml_produk = jml_produk_outside[i]
        chat = chat_outside[i]
        follower = follower_outside[i]
        rating = rating_outside[i]
        bergabung = bergabung_outside[i]
        # promo = '' #hide
        alamat_toko = lokasi_inside[i]
        link_produk = f'{diskon_inside[i]}{nama_produk_outside[i]}{diskon_outside[i]}{murah_outside[i]}{harga_awal_outside[i]}{harga_akhir_outside[i]}{terjual_inside[i]}{lokasi_inside[i]}'
        link_produk_href = product_href[i]
        nama_produk = nama_produk_outside[i]
        promo_produk = diskon_outside[i]
        terjual = terjual_inside[i]
        gratis_ongkir = gratis_ongkir_inside[i].replace('Gratis Ongkir dengan', '')
        favorit = favorit_inside[i]

        with open('export/master.csv', 'a+', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            # writer.writerow(['web-scraper-order','web-scraper-start-url','link_toko','link_toko-href','nama_toko','Jml_produk','chat','follower','rating_toko','bergabung','promo','alamat_toko','link_produk','link_produk-href','nama_produk','promo_produk','terjual','gratis_ongkir','favorit'])
            writer.writerow([order, start_url, link_toko, link_toko_href, nama_toko, jml_produk, chat, follower, rating, bergabung, alamat_toko, link_produk, link_produk_href, nama_produk, promo_produk, terjual, gratis_ongkir, favorit])

        print(f'{diskon_inside[i]}{nama_produk_outside[i]}{diskon_outside[i]}{murah_outside[i]}{harga_awal_outside[i]}{harga_akhir_outside[i]}{terjual_inside[i]}{lokasi_inside[i]}')
        driver.close()

    for i in skip_tab:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()

    driver.switch_to.window(driver.window_handles[0])
    total_alphabet_toko -= 1

# shutdown pc after app done
os.system("shutdown /s /t 1")