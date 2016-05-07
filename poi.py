import falcon
import json
import datetime
from APIHandler.poi_geosearch_api import POIGeosearch


class Resource(object):

    def on_get(self, req, resp, action, city):

        if action == 'get':
            if city == 'amsterdam':
                print 'amsterdam'
                #poi_generator = POIGeosearch()
                #results = poi_generator.call_api(latitude=52.310558, longitude=4.768221, radius=50)
                resp.body = "[{u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Amsterdam_-_Rembrandtplein.jpg/400px-Amsterdam_-_Rembrandtplein.jpg', u'title': u'Rembrandtplein', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xpt1/t51.2885-15/s320x320/e35/12519271_161293804241224_18092809_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12627900_1109783172395892_1672913314_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12523517_1700154446896729_211954136_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12534639_1106782979340072_884855857_n.jpg'}}], u'geoname_id': 6930385, u'grades': {u'yapq_grade': 5, u'city_grade': 1}, u'details': {u'short_description': u'Rembrandtplein  is a major square in central Amsterdam, the Netherlands, named after the famous painter Rembrandt van Rijn who owned a house nearby from 1639 to 1656.', u'description': u'Rembrandtplein  is a major square in central Amsterdam, the Netherlands, named after the famous painter Rembrandt van Rijn who owned a house nearby from 1639 to 1656.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Rembrandtplein'}, u'categories': [u'Gay villages in the Netherlands', u'Rembrandt'], u'location': {u'latitude': 52.3661, u'google_maps_link': u'http://maps.google.com?q=52.3661,4.89667', u'longitude': 4.89667}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/NationaalMonumentVanuitReuzenrad.JPG/400px-NationaalMonumentVanuitReuzenrad.JPG', u'title': u'Dam Square', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/1168444_1680561482203041_949776682_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12555869_521552514691734_1759881311_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12534241_1676888792596593_1155853042_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12479509_584524745036889_175633253_n.jpg'}}], u'geoname_id': 6930383, u'grades': {u'yapq_grade': 4.95, u'city_grade': 2}, u'details': {u'short_description': u'Dam Square, or simply the Dam , is a town square in Amsterdam, the capital of the Netherlands.', u'description': u'Dam Square, or simply the Dam , is a town square in Amsterdam, the capital of the Netherlands. Its notable buildings and frequent events make it one of the most well-known and important locations in the city and the country.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Dam Square'}, u'categories': [u'National squares', u'Squares in Amsterdam'], u'location': {u'latitude': 52.373, u'google_maps_link': u'http://maps.google.com?q=52.373,4.893', u'longitude': 4.893}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Amsterdam_oude_kerk2.jpg/300px-Amsterdam_oude_kerk2.jpg', u'title': u'Oude Kerk (Amsterdam)', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xpf1/t51.2885-15/s320x320/e35/12501942_688999944575764_1686687572_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12552305_1092592070799760_712228905_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12519196_1529048174055414_1013380282_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12545367_1735162970048919_1579984354_n.jpg'}}], u'geoname_id': 6951692, u'grades': {u'yapq_grade': 4.93, u'city_grade': 3}, u'details': {u'short_description': u'The 800-year-old Oude Kerk  is Amsterdam\u2019s oldest building and oldest parish church, founded ca.', u'description': u"The 800-year-old Oude Kerk  is Amsterdam\u2019s oldest building and oldest parish church, founded ca. 1213 and consecrated in 1306 by the bishop of Utrecht with Saint Nicolas as its patron saint. After the Reformation in 1578 it became a Calvinist church, which it remains today. It stands in De Wallen, now Amsterdam's main red-light district. The square surrounding the church is the Oudekerksplein.\n\n", u'wiki_page_link': u'https://en.wikipedia.org/wiki/Oude Kerk (Amsterdam)'}, u'categories': [u'1210s establishments'], u'location': {u'latitude': 52.3744, u'google_maps_link': u'http://maps.google.com?q=52.3744,4.89806', u'longitude': 4.89806}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Amsterdam_-_Rijksmuseum.jpg/400px-Amsterdam_-_Rijksmuseum.jpg', u'title': u'Museumplein', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xaf1/t51.2885-15/s320x320/e35/12545243_1730631840502244_527016889_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xft1/t51.2885-15/s320x320/e35/12568283_968501859897084_1860895020_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12547506_1126363204070721_207390270_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12568707_931991440231236_319709155_n.jpg'}}], u'geoname_id': 7602112, u'grades': {u'yapq_grade': 4.89, u'city_grade': 4}, u'details': {u'short_description': u'The Museumplein  is a public space in the borough Amsterdam South in Amsterdam, Netherlands.', u'description': u'The Museumplein  is a public space in the borough Amsterdam South in Amsterdam, Netherlands. Located at the Museumplein are three major museums - the Rijksmuseum, Van Gogh Museum, and Stedelijk Museum - and the concert hall Concertgebouw.\nThe area was the location of the International Colonial and Export Exhibition in 1883.\nThe Museumplein was reconstructed after a design by the Swedish/Danish landscape architect Sven-Ingvar Andersson in 1999. It now includes underground parking spaces and an underground supermarket. In the winter, the pond can be transformed into an artificial ice skating area.\nThe space is also used for  events such as festivals, celebrations, and demonstrations and Armin Van Buuren honoured The Dutch Team at Museumplein in 2010 by playing Swedish House Mafia.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Museumplein'}, u'categories': [u'Museum districts', u'North Holland geography stubs'], u'location': {u'latitude': 52.3572, u'google_maps_link': u'http://maps.google.com?q=52.3572,4.88194', u'longitude': 4.88194}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Amsterdam_rijkmuseum.JPG/400px-Amsterdam_rijkmuseum.JPG', u'title': u'Rijksmuseum', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xtp1/t51.2885-15/s320x320/e35/12534481_1516695028660428_479434465_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xap1/t51.2885-15/s320x320/e35/12530989_1545135939136340_579919657_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xap1/t51.2885-15/s320x320/e35/12383214_1052609091456433_1545322593_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xpf1/t51.2885-15/s320x320/e35/12523565_489066871278925_1255716361_n.jpg'}}], u'geoname_id': 6884785, u'grades': {u'yapq_grade': 4.88, u'city_grade': 5}, u'details': {u'short_description': u'The Rijksmuseum  is a Netherlands national museum dedicated to arts and history in Amsterdam.', u'description': u'The Rijksmuseum  is a Netherlands national museum dedicated to arts and history in Amsterdam. The museum is located at the Museum Square in the borough Amsterdam South, close to the Van Gogh Museum, the Stedelijk Museum Amsterdam, and the Concertgebouw.\nThe Rijksmuseum was founded in The Hague in 1800 and moved to Amsterdam in 1808, where it was first located in the Royal Palace and later in the Trippenhuis. The current main building was designed by Pierre Cuypers and first opened its doors in 1885. On 13 April 2013, after a ten-year renovation which cost \u20ac 375 million, the main building was reopened by Queen Beatrix. In 2013, it was the most visited museum in the Netherlands with a record number of 2.2 million visitors.\nThe museum has on display 8,000 objects of art and history, from their total collection of 1 million objects from the years 1200\u20132000, among which are some masterpieces by Rembrandt, Frans Hals, and Johannes Vermeer. The museum also has a small Asian collection which is on display in the Asian pavilion.\n^ a b History of the Rijksmuseum, Rijksmuseum. Retrieved 4 April 2013.\n^ a b Address and route, Rijksmuseum. Retrieved 4 April 2013.\n^ a b c The renovation, Rijksmuseum. Retrieved on 4 April 2013.\n^  |Recordaantal van bijna 2,5 miljoen bezoekers naar Rijksmuseum", Trouw, 2014. Retrieved on 30 December 2014.\n^ a b  Daan van Lent & Pieter van Os "Musea doen het goed: aantal bezoekers in 2013 fors gestegen", NRC Handelsblad, 2013. Retrieved on 2 January 2014.\n^ Top 100 Art Museum Attendance, The Art Newspaper, 2014. Retrieved on 28 June 2014.\n^ a b c Board of Directors, Rijksmuseum. Retrieved 4 April 2013.\n^ Museumplein, I Amsterdam. Retrieved 4 April 2013.\n^ "Rijksmuseum set for grand reopening in Amsterdam". BBC News. 4 April 2013. Retrieved 4 April 2013.\n^ "The Rijksmuseum reopens: A new golden age". The Economist . 13 April 2013. Retrieved 14 April 2013.\n^ "The Dutch Prize Their Pedal Power, but a Sea of Bikes Swamps Their Capital". The New York Times. 20 June 2013.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Rijksmuseum'}, u'categories': [u'1800 establishments in the Batavian Republic', u'Amsterdam-Zuid', u'Art museums and galleries in the Netherlands', u'Art museums established in 1800', u'European Museum of the Year Award winners', u'Museums in Amsterdam', u'National museums of the Netherlands', u'Order of Arts and Letters of Spain recipients', u'Pierre Cuypers buildings', u'Rijksmonuments in Amsterdam', u'Rijksmuseum Amsterdam'], u'location': {u'latitude': 52.36, u'google_maps_link': u'http://maps.google.com?q=52.36,4.88528', u'longitude': 4.88528}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Leidseplein.jpg/400px-Leidseplein.jpg', u'title': u'Leidseplein', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xat1/t51.2885-15/s320x320/e35/12479211_1395423604090457_472893097_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xtf1/t51.2885-15/s320x320/e35/12568285_995833223821612_192104662_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12519135_1517753508554539_1822161056_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e15/12545501_1681806412093435_326416457_n.jpg'}}], u'geoname_id': 6501323, u'grades': {u'yapq_grade': 4.88, u'city_grade': 6}, u'details': {u'short_description': u'The Leidseplein is a square in central Amsterdam, the Netherlands.', u'description': u'The Leidseplein is a square in central Amsterdam, the Netherlands. Lying in the southwest of the Grachtengordel district of Amsterdam, the Leidseplein is immediately northeast of the Singelgracht canal. It is situated on the crossroads of the Weteringschans, the Marnixstraat, and the Leidsestraat.\nThe Leidseplein is one of the busiest centres for nightlife in the city. Historically, the square was the end of the road from Leiden, and served as a parking lot for horse-drawn traffic. Today, modern traffic travels through the square and side streets are packed with restaurants and nightclubs. The Stadsschouwburg, a theater, is the most notable architectural landmark on the square, and the American Hotel is close by.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Leidseplein'}, u'categories': [], u'location': {u'latitude': 52.3642, u'google_maps_link': u'http://maps.google.com?q=52.3642,4.88298', u'longitude': 4.88298}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/MelkwegAmsterdam.jpg/400px-MelkwegAmsterdam.jpg', u'title': u'Melkweg', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xpt1/t51.2885-15/s320x320/e35/12558797_506177022895021_2062708696_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xat1/t51.2885-15/s320x320/e35/12558371_1717871131775953_916634204_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12543118_223421881330028_1957556110_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12479359_747572445379351_397249506_n.jpg'}}], u'geoname_id': 6951764, u'grades': {u'yapq_grade': 4.75, u'city_grade': 7}, u'details': {u'short_description': u'The Melkweg  is a popular music venue and cultural center in Amsterdam, Netherlands.', u'description': u'The Melkweg  is a popular music venue and cultural center in Amsterdam, Netherlands. It is located on the Lijnbaansgracht, near the Leidseplein, a prime nightlife center of Amsterdam. It is housed in a former dairy and is divided into a number of spaces of varying sizes. Besides a large hall for varying genres of music concerts, there are also spaces for dance/theater, cinema, photography and media-art. The Melkweg is run by a non-profit organisation that has existed since 1970.\nIt is referenced in the Cracker song "Euro-Trash Girl", the Lagwagon song "Infectious" and in title of the Half Man Half Biscuit song "Prag Vec at the Melkweg". The title of The Church\'s song "Under the Milky Way" is also a reference to the Melkweg. Heather Nova\'s 1995 EP "Live from the Milky Way" was recorded here as was Spacemen 3\'s album Performance.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Melkweg'}, u'categories': [u'Music venue stubs'], u'location': {u'latitude': 52.3647, u'google_maps_link': u'http://maps.google.com?q=52.3647,4.88139', u'longitude': 4.88139}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/De_Balie_overdag_gevel.jpg/400px-De_Balie_overdag_gevel.jpg', u'title': u'De Balie', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12424518_886294181469385_1810612876_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12407398_1543882392588826_1748749418_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12545443_1139414272735310_2076826202_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12568969_820065734769117_626185453_n.jpg'}}], u'geoname_id': 6951728, u'grades': {u'yapq_grade': 4.69, u'city_grade': 8}, u'details': {u'short_description': u'De Balie is a theatre and a centre for politics, culture and media, with a caf\xe9-restaurant at Kleine-Gartmanplantsoen 10, at Leidseplein in Amsterdam, The Netherlands.', u'description': u'De Balie is a theatre and a centre for politics, culture and media, with a caf\xe9-restaurant at Kleine-Gartmanplantsoen 10, at Leidseplein in Amsterdam, The Netherlands. De Balie specialises in a number of territories: politics, art, society, media and cinema, and regularly organises programs. These programs consistently bear the mark of a sharp and deeply analytical character; De Balie leaves no questions of social relevance unasked. Through talk shows, discussions, debates and theatre, De Balie mixes several points of view in a wayward and creative fashion.\nDe Balie was founded in 1982 and is situated in the previous District Court, built around the end of the nineteenth century, which moved to the Parnassusweg in Amsterdam.\nFelix Rottenberg is co-founder of De Balie. Anil Ramdas was director from 2003 to 2005. Writer and journalist Yoeri Albrecht has been director from December 1, 2010, to present. He succeeded Ellen Walraven, who is currently working as a dramaturge at Toneelgroep Amsterdam. The current Managing Director is Jolanda Beyer. Next to the direction, the organisation of De Balie contains multiple departments including programming, communications, finances, technicians, building and system management and the Grandcaf\xe9.\nFor some programs, De Balie cooperates with a number of set partners. For instance, the programmes in the series Mind the Gap and Justice for All are produced in cooperation with Oxfam Novib, while the Volkskrant, KNAW and Nemo have teamed up for years on the monthly program Kenniscaf\xe9, in which journalist-presenter Martijn van Calmthout discusses science in relation to current and controversial topics. Also, De Balie is part of the Cineville partnership and often collaborates with the SLAA.\n\n', u'wiki_page_link': u'https://en.wikipedia.org/wiki/De Balie'}, u'categories': [u'Theatres in the Netherlands'], u'location': {u'latitude': 52.3631, u'google_maps_link': u'http://maps.google.com?q=52.3631,4.88333', u'longitude': 4.88333}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Amsterdam_Heineken_Music_Hall_001.JPG/400px-Amsterdam_Heineken_Music_Hall_001.JPG', u'title': u'Heineken Music Hall', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12568969_614154798731603_1598047647_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12568077_1032408666820157_1000159112_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12558355_449593055236541_1795462347_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12545507_1665117037094198_1078001909_n.jpg'}}], u'geoname_id': 6951761, u'grades': {u'yapq_grade': 4.63, u'city_grade': 9}, u'details': {u'short_description': u'Heineken Music Hall  is a concert hall in Amsterdam, Netherlands, near the Amsterdam ArenA .', u'description': u'Heineken Music Hall  is a concert hall in Amsterdam, Netherlands, near the Amsterdam ArenA . The big hall has a capacity of 5500 and is 3000 m\xb2; a smaller hall  has a capacity of 700.\nThe Heineken Music Hall was specially designed for amplified music. The architect was Frits van Dongen of Architekten Cie. The building was constructed between 1996 and 2001, and cost \u20ac30 million.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Heineken Music Hall'}, u'categories': [u'Amsterdam-Zuidoost', u'Dutch building and structure stubs'], u'location': {u'latitude': 52.312, u'google_maps_link': u'http://maps.google.com?q=52.312,4.9444', u'longitude': 4.9444}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Canal_in_Jordaan%2C_Amsterdam_%289258952020%29.jpg/400px-Canal_in_Jordaan%2C_Amsterdam_%289258952020%29.jpg', u'title': u'Amsterdam-Centrum', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/1168444_1680561482203041_949776682_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12555869_521552514691734_1759881311_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12552346_1724780841136721_1809780436_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12534241_1676888792596593_1155853042_n.jpg'}}], u'geoname_id': 0, u'grades': {u'yapq_grade': 4.6, u'city_grade': 10}, u'details': {u'short_description': u'Amsterdam-Centrum is the inner-most borough of Amsterdam, Netherlands.', u'description': u'Amsterdam-Centrum is the inner-most borough of Amsterdam, Netherlands. Established in 2002, Amsterdam-Centrum was the last area in the city to be granted the status of self-governing borough. The borough is only 8.04 km2 large and covers the old innercity and the UNESCO-listed Amsterdam canal belt. In 2013, the borough had approximately 85,000 inhabitants, who on average had the second-highest income per household in the city.\n\n', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Amsterdam-Centrum'}, u'categories': [u'2002 establishments in the Netherlands', u'Boroughs of Amsterdam'], u'location': {u'latitude': 52.3731, u'google_maps_link': u'http://maps.google.com?q=52.3731,4.89222', u'longitude': 4.89222}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Paradiso_Amsterdam.jpg/400px-Paradiso_Amsterdam.jpg', u'title': u'Paradiso (Amsterdam)', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12424518_886294181469385_1810612876_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12407398_1543882392588826_1748749418_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12568969_820065734769117_626185453_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12677423_558269530995270_1306658424_n.jpg'}}], u'geoname_id': 6951766, u'grades': {u'yapq_grade': 4.55, u'city_grade': 11}, u'details': {u'short_description': u'Paradiso is a rock music venue and cultural center in Amsterdam, Netherlands.', u'description': u'Paradiso is a rock music venue and cultural center in Amsterdam, Netherlands.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Paradiso (Amsterdam)'}, u'categories': [u'Concert halls in Amsterdam', u'Music venues in the Netherlands', u'Rock music venues'], u'location': {u'latitude': 52.3622, u'google_maps_link': u'http://maps.google.com?q=52.3622,4.88389', u'longitude': 4.88389}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/SingelBloemenmarkt.jpg/400px-SingelBloemenmarkt.jpg', u'title': u'Bloemenmarkt', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xfp1/t51.2885-15/s320x320/e35/12446103_798883020234131_1373252570_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xpt1/t51.2885-15/s320x320/e35/12558953_173061023057168_1784759989_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xtf1/t51.2885-15/s320x320/e35/12568137_458255294364918_1792328174_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xft1/t51.2885-15/s320x320/e35/12558810_1561999007457150_711172706_n.jpg'}}], u'geoname_id': 6944487, u'grades': {u'yapq_grade': 4.53, u'city_grade': 12}, u'details': {u'short_description': u"The Bloemenmarkt is the world's only floating flower market.", u'description': u"The Bloemenmarkt is the world's only floating flower market. Founded in 1862, it is sited in Amsterdam, Netherlands, on Singel between Muntplein and Koningsplein in the city's southern canal belt. It includes 15 florists and garden shops as well as a range of souvenir gifts. The market is one of the main suppliers of flowers to central Amsterdam.\n\n", u'wiki_page_link': u'https://en.wikipedia.org/wiki/Bloemenmarkt'}, u'categories': [u'1862 establishments in the Netherlands', u'Culture in Amsterdam', u'Flower markets', u'Netherlands stubs', u'Retail markets in Amsterdam'], u'location': {u'latitude': 52.3667, u'google_maps_link': u'http://maps.google.com?q=52.3667,4.89194', u'longitude': 4.89194}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Willet-holthuysen.jpg/400px-Willet-holthuysen.jpg', u'title': u'Museum Willet-Holthuysen', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12558921_1696497803896491_951197333_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12547174_177153165981845_423715403_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12479561_811801172299865_542502145_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12558384_507389206107581_1608893248_n.jpg'}}], u'geoname_id': 6951749, u'grades': {u'yapq_grade': 4.48, u'city_grade': 13}, u'details': {u'short_description': u'Museum Willet-Holthuysen is a museum in Amsterdam, the Netherlands, on the Herengracht canal.', u'description': u'Museum Willet-Holthuysen is a museum in Amsterdam, the Netherlands, on the Herengracht canal. It is the only fully furnished canalside patrician house in Amsterdam that is open to the public. The museum has a large collection of silverware, plates, and books from the Dutch Golden Age. It also has a substantial collection of art.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Museum Willet-Holthuysen'}, u'categories': [u'Houses completed in 1685', u'Houses in the Netherlands', u'Museums established in 1895'], u'location': {u'latitude': 52.3656, u'google_maps_link': u'http://maps.google.com?q=52.3656,4.89917', u'longitude': 4.89917}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/AnneFrankMuseum.jpg/400px-AnneFrankMuseum.jpg', u'title': u'Anne Frank House', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xap1/t51.2885-15/s320x320/e35/12534213_1533037760327782_471792291_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xfp1/t51.2885-15/s320x320/e35/12534458_1566269493693003_1645250920_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12558268_183688348656619_522743306_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/918138_961003080619373_1372171444_n.jpg'}}], u'geoname_id': 6618987, u'grades': {u'yapq_grade': 4.46, u'city_grade': 14}, u'details': {u'short_description': u'The Anne Frank House  is a historic house and biographical museum dedicated to Jewish wartime diarist Anne Frank.', u'description': u'The Anne Frank House  is a historic house and biographical museum dedicated to Jewish wartime diarist Anne Frank. The building is located at the Prinsengracht, close to the Westerkerk, in central Amsterdam in the Netherlands.\nDuring World War II, Anne Frank hid from Nazi persecution with her family and four other people in hidden rooms at the rear of the 17th-century canal house, known as the Secret Annex . Anne Frank did not survive the war, but in 1947 her wartime diary was published. In 1957, the Anne Frank Foundation was established to protect the property from developers who wanted to demolish the block.\nThe museum opened on 3 May 1960.It preserves the hiding place, has a permanent exhibition on the life and times of Anne Frank, and has an exhibition space about all forms of persecution and discrimination. In 2013, the museum had 1.2 million visitors and was the 3rd most visited museum in the Netherlands, after the Rijksmuseum and Van Gogh Museum.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Anne Frank House'}, u'categories': [u'Anne Frank', u'Biographical museums in the Netherlands', u'Historic house museums in the Netherlands', u'Holocaust museums', u'Houses completed in 1635', u'Literary museums in the Netherlands', u'Museums established in 1960', u'The Holocaust in the Netherlands', u'World War II museums in the Netherlands'], u'location': {u'latitude': 52.3753, u'google_maps_link': u'http://maps.google.com?q=52.3753,4.884', u'longitude': 4.884}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Zaanse_Schans_LCD.jpg/400px-Zaanse_Schans_LCD.jpg', u'title': u'Zaanse Schans', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12534306_655182011251189_1442629370_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12523745_1509959942639487_300159216_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12446260_950635671690326_1378648637_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12424353_1747995348762658_374876555_n.jpg'}}], u'geoname_id': 2744115, u'grades': {u'yapq_grade': 4.46, u'city_grade': 15}, u'details': {u'short_description': u'Zaanse Schans  is a neighbourhood of Zaandam, near Zaandijk in the municipality of Zaanstad in the Netherlands, in the province of North Holland.', u'description': u'Zaanse Schans  is a neighbourhood of Zaandam, near Zaandijk in the municipality of Zaanstad in the Netherlands, in the province of North Holland. It has a collection of well-preserved historic windmills and houses; the ca. 35 houses from all over the Zaanstreek were moved to the museum area starting in 1961. The Zaans Museum, established in 1994, is located in the Zaanse Schans.\nThe Zaanse Schans is one of the popular tourist attractions of the region and an anchor point of ERIH, the European Route of Industrial Heritage. The neighbourhood attracts approximately 900,000 visitors every year.\nThe windmills were built after 1574.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Zaanse Schans'}, u'categories': [u'Museums in North Holland', u'Open-air museums in the Netherlands', u'Populated places in North Holland', u'Windmills in North Holland', u'Zaanstad'], u'location': {u'latitude': 52.4739, u'google_maps_link': u'http://maps.google.com?q=52.4739,4.81639', u'longitude': 4.81639}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Damrak.jpg/400px-Damrak.jpg', u'title': u'Damrak', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xap1/t51.2885-15/s320x320/e35/12424722_927681453987877_123295546_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xtf1/t51.2885-15/s320x320/e35/12568703_1541178662859639_11494941_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xat1/t51.2885-15/s320x320/e35/12552240_1650851441844772_1279357563_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12628136_1697501587157768_1468900070_n.jpg'}}], u'geoname_id': 6951689, u'grades': {u'yapq_grade': 4.37, u'city_grade': 16}, u'details': {u'short_description': u'The Damrak is an avenue and partially filled in canal at the centre of Amsterdam, running between Amsterdam Centraal in the north and Dam Square in the south.', u'description': u'The Damrak is an avenue and partially filled in canal at the centre of Amsterdam, running between Amsterdam Centraal in the north and Dam Square in the south. It is the main street where people arriving at the station enter the centre of Amsterdam. Also it is one of the two GVB tram routes from the station into the centre, with lines 4, 9, 16, 24, and 25 running down it. It is also on the route of the North/South Line  being constructed between the existing metro station at Centraal Station and the new Rokin station.\nThe street was located on a rak , a straight part of the Amstel river near a dam; hence the name. In the 19th century, a section of it was filled in. Because of the former stock exchange building, the monumental Beurs van Berlage, and several other buildings related to financial activities erected there in the early 20th century, the term "Damrak" has come to be a synonym for the Amsterdam Stock Exchange in the same way "Wall Street" is synonymous with the New York Stock Exchange and NASDAQ. The Beurs van Berlage now serves as a concert and exhibition hall. Today, the area is known for its restaurants, bars, and currency exchanges. Its canals serve as a busy area for canal boats, as well.\n\n', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Damrak'}, u'categories': [u'Streets in Amsterdam'], u'location': {u'latitude': 52.3761, u'google_maps_link': u'http://maps.google.com?q=52.3761,4.89722', u'longitude': 4.89722}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Amsterdam_west_kerk2.jpg/300px-Amsterdam_west_kerk2.jpg', u'title': u'Westerkerk', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xfa1/t51.2885-15/s320x320/e35/12552492_876904539092646_985977315_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xta1/t51.2885-15/s320x320/e35/12519192_1196131300401507_265072315_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12547545_189587898066622_1638344216_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12383597_1686772838258394_1894392167_n.jpg'}}], u'geoname_id': 6950949, u'grades': {u'yapq_grade': 4.34, u'city_grade': 17}, u'details': {u'short_description': u'Westerkerk  is a Dutch Protestant church in central Amsterdam in the Netherlands.', u'description': u"Westerkerk  is a Dutch Protestant church in central Amsterdam in the Netherlands. It is next to Amsterdam's Jordaan district, on the bank of the Prinsengracht canal.\n\n", u'wiki_page_link': u'https://en.wikipedia.org/wiki/Westerkerk'}, u'categories': [u'Buildings of the Dutch Golden Age', u'Canon of Amsterdam', u'Churches in Amsterdam', u'Protestant churches in the Netherlands', u'Religious buildings completed in 1631'], u'location': {u'latitude': 52.3744, u'google_maps_link': u'http://maps.google.com?q=52.3744,4.88361', u'longitude': 4.88361}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Ac.homomonument.jpg/400px-Ac.homomonument.jpg', u'title': u'Homomonument', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xfa1/t51.2885-15/s320x320/e35/12552492_876904539092646_985977315_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xta1/t51.2885-15/s320x320/e35/12519192_1196131300401507_265072315_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12547545_189587898066622_1638344216_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12534338_208045252875918_556047415_n.jpg'}}], u'geoname_id': 6951798, u'grades': {u'yapq_grade': 4.33, u'city_grade': 18}, u'details': {u'short_description': u'The Homomonument is a memorial in the centre of Amsterdam, the capital of the Netherlands.', u'description': u'The Homomonument is a memorial in the centre of Amsterdam, the capital of the Netherlands. It commemorates all gay men and lesbians who have been subjected to persecution because of their homosexuality. Opened on September 5, 1987, it takes the form of three large pink triangles made of granite, set into the ground so as to form a larger triangle, on the bank of the Keizersgracht canal, near the historic Westerkerk church. The Homomonument was designed to "inspire and support lesbians and gays in their struggle against denial, oppression and discrimination." It was the first monument in the world to commemorate gays and lesbians who were killed by the Nazis.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Homomonument'}, u'categories': [u'1987 in LGBT history', u'1987 sculptures', u'Buildings and structures in Amsterdam', u'Holocaust commemoration', u'LGBT in the Netherlands', u'LGBT monuments and memorials', u'Monuments and memorials in the Netherlands', u'Persecution of homosexuals in Nazi Germany and the Holocaust'], u'location': {u'latitude': 52.3744, u'google_maps_link': u'http://maps.google.com?q=52.3744,4.88476', u'longitude': 4.88476}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/DeKrijtberg_1.JPG/273px-DeKrijtberg_1.JPG', u'title': u'De Krijtberg', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12446208_747592755371149_2044104944_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12424386_1076045222446870_1640190593_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12555842_1678824245708066_1613831093_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12407733_970447823008395_1722280200_n.jpg'}}], u'geoname_id': 6951717, u'grades': {u'yapq_grade': 4.32, u'city_grade': 19}, u'details': {u'short_description': u'De Krijtberg Kerk is a Roman Catholic church in Amsterdam, located at the Singel.', u'description': u'De Krijtberg Kerk is a Roman Catholic church in Amsterdam, located at the Singel. The church was designed by Alfred Tepe and was opened in 1883.', u'wiki_page_link': u'https://en.wikipedia.org/wiki/De Krijtberg'}, u'categories': [u'Ignatian spirituality', u'Jesuit churches', u'Roman Catholic churches in the Netherlands', u'Spiritual retreats'], u'location': {u'latitude': 52.3678, u'google_maps_link': u'http://maps.google.com?q=52.3678,4.88806', u'longitude': 4.88806}}, {u'main_image': u'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/BegijnhofAmsterdamEurope.jpg/400px-BegijnhofAmsterdamEurope.jpg', u'title': u'Begijnhof, Amsterdam', u'contextual_images': [{u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xfp1/t51.2885-15/s320x320/e35/12362143_1024873100904610_70910299_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xpf1/t51.2885-15/s320x320/e35/12558307_909606252427326_972260301_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/hphotos-xaf1/t51.2885-15/s320x320/e35/12627885_1738104543077636_803751500_n.jpg'}}, {u'medium': {u'url': u'https://scontent.cdninstagram.com/t51.2885-15/s320x320/e35/12568239_473954026130571_1154247648_n.jpg'}}], u'geoname_id': 6951709, u'grades': {u'yapq_grade': 4.32, u'city_grade': 20}, u'details': {u'short_description': u'The Begijnhof is one of the oldest inner courts in the city of Amsterdam.', u'description': u'The Begijnhof is one of the oldest inner courts in the city of Amsterdam. A group of historic buildings, mostly private dwellings, centre on it. As the name suggests, it was originally a B\xe9guinage. Today it is also the site of the English Reformed Church.\n\n', u'wiki_page_link': u'https://en.wikipedia.org/wiki/Begijnhof, Amsterdam'}, u'categories': [u'Beguines and Beghards', u'Hofjes in Amsterdam', u'Visitor attractions in Amsterdam'], u'location': {u'latitude': 52.3694, u'google_maps_link': u'http://maps.google.com?q=52.3694,4.8901', u'longitude': 4.8901}}]"
                resp.status = falcon.HTTP_200
