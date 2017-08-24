# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')

base_url = 'http://www.muthead.com'
ovr_min = 60
ovr_max = 64

market = {'xbox-one':4,'playstation-4':3}

teams = {'cardinals':67,'falcons':41,'ravens':52,'bills':63,'panthers':48,'bears':61,'bengals':62,'browns':65,'cowboys':38,'broncos':64,
         'lions':46,'packers':47,'texans':59,'colts':70,'jaguars':44,'chiefs':69,'rams':51,'dolphins':39,'vikings':58,'patriots':49,'saints':54,
         'giants':43,'jets':45,'raiders':50,'eagles':40,'steelers':56,'chargers':68,'49ers':42,'seahawks':55,'buccaneers':66,'titans':57,
         'redskins':53}

for market_key, market_value in market.items():
    print(market_key)
    for teams_key, teams_value in teams.items():
        prices = []
        page_num = 1
        isNext = True
        while(isNext):
            url = base_url + '/18/players' + '?filter-ovr-min=' + str(ovr_min) + '&filter-ovr-max=' + str(ovr_max) + '&filter-team=' + str(teams_value) + '&filter-market=' + str(market_value)
            if page_num > 1:
                url = url + "&page=" + str(page_num)

            page = urllib2.urlopen(url)

            soup = BeautifulSoup(page,"html.parser")
            filtered = soup.find_all(attrs={"class":"player-price tip"})

            for item in filtered:
                player_url = base_url + item.get("href") + "/" + market_key
                player_page = urllib2.urlopen(player_url)
                player_soup = BeautifulSoup(player_page,"html.parser")
                price = player_soup.find_all(attrs={"class":"item-price"})
                if market_value == 4:
                    price = price[0].get_text()
                elif market_value == 3:
                    price = price[1].get_text()


                price = price.split(" ")[0]
                if "—" not in price:
                    if "K" in price:
                        price = int(float(price.split("K")[0]) * 1000)
                    elif "M" in price:
                        price = int(float(price.split("M")[0]) * 1000000)
                    elif "," in price:
                        price = price.split(",")[0] + price.split(",")[1]
                    prices.append(int(price))
            next_page = soup.find_all(attrs={"rel":"next"})
            if len(next_page) > 0:
                isNext = True
                page_num = page_num + 1
            else:
                isNext = False

        average = sum(prices)/len(prices)
        print teams_key + ":" + str(average)
