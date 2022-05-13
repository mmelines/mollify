import datetime
import random
from calendar import monthrange

class Lorem:

	def __init__(self):
		self.location_names = ['San Francisco', 'New York', 'Los Angeles', 'New Orleans',
			'Nashville', 'Chicago', 'Austin', 'Philadelphia', 'Atlanta']
		self.locations = {
			'San Francisco' : {
				'artist_ids': [],
				'venue_ids': [],
				'state' : "CA",
				'area_codes' : [415, 628],
				'zip_codes': [94109, 94110, 94122, 94112,
					94115, 94102, 94117, 94121, 94103,
					94118, 94107, 94114, 94116, 94123,
					94131, 94133, 94134, 94124, 94132,
					94105, 94127, 94108, 94158, 94111,
					94129, 94119, 94188, 94142, 94141,
					94130, 94140, 94147, 94164, 94159,
					94104, 94146, 94126, 94016, 94172,
					94125, 94120, 94143, 94144, 94145,
					94136, 94137, 94150, 94151, 94152,
					94153, 94154, 94155, 94156, 94157,
					94138, 94139, 94160, 94161, 94162,
					94163, 94101, 94165, 94166, 94167,
					94168, 94169, 94170, 94171, 94106,
					94175, 94177, 94135, 94199]},
			'New York' : {
				'artist_ids': [],
				'venue_ids': [],
				'state' : "NY",
				'area_codes': [300, 914, 718, 212],
				'zip_codes': [10025, 10023, 10002, 10016,
					10029, 10009, 10011, 10128, 10019,
					10003, 10463, 10024, 10028, 10027,
					10021, 10032, 10031, 10451, 10014,
					10036, 10033, 10010, 10022, 10065,
					10001, 10040, 10034, 10026, 10013,
					10035, 10075, 10012, 10454, 10038,
					10030, 10017, 10039, 10037, 10018,
					10005, 10044, 10280, 10069, 10007,
					10282, 10006, 10004, 10116, 10163,
					10150, 10162, 10008, 10276, 10101,
					10159, 10108, 10113, 10185, 10272,
					10156, 10274, 10129, 10268, 10102,
					10103, 10104, 10105, 10106, 10107,
					10043, 10109, 10110, 10111, 10112,
					10015, 10114, 10115, 10045, 10117,
					10118, 10119, 10120, 10121, 10122,
					10123, 10124, 10125, 10126, 10046,
					10047, 10130, 10131, 10132, 10133,
					10138, 10149, 10048, 10151, 10152,
					10153, 10154, 10155, 10055, 10157,
					10158, 10060, 10160, 10161, 10020,
					10072, 10164, 10165, 10166, 10167,
					10168, 10169, 10170, 10171, 10172,
					10173, 10174, 10175, 10176, 10177,
					10178, 10179, 10184, 10079, 10196,
					10197, 10199, 10203, 10211, 10212,
					10213, 10242, 10249, 10256, 10257,
					10258, 10259, 10260, 10261, 10265,
					10080, 10269, 10270, 10271, 10081,
					10273, 10082, 10275, 10087, 10277,
					10278, 10279, 10090, 10281, 10094,
					10285, 10286, 10292, 10095, 10096,
					10098, 10099, 10041]},
			'Los Angeles' : {
				'artist_ids': [],
				'venue_ids': [],
				'state': "CA",
				'area_codes': [213, 310, 424, 661, 818, 323],
				'zip_codes': [90250, 90046, 90034, 90805, 90650,
					90044, 90026, 90066, 90019, 90004,
					90280, 91342, 90201, 90706, 90025,
					90011, 90027, 91335, 90731, 93536,
					93550, 93535, 90802, 90631, 90036,
					90640, 91331, 91801, 90042, 90028,
					90006, 90255, 90024, 91402, 91367,
					91766, 91406, 90049, 91706, 90277,
					90020, 91744, 91601, 91405, 90813,
					90005, 90803, 91702, 90503, 91343,
					90043, 91770, 90047, 90003, 90247,
					90045, 90016, 90037, 91304, 90018,
					93551, 90022, 91344, 90278, 90703,
					90057, 91745, 90660, 91765, 91605,
					90275, 90745, 91016, 90804, 90815,
					90065, 93534, 91606, 90292, 90029,
					90291, 91732, 91423, 90501, 90262,
					90723, 90069, 92821, 90241, 90405,
					91401, 91767, 90638, 90008, 90266,
					91205, 91387, 90505, 91604, 90403,
					90808, 90744, 90017, 91306, 91748,
					90012, 91311, 90035, 91607, 90007,
					90048, 91350, 91505, 91750, 90015,
					91107, 90032, 90068, 91206, 90001,
					90807, 91326, 90063, 90064, 90033]
				},
			'Nashville': {
				'artist_ids': [],
				'venue_ids': [],
				'state': "TN",
				'area_codes': [423, 615, 629, 731, 865, 901, 931],
				'zip_codes': [37013, 37211, 37027, 37209, 37221,
					37076, 37115, 37207, 37214, 37203,
					37217, 37206, 37072, 37086, 37205,
					37215, 37208, 37138, 37216, 37212,
					37210, 37204, 37218, 37080, 37220,
					37219, 37143, 37189, 37228, 37201,
					37024, 37011, 37070, 37229, 37116,
					37222, 37202, 37224, 37213, 37227,
					37230, 37232, 37234, 37235, 37236,
					37237, 37238, 37240, 37241, 37242,
					37243, 37244, 37245, 37246, 37247,
					37248, 37249, 37250]
				},
			'New Orleans': {
				'artist_ids': [],
				'venue_ids': [],
				'state': "LA",
				'area_codes': [504],
				'zip_codes':[70119, 70115, 70118, 70117, 70122,
					70126, 70130, 70131, 70114, 70124,
					70127, 70116, 70125, 70128, 70113,
					70112, 70129, 70187, 70174, 70179,
					70175, 70182, 70185, 70177, 70158,
					70156, 70186, 70157, 70184, 70152]
				},
			'Chicago': {
				'artist_ids': [],
				'venue_ids': [],
				'state': "IL",
				'area_codes': [312, 773],
				'zip_codes': [60657, 60614, 60640, 60647, 60618,
					60613, 60610, 60625, 60629, 60611,
					60619, 60617, 60620, 60634, 60016,
					60628, 60626, 60649, 60622, 60616,
					60615, 60641, 60660, 60453]
				},
			'Austin': {
				'artist_ids': [],
				'venue_ids': [],
				'state': "TX",
				'area_codes': [512],
				'zip_codes': [77474, 77418, 78950, 78933, 78944,
					78931, 77473, 77452]
				},
			'Philadelphia': {
				'artist_ids': [],
				'venue_ids': [],
				'state': "PA",
				'area_codes': [267, 215, 445],
				'zip_codes': [19143, 19111, 19124, 19104, 19120,
					19134, 19148, 19131, 19144, 19146,
					19145, 19140, 19147, 19149, 19103,
					19139, 19121, 19128, 19130, 19132,
					19115, 19114, 19152]
				},
			'Atlanta': {
				'artist_ids': [],
				'venue_ids': [],
				'state': "GA",
				'area_codes': [404, 470, 678, 770],
				'zip_codes': [30349, 30318, 30331, 30004, 30022,
					30075, 30319, 30328, 30309, 30324,
					30097, 30339, 30076, 30350, 30305,
					30213, 30316, 30311, 30344, 30342,
					30308, 30312, 30005, 30315, 30310,
					30306]
				}
			}
		self.names = { 'street_self.names': [ "Second", "Third", "First", "Fourth", "Park",
					"Fifth", "Main", "Sixth", "Oak", "Seventh", "Pine", "Maple",
					"Cedar", "Eighth", "Elm", "View", "Washington", "Ninth",
					"Lake", "Hill", "Lee", "Dogwood", "Magnolia", "Aspen",
					"Church", "School", "Hemlock", "Jackson", "Mulberry", "Broad",
					"King", "Ridge", "Cherry"],
					'street_ends': ['Road', "Street", "Lane", "Blvd", "Ave"],
					'first_self.names': [ "Michael", "Christopher", "Jessica", "Matthew",
					"Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David",
					"James", "Robert", "John", "Joseph", "Andrew", "Ryan",
					"Brandon", "Jason", "Justin", "Sarah", "William", "Jonathan",
					"Stephanie", "Brian", "Nicole", "Nicholas", "Anthony",
					"Heather", "Eric", "Elizabeth", "Adam", "Megan", "Melissa",
					"Kevin", "Steven", "Thomas", "Timothy", "Christina", "Kyle",
					"Rachel", "Laura", "Lauren", "Amber", "Brittany", "Danielle",
					"Richard", "Kimberly", "Jeffrey", "Amy", "Crystal", "Michelle",
					"Tiffany", "Jeremy", "Benjamin", "Mark", "Emily", "Aaron",
					"Charles", "Rebecca", "Jacob", "Stephen", "Patrick", "Sean",
					"Erin", "Zachary", "Jamie", "Kelly", "Samantha", "Nathan",
					"Sara", "Dustin", "Paul", "Angela", "Tyler", "Scott",
					"Katherine", "Andrea", "Gregory", "Erica", "Mary", "Travis",
					"Lisa", "Kenneth", "Bryan", "Lindsey", "Kristen", "Jose",
					"Alexander", "Jesse", "Katie", "Lindsay", "Shannon", "Vanessa",
					"Courtney", "Christine", "Alicia", "Cody", "Allison", "Bradley",
					"Samuel", "Shawn", "April", "Derek", "Kathryn", "Kristin",
					"Chad", "Jenna", "Tara", "Maria", "Krystal", "Jared", "Anna",
					"Edward", "Julie", "Peter", "Holly", "Marcus", "Kristina",
					"Natalie", "Jordan", "Victoria", "Jacqueline", "Corey",
					"Keith", "Monica", "Juan", "Donald", "Cassandra", "Meghan",
					"Joel", "Shane", "Phillip", "Patricia", "Brett", "Ronald",
					"Catherine", "George", "Antonio", "Cynthia", "Stacy",
					"Kathleen", "Raymond", "Carlos", "Brandi", "Douglas",
					"Nathaniel", "Ian", "Craig", "Brandy", "Alex", "Valerie",
					"Veronica", "Cory", "Whitney", "Gary", "Derrick", "Philip",
					"Luis", "Diana", "Chelsea", "Leslie", "Caitlin", "Leah",
					"Natasha", "Erika", "Casey", "Latoya", "Erik", "Dana",
					"Victor", "Brent", "Dominique", "Frank", "Brittney", "Evan",
					"Gabriel", "Julia", "Candice", "Karen", "Melanie", "Adrian",
					"Stacey", "Margaret", "Sheena", "Wesley", "Vincent",
					"Alexandra", "Katrina", "Bethany", "Nichole", "Larry",
					"Jeffery", "Curtis", "Carrie", "Todd", "Blake", "Christian",
					"Randy", "Dennis", "Alison", "Trevor", "Seth", "Kara", "Joanna",
					"Rachael", "Luke", "Felicia", "Brooke", "Austin", "Candace",
					"Jasmine", "Jesus", "Alan", "Susan", "Sandra", "Tracy", "Kayla",
					"Nancy", "Tina", "Krystle", "Russell", "Jeremiah", "Carl",
					"Miguel", "Tony", "Alexis", "Gina", "Jillian", "Pamela",
					"Mitchell", "Hannah", "Renee", "Denise", "Molly", "Jerry",
					"Misty", "Mario", "Johnathan", "Jaclyn", "Brenda", "Terry",
					"Lacey", "Shaun", "Devin", "Heidi", "Troy", "Lucas", "Desiree",
					"Jorge", "Andre", "Morgan", "Drew", "Sabrina", "Miranda",
					"Alyssa", "Alisha", "Teresa", "Johnny", "Meagan", "Allen",
					"Krista", "Marc", "Tabitha", "Lance", "Ricardo", "Martin",
					"Chase", "Theresa", "Melinda", "Monique", "Tanya", "Linda",
					"Kristopher", "Bobby", "Caleb", "Ashlee", "Kelli", "Henry",
					"Garrett", "Mallory", "Jill", "Jonathon", "Kristy", "Anne",
					"Francisco", "Danny", "Robin", "Lee", "Tamara", "Manuel",
					"Meredith", "Colleen", "Lawrence", "Christy", "Ricky", "Jay",
					"Randall", "Marissa", "Ross", "Mathew", "Jimmy", "Abigail",
					"Kendra", "Carolyn", "Billy", "Deanna", "Jenny", "Jon",
					"Albert", "Taylor", "Lori", "Rebekah", "Cameron", "Ebony",
					"Wendy", "Angel", "Micheal", "Kristi", "Caroline", "Colin",
					"Dawn", "Kari", "Clayton", "Arthur", "Roger", "Roberto",
					"Priscilla", "Darren", "Kelsey", "Clinton", "Walter", "Louis",
					"Barbara", "Isaac", "Cassie", "Grant", "Cristina", "Tonya",
					"Rodney", "Bridget", "Joe", "Cindy", "Oscar", "Willie",
					"Maurice", "Jaime", "Angelica", "Sharon", "Julian", "Jack"],
					'last_self.names': ["Smith", "Johnson", "Williams", "Brown", "Jones",
					"Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
					"Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
					"Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee",
					"Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
					"Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen",
					"King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
					"Green", "Adams", "Nelson", "Baker", "Hall", "Rivera",
					"Campbell", "Mitchell", "Carter"],
					'addr2_type': ["Apt", "Unit"]}
		self.char_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
						"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
						"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", 
						"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", 
						"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
		self.charset = {"lower": self.char_list[36:],
			            "upper": self.char_list[:26],
			            "nos": self.char_list[26:36]}

	def new_location(self):
		"""
		return dictionary of location information
		"""
		loc = random.choice(self.location_names)
		location = {"city": loc}
		loc_dict = self.locations[loc]
		location["zip_code"] = random.choice(loc_dict["zip_codes"])
		location["area_codes"] = random.choice(loc_dict["area_codes"])
		location["state"] = loc_dict["state"]
		return location

	@staticmethod
	def new_phone(area_code):
		"""
		return phone number formatted as a string
		"""
		phone = str(area_code)
		phone = phone + str(random.choice(range(101, 999)))
		phone = phone + str(random.choice(range(1000, 9999)))
		return phone

	def new_address(self):
		"""
		generate random specific street address
		"""
		street = random.choice(self.names["street_self.names"])
		street_end = random.choice(self.names["street_ends"])
		full_street = street + " " + street_end
		address = str(random.choice(range(100, 9999))) + " "
		address = address + full_street
		return address

	@staticmethod
	def new_addr_two():
		"""
		generate random address line 2
		"""
		part_one = random.choice(["Unit", "Apartment"])
		part_two = random.choice(["A", "B", "C", "D", "1", "2", "3", "4", "5"])
		return part_one + " " + part_two

	def short_location(self):
		"""
		generate only general location information
		"""
		loc = self.new_location()
		obj = {"city": loc["city"],
				"state": loc["state"],
				"phone": self.new_phone(loc["area_codes"]), 
				"country": "United States"}
		return obj

	def full_location(self):
		"""
		generate complete address
		"""
		loc = self.new_location()
		loc["phone"] = self.new_phone(loc["area_codes"])
		loc["address_ln1"] = self.new_address()
		loc["address_ln2"] = self.new_addr_two()
		loc["country"] = "United States"
		return loc

	def new_full_name(self):
		"""
		returns random first & last name pair as tuple to be used by
		generate_name methods in Artist and Venue entities
		"""
		first_name = random.choice(self.names["first_self.names"])
		last_name = random.choice(self.names["last_self.names"])
		return (first_name, last_name)

	@staticmethod
	def bool():
		"""
		returns a bool from a coin flip
		"""
		return random.choice([True, False])

	def controlled_bool(self, completed_bool):
		"""
		returns control bool to determine if attribute ftns should 
		be called
		accepts completed_bool:
		- if complteted_bool is True or False, returns True or False
		- if completed_bool is None, returns a coin flip
		"""
		if completed_bool is None:
			return random.choice([True, False])
		return completed_bool

	@staticmethod
	def new_named_email(name_tuple):
		"""
		returns a fake email address based on a first and last name
		(which I would assume comes from new_full_name) already used elsewhere
		"""
		email = name_tuple[0] + name_tuple[1]
		email = email.lower()
		email += str(random.choice(range(100, 10000)))
		email += "@fakesite.web"
		return email

	def new_anonymous_email(self):
		"""
		returns a fake email address based on a first and last name from
		new_fake_name and requires no input parameter
		use with caution; does not return the fake name. Just the email.
		"""
		name_tuple = self.new_full_name()
		email = name_tuple[0] + name_tuple[1]
		email = email.lower()
		email += str(random.choice(range(100, 10000)))
		email += "@fakesite.web"
		return email

	def secondary_email(self, email):
		"""
		returns additional email(s) based on existing email to (all but)
		ensure unique emails
		"""
		email = email.split('@')
		i = 0
		email[0] = email[0][:-3]
		while i < 4:
			email[0] += random.choice(self.char_list)
			i += 1
		new_email = email[0] + "@" + email[1]
		return new_email

	def username(self):
		"""
		returns a fake and pretty random username
		"""
		username = random.choice(self.charset["upper"])
		u_len = random.choice(range(5, 8))
		i = 0
		while i < u_len:
			username += random.choice(self.charset["lower"])
			i += 1
		u_len = u_len + random.choice(range(0, 4))
		while i < u_len:
			username += random.choice(self.charset['nos'])
			i += 1
		return username

	def new_id(self):
		"""
		returns a fake id value with 14 chars
		"""
		i = 0
		random_id = self.new_char_string(4)
		while i < 6:
			random_id += random.choice(self.charset["nos"])
			i += 1
		return random_id

	def new_char_string(self, str_len):
		"""
		returns a string of specified length for chaotic lorem
		or False if the len is not feasable (> 20 chars)
		"""
		i = 0
		char_string = ""
		if str_len < 20:
			while i < str_len:
				char_string += random.choice(self.char_list)
				i += 1
		else:
			char_string = False
		return char_string

	@staticmethod
	def eval_args(args, min, max):
		"""
		evaluates weather args has len 1, is an integer, and if that integer 
		is less than max (also an integer). Returns integer in args if True
		and a random integer less than the max if False
		"""
		if len(args) == 1 and isinstance(args[0], int):
			if args[0] < 10:
				return args[0]
		return random.choice(range(min, max))

	def true_nonsense(self, *args):
		"""
		returns a random string of alphanumeric chars
		- if args has len 1 and args[0] is an integer < 10,
			the nonsense will be of the specified length.
		"""
		nonsense_length = self.eval_args(args, 1, 10)
		nonsense = ""
		while len(nonsense) < nonsense_length:
			nonsense += random.choice(self.char_list)
		return nonsense

	def nonsense_word(self, has_upper, *args):
		"""
		returns a random word of length 3-8 lowercase alphabet chars
		- if requires_upper (boolean) is True, the first char will
			begin with an uppercase letter
		- if args contains one int and that int is < 10, 
			the word will be of a specified length
		"""
		word_length = self.eval_args(args, 1, 10)
		if has_upper == True:
			word = random.choice(self.charset["upper"])
		else:
			word = ""
		while len(word) < word_length:
			word += random.choice(self.charset["lower"])
		return word

	def nonsentence(self, *args):
		"""
		returns a sentence of random words that starts with an uppercase
		letter and ends with a period. 
		- if args has len 1 and args[0] is an integer < 50,
			the sentence will be of the specified length.
		- a sentance will be at least 15 chars.
		note: sentence length includes .
		if they send me to jail ima finish the sent--
		"""
		sentence_length = self.eval_args(args, 15, 50) - 1
		if sentence_length < 15:
			sentence_length = 15
		sentence = self.nonsense_word(True) + " "
		while len(sentence) < sentence_length:
			sentence += self.nonsense_word(False) + " "
			if (sentence_length - len(sentence)) < 10:
				difference = sentence_length - len(sentence)
				sentence += self.nonsense_word(False, difference)
		return sentence + "."

	def fake_filepath(self):
		"""
		returns something that looks like a filepath, but is garbage
		"""
		subdirectories = random.choice(range(1,5))
		i = 0
		filepath = ""
		while i <= subdirectories:
			filepath += self.nonsense_word(False, random.choice(range(4, 8)))
			i += 1
			if i < subdirectories:
				filepath += "/"
		filepath += random.choice(['.js', '.pdf', '.html', '.txt', '.py'])
		return filepath

	def new_date(self, *args):
		"""
		returns a random date in the nearish past or nearish future
		if args has a length of 1 and is "past", date will be in the past
		if args has a length of 1 and is "future", date will be in the future
		if there are no args, date may be in the past or the future
		note: "past" and "future" are case sensitive
		note: timezones are not implemented in this program
		"""
		now = datetime.date.today()
		m_val = random.choice(range(1, 13))
		if len(args) == 1 and args[0] in ["past", "future"]:
			if args[0] == "future":
				y_val = random.choice(range(now.year, now.year + 6))
				if y_val == now.year:
					m_val = random.choice(range(now.month + 1, 13))
			elif args[0] == "past":
				y_val = random.choice(range(now.year - 5, now.year + 1))
				if y_val == now.year:
					m_val = random.choice(range(1, now.month))
		else:
			y_val = random.choice(range(now.year - 6, now.year + 6))
		max_date = monthrange(y_val, m_val)[1] + 1
		d_val = random.choice(range(1, max_date))
		return datetime.date(y_val, m_val, d_val)

	def new_datetime(self, *args):
		"""
		returns a random datetime in the nearish past or nearish future
		if args has a length of 1 and is "past", datetime will be in the past
		if args has a length of 1 and is "future", datetime will be in the 
		  future
		if there are no args, or if args are invalid, date may be in the past or
		  the future
		note: "past" and "future" are case sensitive
		note: timezones are not implemented in this program
		"""
		date = self.new_date(args[0])
		hh = random.choice(range(0, 24))
		mm = random.choice(range(0, 60))
		ss = random.choice(range(0, 60))
		return datetime.datetime(date.year, date.month, date.day, hh, mm, ss)

	def new_event(self, hours, minutes, *args):
		"""
		return start time and end time for event
		takes 
		"""
		date = self.new_datetime(args)
		hh = date.hour
		mm = date.minute
		end = datetime.datetime(date.year, date.month, date.day, hh, mm, 0)
		return [date, end]

	def new_code(self, stn_list):
		"""
		returns a fake unique numeric identification code seperated by dashes
		takes as an input a list of integers with len < 5 and sum < 20
		returns -1 for invalid input
		"""
		valid_input = True
		if len(stn_list) > 4:
			print("too long")
			valid_input = False
		if valid_input == True:
			for stn_length in stn_list:
				if not isinstance(stn_length, int):
					print("not int")
					valid_input = False
		if valid_input == True:
			stns_sum = 0
			for stn_len in stn_list:
				stns_sum += stn_len
			if stns_sum > 20:
				print("too great")
				valid_input = False
		if valid_input == True:
			code = ""
			sections = []
			for stn in stn_list:
				i = 0
				while i < stn:
					code += random.choice(self.charset["nos"])
					i += 1
				if stn_list.index(stn) < len(stn_list) - 1:
					code += "-"
			return code
		return "-1"

	def fake_cert_no(self, fake_prefix):
		"""
		returns a fake serial number with maximum length 16
		"""
		i = 0
		cert_no = str(fake_prefix)
		if len(cert_no) > 6:
			cert_no = cert_no[:6]
		while i < 10:
			cert_no += random.choice(self.char_list)
			i += 1
		return cert_no

	def auth_id(self):
		"""
		returns a fake authorizaiton code for user auth flow testing
		"""
		a_id = "f-"
		i = 0
		while i < 5:
			a_id += random.choice(self.charset["lower"])
			i += 1
		a_id += "-"
		while i < 12:
			a_id += random.choice(self.char_list)
			i += 1
		return a_id

	def org_assc_name(self):
		"""
		returns a fake organizaiton name
		"""
		wd_len = random.choice(range(1, 4))
		org_name = ""
		i = 0
		while i < wd_len:
			org_name += random.choice(self.names["street_self.names"]) + " "
			i += 1
		org_name += random.choice(["Group", "Org", "Associates", "Ltd", "LLC"])
		return org_name