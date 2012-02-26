run:
	@clear
	@python manage.py runserver 3000

createdb:
	@clear
	@python manage.py syncdb

clean:
	@find . -type f -name "*.pyc" | xargs rm -rf
	@clear

search:
	@clear
	@grep -r --color=always --exclude=Makefile 'TODO' .

