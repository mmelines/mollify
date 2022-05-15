r_path = 'model.py'
w_path = 'scaffold.py'

import logging
import os
from mollify_config import DataConfig as config
from scaffold import Scaffold
from pprint import pprint

logging.basicConfig(filename='tryrun.log', level=logging.DEBUG)

class CliCtl:
	"""
	"""

	def __init__(self, control_obj):
		"""
		"""
		self.ctl = control_obj
		self.stage = self.ctl.stage
		self.stage_switch()

	def stage_switch(self):
		if self.stage == -1:
			print("error; exiting")
		if self.stage == 1:
			print("Welcome to Mollify\nInitiating Stage 1 Run")
			print("\n"*2)
			self.ctl.iter1()
		else:
			print("stage " + str(self.stage) + " found but not defined")


class MainCtl:
	"""
	"""

	def __init__(self):
		self.txt = Scaffold()
		self.dirs = {}
		self.has_dirs = False
		self.stage = self.eval_stage()
		self.iter_lists = {}
		self.files = {"__init__.py": {"stages": True,
										"filename": '__init__.py',
										"stage1": {"src": self.txt.init_txt, 
													"required": {"<APP_NAME>": config.APP_NAME}},
										"stage2": {"src": self.txt.init_api}},
						"setup.py": {"stages": False,
										"filename": 'setup.py',
										"src": self.txt.setup_txt,
										"required": {}},
						"model.py": {"stages": False,
										"filename": 'model.py',
										"src": self.txt.model_txt,
										"required": {}},
						"config.py": {"stages": False,
										"filename": 'config.py',
										"src": self.txt.config_txt,
										"required": {"<DB_URI>": config.SQLALCHEMY_DATABASE_URL,
													"<TEST_DB_URI>": config.TEST_SQLALCHEMY_DATABASE_URL}}}
		self.assess_filetree()
		print("STAGE " + str(self.stage) + " RUN")
		
	def eval_stage(self):
		stage = -1
		if self.has_dirs == False:
			stage = 1
		if hasattr(self.dirs, config.APP_NAME):
			model = self.dirs[config.APP_NAME]["model.py"]
			if model["found"] == False:
				stage = 2
			else:
				if model["complete"] == False:
					stage = 3
		return stage
	
	def mkmdirs(self):
		self.stage = "create directories"
		run_eval = None
		home = os.getcwd()
		try:
			os.makedirs(home+("/"+str(DataConfig.APP_NAME))*2)
			run_eval = "1"
		except FileExistsError:
			run_eval = "2"
		finally:
			print(run_eval)

	def text_array(self, txt):
		text_array = []
		prev_whitespace = False
		i = 0
		if txt[0] == "#":
			return [[0, txt]]
		for text in txt.splitlines():
			indent = 0
			for char in text:
				if char == " ":
					indent += 1
				else:
					break
			if indent == len(text):
				if prev_whitespace == False and i > 0:
					text_array.append(["whitespace"])
				prev_whitespace = True
			if indent < len(text):
				indent_level = (indent - 8) / 4
				text_array.append([int(indent_level), text.strip()])
				prev_whitespace = False
			i += 1
		return text_array

	def replicate(self, text, destination):
		text_array = self.text_array(text)
		with open(destination, 'a') as file:
			for line in text_array:
				if line == ["whitespace"]:
					file.write('\n')
				else:
					indent = "    " * line[0] if line[0] > 0 else ""
					file.write(indent + line[1] + "\n")

	def customize(self, text, values):
		text = str(text)
		start = text.find("start_read") + 10
		end = text.find("end_read")
		if start > -1 and end > 0:
			custom_text = text[start:end]
			for key in values.keys():
				custom_text = custom_text.replace(key, values[key])
			return custom_text			
		return "#intentionally blank"

	def generate(self, gen, **kwargs):
		if gen["stages"] == True:
			if "stage" in kwargs.keys():
				if isinstance(kwargs["stage"], int):
					key = "stage" + str(kwargs["stage"])
					gen["src"] = gen[key]["src"] #jinkies!
					gen["required"] = gen[key]["required"]
					text = gen["src"](kwargs["stage"])
		else:
			text = gen["src"]()
		text = self.customize(text, gen["required"])
		self.replicate(text, gen["path"])

	def take_step(self, obj):
		if hasattr(obj, "inst"):
			print("special instructions")
		else:
			ctl_var = False
			try:
				if os.stat(obj["path"]).st_size == 0: 
					#prevent re-write/duplicate
					ctl_var = True
			except FileNotFoundError:
				#write file if it doesn't exist
				ctl_var = True
			finally:
				if ctl_var == True:
					obj["info"]["path"] = obj["path"]
					if obj["info"]["stages"] == True:
						self.generate(obj["info"], stage=1)
					else:
						self.generate(obj["info"])

	def iter1(self):
		flask_main = self.dirs[config.APP_NAME]
		pprint(flask_main)
		steps = [flask_main["__init__.py"], 
					flask_main["setup.py"], 
					flask_main["model.py"], 
					flask_main["config.py"]]
		for step in steps:
			print("*"*25 +"STEP " + str(step) + ".")
			print(step)
			self.take_step(step)

	def static_css():
		print("static")
		return None

	def js_libs():
		print("js_libs")
		return None

	def assess_filetree(self):
		complete = {"flask_dir": {"__init__.py": {"found": False,
															"name": "__init__",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": ".py"},
											"setup.py": {"found": False,
															"name": "setup",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 1,
															"type": "file",
															"extension": ".py"},
											"config.py": {"found": False,
															"name": "config",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 1,
															"type": "file",
															"extension": ".py"},
											"model.py": {"found": False,
															"complete": False,
															"name": "model",
															"exists_iter": 1,
															"complete_iter": 1,
															"type": "file",
															"extension": ".py"},
											"static": {"found": False,
															"complete": False,
															"name": "static",
															"exists_iter": 2,
															"complete_iter": 2,
															"type": "dir"},
											"templates": {"found": False,
															"complete": False,
															"name": "templates",
															"exists_iter": 2,
															"complete_iter": 2,
															"type": "dir"},
											"views": {"found": False,
															"complete": False,
															"name": "",
															"exists_iter": 2,
															"complete_iter": 2,
															"type": "dir"},
											"relative_path": "/<APP_NAME>"},
							"project_root": {"requirements.txt": {"found": False,
															"name": "requirements",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": ".txt"},
												".flaskenv": {"found": False,
															"name": ".flaskenv",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": ""},
												"Makefile": {"found": False,
															"name": "Makefile",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": ""},
												"flask_dir": {"found": False,
															"name": config.APP_NAME,
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "dir"},
												'relative_path': ''},
							"static": {"css": {"found": False,
															"name": "css",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "dir"},
											"js": {"found": False,
															"name": "js",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "dir"},
											"img": {"found": False,
															"name": "img",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "dir"},
										"relative_path": "/<APP_NAME>/static"},
							"css": {"relative_path": "/<APP_NAME>/css",
									"inst": self.static_css},
							"js": {"libs": {"found": False,
															"name": "libs",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "dir"},
									"site_scripts.js": {"found": False,
															"name": "site_scripts",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": ".js"},
									"form_scripts.js": {"found": False,
															"name": "form_scripts",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": ".js"},
										"relative_path": "/<APP_NAME>/js"},
							"libs": {"relative_path": "/<APP_NAME>/js/libs",
										"inst": self.js_libs},
							"img": {"relative_path": "/<APP_NAME>/img"},
							"templates": { "errors": {"found": False,
															"name": "errors",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "dir"},
											"forms": {"found": False,
															"name": "forms",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "dir"},
											"layout": {"found": False,
															"name": "layout",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "dir"},
											"pages": {"found": False,
															"name": "pages",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "dir"},
											"relative_path": "/<APP_NAME>/templates"},
							"errors": {"404.html": {"found": False,
															"name": "404",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": ".html"},
											"500.html": {"found": False,
																"name": "500",
																"complete": False,
																"exists_iter": 1,
																"complete_iter": 2,
																"type": "html",
																"extension": ".html"},
											"relative_path": "/<APP_NAME>/templates/errors"},
							"forms":	{"relative_path": "/<APP_NAME>/templates/forms"},
							"layouts":	{"main.html": {"found": False,
															"name": "main",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": "html"},
										"form.html": {"found": False,
															"name": "form",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": ".html"},
										"relative_path": "/<APP_NAME>/templates/layouts"},
							"pages":	{"index.html": {"found": False,
															"name": "index",
															"complete": False,
															"exists_iter": 1,
															"complete_iter": 2,
															"type": "file",
															"extension": ".html"},
											"relative_path": "/<APP_NAME>/templates/pages"}}
		rootdir = os.getcwd() + "/" + config.APP_NAME
		i = 0
		# create root path if it doesn't exist
		if not os.path.exists(rootdir):
			os.makedirs(rootdir, exist_ok=False)
		if self.has_dirs == False:
			for dirname in complete.keys():
				print(dirname)
				# set path and remove relative path placeholder
				rel_path = complete[dirname]["relative_path"]
				rel_path = rel_path.replace("<APP_NAME>", config.APP_NAME)
				path = rootdir + rel_path
				complete[dirname]["path"] = path
				del complete[dirname]["relative_path"]
				# see if path exists
				if not os.path.exists(path):
					os.makedirs(path, exist_ok=False)
				content = os.listdir(path)
				# check content of path
				for item in content:
					if item in complete[dirname].keys():
						complete[dirname][item]["found"] = True
				# include file instructions
				for item in complete[dirname].keys():
					if isinstance(complete[dirname][item], dict):
						complete[dirname][item]["path"] = path+"/"+item
						if complete[dirname][item]["type"] == "file":
							obj = complete[dirname][item]
							print(obj)
							filename = obj["name"] + obj["extension"]
							print("??????"+filename)
							if filename in self.files.keys():
								print("!!!!!!!!!!!")
								print(self.files[filename])
								obj["info"] = self.files[filename]
								print(obj)
								print("\n"*2)
				# change default name for project_root and flask_dir
				if dirname in ["project_root", "flask_dir"]:
					complete[dirname]["role"] = dirname
					if dirname == "flask_dir":
						self.dirs[config.APP_NAME] = complete[dirname]
				else:
					self.dirs[dirname] = complete[dirname]
			self.has_dirs = True

class DBText:

	def __init__(self, *args):
		"""
		init new DBText Object
		"""
		self.string = None
		self.lines = None
		self.order = None
		self.db_class_name = None
		self.tablename = None
		self.docstring = None
		self.primary_key = None
		self.primary_foreign_key = None
		self.entity_kind = None
		self.attributes = None
		self.attribute_data = {"foreign_key_count": 0,
								"total_attributes": 0}
		self.foreign_keys = None
		self.relationships = None
		self.parents = None
		self.required_parents = None
		self.children = None
		self.ancestors = None
		if len(args) > 0:
			for item in args:
				if isinstance(item, str):
					self.parse(item)
				if isinstance(item, int):
					self.order = item

	def __repr__(self):
		"""
		string representation of DBText object
		"""
		if self.string is None:
			msg = "blank db.Model object"
		else:
			i = 0
			if self.lines is None:
				msg = "unprocessed db.Model object: " + self.string
			elif self.attributes is None:
				msg = "db.Model object: \n"
				for line in self.lines:
					i += 1
					msg += str(i) + ". " + str(line) + "\n"
				msg += " with no defined attributes"
			else:
				msg = "db.Model object"
				if not self.db_class_name is None:
					msg += " type " + self.db_class_name
					if not self.tablename is None:
						msg += " (" + self.tablename + ")"
				msg += "\n    - order: " + str(self.order) + "\n"
				msg += "    - docstring: " + str(self.docstring) + "\n"
				msg += "    - primary_key: " + str(self.primary_key) + "\n"
				msg += "    - attribute_data: " + str(self.attribute_data) + "\n"
				msg += "    - entity_kind: " + str(self.entity_kind) + "\n"
				msg += "    - attributes: "
				if not self.attributes is None:
					pprint(self.attributes)
					for attribute in self.attributes:
						msg += "\n " + attribute
					msg += "\n"
				if not self.foreign_keys is None:
					msg += "\n    - foreign keys: "
					for foreign_key in self.foreign_keys:
						msg += str(foreign_key) + " | "
					msg += "\n    - parents: " + str(self.parents)
					msg += "\n    - required_parents " + str(self.required_parents)
					msg += "\n"
				else:
					msg += "no foreign keys\n"
				if not self.relationships is None:
					pprint(self.relationships)
					msg += "\n    - children: " + str(self.children)
					msg += "\n    - foreign keys: "
					for relationship in self.relationships:
						msg += "      * " + str(self.relationships[relationship])
					msg += "\n"
				else:
					msg += "no relationships\n"
		return msg

	def parse(self, raw_string):
		"""
		process model string from text file if it does not exist
		"""
		logging.info("init DBText.parse")
		self.string = raw_string
		self.lines = self.form_raw_lines()
		self.attributes = self.add_attributes()
		self.relationships = self.add_relationships()
		# access and save identifying entity information
		attr_string = self.identify(raw_string)
		logging.info("completed DBText.parse")
		return self

	def divide(self, param_string):
		"""
		split list of entity attributes and assign:
		- original lines from model.py document
		- model attribute tuple list
		- model attribute detailed object list
		"""
		logging.info("called DBText.divide")
		lines = self.split_params(param_string)
		logging.info("completed DBText.divide")
		return lines

	def identify(self, model):
		"""
		identify entity information
		"""
		logging.info("called DBText.identify")
		first_close_paren_loc = model.find("(")
		if first_close_paren_loc > 0:
			self.db_class_name = model[:first_close_paren_loc].strip()
		docstring_open = model.find('"""')
		docstring_close = model.find('"""', docstring_open + 1)
		if (docstring_open > 0 and docstring_close > 0):
			docstring_content = model[docstring_open: docstring_close]
			docstring_content = docstring_content.replace("\n", "")
			docstring_content = docstring_content.replace('"""', "")
			self.docstring = docstring_content.strip()
		tablename_open = model.find("__tablename__")
		tablename_close = -2
		if tablename_open > 0:
			tablename_open = model.find("'", tablename_open+1) + 1
			if tablename_open > 0:
				tablename_close = model.find("'", tablename_open)
			else:
				tablename_open = model.find('"', tablename_open+1) + 1
				if tablename_open > 0:
					tablename_close = model.find('"', tablename_open)
			if tablename_open > 0 and tablename_close > 0:
				self.tablename = model[tablename_open:tablename_close]
		logging.debug("  >>>>> self.tablename now: " + str(self.tablename))
		logging.info("completed DBText.identify")
		return model[tablename_open:]

	def form_raw_lines(self):
		"""
		turn lines into a list of seperated, cleaned strings
		"""
		logging.info("called DBText.raw_lines")
		lines = self.string.split("\n")
		line_list = []
		for line in lines:
			line = self.clean_line(line)
			if not line is None:
				line_list.append(line)
		logging.info("DBText.raw_lines completed")
		return line_list

	def add_attributes(self):
		"""
		create attribute object 
		"""
		logging.info("called DBText.add_attributes")
		attributes = {}
		for line in self.lines:
			if line.find("=") > -1 and line.find(".Column") > -1:
				if line.find("relationship") == -1:
					line_obj = self.parse_assignment(line)
					if not line_obj is None:
						attributes[line_obj["attribute_name"]] = line_obj
						self.attribute_data["total_attributes"] += 1
						if line_obj["foreign_key"] == True:
							self.attribute_data["foreign_key_count"] += 1
							if self.foreign_keys is None:
								self.foreign_keys = [line_obj["attribute_name"]]
							else:
								self.foreign_keys.append(line_obj["attribute_name"])
						if line_obj["primary_key"] == True:
							self.primary_key = line_obj["attribute_name"]
		logging.info("DBText.add_attributes completed")
		return attributes

	def add_relationships(self):
		logging.info("DBText.add_relationships")
		relationships = {}
		children = []
		for line in self.lines:
			obj = {}
			if line.find("=") > -1 and line.find(".relationship") > -1:
				obj = {"variable_name": line[:line.find("=")].strip(),
						"string":line[line.find("=") + 1:].strip()}
				obj = self.categorize_relationship(obj)
			if obj != {}:
				relationships[obj["backref"]] = obj
				if not obj["child"] in children:
					children.append(obj["child"])
		if relationships != {}:
			self.children = children
		logging.info("DBText.add_relationships")
		return relationships

	def parse_assignment(self, line):
		"""
		get information for entire db.Column assignment function
		"""
		logging.info("called DBText.parse_assignment")
		assn_index = line.find("=")
		line_halves = [line[:assn_index], line[assn_index + 1:]]
		attribute_obj = {"variable_name": line_halves[0].strip(),
				"values": [],
				"attribute_name": "",
				"foreign_primary_key": False,
				"primary_key": False,
				"foreign_key": False}
		param_list = self.get_all_params(line_halves[1])
		if not param_list is None:
			for param in param_list:
				## add update to combine objects
				param_obj = self.categorize_param(param)
				if not param_obj is None:
					attribute_obj["values"].append(param_obj)
					if param_obj["type"] == "name":
						if attribute_obj["attribute_name"] == "":
							attribute_obj["attribute_name"] = param_obj["name"]
					if param_obj["primary_key"] == True:
						attribute_obj["primary_key"] = True
						if param_obj["foreign_key"] == True:
							attribute_obj["primary_foreign_key"] == True
					if param_obj["foreign_key"] == True:
						attribute_obj["foreign_key"] = True
			if not len(attribute_obj["attribute_name"]) > 1:
				attribute_obj["attribute_name"] = attribute_obj["variable_name"]
		else:
			attribute_obj = None
		logging.debug("parse_assignment returned " + str(attribute_obj))
		logging.info("DBText.parse_assignment complete")
		return attribute_obj

	def categorize_param(self, param):
		"""
		categorize individual parameter, expanding its object further
		"""
		logging.info("called DBText.categorize_param")
		obj = {"string": param,
				"primary_key": False,
				"foreign_key": False, 
				"type": False}
		cats = {"db.": {"options": ["Integer", "String", "Boolean", "Numeric", 
									"DateTime", "relationship", "ForeignKey"],
						"Integer": {"type": "data_type",
									"data_type": "int"},
						"String": {"type": "data_type",
									"data_type": "str"},
						"Boolean": {"type": "data_type",
									"data_type": "bool"},
						"Numeric": {"type": "data_type",
									"data_type": "num"},
						"DateTime": {"type": "data_type",
									"data_type": "datetime"},
						"Date": {"type": "data_type",
									"data_type": "date"},
						"ForeignKey": {"type": "role",
									"role": "fk"}},
				"=": {"options":["primary_key", "nullable", "unique"],
						"primary_key": {"type": "role",
										"role": "pk"}, 
						"nullable": {"type": "param_rule",
										"rule": "nullable"},
						"unique": {"type": "param_rule",
										"rule": "unique"}}}
		# add switch object information
		if param.find("db.") > -1:
			for param_key in cats["db."]["options"]:
				if param.find(param_key) > -1:
					obj.update(cats["db."][param_key])
			if obj["type"] == "data_type":
				obj = self.categorize_data_type(obj)
			if obj["type"] == "role":
				if obj["role"] == "fk":
					obj = self.categorize_foreign_key(obj)
		elif param.find("=") > -1:
			for param_key in cats["="]["options"]:
				if param.find(param_key) > -1:
					obj.update(cats["="][param_key])
			if obj["type"] == "role":
				if obj["role"] == "pk":
					obj = self.categorize_primary_key(obj)
			if obj["type"] == "param_rule":
				obj = self.categorize_param_rule(obj)
		else:
			obj["type"] = "name"
			obj = self.categorize_db_name(obj)
		logging.debug("DBText.categorize_param will return " + str(obj))
		logging.info("completed DBText.categorize_param")
		return obj

	def categorize_data_type(self, obj):
		"""
		add contextual information for data type db.Column parameter
		"""
		logging.info("called DBText.categorize_data_type")
		logging.debug("running DBText.categorize_data_type with " + str(obj))
		if obj["data_type"] == "str":
			obj["limit"] = self.get_all_params(obj["string"])
		if obj["data_type"] == "num":
			specifics = self.get_all_params(obj["string"])
			if len(specifics) > 0:
				for item in specifics:
					if item.find("=") > 0:
						items = item.split("=")
						key = items[0].strip()
						value = str(items[1]).strip()
						obj[key] = value
		logging.info("DBText.categorize_data_type completed")
		return obj

	def categorize_primary_key(self, obj):
		"""
		add contextual information for db.relationship
		"""
		logging.info("called DBText.categorize_primary_key")
		logging.debug("running DBText.categorize_primary_key with " + str(obj))
		obj["primary_key"] = True
		logging.info("DBText.categorize_primary_key completed")
		return obj

	def categorize_foreign_key(self, obj):
		"""
		add contextual information for db.relationship
		"""
		logging.info("called DBText.categorize_foreign_key")
		logging.debug("running DBText.categorize_foreign_key with " + str(obj))
		obj["foreign_key"] = True
		parent = self.get_params(obj["string"]).split(".")
		obj["parent_entity"] = parent[0]
		obj["parent_pk_name"] = parent[1]
		logging.info("DBText.categorize_foreign_key completed")
		return obj

	def categorize_relationship(self, obj):
		"""
		add contextual information for db.relationship
		"""
		logging.info("called DBText.categorize_relationship")
		logging.debug("running DBText.categorize_relationship with " + str(obj))
		specifics = self.get_all_params(obj["string"])
		for item in specifics:
			if item.find("=") > 0:
				if item.find("backref") > -1:
					items = item.split("=")
					obj["backref"] = items[1].strip()
				else:
					items = item.split("=")
					obj["loading_method"] = self.clean_line(items[0])
					obj["loading_value"] = self.clean_line(items[1])
			else:
				obj["child"] = self.clean_line(item)
		logging.info("DBText.categorize_relationship completed")
		return obj

	def categorize_param_rule(self, obj):
		"""
		add contextual information for param rule db.Column parameter
		"""
		logging.info("called DBText.categorize_param_rule")
		logging.debug("running DBText.categorize_param_rule with " + str(obj))
		items = self.clean_line(obj["string"]).split("=")
		obj["rule_type"] = items[0]
		obj["rule_value"] = items[1]
		logging.info("DBText.categorize_param_rule completed")
		return obj

	def categorize_db_name(self, obj):
		"""
		add contextual information for name db.Column parameter
		"""
		logging.info("called DBText.categorize_db_name")
		logging.debug("running DBText.categorize_db_name with " + str(obj))
		obj["name"] = obj["string"].strip()
		logging.info("DBText.categorize_db_name completed")
		return

	def get_all_params(self, line):
		"""
		"""
		def snip_line(line):
			if line.find("(") > -1:
				opens = line.count(")")
				closes = line.count("(")
				line = line[line.find("("):]
				if opens == closes:
					if line[0] == "(" and line[-1] == ")":
						line = line[1:-1]
				else:
					if opens > closes:
						if line[0] == "(":
							line = line[1:]
					if closes > opens:
						if line[-1] == ")":
							line = line[:-1]
				line = line.strip()
			return line

		def replace_delim(segment, part):
			preceding = segment[:part[1] - 1]
			following = segment[part[2]+1:]
			string = preceding + part[0] + following
			return string

		def alter_part(part):
			part = part.replace(",", "*")
			return part

		def select_excerpt(segment):
			close_paren = segment.find(")")
			segment = segment[:close_paren]
			open_paren = (len(segment) - segment[::-1].find("("))
			if close_paren > open_paren:
				segment = segment[open_paren:]
			segment = "[" + segment + "]"
			return [segment, open_paren, close_paren]

		loop_ctl = True
		nest_level = 0
		segment = snip_line(line)
		emergency_debug = 0
		while loop_ctl == True:
			emergency_debug += 1
			if segment.find(")") > -1:
				part = select_excerpt(segment)
				part[0] = alter_part(part[0])
				segment = replace_delim(segment, part)
			else:
				loop_ctl = False
			if emergency_debug > 5:
				loop_ctl = False
		segment = segment.replace("[", "(")
		segment = segment.replace("]", ")")
		segment = segment.split(",")
		param_list = []
		for item in segment:
			item = item.replace("*", ",")
			param_list.append(item.strip())
		logging.debug("DBText.get_all_params will return: " + str(segment))
		logging.info("DBText.get_all_params complete")
		return param_list

	def get_params(self, line):
		logging.info("called get_params with " + line)
		index = self.get_outer_parens(line)
		if not index is None:
			function_name = line[:index[0]]
			line = line[index[0] + 1 : index[1]]
		else:
			function_name = None
			line = None
		logging.info("get_params line is " + str(line))
		return line

	def snip_paren(self, line):
		if line.find("(") > 0:
			line = line[line.find("(") + 1:]
		if line.find(")") > 0:
			line = line.replace(")", "")
		return line

	@staticmethod
	def get_outer_parens(line):
		"""

		"""
		logging.info("called DBText.get_outer_parens with " + line)
		open_paren = line.find("(")
		close_paren = len(line) - line[::-1].find(")")
		if open_paren > -1 and close_paren > -1:
			paren_tuple = [open_paren, close_paren - 1]
		else:
			paren_tuple = None
		logging.info("completed DBText.get_outer_parens (" + str(open_paren) + ", " + str(close_paren) + ")")
		return paren_tuple

	def eval_assignment(self, line):
		"""
		expand entity attribute into an object, including param list
		"""
		logging.info("called DBText.eval_assignment")
		logging.debug("DBText with: " + str(line))
		eval_obj = None
		# if line is valid assignment statement:
		if not line is None and line.find("=") > -1:
			value = line[line.find("=") + 1:]
			# create object to 
			# assign left side of assignment to "variable name" attr
			# save the entire line to "full" attr
			eval_obj = {"variable_name" : line[:line.find("=")].strip(),
						"full": line}
			value_list = []
			# if db.Column in line, evaluate parameter values and add them
			# to the object
			if ".Column" in value:
				# call DBText get_outer_parens to remove chars around params
				index = self.get_outer_parens(value)
				if not index is None:
					# create value_list of each parameter value
					param_list = value[index[0] + 1:index[1]]
					param_list = param_list.split(",")
					for param in param_list:
						value_list.append(param.strip())
					# assign name value if attribute has an explicit name
					setname = False
					for disallowed in ["=", "db."]:
						if param_list[0].find(disallowed) > -1:
							setname = True
					if setname == False:
						name = param_list[0]
					for disallowed in [".", "(", "="]:
						if name.find(disallowed) > -1:
							name = None
							break
					eval_obj["attribute_name"] = name
					eval_obj["param_list"] = value_list
		logging.info("completed DBText.eval_assignment")
		return eval_obj

	@staticmethod
	def clean_line(line):
		"""

		"""
		logging.info("called DBText.clean_line")
		line = line.replace("'", "")
		line = line.replace('"', "")
		line = line.strip()
		if len(line) == 0:
			line = None
		elif line.find("#") >= 0:
			line = None
		return line

	def snip(counter, model):
		"""

		"""
		logging.info("called DBText.")
		first_close_paren_loc = model.find("(")
		firstline = None
		if first_close_paren_loc > 0:
			firstline = model[:first_close_paren_loc].strip()
		docstring_open = model.find('"""')
		docstring_close = model.find('"""', docstring_open + 1)
		docstring_content = None
		if (docstring_open > 0 and docstring_close > 0):
			docstring_content = model[docstring_open: docstring_close]
			docstring_content = docstring_content.replace("\n", "")
			docstring_content = docstring_content.replace('"""', "")
			docstring_content = docstring_content.strip()
		tablename_open = model.find("__tablename__")
		tablename_close = None
		tablename_line = None
		if tablename_open > 0:
			tablename_open = model.find("'", tablename_open+1) + 1
			if tablename_open > 0:
				tablename_close = model.find("'", tablename_open)
			else:
				tablename_open = model.find('"', tablename_open+1) + 1
				if tablename_open > 0:
					tablename_close = model.find('"', tablename_open)
			if tablename_open > 0 and tablename_close > 0:
				tablename_line = model[tablename_open:tablename_close]
		return (model[tablename_close:], {"order": counter,
					"db_entity": firstline,
					"docstring": docstring_content,
					"tablename": tablename_line})

	def objectify(line):
		"""

		"""
		def find_all(paren, line):
			loop_ctl = True
			last_index = -1
			all_parens = []
			while loop_ctl == True:
				last_index = line.find(paren, last_index+1)
				if last_index > 0:
					all_parens.append(last_index)
				else:
					loop_ctl = False
			return all_parens

		hashtag = line.find("#")
		assign_op = line.find("=")
		all_open_parens = find_all("(", line)
		all_close_parens = find_all(")", line)
		# exclude comment lines and EOL comments
		if hashtag > 0 and hashtag < 4:
			return False
		else:
			line = line[:hashtag]
		if assign_op > 0 and line.find("==") == -1:
			if len(all_open_parens) > 0 and line.find("db.Column") > -1:
				if len(all_open_parens) == len(all_close_parens):
					col_params = line[all_open_parens[0] + 1:]
					for param in col_params:
						col_params = param.split(",")
						col_params = param.replace("'", "")
						col_params = param.replace('"', "")
						col_params = param.split()

	def add_warning(self):
		"""
		adds a warning when model cannot be read correctly
		"""
		return None

'''
with open(r_path, 'r') as reader:
	model = reader.read()
model_list = model.split("class ")
i = 0
for item in model_list:
	i += 1
	if item.find("Model)") > 0:
		item = DBText(item, i)
'''

control = MainCtl()
interface = CliCtl(control)
#control.generate("__init__.py", stage=1)
