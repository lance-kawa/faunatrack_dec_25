.PHONY: messages compilemessages

# Extraire les messages à traduire
messages:
	python manage.py makemessages -l fr --ignore=venv/*

# Compiler les fichiers de traduction
compilemessages:
	python manage.py compilemessages

# Raccourci pour extraire et compiler
trad: messages compilemessages
