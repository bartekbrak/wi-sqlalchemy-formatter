Wi-SQLAlchemy-Formatter
-----------------------

Console logging beautifier for SQLAlchemy using Pygments and SQLParse.
Helps in debugging by colouring, indenting and filling in values in your 
SQLAclhemy queries. 

Inspired by [sqlformatter](https://pypi.python.org/pypi/sqlformatter/1.0).

Install
-------

    pip install -U wi-sqlalchemy-formatter
    
in your.ini:

    [formatter_sqlalchemy]
    class = wi_sqlalchemy_formatter.SqlAlchemyFormatter
    format = %(levelname)s %(message)s

and then tie loggers and handlers to this formatter. 

Sample INI logging section provided:

	###############################################################################
	[loggers]
	keys = root, sqlalchemy

	[handlers]
	keys = console, sqlalchemy

	[formatters]
	keys = generic, sqlalchemy

	###############################################################################

	[logger_root]
	level = INFO
	handlers = console

	[logger_sqlalchemy]
	level = INFO
	handlers = sqlalchemy
	qualname = sqlalchemy.engine
	# no need to send this debug info to root logger
	propagate = 0
	# "level = INFO" logs SQL queries.
	# "level = DEBUG" logs SQL queries and results.
	# "level = WARN" logs neither.  (Recommended for production systems.)

	###############################################################################

	[handler_console]
	class = StreamHandler
	args = (sys.stderr,)
	level = NOTSET
	formatter = generic

	[handler_sqlalchemy]
	class = StreamHandler
	args = (sys.stderr,)
	level = NOTSET
	formatter = sqlalchemy


	###############################################################################

	[formatter_generic]
	format = %(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s

	[formatter_sqlalchemy]
	class = wi_sqlalchemy_formatter.SqlAlchemyFormatter
	format = %(levelname)s %(message)s


Extras
------

This library also provides some useful debug-time methods:

    wi_sqlalchemy_formatter.color_sql
    """
    Beautify and colorify SQL snippet.
    @param code: string
    @return: string
    """
 
    wi_sqlalchemy_formatter.compile_query
    """
    Compile sqlalchemy query object to regular SQL with escaped values
    @param query: sqlalchemy query object
    @return: string
    """

They work and work beautifully but they kind of shouldn't belon here so they 
might be here temporarily.

Changelog
---------

0.1b (2014-10-29)
-----------------

* works, tested on four separate systems but problems might happen as 
Alchemy is no trfile. 