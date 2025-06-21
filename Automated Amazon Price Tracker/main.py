import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


URL = "https://www.amazon.in/Haier-Inverter-Refrigerator-HEB-333DS-P-Convertible/dp/B0BTHLGYHZ/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.R3t0sYDGe4YgvlPwB9OuOaSPnA4sCEwiNWz0WNwGugnPy4BHQejaTHoXRClBtokGxgAn5Tu1nDNt9TcXoH3FjMIyJ_dMCzWPcqE6HZ0hHi82_omvi0gFwchSkNPlin4JxpNVC8rHTVr5LYs1lpYYXAy5k6lp-cYoMeR4C8Lo9qUcVlBKiQaY8i-IjlnoR_CTQqpGcWNaDsJ5eSeH_TNhjQxSUIlwqpnxqguBqIXe3ua_S6PObuJJ0wkkuBGbzku3hsDsx2Z8R8-OI1IFOv5sHItGqMAwN4jJy3_DKf8gFOY.BmHq5zfQYecP75GvlbSj9l2fi-V09Qgs6pH2THFWQTo&dib_tag=se&pd_rd_r=302c0b74-153b-4f7a-8e3e-8a71b8ee78a3&pd_rd_w=yNbSa&pd_rd_wg=kXNVG&qid=1750229268&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&th=1"
Header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.amazon.in/",
    "Cookie": "ad-id=A_Hd57lwm08blOUlf_eZmgg; ad-privacy=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
}
response = requests.get(URL,headers = Header)
website_html = response.content

soup = BeautifulSoup(website_html, "html.parser")

# price = soup.find(class_= "a-offscreen").get_text()


# # Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

# # Remove the dollar sign using split
price_without_currency = float(price.split("₹")[1].replace(",", ""))

title = soup.find(id="productTitle").get_text().strip()


MyMail = os.environ["mymail"]
Password = os.environ["password"]
SMTP_Address = os.environ["SMTP_Address"]
SMTP_Port = int(os.environ["SMTP_Port"])

Buy_price = 35000.00

if price_without_currency < Buy_price:
    
    message = f"{title} is now available for {price} \n\n Buy it now at {URL}"
    with smtplib.SMTP(SMTP_Address, SMTP_Port) as connection:
        connection.starttls()
        connection.login(user=MyMail, password = Password)
        connection.sendmail(from_addr= MyMail, 
                            to_addrs= ["12aashish3456@gmail.com","bagmaraayush@gmail.com"],
                            msg = f"Subject: Amazon Price Alert\n\n{message} \n\n".encode("utf-8"))





# from bs4 import BeautifulSoup
# import requests
# import smtplib
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Practice
# # url = "https://appbrewery.github.io/instant_pot/"
# # Live Site

# # ====================== Add Headers to the Request ===========================
# URL = "https://www.amazon.in/Haier-Inverter-Refrigerator-HEB-333DS-P-Convertible/dp/B0BTHLGYHZ/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.R3t0sYDGe4YgvlPwB9OuOaSPnA4sCEwiNWz0WNwGugnPy4BHQejaTHoXRClBtokGxgAn5Tu1nDNt9TcXoH3FjMIyJ_dMCzWPcqE6HZ0hHi82_omvi0gFwchSkNPlin4JxpNVC8rHTVr5LYs1lpYYXAy5k6lp-cYoMeR4C8Lo9qUcVlBKiQaY8i-IjlnoR_CTQqpGcWNaDsJ5eSeH_TNhjQxSUIlwqpnxqguBqIXe3ua_S6PObuJJ0wkkuBGbzku3hsDsx2Z8R8-OI1IFOv5sHItGqMAwN4jJy3_DKf8gFOY.BmHq5zfQYecP75GvlbSj9l2fi-V09Qgs6pH2THFWQTo&dib_tag=se&pd_rd_r=302c0b74-153b-4f7a-8e3e-8a71b8ee78a3&pd_rd_w=yNbSa&pd_rd_wg=kXNVG&qid=1750229268&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&th=1"
# Header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate br, zstd",
#     "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
#     "Dnt": "1",
#     "Priority": "u=1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "Referer": "https://www.amazon.in/",
#     "Cookie": "ad-id=A_Hd57lwm08blOUlf_eZmgg; ad-privacy=0",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
# }

# # Adding headers to the request
# response = requests.get(URL, headers=Header)

# soup = BeautifulSoup(response.content, "html.parser")
# # Check you are getting the actual Amazon page back and not something else:
# print(soup.prettify())

# # Find the HTML element that contains the price
# price = soup.find(class_="a-offscreen").get_text()

# # Remove the dollar sign using split
# price_without_currency = price.split("₹")[1].replace(",", "").strip()


# # Convert to floating point number
# price_as_float = float(price_without_currency)
# print(price_as_float)

# # Get the product title
# title = soup.find(id="productTitle").get_text().strip()
# print(title)

# # Set the price below which you would like to get a notification
# BUY_PRICE = 70

# if price_as_float < BUY_PRICE:
#     message = f"{title} is on sale for {price}!"

#     # ====================== Send the email ===========================

#     with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
#         connection.starttls()
#         result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
#         connection.sendmail(
#             from_addr=os.environ["EMAIL_ADDRESS"],
#             to_addrs=os.environ["EMAIL_ADDRESS"],
#             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
#         )
