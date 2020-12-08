import datetime

class DateTime:
	def __init__(self):
		self.number_bangla = ['০', '১','২', '৩','৪','৫','৬', '৭', '৮', '৯', "-"]
		self.week_bangla = ["সোমবার", "মঙ্গলবার", "বুধবার","বৃহস্পতিবার", "শুক্রবার", "শনিবার", "রবিবার"]
		self.season_bangla = ["শীতকাল", "বসন্তকাল", "গ্রীষ্মকাল", "বর্ষাকাল", "শরৎকাল", "হেমন্তকাল"]
		self.month_bangla = ["পৌষ", "মাঘ", "ফাল্গুন", "চৈত্র", "বৈশাখ", "জ্যৈষ্ঠ","আষাঢ়", "শ্রাবণ", "ভাদ্র", "আশ্বিন", "কার্তিক", "অগ্রহায়ণ"]
		self.month_english = ["জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন", "জুলাই", "অগাস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর"]
		self.year_now = []

	# For Year
	def year_(self):
		date_time = str(datetime.datetime.now()).split()
		date = date_time[0].split("-")
		time = date_time[1].split(":")[:2]
		s = [d for d in date]
		
		year = s[0]
		month = s[1]
		day = s[2]

		year_split = [int(d) for d in year]
		month_split = [int(e) for e in month]
		day_split = [int(f) for f in day]
		# print(year_split)
		for k in range(len(day_split)):
			c = self.number_bangla[day_split[k]]
			self.year_now.append(c)

		for j in range(len(month_split)):
			b = self.number_bangla[month_split[j]]
			self.year_now.extend(b)

		for i in range(len(year_split)):
			a = self.number_bangla[year_split[i]]
			self.year_now.append(a)
		
		list_b = ["-", "-"]
		pos = [2, 5]
		for m in range(len(list_b)):
			self.year_now.insert(pos[m], list_b[m])
		str1 = ""
		year_now = str1.join(self.year_now)
		return year_now
		
	# year, month, day
	def get_all(self):
		date_time = str(datetime.datetime.now()).split()
		date = date_time[0].split("-")
		time = date_time[1].split(":")[:2]
		s = [d for d in date]
		
		year = int(s[0])
		month = int(s[1]) -1
		day = int(s[2])
		
		return year, month, day

	# For Month
	def month_(self):
		get_month = self.get_all()[1]
		month_name = self.month_english[get_month]
		return month_name

	# For Day
	def day_(self):
		get_day = self.get_all()[2]
		day_name = self.week_bangla[get_day%7]
		return day_name

