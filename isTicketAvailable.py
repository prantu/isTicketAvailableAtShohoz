__author__ = 'tamal.2k14@gmail.com (Tamal Sen)'
import mechanize #Browser for python
import lxml.html #Sorting elements of html
import  lxml.etree #Same
import winsound #To play beep sound
import colorama #To colorize output
from datetime import datetime
import time

colorama.init(strip=False, autoreset=True)
TicketPaisi = False
abort_after = 10 #Interval time for checking
url = 'https://www.shohoz.com/events/bangladesh-vs-england-series-2016/book-now/2016-10-12' # url of ticket selling event

print ("---Initiating Program---")
while (TicketPaisi== False):
    print "\t\t\t\t\t\t%s" % datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    start_time = time.time()
    br = mechanize.Browser()
    r = br.open(url)
    content = r.read()
    
    tree = lxml.html.fromstring(content)
    info = tree.xpath('//select[@id="ticket_type"]/option')
    all_tickets = [option.text for option in info]
    all_tickets.remove('Select Ticket Category') #unnecessary option value

#for seats in all_tickets:
#    print seats

    available_tickets = [s for s in all_tickets if "Sold Out" not in s]
    print "Avaible Tickets Category: %d" % len(available_tickets)
    if len(available_tickets) > 0: #if tickets are available play beep sound
        Freq = 3000  # Set Frequency To 2500 Hertz
        Dur = 3000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(Freq, Dur)
    for seats in available_tickets:
        print "{}\t%s".format(colorama.Fore.LIGHTGREEN_EX) % seats

    sold_out_tickets = [y for y in all_tickets if "Sold Out" in y]
    print "Unavailable Tickets Category: %d" % len(sold_out_tickets)
    for seats in sold_out_tickets:
        print "{}\t%s".format(colorama.Fore.RED) % (seats)
    while True:
        delta = time.time() - start_time
        if delta >= abort_after:
            break
