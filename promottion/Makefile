run:
	@clear
	@sed -i 5d settings.py
	@sed -i "5iPATH_PROMOTION = '/home/tacsio/Projects/promotion/promottion'" settings.py
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

