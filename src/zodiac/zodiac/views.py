import datetime
from datetime import datetime, date, time

def home_view(request):
	if(request.POST.get("dia")!="" and request.POST.get("mes")!=""):
		dia = request.POST.get("dia")
		mes = request.POST.get("mes")
		an = 1989

		if not dia and not mes:
			return {'project':'zodiac','signe':''}

		naix = date(an,int(mes),int(dia))
		signe = ""

		zodnom = [ "aquarius", "piscis", "aries", "tauro", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagitari", "capricorn"]
		zodin = [date(an, 1, 20), date(an, 2, 18), date(an, 3, 20), date(an, 4, 20), date(an, 5, 21), date(an, 6, 21), date(an, 7, 23), date(an, 8, 23), date(an, 9, 23), date(an, 10, 23), date(an, 11, 22), date(an, 12, 23), date(an, 12, 31)]


		for i in xrange(0, len(zodnom)):
		    if (naix >= zodin[i] and naix < zodin[i + 1]):
			    signe = zodnom[i]
		if (signe == ""):
		    signe = zodnom[len(zodnom) - 1]    
	    	
		return {'project':'zodiac','signe':signe}


